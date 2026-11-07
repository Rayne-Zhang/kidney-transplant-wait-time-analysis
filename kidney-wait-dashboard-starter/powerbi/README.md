# Power BI — Next Steps (not an actual .pbix file)

The team's **finalized proposal** specifies Microsoft Power BI. This starter does not contain a Power BI project file. The Python pipeline outputs ready-to-import tables in `../build/`.

## How to create an honest Power BI prototype on Windows

1. Open Power BI Desktop → **Get data** → **Text/CSV**.
2. Import `build/provincial_metrics.csv`, `build/national_metrics.csv`, and `build/us_metrics.csv` (and policy notes if needed).
3. Confirm `year` is whole number and count/rate fields are numeric.
4. Make a **provincial wait-list/transplant bar chart** from provincial metrics and a year slicer.
5. Make a **Canada vs US donor rate trend** from separate *national* tables. Model year relationships carefully. Do not sum a country aggregate into a province aggregate.
6. Add a conspicuous title or annotation `SYNTHETIC DEMO DATA — NOT ACTUAL HEALTH STATISTICS` on every demonstration page.
7. Validate source definitions and replace demo data with cited public data before presenting findings.
8. Save a `.pbix` using Power BI Desktop and add it to the repository in a new genuine commit if sharing is permitted.

## Example DAX expressions (only after choosing table and column types)

```dax
Total Sample Waitlist = SUM(provincial_metrics[waitlist_patients])
Total Sample Transplants = SUM(provincial_metrics[transplants])
Total Sample Waitlist Deaths = SUM(provincial_metrics[waitlist_deaths])
```

The totals are aggregates **only of the selected provincial rows and year filters**. They are not national statistics and must not be used as real data.
