"""Optional MySQL 8+ loader for the validated build/*.csv files.

Dry-run (default) needs no third-party packages and never changes a database.
To load data: pip install -r requirements-mysql.txt, configure env vars, use --apply.
"""
from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

from .pipeline import ROOT

TABLE_FILES = {
    "province_year_metrics": "provincial_metrics.csv",
    "canada_national_metrics": "national_metrics.csv",
    "us_year_metrics": "us_metrics.csv",
    "provincial_policy_notes": "policy_notes.csv",
}


def csv_rows(path: Path) -> tuple[list[str], list[dict]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}; first run python -m kidney_wait.pipeline")
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"Missing header in {path}")
        return reader.fieldnames, list(reader)


def main():
    parser = argparse.ArgumentParser(description="Load build CSVs into MySQL; no writes unless --apply")
    parser.add_argument("--out", type=Path, default=ROOT / "build")
    parser.add_argument("--apply", action="store_true", help="Perform real database writes")
    args = parser.parse_args()
    prepared = []
    for table, filename in TABLE_FILES.items():
        fields, rows = csv_rows(args.out / filename)
        prepared.append((table, fields, rows))
        print(f"{table}: {len(rows)} rows")
    if not args.apply:
        print("DRY RUN ONLY. Create schema with sql/01_schema.sql, then use --apply to load.")
        return

    try:
        import mysql.connector
    except ImportError as exc:
        raise SystemExit("Install dependency first: pip install -r requirements-mysql.txt") from exc
    cfg = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", ""),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "kidney_wait_demo"),
    }
    if not cfg["user"]:
        raise SystemExit("Set MYSQL_USER (and MYSQL_PASSWORD if needed); see .env.example")
    connection = mysql.connector.connect(**cfg)
    try:
        cur = connection.cursor()
        for table, fields, rows in prepared:
            if not rows:
                continue
            # Names originate from this repository's fixed table definitions and validated CSV headers.
            placeholders = ", ".join(["%s"] * len(fields))
            cols = ", ".join(f"`{field}`" for field in fields)
            update_cols = [f for f in fields if f not in ("year", "province", "country", "policy_note")]
            # For policy notes use composite key (province, policy_note); no updates required.
            update = ", ".join(f"`{f}`=VALUES(`{f}`)" for f in update_cols) or "`province`=`province`"
            stmt = f"INSERT INTO `{table}` ({cols}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE {update}"
            for row in rows:
                cur.execute(stmt, [row[f] for f in fields])
        connection.commit()
        print("Committed data to MySQL. These are demo rows if you used the included inputs.")
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if __name__ == "__main__":
    main()
