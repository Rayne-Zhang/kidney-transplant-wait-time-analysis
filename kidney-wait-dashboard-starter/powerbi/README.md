Power BI Dashboard — Prototype & Implementation Guide

⚠️ DATA SCOPE & DISCLAIMER:

The figures presented in this dashboard reflect actual sampled metrics sourced from project datasets across selected participating provinces (AB, BC, ON, QC) for 2022–2024.

SAMPLED DATASET — NOT FULL NATIONAL TOTALS

Provincial aggregates represent participating reporting units only and are not complete national totals. Wait-list deaths represent raw reported cohort deaths on active waitlists and must not be interpreted as overall patient-level mortality rates.

📁 Repository Contents & File Structure

This repository contains the complete Power BI project along with the underlying dataset files:

📊 Updated Midterm Demo Report Kidney Wait Time Analysis.pbix: The primary Power BI report containing all pre-built dashboards, data models, DAX measures, dynamic slicers, and multi-visual layouts.

📁 ../build/: Contains the source data tables exported from the project pipeline:

provincial_metrics.csv — Sampled provincial wait-list, transplant, and mortality counts.

national_metrics.csv — Canadian national donor rate metrics per million.

us_metrics.csv — United States national donor rate metrics per million.

provincial_policy_notes.csv — Policy metadata used for context tooltips.

🚀 Quick Start: Opening the Project

Open Power BI Desktop on Windows.

Open Updated Midterm Demo Report Kidney Wait Time Analysis.pbix directly from the root repository folder.

If prompt for data sources appears, navigate to Transform Data → Data Source Settings and re-point the sources to your local ../build/ directory.

📊 Dashboard Visualizations Overview

The completed .pbix file includes three primary report pages:

1. Provincial Snapshot (Figure 4a)

Interactive Year Slicer: Dynamically filters provincial metrics across 2022, 2023, and 2024.

KPI Summary Cards: Real-time summary of sampled wait-list patients, transplants, and wait-list deaths.

Provincial Comparison Charts: Visualizes wait-list volume versus successful transplants broken down by participating province.

2. International Donor Rate Comparison (Figure 4b)

Canada vs. U.S. Trend Line: Compares deceased donor rates per million population across 2022–2024 between Canada and the United States.

Appended National Table (National_Donor_Rates): Combines Canadian and U.S. national metrics to plot both trend lines cleanly on a single axis using the legend dimension.

3. Wait-List Outcomes & Donor Mix

Outcome Funnel Chart: Displays the progression from total active wait-list patients down to successful transplants and wait-list mortality.

Living vs. Deceased Donor Split: 100% stacked bar chart analyzing the proportion of living vs. deceased organ donor rates.

📐 Data Model & Key DAX Measures

Data Modeling Architecture

Aggregate Isolation: National tables (canada_national_metrics, us_year_metrics) are kept separate from provincial granular records to avoid invalid rollups.

Cross-Country Analysis: Built via Power Query table appending (National_Donor_Rates) with relationships to country and year.
