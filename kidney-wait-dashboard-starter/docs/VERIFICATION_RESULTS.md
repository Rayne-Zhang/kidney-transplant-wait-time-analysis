# Verification performed while preparing the starter package

The following checks actually ran in the project root:

- `python -m kidney_wait.pipeline`: **PASS**; generated 12 synthetic provincial rows, 3 synthetic Canadian national rows, 3 synthetic US rows and 3 fictional policy notes; generated quality report and four CSVs.
- `python -m unittest discover -s tests -v`: **PASS**, all **8** automated tests.
- `python -m kidney_wait.mysql_loader`: **PASS in dry-run mode only**, identifies the four input tables and row counts, no database writes.
- `python -m compileall -q kidney_wait dashboard tests`: **PASS** (Python syntax compilation).

**Not verified in this environment:** the interactive Streamlit dashboard (the `streamlit` package is not installed), MySQL connection/loading/queries (no live MySQL server or connector in use), and any actual Power BI `.pbix` file (not created). Team members should perform and capture the real demonstrations themselves. All sample data is **SYNTHETIC**.
