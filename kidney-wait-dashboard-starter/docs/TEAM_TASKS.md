# Team Task Plan (proposal-derived roles; not proof of completion)

The finalized proposal names: **Claudine Reid — Data Analyst and Project Manager; Puhua Yang — Data Engineer; Haowei Zhang — Dashboard Developer.** These are the **planned roles**, not evidence that those people have already made code contributions.

| Proposed task ID | Task | Proposed owner | Dependency | Status requiring team confirmation |
|---|---|---|---|---|
| T01 | Confirm scope and collect CIHI/OPTN data | Claudine / Puhua | None | Not verified |
| T02 | Prepare source dictionary and cross-source definitions | Puhua | T01 | Not verified |
| T03 | Implement real-source data ingestion and cleaning | Puhua | T01–T02 | Not verified (starter only implements local demo) |
| T04 | Validate MySQL schema and load verified data | Puhua | T03 | Not verified (schema provided as starter) |
| T05 | Produce EDA and select dashboard indicators | Claudine / Puhua | T04 | Not verified |
| T06 | Design Power BI report and interactions | Haowei | T05 | Not verified (Streamlit interim prototype only) |
| T07 | Validate charts and source accuracy | All | T04–T06 | Not verified |
| T08 | Prepare final report, deployment and presentation | All | T07 | Not verified |
| T09 | Create genuine GitHub / ClickUp history | All | Ongoing | Not verified |

**Suggestion for your next actual contributions:** Claudine can define metrics and verify provenance; Puhua can test/expand ETL/MySQL; Haowei can build Power BI charts based on `build/*.csv`. Each student should independently review the starter, modify code/docs genuinely, test and commit their work. Do not backdate commits.
