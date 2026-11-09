USE kidney_wait_demo;

ALTER TABLE us_year_metrics
ADD COLUMN country_id INT AFTER country;

SET @previous_safe_updates = @@SESSION.SQL_SAFE_UPDATES;
SET SESSION SQL_SAFE_UPDATES = 0;

UPDATE us_year_metrics AS m
JOIN country_junction AS c
    ON m.country = c.country
SET m.country_id = c.country_id;

SET SESSION SQL_SAFE_UPDATES = @previous_safe_updates;

SELECT *
	FROM us_year_metrics