# Input Data Dictionary

All input data included in this repository are **synthetic and fictional**. Units and definitions in real CIHI/OPTN files may differ, so do not assume their native formats already match this schema. Do not mix annual counts with patient-level cohorts.

## `DEMO_canada_provincial.csv`

Required columns:

| Column | Type | Meaning in **fictional demonstration** |
|---|---|---|
| year | integer | Sample reporting year |
| province | 2-letter text | Province identifier such as ON |
| province_name | text | Human-readable name |
| waitlist_patients | nonnegative integer | Hypothetical wait-list count in this province-year |
| transplants | nonnegative integer | Hypothetical transplant count |
| waitlist_deaths | nonnegative integer | Hypothetical deaths among wait-listed patients |
| deceased_donors | nonnegative integer | Hypothetical number of deceased donors |
| living_donors | nonnegative integer | Hypothetical number of living donors |
| median_dialysis_to_transplant_years | nonnegative decimal | Hypothetical median years from dialysis to transplantation; **not** universal wait time |
| deceased_donor_rate_per_million | nonnegative decimal | Hypothetical rate per million population |
| living_donor_rate_per_million | nonnegative decimal | Hypothetical rate per million population |

Unique key: `(year, province)`.

## `DEMO_canada_national.csv`

Required columns: `year,country,waitlist_patients,transplants,waitlist_deaths,median_dialysis_to_transplant_years,deceased_donor_rate_per_million,living_donor_rate_per_million`. Country must be `CAN` / `CA` / `Canada`. Unique key: `year`. National rows are **independent** demo figures, not a sum of the limited sample provinces.

## `DEMO_us_benchmarks.json`

Shape: `{ "records": [ { "year": 2022, "country": "US", "deceased_donor_rate_per_million": 0, "living_donor_rate_per_million": 0 } ] }`. Country may be `US`, `USA` or `United States`; unique key: `year`.

## `DEMO_policy_notes.html`

Local `article` blocks of the form `<article data-province="ON"><p>Example only...</p></article>`. This tests text extraction, **not** production web scraping or an authoritative policy database.

## Generated data

Every generated CSV includes `source_status`: `SYNTHETIC_DEMO` for bundled DEMO inputs, otherwise `USER_SUPPLIED_UNVERIFIED`. The JSON quality report includes provenance, counts, common years and warnings. Neither label implies source authenticity.

## Real-data review checklist

Before drawing conclusions, identify cohort definitions, missingness, age adjustment, geography coverage, denominator population and source licensing. Confirm whether CIHI published statistics are directly comparable to OPTN/SRTR measures. Treat a reported median wait time as source-specific rather than universally describing all wait-listed patients.
