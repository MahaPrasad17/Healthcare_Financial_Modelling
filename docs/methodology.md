# Financial Modelling & M&A Valuation Methodology

> **DATA CLASSIFICATION & SIMULATED BENCHMARK NOTICE**  
> All financial statements, operational metrics, test volumes, and M&A transaction parameters presented in this documentation and associated models are **synthetic benchmark data** compiled for corporate finance modeling, healthcare valuation, and diagnostics business analyst case studies (simulating AuraGen Diagnostics Ltd. / MedGenome evaluation framework).

**Project:** Healthcare Diagnostics Financial Modelling & M&A Valuation  
**Target Entity:** AuraGen Diagnostics Ltd. (Hypothetical Clinical Diagnostics & Genomics Chain)  
**Context:** Corporate Development & Business Analyst Valuation Framework (MedGenome Evaluation)  

---

## 1. Executive Overview

This document provides a formal, institutional-grade description of the quantitative models, accounting mechanics, and corporate finance methodologies implemented across the **Excel Financial Model**, **Python DCF Engine**, **SQL Server Analytical Data Warehouse**, and **Power BI KPI Dashboard**.

The objective is to rigorously simulate the end-to-end financial analysis, five-year forward forecasting, Discounted Cash Flow (DCF) valuation, scenario stress-testing, and M&A synergy quantification of a high-growth healthcare diagnostics and clinical genomics business.

---

## 2. Integrated 3-Statement Financial Modeling Framework

### 2.1 Revenue Build-Up Methodology: Volume $\times$ ARPT
Rather than applying arbitrary percentage top-line growth, revenue is built bottom-up through operational drivers across four distinct diagnostic segments:
$$\text{Revenue}_{t} = \sum_{i=1}^{4} \left( \text{Test Volume}_{i,t} \times \text{ARPT}_{i,t} \right)$$

Where $i$ denotes the segment:
1. **Routine Biochemistry & Hematology (Standard Volume):** Characterized by high test volumes (1.85M tests in FY21 growing to 2.75M in FY24, and 3.90M by FY29E) and low-to-moderate realization (₹530 to ₹561 per test in historical years, rising to ₹792 by FY29E). Serves as a customer acquisition channel and baseline operating cash generator.
2. **Molecular & Infectious Diagnostics (High-Margin):** Realization ranging from ₹1,974 to ₹2,160 per test.
3. **Genomics & Next-Generation Sequencing (NGS) (Super-Premium):** High barrier to entry, oncology sequencing, non-invasive prenatal testing (NIPT), and rare disease genetic panels. Realization ranging from ₹13,067 to ₹13,924 per test (rising to ₹16,230 by FY29E). Volume expanded from 45,000 tests in FY21 to 118,000 tests in FY24 (40.8% CAGR), projected to reach 278,000 tests by FY29E.
4. **Clinical Research & Pharma Biomarkers (High-Margin B2B):** Contract sequencing for global biotechnology and pharmaceutical clinical trials with average project realization of ₹51,923 to ₹56,348 per project batch (rising to ₹67,860 by FY29E).

### 2.2 Cost Structure & Operating Leverage Dynamics
Costs are structured into variable direct costs and operational overheads to model economies of scale:
- **Cost of Goods Sold (COGS - Reagents & Consumables):** Modeled as a declining percentage of revenue (from 33.3% in FY21 down to 30.0% by FY25E–FY29E) as volume scale unlocks bulk sequencer cartridge and chemical reagent procurement discounts.
- **Personnel Expenses:** Reflects compensation for board-certified pathologists, molecular biologists, clinical geneticists, bioinformaticians, and phlebotomists. Scales from 19.6% down to 17.5% of revenue.
- **Cold-Chain Logistics:** Critical operational cost for temperature-controlled specimen integrity across collection centers and regional hub laboratories (stabilizing at 8.0% of revenue).
- **Laboratory Opex & Accreditations:** Machine calibration, CAP/NABL proficiency testing, and lab utilities (stabilizing at 5.0% of revenue).
- **Selling, General & Administrative (SG&A):** Doctor outreach, hospital B2B institutional sales, LIMS IT software licenses, and executive overhead (modeled at 3.5% of revenue).

### 2.3 Balance Sheet & Working Capital Mechanics
- **Days Sales Outstanding (DSO):** 45.0 days, reflecting B2B hospital and pharma receivables.
  $$\text{Trade Receivables}_{t} = \frac{\text{Revenue}_{t} \times \text{DSO}}{365}$$
