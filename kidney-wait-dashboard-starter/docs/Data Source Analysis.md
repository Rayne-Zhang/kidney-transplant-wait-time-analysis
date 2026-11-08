**Why Are Patients Waiting So Long to Get New Kidneys in Canada?**

# 1. Data Source Review: CIHI & US OPTN/SRTR Registries

## Overview & Purpose

This document reviews CIHI and OPTN/SRTR as potential sources for comparing kidney transplant waiting times in Canada and the United States. The current technical prototype uses synthetic demonstration data. Official data acquisition and analysis remain future tasks.

##

1.1 Key Data Characteristics & Evaluation

| **Source / Metric**    | **CIHI (Canada)**                                                                                                                                                                            | **OPTN / SRTR (United States)**                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Data Structure**     | Structured multi-sheet Excel & CSV aggregate data tables.                                                                                                                                    | Semi-structured JSON / REST APIs and standardized public data reports.                                                   |
| **Coverage Period**    | Multi-year longitudinal series (2021–2025).                                                                                                                                                  | Multi-year longitudinal series (2021–2025).                                                                              |
| **Primary Indicators** | Dialysis-to-transplant median wait time , active/hold wait-list counts, provincial organ donation rates, and donor categories (NDD, DCD, Living, MAID). | Deceased donor rates per million population (PMP), living donor rates PMP, and state-level wait-list outcome benchmarks. |
| **Credibility**        | Authoritative, government-funded national registry (Canadian Organ Replacement Register - CORR).                                                                                             | Standardized national registry maintained under HRSA/U.S. Department of Health and Human Services contract.              |

# 2. Integration & Validation Notes for the Technical Pipeline

<br/>**2.1 Granularity & Grain Alignment**

CIHI statistics report provincial medians and annual aggregate counts, whereas SRTR reports rate-based metrics per million population (PMP). To avoid mathematical distortion, provincial medians are kept at their native grain and are never averaged into synthetic national metrics.

<br/> **2.2  Cross-Border Comparability Rules**

For the final analysis, cross-border comparisons will be conducted only when indicator definitions, reporting periods, and population denominators are comparable. Incompatible metrics will be flagged or excluded.

<br/> **2.3 Database Schema Storage**


The current prototype validates and transforms local synthetic CSV, JSON, and HTML inputs using Python's standard library. The processed data can be loaded into four demonstration MySQL tables. Live API ingestion, official-source verification, and the proposed dimensional database design remain future development tasks.

