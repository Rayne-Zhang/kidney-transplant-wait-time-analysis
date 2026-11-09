-- TRUNCATE TABLE kidney_wait_demo.province_junction;
-- TRUNCATE TABLE kidney_wait_demo.province_year_metrics;

SET @previous_safe_updates = @@SQL_SAFE_UPDATES;
SET SQL_SAFE_UPDATES = 0;

USE kidney_wait_demo;

CREATE TABLE province_junction (
    provinceID INT PRIMARY KEY,
    province VARCHAR(2) NOT NULL UNIQUE
);

INSERT INTO province_junction (provinceID, province)
VALUES
    (1, 'AB'),
    (2, 'BC'),
    (3, 'ON'),
    (4, 'QC');

SELECT * FROM province_junction;

/*
ALTER TABLE province_year_metrics
DROP COLUMN country_id;*/


UPDATE province_year_metrics AS m
JOIN province_junction AS p
    ON m.province = p.province
SET m.provinceID = p.provinceID
WHERE m.provinceID IS NULL;

ALTER TABLE province_year_metrics
ADD COLUMN country VARCHAR(40) NOT NULL DEFAULT 'Canada' AFTER province_name;

ALTER TABLE province_year_metrics
ADD COLUMN country_id INT AFTER country;

SET @previous_safe_updates = @@SESSION.SQL_SAFE_UPDATES;
SET SESSION SQL_SAFE_UPDATES = 0;

UPDATE province_year_metrics AS m
JOIN country_junction AS c
    ON m.country = c.country
SET m.country_id = c.country_id;

SET SESSION SQL_SAFE_UPDATES = @previous_safe_updates;

SELECT *
	From province_year_metrics;