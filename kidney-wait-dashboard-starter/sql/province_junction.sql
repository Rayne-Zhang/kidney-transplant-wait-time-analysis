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

ALTER TABLE province_junction
ADD COLUMN country_id INT NOT NULL DEFAULT 1 AFTER province;

SELECT * FROM province_junction;