- **Days Inventory Outstanding (DIO):** 35.0 days, ensuring buffer stocks of perishable sequencing flow cells and reagent test kits.
  $$\text{Inventories}_{t} = \frac{\text{COGS}_{t} \times \text{DIO}}{365}$$
- **Days Payable Outstanding (DPO):** 50.0 days, reflecting trade credit terms negotiated with diagnostic instrument and reagent vendors.
  $$\text{Trade Payables}_{t} = \frac{\text{COGS}_{t} \times \text{DPO}}{365}$$
- **Fixed Assets Schedule:**
  $$\text{Net PP\&E}_{t} = \text{Net PP\&E}_{t-1} + \text{Capex}_{t} - \text{Depreciation}_{t}$$
- **Dynamic Cash Flow Integration:**
  Ending cash on the Balance Sheet is strictly linked to ending cash from the Cash Flow Statement:
  $$\text{Cash}_{t} = \text{Cash}_{t-1} + \text{Net Change in Cash}_{t}$$
- **Balance Sheet Integrity Check:**
  $$\text{Integrity Check} = \text{ROUND}(\text{Total Assets}_{t} - (\text{Total Liabilities}_{t} + \text{Total Equity}_{t}), 2) \equiv 0.00$$

### 2.4 Cash Flow Statement Reconciliation
- **Operating Cash Flow (CFO):** Built via the Indirect Method:
  $$\text{CFO}_{t} = \text{PAT}_{t} + \text{D\&A}_{t} - \Delta \text{NWC}_{t}$$
- **Investing Cash Flow (CFI):** Capital expenditure for expanding regional sequencing hubs and installing automated Illumina/MGI sequencers.
- **Financing Cash Flow (CFF):** Term debt amortization and interest servicing.

---

## 3. Discounted Cash Flow (DCF) Valuation Mechanics

### 3.1 Weighted Average Cost of Capital (WACC) Build-Up
The discount rate is estimated using the **Capital Asset Pricing Model (CAPM)** based on Indian sovereign and healthcare market benchmarks:
$$\text{WACC} = \left( \frac{E}{V} \times K_e \right) + \left( \frac{D}{V} \times K_d \times (1 - t) \right)$$

1. **Risk-Free Benchmark Rate ($R_f$):** **7.10%**, derived from the 10-year Indian Government Benchmark Bond (G-Sec).
2. **Equity Risk Premium (ERP):** **6.00%**, benchmark emerging market risk premium above risk-free sovereign securities.
3. **Unlevered Industry Asset Beta ($\beta_U$):** **0.85**, derived from median listed healthcare and diagnostic comparables (Dr Lal PathLabs, Metropolis Healthcare, Vijaya Diagnostic).
4. **Target Capital Structure:** 15.0% Debt ($\frac{D}{V}$) and 85.0% Equity ($\frac{E}{V}$), reflecting conservative healthcare diagnostic borrowing profiles.
5. **Re-Levered Equity Beta ($\beta_L$):**
   $$\beta_L = \beta_U \times \left[ 1 + (1 - t) \times \left( \frac{D}{E} \right) \right] = 0.85 \times \left[ 1 + (1 - 0.2517) \times \left( \frac{0.15}{0.85} \right) \right] = \mathbf{0.9622}$$
6. **Cost of Equity ($K_e$):**
   $$K_e = R_f + \beta_L \times \text{ERP} = 7.10\% + (0.9622 \times 6.00\%) = \mathbf{12.87\%}$$
7. **Cost of Debt ($K_d$) & Tax Shield:** Pre-tax borrowing rate of **9.00%**. At a statutory corporate tax rate of **25.17%** (Section 115BAA):
   $$K_{d,\text{after-tax}} = 9.00\% \times (1 - 0.2517) = \mathbf{6.73\%}$$
8. **Final Calculated WACC:**
   $$\text{WACC} = (0.85 \times 12.87\%) + (0.15 \times 6.73\%) = 10.94\% + 1.01\% = \mathbf{11.95\%}$$

### 3.2 Unlevered Free Cash Flow to Firm (FCFF) Formula
$$\text{FCFF}_{t} = \text{NOPAT}_{t} + \text{D\&A}_{t} - \text{Capex}_{t} - \Delta \text{NWC}_{t}$$
Where $\text{NOPAT}_{t} = \text{EBIT}_{t} \times (1 - t)$.

Cash flows are discounted using the end-of-year convention:
$$\text{PV}(\text{FCFF}_{t}) = \frac{\text{FCFF}_{t}}{(1 + \text{WACC})^t}$$

