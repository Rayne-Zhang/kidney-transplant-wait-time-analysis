import csv
import json
import tempfile
import unittest
from pathlib import Path

from kidney_wait.pipeline import ROOT, build, parse_int, parse_policy, validate_provinces, validate_us

RAW = ROOT / "data" / "raw"


class PipelineTests(unittest.TestCase):
    def test_negative_value_fails(self):
        with self.assertRaisesRegex(ValueError, "Negative"):
            parse_int("-1", "waitlist_patients")

    def test_bad_integer_fails(self):
        with self.assertRaises(ValueError):
            parse_int("unknown", "transplants")

    def test_provincial_examples_are_labeled_synthetic(self):
        items = validate_provinces(RAW / "DEMO_canada_provincial.csv")
        self.assertGreater(len(items), 3)
        self.assertTrue(all(r["source_status"] == "SYNTHETIC_DEMO" for r in items))

    def test_us_json_works(self):
        items = validate_us(RAW / "DEMO_us_benchmarks.json")
        self.assertEqual(items[0]["country"], "United States")
        self.assertEqual(len({r["year"] for r in items}), len(items))

    def test_policy_html_parser(self):
        items = parse_policy(RAW / "DEMO_policy_notes.html")
        self.assertEqual(len(items), 3)
        self.assertTrue(all("EXAMPLE ONLY" in r["policy_note"] for r in items))

    def test_duplicate_province_year_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            original = RAW / "DEMO_canada_provincial.csv"
            with original.open(encoding="utf-8", newline="") as source:
                rows = list(csv.DictReader(source))
            with (Path(d) / "duplicate.csv").open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows([rows[0], rows[0]])
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                validate_provinces(Path(d) / "duplicate.csv")

    def test_duplicate_us_year_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "bad.json"
            out.write_text(json.dumps({"records": [
                {"year": 2024, "country": "US", "deceased_donor_rate_per_million": 1, "living_donor_rate_per_million": 1},
                {"year": 2024, "country": "US", "deceased_donor_rate_per_million": 2, "living_donor_rate_per_million": 2},
            ]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                validate_us(out)

    def test_build_generates_expected_csvs_and_quality(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            report = build(RAW / "DEMO_canada_provincial.csv", RAW / "DEMO_canada_national.csv",
                           RAW / "DEMO_us_benchmarks.json", RAW / "DEMO_policy_notes.html", out)
            self.assertTrue(report["all_inputs_synthetic"])
            self.assertTrue((out / "national_metrics.csv").exists())
            self.assertTrue((out / "quality_report.json").exists())
            self.assertEqual(report["comparability"]["country_benchmark_common_years"], [2022, 2023, 2024])


if __name__ == "__main__":
    unittest.main()
