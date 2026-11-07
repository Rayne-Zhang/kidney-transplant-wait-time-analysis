# Technical Architecture — Initial Prototype

## Proposed project versus actual prototype

Finalized team proposal: CIHI structured tables + U.S. OPTN/SRTR JSON/API + official provincial web policy pages → Python cleaning → MySQL → Power BI, managed through GitHub + ClickUp.

Implemented **today in this new starter**:

```text
LOCAL DEMO canada_provincial.csv ─┐
LOCAL DEMO canada_national.csv  ──┤
LOCAL DEMO us_benchmarks.json   ──┼── Python validation and transformation ── build/*.csv
LOCAL DEMO policy_notes.html    ──┘                   │                     ├─ Streamlit demo
                                                     └─ quality_report.json └─ Power BI import candidates
                                                                          └─ Optional MySQL loader
```

- No live URL queries or API requests are performed.
- All DEMO sources are synthetic. Source identity is preserved in `source_status` in each output.
- Separate Canada national data from provincial slices; they should not be summed together.
- The U.S. benchmark values are country-level, not province or state-level.
- This is not a medical decision system and should not be used for actual healthcare planning.

## Next engineering steps

1. Obtain permissible verified public CIHI and OPTN/SRTR source tables, with citations, timestamps and definitions.
2. Document source transformations and harmonize denominator, years, definitions and reporting coverage.
3. Implement audited data acquisition rather than manual staging, including error handling and reproducibility.
4. Validate data against published counts and rates; add non-synthetic regression fixtures.
5. Create the final Power BI `.pbix`, connect to MySQL or vetted CSV exports, check every visual.
6. Record genuine per-person Git commits, run demo and fill project report from evidence.
