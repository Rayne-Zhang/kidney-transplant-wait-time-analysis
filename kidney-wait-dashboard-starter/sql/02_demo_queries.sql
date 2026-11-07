-- IMPORTANT: results are SYNTHETIC / DEMONSTRATION ONLY if bundled data were loaded.
USE kidney_wait_demo;

-- Query 1: available provinces and reporting years
SELECT year, province, waitlist_patients, transplants
FROM province_year_metrics ORDER BY year, province;

-- Query 2: illustration of waiting-list volume by province (latest demo year)
SELECT province_name, waitlist_patients
FROM province_year_metrics
WHERE year = (SELECT MAX(year) FROM province_year_metrics)
ORDER BY waitlist_patients DESC;

-- Query 3: Canada and US comparable-named donor-rate fields by year
-- This is a schema demonstration, NOT a scientifically validated comparison.
SELECT ca.year, ca.deceased_donor_rate_per_million AS canada_deceased_rate,
       us.deceased_donor_rate_per_million AS us_deceased_rate,
       ca.living_donor_rate_per_million AS canada_living_rate,
       us.living_donor_rate_per_million AS us_living_rate
FROM canada_national_metrics ca
JOIN us_year_metrics us ON ca.year = us.year
ORDER BY ca.year;
