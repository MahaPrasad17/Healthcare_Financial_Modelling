# Healthcare Diagnostics Financial Modelling & M&A Valuation

[![Python 3.11](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Excel Model](https://img.shields.io/badge/Financial%20Model-Excel%20Audited%20%26%20Reconciled-green.svg)](excel/Healthcare_Financial_Model.xlsx)
[![SQL Dialect](https://img.shields.io/badge/SQL-T--SQL%20Server%20%2F%20ANSI-red.svg)](sql/financial_analysis.sql)
[![Power BI](https://img.shields.io/badge/Power%20BI-PBIP%20%26%20PBIX%20Ready-yellow.svg)](powerbi/AuraGen_Diagnostics_Dashboard.pbip)
[![Audit Status](https://img.shields.io/badge/Audit-100%25%20Verified%20(Zero%20Variance)-brightgreen.svg)](python/validate_model.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

> **DATA CLASSIFICATION: SYNTHETIC DATA NOTICE**  
> All financial statements, operational metrics, test volumes, and M&A transaction parameters presented in this repository are **synthetic benchmark data** compiled for corporate finance modeling, healthcare valuation, and diagnostics business analyst case studies (simulating **AuraGen Diagnostics Ltd.** within a corporate development framework inspired by MedGenome and listed diagnostics peers).

An institutional-grade, corporate development and financial valuation model simulating the financial evaluation, five-year forward projections, Discounted Cash Flow (DCF) valuation, scenario stress-testing, and M&A synergy quantification of a specialized clinical genomics and healthcare diagnostics chain (**AuraGen Diagnostics Ltd.**).

Prepared specifically for candidates interviewing for **Business Analyst** and **Corporate Development** roles at **MedGenome** and leading healthcare investment platforms.

---

## Executive Summary & Reconciled Financial Metrics

| Metric | Historical (FY24 Actual) | Forecast (FY29E Projected) | Growth / Expansion |
|:---|:---:|:---:|:---:|
| **Total Revenue** | ₹498.00 Cr ($60.0M) | ₹1,187.46 Cr ($143.1M) | **18.98% 5-Yr CAGR** (26.67% Hist. CAGR) |
| **Genomics & NGS Revenue** | ₹164.30 Cr (33.0% mix) | ₹451.23 Cr (38.0% mix) | **22.38% 5-Yr CAGR** (40.85% Hist. CAGR) |
| **EBITDA & Margin** | ₹167.50 Cr (**33.63%**) | ₹427.49 Cr (**36.00%**) | **+237 bps Margin Expansion** |
| **Net Profit (PAT)** | ₹99.90 Cr (**20.06%**) | ₹272.56 Cr (**22.95%**) | **+289 bps Margin Expansion** |
| **Free Cash Flow (FCFF)** | ₹81.90 Cr | ₹256.25 Cr | **81.98% Cash Conversion** |
| **Return on Invested Capital (ROIC)** | **29.00%** | **31.50%** | **Industry-leading capital efficiency** |
| **Net Debt Position** | **-₹65.00 Cr (Net Cash)** | **-₹340.00 Cr (Net Cash)** | **Pristine, unleveraged balance sheet** |

### M&A Valuation & Transaction Highlights
- **Weighted Average Cost of Capital (WACC):** **11.95%** ($R_f = 7.10\%$, $\text{ERP} = 6.00\%$, $\beta_U = 0.85$, $\beta_L = 0.9622$, $K_e = 12.87\%$, $K_d = 9.00\%$, $t = 25.17\%$).
- **Standalone DCF Intrinsic Value (Gordon Growth):** **Enterprise Value: ₹2,800.46 Cr** | **Equity Value: ₹2,865.46 Cr** | **Implied Share Price: ₹573.09**.
- **Standalone DCF Intrinsic Value (Exit Multiple 18.0x):** **Enterprise Value: ₹4,975.36 Cr** | **Equity Value: ₹5,040.36 Cr** | **Implied Share Price: ₹1,008.07**.
- **Agreed Acquisition Offer Price:** **Enterprise Value: ₹3,350.00 Cr** (20.0x FY24 Actual EBITDA; 19.6% control premium of ₹549.54 Cr over Gordon Growth EV).
- **Net Present Value (NPV) of Synergies:** **₹564.06 Cr** (PV of 5-Yr Explicit Synergies: ₹112.95 Cr + PV of Terminal Synergies: ₹451.11 Cr).
- **Net Deal Value Creation:** **+₹14.52 Cr Net Accretion** (+₹2.90 per share accretion), confirming the acquisition is **economically accretive and highly recommended**.
- **Pro-Forma Combined Enterprise Value:** **₹3,364.52 Cr** (Standalone EV ₹2,800.46 Cr + Synergies NPV ₹564.06 Cr).

---

## Audit & Repair Changelog (Issues Resolved)

This repository reflects an extensive, independent audit and remediation of all model components:

1. **Eliminated Circular References in Excel:**
   - Fixed self-referencing formulas in `Cash Flow Statement` (Row 13, Row 17, Row 19, Row 20, Row 21).
   - Fixed circular references in `Balance Sheet` (Row 22, 23, 26, 27, 28, 29).
2. **Corrected Cell References:**
   - Replaced all incorrect text column lookups (`Assumptions!C...` to `Assumptions!D...`) across `Operational Drivers`, `Income Statement`, `DCF Valuation`, and `M&A & Synergies`.
   - Corrected operational driver period lag in Column G (aligned to Column F).
3. **Integrated 3-Statement Architecture:**
   - Modeled direct dynamic flow: Income Statement PAT & D&A $\rightarrow$ Cash Flow Statement CFO $\rightarrow$ Net Change in Cash $\rightarrow$ Balance Sheet Cash.
   - Dynamic Gross PP&E addition linked directly to Cash Flow Statement Capex.
4. **Balanced Balance Sheet (Zero Variance):**
   - Verified Assets = Liabilities + Equity with **₹0.00 variance** across all 9 years (FY21 through FY29E).
5. **Reconciled Excel and Python DCF Calculations:**
   - Perfect arithmetic alignment between `Healthcare_Financial_Model.xlsx` and `python/dcf_valuation.py`.
6. **Corrected WACC and Valuation Engine:**
   - WACC mathematically derived at 11.95%; terminal value, EV, and equity value fully reconciled.
7. **Corrected M&A Synergies & Accretion Recommendation:**
   - Phased pre-tax synergies (₹10.20 Cr to ₹70.20 Cr) and post-tax synergies (₹7.63 Cr to ₹52.53 Cr), yielding NPV of ₹564.06 Cr vs. ₹549.54 Cr premium, creating **+₹14.52 Cr net accretion**.
8. **Validated SQL Scripts:**
   - Replaced dialect-specific functions with ANSI `COALESCE`, checked execution integrity, and added synthetic data disclosures.
9. **Clearly Labeled All Synthetic Data:**
   - Explicit disclaimers added across all CSVs, Python scripts, SQL scripts, Excel sheets, and documentation.
10. **Completed Power BI Dashboard Deliverables:**
    - Delivered Microsoft Power BI Project master file (`AuraGen_Diagnostics_Dashboard.pbip`), multi-page layout (`.Report/`), tabular semantic model (`.SemanticModel/`), complete DAX catalog (`DAX_Measures.dax`), and step-by-step export guide to `.pbix`.
11. **Updated Documentation & Added `.gitignore`:**
    - Updated `README.md`, added clean `.gitignore`, synchronized `docs/methodology.md` and `docs/project_conclusions.md`.

---

## Repository Folder Structure

```
Healthcare_Financial_Modelling_Final/
│
├── .gitignore                           # Git ignore rules for Python, Excel, Power BI & OS
├── README.md                            # Project documentation, execution & audit report
├── requirements.txt                     # Python library dependencies
│
├── data/                                # Cleaned input datasets (Synthetic & clearly labeled)
│   ├── README.md                        # Dataset documentation & synthetic data disclaimers
│   ├── historical_financials.csv        # 4-year audited financial actuals (FY21-FY24)
│   ├── operational_data.csv             # Test volumes, ARPT, lab infrastructure, TAT
│   └── assumptions.csv                  # Macro parameters, WACC, growth & cost drivers
│
├── excel/                               # Institutional Excel Financial Model
│   └── Healthcare_Financial_Model.xlsx  # Fully formula-driven, multi-tab integrated model
│
├── sql/                                 # SQL Server (T-SQL) Database & Queries
│   ├── create_tables.sql                # Star schema DDL, indexing & realistic seed data
│   └── financial_analysis.sql           # 15 complex business & corporate finance queries
│
├── python/                              # Automated financial analytics & valuation scripts
│   ├── generate_datasets.py             # Generates historical & projected datasets
│   ├── build_excel_model.py             # OpenPyXL script creating the Excel model
│   ├── data_cleaning.py                 # Schema validation, missing check & identity audit
│   ├── financial_analysis.py            # Financial ratios, ROIC, ROCE, leverage & CAGRs
│   ├── dcf_valuation.py                 # Python DCF valuation engine & sensitivity grids
│   ├── visualizations.py                # Generates publication-grade dashboard charts
│   └── validate_model.py                # Automated audit & mathematical verification suite
│
├── powerbi/                             # Business Intelligence Dashboard Suite
│   ├── AuraGen_Diagnostics_Dashboard.pbip             # Power BI Project Master File
│   ├── AuraGen_Diagnostics_Dashboard.Report/          # 4-page dashboard visual definition
│   │   ├── definition.pbir                           # Report-to-Dataset binding
│   │   └── report.json                               # Layout & visual configuration
│   ├── AuraGen_Diagnostics_Dashboard.SemanticModel/   # Tabular Data Model (TMSL)
│   │   └── definition.bim                            # Tables, columns, M-query & DAX
│   ├── dashboard_data.csv                            # Denormalized 9-year dataset
│   ├── DAX_Measures.dax                              # Complete production DAX formula library
│   └── README.md                                     # Visual blueprint & PBIX export guide
│
├── outputs/                             # Model outputs, charts & exported summaries
│   ├── revenue_trend.png                # 4-panel revenue, EBITDA margin, ARPT & regions
│   ├── financial_analysis.png           # 4-panel ROIC/ROCE, cost structure & sensitivity
│   ├── valuation_summary.csv            # DCF summary table comparing Gordon vs Multiple
│   └── financial_ratios_summary.csv     # Calculated financial ratios summary
│
└── docs/                                # Technical & Investment Documentation
    ├── methodology.md                   # Mathematical formulations, WACC build-up & mechanics
    └── project_conclusions.md           # Corporate Development memo & MedGenome interview prep
```

---

## Step-by-Step Execution & Verification Guide

### 1. Environment Setup & Dependency Installation
```bash
# Clone or navigate to the repaired project folder
cd Healthcare_Financial_Modelling_Final

# Create and activate Python virtual environment
python -m venv venv

# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 2. Run Comprehensive Model Validation
```bash
# Run automated verification suite (audits Excel, Python DCF, Balance Sheet, M&A)
python python/validate_model.py
```

### 3. Run Individual Pipeline Scripts
```bash
# Step 1: Validate accounting identities and raw data schemas
python python/data_cleaning.py

# Step 2: Compute financial ratios, ROIC/ROCE and leverage metrics
python python/financial_analysis.py

# Step 3: Run Python DCF Valuation model and sensitivity grids
python python/dcf_valuation.py

# Step 4: Generate high-resolution publication charts
python python/visualizations.py
```

### 4. Excel Financial Model Navigation
Open `excel/Healthcare_Financial_Model.xlsx` in **Microsoft Excel**:
- **Tab 1: Cover & Contents:** Navigation index, modeling standards, and color conventions.
- **Tab 2: Executive Summary:** Valuation dashboard, scenario matrix, and KPI cards.
- **Tab 3: Assumptions:** Blue hardcoded inputs, CAPM parameters, and WACC derivation (11.95%).
- **Tab 4: Operational Drivers:** Segment volumes, ARPT escalation, and capacity modeling.
- **Tab 5: Income Statement:** 9-year historical and forecast P&L with operating leverage.
- **Tab 6: Balance Sheet:** Balanced asset and liability schedules with dynamic zero check (`₹0.00`).
- **Tab 7: Cash Flow Statement:** Indirect CFO, CFI capex schedule, CFF debt schedule, and cash bridge.
- **Tab 8: DCF Valuation:** FCFF projections, Gordon Growth & Exit Multiple EV, and 2D sensitivity tables.
- **Tab 9: Scenario Analysis:** Dynamic switch between Bear, Base, and Bull operational scenarios.
- **Tab 10: M&A & Synergies:** Transaction valuation, post-tax synergy phasing, and accretive deal bridge.

### 5. Execute SQL Database & Queries
1. Open **SQL Server Management Studio (SSMS)**, **Azure Data Studio**, or any ANSI SQL editor.
2. Execute `sql/create_tables.sql` to instantiate `HealthcareDiagnosticsDW` and populate seed data.
3. Execute `sql/financial_analysis.sql` to run all 15 financial analysis queries.

### 6. Power BI Dashboard Usage
1. Open `powerbi/AuraGen_Diagnostics_Dashboard.pbip` in **Microsoft Power BI Desktop**.
2. To save as a standalone `.pbix` file, click **File > Save As** and select **Power BI files (*.pbix)**.
3. Review `powerbi/DAX_Measures.dax` and `powerbi/README.md` for measure specifications and layout details.

---

## License & Disclaimer

- **License:** Distributed under the MIT License.
- **Disclaimer:** All financial figures, operational volumes, and corporate metrics are entirely **synthetic and simulated** for educational, modeling, and interview preparation purposes. No non-public or proprietary data from MedGenome or any listed entity has been utilized.
