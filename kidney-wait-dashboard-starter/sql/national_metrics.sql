USE kidney_wait_demo;

ALTER TABLE canada_national_metrics
ADD COLUMN country_id INT NOT NULL DEFAULT 1 AFTER year;

SELECT *
	From canada_national_metrics;