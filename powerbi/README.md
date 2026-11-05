# Power BI Analytics Dashboard: AuraGen Diagnostics Ltd.

> **DATA CLASSIFICATION: SYNTHETIC DATA NOTICE**
> All financial figures, volume records, laboratory operations, and M&A metrics in this Power BI model are **synthetic benchmark data** compiled for corporate finance modeling, valuation, and clinical diagnostics case studies.

---

## 1. Overview & Architecture

This Power BI solution delivers an interactive executive BI reporting suite for **AuraGen Diagnostics Ltd.** (simulating an advanced specialized genomics and molecular diagnostics provider).

The dashboard connects directly to `powerbi/dashboard_data.csv` (180 granular rows covering 9 fiscal years: FY21–FY24 Actuals and FY25E–FY29E Forecasts across 5 regions and 4 clinical segments).

### Project File Structure
```
powerbi/
├── AuraGen_Diagnostics_Dashboard.pbip             # Microsoft Power BI Project Master File
├── AuraGen_Diagnostics_Dashboard.Report/          # Report Visuals & Multi-Page Definitions
│   ├── definition.pbir                           # Report-to-Dataset Binding Pointer
│   └── report.json                               # Layout & 4 Interactive Dashboard Pages
├── AuraGen_Diagnostics_Dashboard.SemanticModel/   # Tabular Data Model (TMSL)
│   └── definition.bim                            # Tables, Data Types, Relationships & Measures
├── dashboard_data.csv                            # Source Flat Fact Table (180 rows, 17 cols)
├── DAX_Measures.dax                              # Complete Production DAX Formula Catalog
└── README.md                                     # Technical Setup & Visual Guide
```

---

## 2. Multi-Page Dashboard Blueprint

The report is structured into **4 Executive Reporting Tabs**:

### Page 1: Executive Financial Summary
- **KPI Top-Ribbon Cards**:
  - `Total Revenue`: ₹498.00 Cr (FY24) expanding to ₹1,187.46 Cr (FY29E)
  - `EBITDA`: ₹167.50 Cr (33.63% margin) expanding to ₹427.49 Cr (36.00% margin)
  - `PAT (Net Profit)`: ₹99.90 Cr (20.06% margin) expanding to ₹272.56 Cr (22.95% margin)
  - `Free Cash Flow (FCFF)`: ₹81.90 Cr (FY24) expanding to ₹256.25 Cr (FY29E)
- **Visuals**:
  - Clustered Bar & Line Chart: Total Revenue & EBITDA vs. EBITDA Margin % (9-year horizon)
  - Donut Chart: Revenue Contribution by Diagnostic Modality (Genomics, Molecular, Routine, Clinical Research)
  - Slicer Controls: Fiscal Year Range, Period Type (`Historical` vs. `Forecast`), and Region

### Page 2: Operational & Segment Performance
- **Visuals**:
  - Dual-Axis Combo Chart: Total Annual Test Volumes (Millions) vs. Blended ARPT (₹/test)
  - Treemap: Regional Hub Revenue Penetration (South Hub HQ, West Hub, North Hub, East Hub, International)
  - Stacked Area Chart: Clinical Segment Mix Progression showing Genomics expansion from 24% to 38%
  - Matrix Table: Volume, ARPT, Gross Profit, and Gross Margin % by Segment and Year

### Page 3: DCF Valuation & Sensitivity Matrix
- **Visuals**:
  - Waterfall Chart: Enterprise Value Bridge (PV of Explicit 5-Yr FCFF ₹599.87 Cr + PV of Terminal Value ₹2,200.59 Cr = ₹2,800.46 Cr EV)
  - Net Debt Bridge: Enterprise Value (₹2,800.46 Cr) + Cash (₹110.00 Cr) – Debt (₹45.00 Cr) = Equity Value (₹2,865.46 Cr) / Implied Share Price: ₹573.09
  - Heatmap Matrix: 2D Sensitivity of Enterprise Value across WACC (10.50% – 13.00%) and Perpetual Growth Rate (4.0% – 6.0%)
  - Gauge Visual: FCF-to-EBITDA Conversion Efficiency (Expanding from 37.5% to 59.9%)

### Page 4: M&A Synergies & Accretion Model
- **Visuals**:
  - Synergies vs. Premium Comparison: Total Post-Tax Synergies NPV (₹564.06 Cr) vs. 20% Target Control Premium (₹549.54 Cr)
  - Net Value Creation Card: **+₹14.52 Cr Net Accretion** (+₹2.90 per share)
  - Deal Decision Pill: **"ACCRETIVE (+VALUE CREATION)"**
  - Combined Pro-Forma Enterprise Value: ₹3,364.52 Cr

---

## 3. How to Open, Refresh, and Export to PBIX

### Step 1: Open Power BI Project
Double-click `AuraGen_Diagnostics_Dashboard.pbip` or open **Microsoft Power BI Desktop**, click **File > Open**, and select `AuraGen_Diagnostics_Dashboard.pbip`.

### Step 2: Refresh Data Source
Power BI Desktop automatically detects `dashboard_data.csv` in the same directory. To refresh manually:
1. Click **Home > Transform Data**.
2. If prompted for file path, point the CSV source to `powerbi/dashboard_data.csv`.
3. Click **Close & Apply**.

### Step 3: Export to Standard `.pbix` File
To create a standalone single-file `.pbix`:
1. In Power BI Desktop, click **File > Save As**.
2. Under "Save as type", select **Power BI files (*.pbix)**.
3. Save as `AuraGen_Diagnostics_Dashboard.pbix` in this `powerbi/` folder.

---

## 4. Key DAX Measures Catalog

All measures are implemented in `DAX_Measures.dax`. Selected definitions:

| Measure Name | DAX Expression | Purpose |
| :--- | :--- | :--- |
| **Total Revenue** | `SUM('dashboard_data'[Revenue_Cr])` | Aggregates segment revenue in ₹ Cr |
| **Gross Margin %** | `DIVIDE(SUM('dashboard_data'[Gross_Profit_Cr]), [Total Revenue], 0)` | Diagnostic unit profitability |
| **Total EBITDA** | `SUM('dashboard_data'[EBITDA_Cr])` | Operating cash earnings |
| **EBITDA Margin %** | `DIVIDE([Total EBITDA], [Total Revenue], 0)` | Operational margin efficiency |
| **Blended ARPT** | `DIVIDE([Total Revenue] * 10000000, SUM('dashboard_data'[Test_Volume]), 0)` | Average Realization Per Test (₹) |
| **FCFF Total** | `SUM('dashboard_data'[FCFF_Allocated_Cr])` | Unlevered Free Cash Flow to Firm |
| **Deal Value Creation** | `[M&A Synergies NPV] - [Target Control Premium]` | Net M&A economic accretion (+₹14.52 Cr) |