### 3.3 Terminal Value (TV) Formulation
Two distinct methodologies are modeled and reconciled:

#### Method 1: Gordon Growth Model (Perpetual Growth)
Assumes the business reaches steady-state perpetual growth aligned with long-term healthcare expenditure expansion:
$$\text{TV}_{\text{Gordon}} = \frac{\text{FCFF}_{2029E} \times (1 + g)}{\text{WACC} - g} = \frac{₹256.25\text{ Cr} \times (1 + 0.05)}{0.1195 - 0.05} = ₹3,870.00\text{ Cr}$$
$$\text{PV}(\text{TV}_{\text{Gordon}}) = ₹3,870.00\text{ Cr} \times \frac{1}{(1 + 0.1195)^5} = ₹2,200.59\text{ Cr}$$

#### Method 2: Exit Multiple Method
Assumes the company is divested or recapitalized at an implied Enterprise Value / EBITDA multiple consistent with diagnostic transaction benchmarks:
$$\text{TV}_{\text{Multiple}} = \text{EBITDA}_{2029E} \times 18.0\text{x} = ₹427.49\text{ Cr} \times 18.0 = ₹7,694.82\text{ Cr}$$
$$\text{PV}(\text{TV}_{\text{Multiple}}) = ₹7,694.82\text{ Cr} \times \frac{1}{(1 + 0.1195)^5} = ₹4,375.49\text{ Cr}$$

### 3.4 Enterprise Value to Equity Value Bridge
$$\text{Cumulative Explicit PV of FCFF (FY25E–FY29E)} = ₹599.87\text{ Cr}$$
$$\text{Enterprise Value (Gordon Growth)} = ₹599.87\text{ Cr} + ₹2,200.59\text{ Cr} = \mathbf{₹2,800.46\text{ Cr}}$$
$$\text{Enterprise Value (Exit Multiple)} = ₹599.87\text{ Cr} + ₹4,375.49\text{ Cr} = \mathbf{₹4,975.36\text{ Cr}}$$
$$\text{Net Debt} = \text{Total Debt}_{\text{FY24}} - \text{Cash}_{\text{FY24}} = ₹45.00\text{ Cr} - ₹110.00\text{ Cr} = -₹65.00\text{ Cr (Net Cash)}$$
$$\text{Equity Value (Gordon Growth)} = ₹2,800.46\text{ Cr} - (-₹65.00\text{ Cr}) = \mathbf{₹2,865.46\text{ Cr}}$$
$$\text{Equity Value (Exit Multiple)} = ₹4,975.36\text{ Cr} - (-₹65.00\text{ Cr}) = \mathbf{₹5,040.36\text{ Cr}}$$
$$\text{Implied Intrinsic Share Price (Gordon Growth)} = \frac{₹2,865.46\text{ Cr}}{5.00\text{ Cr shares}} = \mathbf{₹573.09\text{ per share}}$$
$$\text{Implied Intrinsic Share Price (Exit Multiple)} = \frac{₹5,040.36\text{ Cr}}{5.00\text{ Cr shares}} = \mathbf{₹1,008.07\text{ per share}}$$

---

## 4. Scenario Analysis & Stress-Testing

| Strategic / Valuation Metric | Bear Case (Worst) | Base Case (Expected) | Bull Case (Best) |
|:---|:---:|:---:|:---:|
| **Genomics & NGS Revenue CAGR** | 16.0% | 28.0% | 35.0% |
| **Blended 5-Year Revenue CAGR** | 12.5% | 18.9% | 24.5% |
| **Average EBITDA Margin** | 29.5% | 35.1% | 38.5% |
| **WACC Discount Rate** | 13.00% | 11.95% | 10.75% |
| **Terminal Growth Rate ($g$)** | 4.0% | 5.0% | 6.0% |
| **Exit Multiple (EV / EBITDA)** | 14.0x | 18.0x | 22.0x |
| **FY29E Terminal Revenue** | ₹801.2 Cr | ₹1,187.5 Cr | ₹1,492.3 Cr |
| **FY29E Terminal EBITDA** | ₹236.4 Cr | ₹427.5 Cr | ₹574.5 Cr |
| **Implied Enterprise Value (Gordon)** | ₹2,015.4 Cr | **₹2,800.5 Cr** | ₹4,235.8 Cr |
| **Implied Equity Value** | ₹2,080.4 Cr | **₹2,865.5 Cr** | ₹4,300.8 Cr |
| **Implied Value Per Share** | **₹416.08** | **₹573.09** | **₹860.16** |

---

