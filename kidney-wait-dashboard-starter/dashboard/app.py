"""Optional Streamlit interactive midterm demonstration using validated CSV outputs.

Not a Power BI .pbix. Bundled sample numbers are invented for interface testing.
"""
import json
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build"
st.set_page_config(page_title="Kidney Transplant Wait-Time Prototype", page_icon="🫘", layout="wide")
st.title("Kidney Transplant Waiting-Time Analysis")
st.caption("Group 6 • BSMM 8730 • INITIAL, AI-ASSISTED TECHNICAL PROTOTYPE")

required = ["provincial_metrics.csv", "national_metrics.csv", "us_metrics.csv", "policy_notes.csv", "quality_report.json"]
missing = [name for name in required if not (OUT / name).exists()]
if missing:
    st.error(f"Missing generated files: {', '.join(missing)}. From repository root run: python -m kidney_wait.pipeline")
    st.stop()

province = pd.read_csv(OUT / "provincial_metrics.csv")
canada = pd.read_csv(OUT / "national_metrics.csv")
us = pd.read_csv(OUT / "us_metrics.csv")
policies = pd.read_csv(OUT / "policy_notes.csv")
report = json.loads((OUT / "quality_report.json").read_text(encoding="utf-8"))
if report.get("contains_synthetic_data"):
    st.error("SYNTHETIC DEMONSTRATION DATA — values are fictional. Do not cite as actual CIHI, OPTN/SRTR or provincial policy findings.")
else:
    st.warning("User-supplied data have not been independently authenticated; validate source, definitions and comparability before publishing.")

page1, page2, page3, page4 = st.tabs(["Province metrics", "Canada vs US", "Policy text parser", "Data quality"])
with page1:
    years = sorted(province["year"].unique().tolist())
    year = st.selectbox("Reporting year", years, index=len(years) - 1)
    d = province.loc[province["year"] == year].sort_values("province")
    st.subheader("Provincial snapshot (synthetic sample)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Wait-list patients (sampled provinces)", f"{int(d['waitlist_patients'].sum()):,}")
    c2.metric("Transplants (sampled provinces)", f"{int(d['transplants'].sum()):,}")
    c3.metric("Wait-list deaths (sampled provinces)", f"{int(d['waitlist_deaths'].sum()):,}")
    st.caption("Sampled provinces only. Not a national total, and not a patient-level death rate.")
    st.bar_chart(d.set_index("province_name")[["waitlist_patients", "transplants"]])
    st.dataframe(d.drop(columns=["source_status"]), hide_index=True, use_container_width=True)
with page2:
    st.subheader("Canada vs United States: donor rates per million (synthetic)")
    merged = canada.merge(us, on="year", suffixes=("_canada", "_us"))
    if merged.empty:
        st.warning("No overlapping years.")
    else:
        metric = st.selectbox("Metric", ["deceased_donor_rate_per_million", "living_donor_rate_per_million"])
        frame = merged.set_index("year")[[f"{metric}_canada", f"{metric}_us"]]
        frame.columns = ["Canada", "United States"]
        st.line_chart(frame)
        st.dataframe(frame.reset_index(), hide_index=True, use_container_width=True)
        st.caption("Real benchmarking requires consistent donor definitions, reporting windows and population denominators; this prototype does not verify these.")
with page3:
    st.subheader("Local HTML text extraction proof of concept")
    st.caption("These are explicitly fictional placeholder notes; the app performs NO live provincial-policy scraping.")
    st.dataframe(policies, hide_index=True, use_container_width=True)
with page4:
    st.subheader("Automated pipeline quality report")
    st.json(report)
    st.caption("Replace each DEMO file with appropriately licensed, verified source data before making health-system claims.")
