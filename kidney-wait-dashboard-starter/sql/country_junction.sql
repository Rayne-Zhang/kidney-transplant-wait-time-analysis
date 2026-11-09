USE kidney_wait_demo;

CREATE TABLE country_junction (
    country_id INT PRIMARY KEY,
    country VARCHAR(40) NOT NULL UNIQUE
);

INSERT INTO country_junction (country_id, country)
VALUES
    (1, 'Canada'),
    (2, 'United States');

SELECT * FROM country_junction;