**Why Are Patients Waiting So Long to Get New Kidneys in Canada?**

# 1. Data Source Review: CIHI & US OPTN/SRTR Registries

## Overview & Purpose

To evaluate provincial wait-time disparities and benchmark Canadian performance against international standards, our pipeline synthesizes open-access statistics from two primary health data repositories: the Canadian Institute for Health Information (CIHI) and the U.S. Organ Procurement and Transplantation Network / Scientific Registry of Transplant Recipients (OPTN/SRTR).

##

1.1 Key Data Characteristics & Evaluation

| **Source / Metric**    | **CIHI (Canada)**                                                                                                                                                                            | **OPTN / SRTR (United States)**                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Data Structure**     | Structured multi-sheet Excel & CSV aggregate data tables.                                                                                                                                    | Semi-structured JSON / REST APIs and standardized public data reports.                                                   |
| **Coverage Period**    | Multi-year longitudinal series (2021–2025).                                                                                                                                                  | Multi-year longitudinal series (2021–2025).                                                                              |
| **Primary Indicators** | Dialysis-to-transplant median wait time (1,351-day median national benchmark), active/hold wait-list counts, provincial organ donation rates, and donor categories (NDD, DCD, Living, MAID). | Deceased donor rates per million population (PMP), living donor rates PMP, and state-level wait-list outcome benchmarks. |
| **Credibility**        | Authoritative, government-funded national registry (Canadian Organ Replacement Register - CORR).                                                                                             | Standardized national registry maintained under HRSA/U.S. Department of Health and Human Services contract.              |

# 2. Integration & Validation Notes for the Technical Pipeline

<br/>**2.1 Granularity & Grain Alignment**

CIHI statistics report provincial medians and annual aggregate counts, whereas SRTR reports rate-based metrics per million population (PMP). To avoid mathematical distortion, provincial medians are kept at their native grain and are never averaged into synthetic national metrics.

## 2.2 Cross-Border Comparability Rules

Direct comparisons (e.g., Canadian donation rank of 12th vs. U.S. rank of 2nd for deceased / 6th for living donors) are executed only where indicator definitions and reporting periods align. Incompatible or mismatched metrics are flagged or excluded to prevent misleading policy conclusions.

##

<br/><br/>2.3 Database Schema Storage

Raw files and API responses are cleaned via Python (Pandas) and stored in normalized MySQL dimension tables (Dim_Geography, Dim_Time, Dim_Donor_Type) connected to an Observation-grain fact table to ensure 100% data traceability and query integrity