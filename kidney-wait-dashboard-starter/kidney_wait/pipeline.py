"""Validate and transform sample kidney-transplant metrics into dashboard-ready CSVs.

IMPORTANT: Bundled DEMO inputs are fictional and NOT Canadian/US health statistics.
No external data is downloaded or scraped by this program.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUTPUTS = {
    "provincial": ("provincial_metrics.csv", ["year", "province", "province_name", "waitlist_patients", "transplants", "waitlist_deaths", "deceased_donors", "living_donors", "median_dialysis_to_transplant_years", "deceased_donor_rate_per_million", "living_donor_rate_per_million", "source_status"]),
    "national": ("national_metrics.csv", ["year", "country", "waitlist_patients", "transplants", "waitlist_deaths", "median_dialysis_to_transplant_years", "deceased_donor_rate_per_million", "living_donor_rate_per_million", "source_status"]),
    "us": ("us_metrics.csv", ["year", "country", "deceased_donor_rate_per_million", "living_donor_rate_per_million", "source_status"]),
    "policy": ("policy_notes.csv", ["province", "policy_note", "source_status"]),
}


def demo_status(path: Path) -> str:
    return "SYNTHETIC_DEMO" if path.name.startswith("DEMO_") else "USER_SUPPLIED_UNVERIFIED"


def parse_int(value: object, column: str) -> int:
    try:
        number = int(str(value).strip())
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid integer in {column}: {value!r}") from exc
    if number < 0:
        raise ValueError(f"Negative value in {column}: {value!r}")
    return number


def parse_positive_float(value: object, column: str) -> float:
    try:
        number = float(str(value).strip())
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid number in {column}: {value!r}") from exc
    if not (0 <= number < float('inf')):
        raise ValueError(f"Out-of-range value in {column}: {value!r}")
    return number


def parse_year(value: object) -> int:
    year = parse_int(value, "year")
    if year < 2000 or year > 2100:
        raise ValueError(f"Year outside supported range 2000-2100: {year}")
    return year


def read_csv(path: Path, required_columns: list[str]) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"Missing CSV header: {path}")
        missing = sorted(set(required_columns) - set(reader.fieldnames))
        if missing:
            raise ValueError(f"Missing columns in {path.name}: {', '.join(missing)}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"No rows in {path.name}")
    return rows


def validate_provinces(path: Path) -> list[dict]:
    fields = OUTPUTS["provincial"][1][:-1]
    results, seen = [], set()
    for raw in read_csv(path, fields):
        year = parse_year(raw["year"])
        province = raw["province"].strip().upper()
        if not re.fullmatch(r"[A-Z]{2}", province):
            raise ValueError(f"Invalid province code: {province!r}")
        key = (year, province)
        if key in seen:
            raise ValueError(f"Duplicate provincial year/province: {key}")
        seen.add(key)
        name = raw["province_name"].strip()
        if not name:
            raise ValueError("province_name cannot be empty")
        rec = {"year": year, "province": province, "province_name": name}
        for col in ["waitlist_patients", "transplants", "waitlist_deaths", "deceased_donors", "living_donors"]:
            rec[col] = parse_int(raw[col], col)
        for col in ["median_dialysis_to_transplant_years", "deceased_donor_rate_per_million", "living_donor_rate_per_million"]:
            rec[col] = parse_positive_float(raw[col], col)
        rec["source_status"] = demo_status(path)
        results.append(rec)
    return sorted(results, key=lambda r: (r["year"], r["province"]))


def validate_national(path: Path) -> list[dict]:
    fields = OUTPUTS["national"][1][:-1]
    results, seen = [], set()
    for raw in read_csv(path, fields):
        year = parse_year(raw["year"])
        country = raw["country"].strip().upper()
        if country not in {"CAN", "CA", "CANADA"}:
            raise ValueError(f"National file must contain Canada only, got {country!r}")
        if year in seen:
            raise ValueError(f"Duplicate Canadian national year: {year}")
        seen.add(year)
        rec = {"year": year, "country": "Canada"}
        for col in ["waitlist_patients", "transplants", "waitlist_deaths"]:
            rec[col] = parse_int(raw[col], col)
        for col in ["median_dialysis_to_transplant_years", "deceased_donor_rate_per_million", "living_donor_rate_per_million"]:
            rec[col] = parse_positive_float(raw[col], col)
        rec["source_status"] = demo_status(path)
        results.append(rec)
    return sorted(results, key=lambda r: r["year"])


def validate_us(path: Path) -> list[dict]:
    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(encoding="utf-8") as f:
        payload = json.load(f)
    records = payload.get("records") if isinstance(payload, dict) else payload
    if not isinstance(records, list) or not records:
        raise ValueError("US JSON must contain a nonempty 'records' array")
    results, seen = [], set()
    for raw in records:
        if not isinstance(raw, dict):
            raise ValueError("Each US record must be an object")
        year = parse_year(raw.get("year"))
        country = str(raw.get("country", "")).strip().upper()
        if country not in {"US", "USA", "UNITED STATES"}:
            raise ValueError(f"Unexpected US country label: {country!r}")
        if year in seen:
            raise ValueError(f"Duplicate US benchmark year: {year}")
        seen.add(year)
        results.append({
            "year": year,
            "country": "United States",
            "deceased_donor_rate_per_million": parse_positive_float(raw.get("deceased_donor_rate_per_million"), "deceased_donor_rate_per_million"),
            "living_donor_rate_per_million": parse_positive_float(raw.get("living_donor_rate_per_million"), "living_donor_rate_per_million"),
            "source_status": demo_status(path),
        })
    return sorted(results, key=lambda r: r["year"])


class PolicyParser(HTMLParser):
    """Parse local <article data-province='XX'> notes, not a live scraping client."""
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.province = ""
        self.parts: list[str] = []
        self.notes: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        if tag == "article" and self.depth == 0:
            self.province = dict(attrs).get("data-province", "").strip().upper()
            self.parts = []
            self.depth = 1
        elif self.depth:
            self.depth += 1

    def handle_endtag(self, tag):
        if not self.depth:
            return
        self.depth -= 1
        if self.depth == 0:
            note = " ".join(" ".join(self.parts).split())
            if not re.fullmatch(r"[A-Z]{2}", self.province) or not note:
                raise ValueError("Each article requires data-province='XX' and note text")
            self.notes.append((self.province, note))
            self.province = ""
            self.parts = []

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)


def parse_policy(path: Path) -> list[dict]:
    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")
    parser = PolicyParser()
    parser.feed(path.read_text(encoding="utf-8"))
    if not parser.notes:
        raise ValueError("No <article data-province='XX'> policy notes found")
    return [{"province": province, "policy_note": note, "source_status": demo_status(path)} for province, note in parser.notes]


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def build(canada: Path, national: Path, us: Path, policy: Path, out_dir: Path) -> dict:
    inputs = {"provincial": Path(canada), "national": Path(national), "us": Path(us), "policy": Path(policy)}
    data = {
        "provincial": validate_provinces(inputs["provincial"]),
        "national": validate_national(inputs["national"]),
        "us": validate_us(inputs["us"]),
        "policy": parse_policy(inputs["policy"]),
    }
    warnings = []
    years_ca = {r["year"] for r in data["national"]}
    years_us = {r["year"] for r in data["us"]}
    if years_ca != years_us:
        warnings.append(f"National Canada years {sorted(years_ca)} differ from US years {sorted(years_us)}; dashboard compares overlapping years only.")
    provincial_years = {r["year"] for r in data["provincial"]}
    if not provincial_years.issubset(years_ca):
        warnings.append("Some provincial years lack Canada national benchmark rows.")
    all_demo = all(demo_status(p) == "SYNTHETIC_DEMO" for p in inputs.values())
    mixed_demo = any(demo_status(p) == "SYNTHETIC_DEMO" for p in inputs.values())
    if mixed_demo:
        warnings.insert(0, "DEMO DATA WARNING: At least one input is fictional. Do not report metrics as real kidney transplant facts.")
    warnings.append("Live HTTP/API acquisition and official source verification are NOT implemented in this prototype.")
    warnings.append("Cross-border comparisons require matching population, definitions, reporting periods and inclusion criteria before use with real datasets.")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for key, (filename, fields) in OUTPUTS.items():
        write_csv(out_dir / filename, fields, data[key])
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "prototype_phase": "INITIAL_STARTER_REPOSITORY",
        "all_inputs_synthetic": all_demo,
        "contains_synthetic_data": mixed_demo,
        "inputs": {k: {"filename": v.name, "source_status": demo_status(v)} for k, v in inputs.items()},
        "rows": {k: len(rows) for k, rows in data.items()},
        "comparability": {"country_benchmark_common_years": sorted(years_ca & years_us)},
        "warnings": warnings,
    }
    (out_dir / "quality_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Build synthetic demo (default) or transform supplied datasets")
    parser.add_argument("--canada", type=Path, default=RAW / "DEMO_canada_provincial.csv")
    parser.add_argument("--canada-national", type=Path, default=RAW / "DEMO_canada_national.csv")
    parser.add_argument("--us", type=Path, default=RAW / "DEMO_us_benchmarks.json")
    parser.add_argument("--policy", type=Path, default=RAW / "DEMO_policy_notes.html")
    parser.add_argument("--out", type=Path, default=ROOT / "build")
    args = parser.parse_args()
    report = build(args.canada, args.canada_national, args.us, args.policy, args.out)
    print("Pipeline succeeded. Records:", report["rows"])
    print("Outputs:", args.out.resolve())
    if report["contains_synthetic_data"]:
        print("IMPORTANT: SYNTHETIC DEMO DATA - NOT REAL CIHI/OPTN FINDINGS")
    for warning in report["warnings"]:
        print("WARNING:", warning)


if __name__ == "__main__":
    main()
