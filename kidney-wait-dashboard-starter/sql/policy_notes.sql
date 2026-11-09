USE kidney_wait_demo;

/*ALTER TABLE provincial_policy_notes
	DROP COLUMN note_id;*/
/*
ALTER TABLE provincial_policy_notes
ADD COLUMN country_id INT NOT NULL DEFAULT 1 AFTER province;
*/

ALTER TABLE provincial_policy_notes
ADD COLUMN provinceID INT FIRST;

-- Temporarily disable safe updates
SET @previous_safe_updates = @@SQL_SAFE_UPDATES;
SET SQL_SAFE_UPDATES = 0;

UPDATE provincial_policy_notes AS m
JOIN province_junction AS p
    ON m.province = p.province
SET m.provinceID = p.provinceID
WHERE m.provinceID IS NULL;

SET SQL_SAFE_UPDATES = @previous_safe_updates;

SELECT *
	FROM provincial_policy_notes;

INSERT INTO provincial_policy_notes
    (provinceID, province, country_id, policy_note, source_status)
VALUES
    (1, 'AB', 1,
     'EXAMPLE ONLY: A future verified Alberta policy page will be parsed and documented here.',
     'SYNTHETIC_DEMO');

SELECT *
	FROM provincial_policy_notes;