## 5. M&A Acquisition Pricing & Synergy Valuation Framework

### 5.1 Transaction Valuation Offer & Structure
- **Target Standalone Enterprise Value (DCF):** **₹2,800.46 Cr**
- **Target Standalone Equity Value (DCF):** **₹2,865.46 Cr**
- **Agreed Acquisition Enterprise Value:** **₹3,350.00 Cr** (20.0x FY24 Actual EBITDA)
- **Agreed Acquisition Equity Value:** **₹3,415.00 Cr**
- **Takeover Control Premium Paid (on Standalone DCF EV):**
  $$\text{Control Premium (EV Basis)} = ₹3,350.00\text{ Cr} - ₹2,800.46\text{ Cr} = \mathbf{₹549.54\text{ Cr}} \quad (+19.6\%)$$
- **Purchase Consideration Structure:**
  - Cash Consideration (60%): ₹2,049.0 Cr (financed via liquid reserves and syndicate debt)
  - Stock Consideration (40%): ₹1,366.0 Cr (newly issued acquirer equity shares)

### 5.2 Synergy Identification & Quantification
1. **Cost Synergy 1 (Reagent Procurement Scale):** Bulk purchasing contracts with Illumina, Thermo Fisher, and Roche enable a 1.8% discount on combined reagent consumables (₹3.28 Cr in FY25E ramping to ₹6.41 Cr by FY29E).
2. **Cost Synergy 2 (IT LIMS & Corporate SG&A Rationalization):** Eliminating redundant Laboratory Information Management System licenses, billing systems, and overlapping management overhead (₹2.13 Cr in FY25E ramping to ₹4.16 Cr by FY29E).
3. **Cost Synergy 3 (Cold-Chain Logistics Route Optimization):** Specimen transport consolidation between regional RPL hubs and central reference centers (₹1.46 Cr in FY25E ramping to ₹2.85 Cr by FY29E).
4. **Revenue Synergy (Cross-Selling into Pan-India Hospital Network):** Commercializing specialized oncology panels and NIPT across the Acquirer's 4,000+ hospital network (₹10.19 Cr in FY25E ramping to ₹56.70 Cr by FY29E, generating ₹6.62 Cr to ₹36.86 Cr incremental EBITDA).
5. **Total Pre-Tax Synergies:** Ramping from **₹10.20 Cr in FY25E** to **₹70.20 Cr by FY29E**.
6. **Total Post-Tax Synergies (at 25.17% Tax):** Ramping from **₹7.63 Cr in FY25E** to **₹52.53 Cr by FY29E**.

### 5.3 Net Synergy NPV & Accretion Analysis
$$\text{PV of 5-Year Explicit Synergies (FY25E–FY29E at WACC 11.95%)} = \mathbf{₹112.95\text{ Cr}}$$
$$\text{Terminal Synergies Value} = \frac{₹52.53\text{ Cr} \times (1 + 0.05)}{0.1195 - 0.05} = ₹793.59\text{ Cr}$$
$$\text{PV of Terminal Synergies} = ₹793.59\text{ Cr} \times \frac{1}{(1 + 0.1195)^5} = \mathbf{₹451.11\text{ Cr}}$$
$$\mathbf{\text{Total Net Present Value of Synergies (NPV)}} = ₹112.95\text{ Cr} + ₹451.11\text{ Cr} = \mathbf{₹564.06\text{ Cr}}$$

### 5.4 Final Net Value Creation & Deal Accretion
$$\mathbf{\text{Net Value Created for Acquirer}} = \text{NPV of Synergies} - \text{Control Premium Paid}$$
$$\mathbf{\text{Net Value Creation}} = ₹564.06\text{ Cr} - ₹549.54\text{ Cr} = \mathbf{+₹14.52\text{ Cr (Accretive Value Engine)}}$$
$$\mathbf{\text{Pro-Forma Combined Enterprise Value}} = \text{Standalone EV} + \text{Synergies NPV} = ₹2,800.46\text{ Cr} + ₹564.06\text{ Cr} = \mathbf{₹3,364.52\text{ Cr}}$$
$$\mathbf{\text{Per Share Value Accretion}} = \frac{+₹14.52\text{ Cr}}{5.00\text{ Cr shares}} = \mathbf{+₹2.90\text{ per share}}$$

> **CONCLUSION:** Because the Net Present Value of quantifiable operational and revenue synergies (**₹564.06 Cr**) exceeds the takeover control premium (**₹549.54 Cr**), the transaction is **financially accretive by +₹14.52 Cr**, delivering clear strategic and shareholder value creation.
