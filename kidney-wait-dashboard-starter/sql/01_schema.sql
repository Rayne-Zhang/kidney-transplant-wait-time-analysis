-- INITIAL DEMONSTRATION SCHEMA ONLY. Bundled inputs are SYNTHETIC, NOT CIHI/OPTN data.
-- MySQL 8+. Run in MySQL Workbench before python -m kidney_wait.mysql_loader --apply.
CREATE DATABASE IF NOT EXISTS kidney_wait_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE kidney_wait_demo;

CREATE TABLE IF NOT EXISTS province_year_metrics (
    year SMALLINT NOT NULL,
    province CHAR(2) NOT NULL,
    province_name VARCHAR(80) NOT NULL,
    waitlist_patients INT UNSIGNED NOT NULL,
    transplants INT UNSIGNED NOT NULL,
    waitlist_deaths INT UNSIGNED NOT NULL,
    deceased_donors INT UNSIGNED NOT NULL,
    living_donors INT UNSIGNED NOT NULL,
    median_dialysis_to_transplant_years DECIMAL(7,2) NOT NULL,
    deceased_donor_rate_per_million DECIMAL(9,2) NOT NULL,
    living_donor_rate_per_million DECIMAL(9,2) NOT NULL,
    source_status VARCHAR(40) NOT NULL,
    PRIMARY KEY (year, province),
    INDEX idx_province_year (province, year)
);

CREATE TABLE IF NOT EXISTS canada_national_metrics (
    year SMALLINT PRIMARY KEY,
    country VARCHAR(40) NOT NULL,
    waitlist_patients INT UNSIGNED NOT NULL,
    transplants INT UNSIGNED NOT NULL,
    waitlist_deaths INT UNSIGNED NOT NULL,
    median_dialysis_to_transplant_years DECIMAL(7,2) NOT NULL,
    deceased_donor_rate_per_million DECIMAL(9,2) NOT NULL,
    living_donor_rate_per_million DECIMAL(9,2) NOT NULL,
    source_status VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS us_year_metrics (
    year SMALLINT PRIMARY KEY,
    country VARCHAR(40) NOT NULL,
    deceased_donor_rate_per_million DECIMAL(9,2) NOT NULL,
    living_donor_rate_per_million DECIMAL(9,2) NOT NULL,
    source_status VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS provincial_policy_notes (
    note_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    province CHAR(2) NOT NULL,
    policy_note VARCHAR(1000) NOT NULL,
    source_status VARCHAR(40) NOT NULL,
    UNIQUE KEY uq_province_policy (province, policy_note(180))
);
