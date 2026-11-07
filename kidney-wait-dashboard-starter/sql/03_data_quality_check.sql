USE kidney_wait_demo;

/*
SHOW TABLES FROM kidney_wait_demo;

SELECT *
FROM province_year_metrics;
*/

-- 1.1 Confirm provincial data have been loaded.
SELECT COUNT(*) AS provincial_records
FROM province_year_metrics;

-- 1.2 Confirm national data have benn loaded.
SELECT COUNT(*) AS national_rows
FROM canada_national_metrics;


-- 2.1 Find missing or blank province information.
SELECT *
FROM province_year_metrics
WHERE province IS NULL
   OR TRIM(province) = ''
   OR province_name IS NULL
   OR TRIM(province_name) = '';


-- 2.2 Find missing numerical values in province data.
SELECT *
FROM province_year_metrics
WHERE year IS NULL
   OR waitlist_patients IS NULL
   OR transplants IS NULL
   OR waitlist_deaths IS NULL
   OR deceased_donors IS NULL
   OR living_donors IS NULL
   OR median_dialysis_to_transplant_years IS NULL
   OR deceased_donor_rate_per_million IS NULL
   OR living_donor_rate_per_million IS NULL;


-- 2.3 Find duplicate province-year records in province data.
SELECT year, province, COUNT(*) AS duplicate_count
FROM province_year_metrics
GROUP BY year, province
HAVING COUNT(*) > 1;


-- 2.4 Find invalid negative values in province data.
SELECT *
FROM province_year_metrics
WHERE waitlist_patients < 0
   OR transplants < 0
   OR waitlist_deaths < 0
   OR deceased_donors < 0
   OR living_donors < 0
   OR median_dialysis_to_transplant_years < 0
   OR deceased_donor_rate_per_million < 0
   OR living_donor_rate_per_million < 0;

-- 3.1 Find missing or blank required values for ntional data.
SELECT *
FROM kidney_wait_demo.canada_national_metrics
WHERE year IS NULL
   OR country IS NULL
   OR TRIM(country) = ''
   OR waitlist_patients IS NULL
   OR transplants IS NULL
   OR waitlist_deaths IS NULL
   OR median_dialysis_to_transplant_years IS NULL
   OR deceased_donor_rate_per_million IS NULL
   OR living_donor_rate_per_million IS NULL
   OR source_status IS NULL
   OR TRIM(source_status) = '';


-- 3.2 Find duplicate reporting years for national data.
SELECT year, COUNT(*) AS duplicate_count
FROM kidney_wait_demo.canada_national_metrics
GROUP BY year
HAVING COUNT(*) > 1;


-- 3.3 Find invalid negative values for national data.
SELECT *
FROM kidney_wait_demo.canada_national_metrics
WHERE waitlist_patients < 0
   OR transplants < 0
   OR waitlist_deaths < 0
   OR median_dialysis_to_transplant_years < 0
   OR deceased_donor_rate_per_million < 0
   OR living_donor_rate_per_million < 0;