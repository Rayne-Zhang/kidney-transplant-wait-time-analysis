# Kidney Transplant Waiting-Time Analysis — Group 6

**Course:** BSMM 8730 — Data Acquisition and Management (Fall 2026), University of Windsor  
**Project:** *Why Are Patients Waiting So Long to Get New Kidneys in Canada?*  
**Repository status:** Midterm technical prototype using synthetic data. Official data analysis and the final Power BI dashboard remain in progress.

> **Important:** All bundled observations and policy notes are **synthetic demonstration data**. They are fictional and must **not** be described as actual CIHI/OPTN/SRTR findings. This repository does not contain patient records or an authenticated healthcare analysis.

## Find the project files

The working project currently resides in the [`kidney-wait-dashboard-starter/`](kidney-wait-dashboard-starter/) folder:

| Location | Purpose |
| --- | --- |
| [`kidney_wait/`](kidney_wait/) | Python validation, transformation, and optional MySQL loader |
| [`data/raw/`](data/raw/) | Clearly marked `DEMO_` input datasets |
| [`build/`](build/) | Generated synthetic metrics and quality report |
| [`dashboard/app.py`](dashboard/app.py) | Streamlit interactive demonstration (not Power BI) |
| [`sql/`](sql/) | MySQL 8+ schema and example queries |
| [`powerbi/`](powerbi/) | Power BI instructions; no `.pbix` has been created |
| [`tests/`](tests/) | Automated unit tests |
| [`docs/`](docs/) | Architecture, data dictionary, planned team roles, evidence checklist |

Read the [architecture documentation](docs/ARCHITECTURE.md) for implementation details, project limitations, and next steps.

## Reproduce the current Python checks

Install Python 3.10+ and open a terminal in the repository root:

```powershell
cd kidney-wait-dashboard-starter
py -m kidney_wait.pipeline
py -m unittest discover -s tests -v
py -m kidney_wait.mysql_loader
```

The final command is **dry-run only** and does not prove a real MySQL database connection. The optional Streamlit demo can be started after installing dependencies:

```powershell
py -m pip install -r requirements-dashboard.txt
py -m streamlit run dashboard/app.py
```

**Current limitations:** No verified official-data acquisition, no live web/API ingestion, no deployed MySQL database evidence, and no completed Power BI `.pbix`. Team member contributions must be reflected through their genuine GitHub actions, not inferred from the proposed task assignments.

## Midterm evidence and roles

- [Task plan and proposed team responsibilities](kidney-wait-dashboard-starter/docs/TEAM_TASKS.md)
- [Midterm evidence checklist](kidney-wait-dashboard-starter/docs/MIDTERM_EVIDENCE_CHECKLIST.md)
- [Architecture](kidney-wait-dashboard-starter/docs/ARCHITECTURE.md)
- [AI assistance and verification note](docs/AI_ASSISTANCE_NOTE.md)

This root-level README was added to help reviewers navigate the existing nested project directory; no historical development or team contribution is implied.
