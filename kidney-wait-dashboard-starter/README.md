# Kidney Transplant Waiting-Time Analysis — Group 6 (Prototype)

**Course:** BSMM 8730, University of Windsor, Fall 2026  
**Project proposal:** *Why Are Patients Waiting So Long to Get New Kidneys in Canada?*  
**Development stage:** New **initial technical prototype**, not a finished research project.  
**Data warning:** Every included numeric observation and policy note is **SYNTHETIC/fictional**, made only to exercise the code and interface. **No real patient or CIHI/OPTN data are provided.**

This project is an AI-assisted starter implementation based on the team's **finalized** proposal. It offers a reproducible proof of concept for input validation, cross-source transformation, an optional MySQL relational database, a basic dashboard, and Power BI-ready output files.

> **Academic integrity:** Do not claim these files were developed earlier, that the sample metrics are real, or that all three students wrote the same code. GitHub commits must reflect what each contributor actually changes **from now on**. The team should review/test/extend the code, gather reliable source data, and confirm how to disclose AI assistance under course policy.

## Current features (actually implemented)

- Validates a **fictional** provincial Canada CSV (year/province, counts, rate fields).
- Validates a **fictional** Canada-national CSV, stored separately from provincial slices to prevent double-counting.
- Parses a **fictional** U.S. benchmark JSON file.
- Extracts placeholder policy notes from a **local** HTML file. This is **not** a live scraper.
- Checks required fields, duplicate year keys, nonnegative numeric values and cross-source overlapping years.
- Exports normalized CSV files and a JSON quality report to `build/`.
- Includes an interactive **Streamlit demonstration** and Power BI input guidance. Streamlit is **not Power BI**.
- Includes **MySQL 8+ DDL and three example SQL queries**; an optional dry-run / actual loader.
- Includes unit tests and documentation.

## Not yet implemented / still required

- Downloading **verified** source data from CIHI and OPTN/SRTR with provenance and licenses.
- Robust live API requests, authentication and provincial-site web scraping.
- Real population-normalized, definition-matched Canada–U.S. analysis and review by the team.
- An actual `.pbix` Power BI dashboard file, finished user guide and final deployment.
- Individual Git commits, real multi-member history and a live demo recording.

## Quick start — Windows PowerShell

Install **Python 3.10 or later**. Open PowerShell/Terminal in **this extracted project folder**.

```powershell
py -m kidney_wait.pipeline
py -m unittest discover -s tests -v
```

Expected result: the command reports 4 categories of processed rows; the test suite should pass. The outputs are in `build/`. Standard-library ETL and tests need **no pip install**.

For the optional interactive dashboard:

```powershell
py -m pip install -r requirements-dashboard.txt
py -m streamlit run dashboard/app.py
```

A browser opens. Its red banner is intentional: demo observations are **invented**. If PowerShell cannot find `py`, try `python` instead.

### Optional MySQL demonstration

1. Install a **local** MySQL 8+ server and use MySQL Workbench to execute `sql/01_schema.sql`.
2. Test preparation without writing anything:

   ```powershell
   py -m kidney_wait.mysql_loader
   ```

3. Install connector: `py -m pip install -r requirements-mysql.txt`.
4. In the same PowerShell terminal set environment variables (example; use your own password):

   ```powershell
   $env:MYSQL_USER = "root"
   $env:MYSQL_PASSWORD = "YOUR_LOCAL_PASSWORD"
   $env:MYSQL_DATABASE = "kidney_wait_demo"
   py -m kidney_wait.mysql_loader --apply
   ```

5. Execute `sql/02_demo_queries.sql` in Workbench to show sample working queries.

**Do not commit `.env` or real passwords.** MySQL is optional for running the pure-Python pipeline and Streamlit demo.

### Bring your own actual datasets later

The pipeline expects consistent, **year-level aggregated** fields; see `docs/DATA_DICTIONARY.md`. Example:

```powershell
py -m kidney_wait.pipeline --canada data/raw/actual_provinces.csv --canada-national data/raw/actual_national.csv --us data/raw/actual_us.json --policy data/raw/actual_policy.html
```

These inputs must first be prepared to match the documented schema and vetted for accuracy, definitions and usage rights. The pipeline intentionally labels non-`DEMO_` inputs **USER_SUPPLIED_UNVERIFIED** (not “verified”). Never upload private patient records.

## Repository structure

```text
kidney_wait/                Standard-library ETL, policy parser, optional MySQL loader
src: none                   Package lives at repository root for easy execution
Data: data/raw/             Clearly labeled fictional example input files
build/                      Reproducible normalized CSVs + quality_report.json
dashboard/app.py            Optional interactive Streamlit prototype
sql/                        MySQL schema and demonstration queries
powerbi/                    Import instructions and starter DAX measure definitions
tests/                      Automated tests
docs/                       Data dictionary, architecture, team tasks, evidence checklist
```

## Evidence for D.3.1 midterm assignment

Professor's rubric calls for (1) task breakdown/progress (30%), (2) real GitHub version control and team contributions (30%), and (3) demonstration of implemented features (40%). This starter code can contribute to **future** authentic evidence for items (1) and (3) **once the team has run and validated it**. It does **not** itself establish past contributions, a real Git history, live-scraped sources or a completed Power BI deliverable.

See `docs/MIDTERM_EVIDENCE_CHECKLIST.md` and `docs/GITHUB_UPLOAD_GUIDE_ZH.md`.
