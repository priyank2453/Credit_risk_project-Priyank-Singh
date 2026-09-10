# Credit Risk Analysis — Mortgage Loan Default Prediction

## Overview
End-to-end credit risk analysis of mortgage loan data using SQL, Excel, and Power BI. The project identifies default risk patterns across borrower demographics, loan characteristics, and financial ratios, and builds a validated risk-scoring model to classify borrowers into risk tiers.

## Dataset
- Source: Kaggle — Loan Default Dataset (mortgage-level data)
- Full dataset: 148,670 rows (used in SQL)
- Working sample: 85,258 rows (used in Excel and Power BI, due to an export limitation — see Data Notes)
- Target variable: `Status` (0 = non-default, 1 = default)
- Overall default rate: 24.6%

## Tools & What Each One Did
- **SQL (MySQL)**: Data cleaning, relational thinking, aggregation (GROUP BY), a CTE for risk-tier bucketing, and a window function (RANK) to rank risk by category.
- **Excel**: Built and validated a weighted credit scoring model using normalized risk factors, checked with a Pivot Table against real default outcomes.
- **Power BI**: Interactive dashboard with DAX measures and visuals summarizing findings across risk tiers, region, and loan purpose.

## Key Findings
- Loan purpose **p2** has the highest default rate (33.08%) vs. p3/p4 (~23–25%).
- **North-East region** defaults at 30.45%, notably higher than North (22.51%), despite having far fewer loans.
- Default rate follows a U-shaped pattern by age — highest among borrowers **under 25** (28.95%) and **over 74** (30.01%), lowest for the 25–44 range (~22%).
- A custom-built **risk-tier model** (based on LTV and DTI thresholds) confirmed High Risk loans default at 23.72% vs. 11.33% for Low Risk — validating the tiering logic.
- Loans with **missing LTV/DTI data** default at 67.61% — nearly 3x the highest known-risk tier. This suggests incomplete financial documentation is itself a meaningful risk signal, not just a data gap.
- Built a **weighted credit scoring model** in Excel (Credit Score 35%, LTV 25%, DTI 25%, Income 15%, each normalized to a 0–100 scale) — validated against actual outcomes: High Risk borrowers default at 62.85%, Medium Risk at 28.38%, Low Risk at 14.09%.

## Data Notes & Known Limitations
- 200 records had missing/blank `age` values, showing a 100% default rate in early exploration — likely a data entry issue, excluded from age-based analysis rather than assumed accurate.
- `loan_purpose` values are coded (p1–p4) without descriptive labels in the source data — analyzed as-is; category meanings unknown.
- Initial risk-tier logic incorrectly classified loans with NULL LTV/DTI values as "Low Risk" by default (SQL CASE statements treat NULL comparisons as false). Fixed by adding an explicit "Unknown - Missing Data" tier — this also surfaced a meaningful finding (see Key Findings).
- Initial scoring-model normalization formulas used assumed reference values (credit score max of 850, income max from raw data) which produced invalid results (negative scores, income skewed by a single outlier). Corrected using actual data-driven values: real max credit score (900) and 95th percentile income (15,360) instead of raw max, to avoid outlier distortion.
- Excel/Power BI analysis was performed on a sample of 85,258 rows (from the full 148,670-row dataset used in SQL) due to a row-limit setting during CSV export. Sample size remains statistically robust for the analysis performed.

## Project Structure
- `import_data.py` — Python script to load raw CSV into MySQL
- SQL queries — cleaning, exploratory analysis, CTE risk-tier segmentation, window-function ranking
- `loan_data_clean.csv`, `risk_tier_summary.csv`, `loan_purpose_rank.csv` — exported SQL results
- `credit_risk_analysis.xlsx` — cleaned data, scoring model, Pivot Table validation
- Power BI report (.pbix) — interactive dashboard