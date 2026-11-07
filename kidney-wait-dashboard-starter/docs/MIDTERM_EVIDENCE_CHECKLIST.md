# D.3.1 Midterm — Evidence Checklist (as of initial starter repository)

**IMPORTANT:** This repository is **new**. It cannot prove earlier GitHub work or historical progress. The team must verify the actual state before labeling tasks "Completed" in a graded report.

| Grading component | Weight | Evidence available from this starter | Still required |
|---|---:|---|---|
| Progress task breakdown | 30% | Initial architecture, task plan, staged runnable demo | Team-confirmed actual status, dependency sequencing, dates, ClickUp evidence |
| GitHub & version control | 30% | Files ready for initial commit | Actual remote repo URL, real commit history, evidence each student's changes, meaningful commit messages |
| Demonstration of completed work | 40% | Local ETL, local HTML parser, CSV outputs, Streamlit app, MySQL SQL examples, tests | Run and verify locally; screenshots/live demo showing actual results, MySQL table/query evidence if claiming MySQL use |

## Suggested live walkthrough (only after verifying on a real computer)

1. Run `py -m unittest discover -s tests -v` and show test results.
2. Run `py -m kidney_wait.pipeline` and show build outputs + `quality_report.json`.
3. Run `py -m streamlit run dashboard/app.py` and filter a sample year; prominently explain **fictional demo data**.
4. Optional: show Workbench tables/working SQL if MySQL schema was **actually installed and data loaded**.
5. Show GitHub real repository URL, commit graph and contributors from their real account actions.

## Assignment deliverables (separate)

- D.3.1: **4-page English PDF group status report**; report body in paragraph form, no bullet-only report, describe novelty and real work.
- D.3.1.1: Team contribution form as required by Brightspace; check template course header carefully.
- D.3.2: Each member's own **minimum two-page** individual contribution report, submitted in **separate** Brightspace dropbox.

Project deadline in provided professor instructions: **Nov 8, 2026 at 11:59 PM**. Do not assume simply uploading starter files to GitHub fulfills the rubric.
