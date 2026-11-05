# Data Governance & Dataset Documentation

## Synthetic Data Notice & Disclaimer
> [!IMPORTANT]
> **ALL DATA IN THIS REPOSITORY IS STRICTLY SYNTHETIC AND SIMULATED.**
> All financial figures, operational statistics, clinical test volumes, realization rates (ARPT), balance sheet schedules, cash flows, and corporate development transaction terms are hypothetical constructs created specifically for financial modelling evaluation and interview assessment (AuraGen Diagnostics Ltd. / MedGenome Business Analyst case study). No confidential, non-public, or proprietary information of any corporate entity has been used.

---

## Dataset Catalog

### 1. `historical_financials.csv`
- **Horizon:** FY2021 – FY2024 (4 Years Audited Historical Actuals)
- **Granularity:** Annual company-wide financial performance
- **Currency:** INR Crores (₹ Cr)
- **Primary Line Items:**
  - `Fiscal_Year`: Financial year indicator (`FY2021` to `FY2024`)
  - `Period_Type`: `Historical`
  - `Data_Classification`: `Synthetic - Simulated Benchmark`
  - Segment Revenues: `Genomics_Revenue_Cr`, `Molecular_Revenue_Cr`, `Routine_Revenue_Cr`, `Clinical_Research_Revenue_Cr`
  - Core P&L: `Total_Revenue_Cr`, `COGS_Reagents_Consumables_Cr`, `Gross_Profit_Cr`, `Total_Opex_Cr`, `EBITDA_Cr`, `EBIT_Cr`, `Net_Profit_Cr`
  - Cash Flows: `Operating_Cash_Flow_Cr`, `Capital_Expenditure_Cr`, `Free_Cash_Flow_Cr`
  - Balance Sheet: `Cash_and_Equivalents_Cr`, `Total_Debt_Cr`, `Total_Assets_Cr`, `Net_Worth_Equity_Cr`

### 2. `operational_data.csv`
- **Horizon:** FY2021 – FY2024
- **Granularity:** Segment-level operational KPIs and quality metrics
- **Metrics Covered:**
  - `Test_Volume_Number`: Total billable clinical tests conducted
  - `Avg_Realization_Per_Test_INR`: Average realization per test (ARPT in INR)
  - `Segment_Revenue_Cr`: Segment top-line (`Volume * ARPT / 10^7`)
  - `Gross_Margin_Pct`: Direct diagnostic gross margin percentage
  - Network Footprint: `Active_Reference_Labs`, `Active_Regional_Labs`, `Active_Collection_Centers`, `B2B_Hospital_Ties`
  - Clinical Quality: `Sample_Rejection_Rate_Pct` (benchmarked at 0.72% by FY24), `Avg_Turnaround_Time_Hours` (reduced to 26h)

### 3. `assumptions.csv`
- **Scope:** Macro, WACC build-up, 5-year operating forecast, cost structure, working capital, and M&A synergy parameters
- **Categories:**
  - `Valuation Parameters`: Risk-free rate (7.10%), ERP (6.00%), Unlevered Beta (0.85), Levered Beta (0.9622), Ke (12.87%), Kd after-tax (6.73%), WACC (11.95%), Terminal Growth (5.0%), Exit Multiple (18.0x)
  - `Base Case Forecast`: Top-line growth rates (22.0% down to 16.0% steady-state)
  - `Operating Cost Ratios`: COGS % of Rev (30.0%), Personnel % (17.5%), Logistics % (8.0%), Lab Opex % (5.0%), SG&A % (3.5%)
  - `Working Capital`: DSO (45 days), DIO (35 days), DPO (50 days)
  - `M&A Acquisition`: Standalone EV (₹2,800.46 Cr), Offer EV (₹3,350.00 Cr), Control Premium (₹549.54 Cr), Total Synergies NPV (₹564.06 Cr), Net Shareholder Value Created (+₹14.52 Cr to +₹129.26 Cr)

### 4. `../powerbi/dashboard_data.csv`
- **Horizon:** FY2021 – FY2029E (9 Years Historical + Forecast)
- **Granularity:** Year × Region (5 Zones) × Segment (4 Diagnostics Segments)
- **Rows:** 180 fully reconciled dimensional records
- **Use Case:** Direct data source for Power BI interactive dashboards, DAX measures, and drill-through reporting.

