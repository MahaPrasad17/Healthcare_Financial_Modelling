"""
generate_datasets.py
====================
Generates realistic, mathematically reconciled datasets for Healthcare Diagnostics
Financial Modelling & M&A Valuation (Target: AuraGen Diagnostics Ltd.).

ALL DATA GENERATED IS SYNTHETIC AND SIMULATED FOR CORPORATE DEVELOPMENT AND FINANCIAL MODELLING EVALUATION PURPOSES.
"""

import os
import pandas as pd
import numpy as np

# Ensure directories exist
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
POWERBI_DIR = os.path.join(BASE_DIR, "powerbi")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(POWERBI_DIR, exist_ok=True)

# 1. HISTORICAL FINANCIALS (FY2021 - FY2024) in INR Crores (₹ Cr)
hist_financials_data = [
    {
        "Fiscal_Year": "FY2021",
        "Period_Type": "Historical",
        "Data_Classification": "Synthetic - Simulated Benchmark",
        "Genomics_Revenue_Cr": 58.80,
        "Molecular_Revenue_Cr": 61.20,
        "Routine_Revenue_Cr": 98.00,
        "Clinical_Research_Revenue_Cr": 27.00,
        "Total_Revenue_Cr": 245.00,
        "COGS_Reagents_Consumables_Cr": 81.50,
        "Gross_Profit_Cr": 163.50,
        "Personnel_Expenses_Cr": 48.00,
        "Logistics_Collection_Costs_Cr": 21.00,
        "Lab_Operating_Expenses_Cr": 12.50,
        "Selling_Admin_Expenses_Cr": 9.00,
        "Total_Opex_Cr": 90.50,
        "EBITDA_Cr": 73.00,
        "Depreciation_Amortization_Cr": 16.00,
        "EBIT_Cr": 57.00,
        "Interest_Expense_Cr": 4.50,
        "Other_Income_Cr": 1.50,
        "EBT_Cr": 54.00,
        "Tax_Expense_Cr": 13.59,
        "Net_Profit_Cr": 40.41,
        "Operating_Cash_Flow_Cr": 55.41,
        "Capital_Expenditure_Cr": 28.00,
        "Free_Cash_Flow_Cr": 27.41,
        "Cash_and_Equivalents_Cr": 35.00,
        "Total_Debt_Cr": 52.00,
        "Total_Assets_Cr": 285.00,
        "Net_Worth_Equity_Cr": 185.00
    },
    {
        "Fiscal_Year": "FY2022",
        "Period_Type": "Historical",
        "Data_Classification": "Synthetic - Simulated Benchmark",
        "Genomics_Revenue_Cr": 84.20,
        "Molecular_Revenue_Cr": 78.00,
        "Routine_Revenue_Cr": 114.80,
        "Clinical_Research_Revenue_Cr": 35.00,
        "Total_Revenue_Cr": 312.00,
        "COGS_Reagents_Consumables_Cr": 101.40,
        "Gross_Profit_Cr": 210.60,
        "Personnel_Expenses_Cr": 60.00,
        "Logistics_Collection_Costs_Cr": 26.50,
        "Lab_Operating_Expenses_Cr": 15.50,
        "Selling_Admin_Expenses_Cr": 11.60,
        "Total_Opex_Cr": 113.60,
        "EBITDA_Cr": 97.00,
        "Depreciation_Amortization_Cr": 20.50,
        "EBIT_Cr": 76.50,
        "Interest_Expense_Cr": 4.80,
        "Other_Income_Cr": 2.10,
        "EBT_Cr": 73.80,
        "Tax_Expense_Cr": 18.58,
        "Net_Profit_Cr": 55.22,
        "Operating_Cash_Flow_Cr": 74.22,
        "Capital_Expenditure_Cr": 34.00,
        "Free_Cash_Flow_Cr": 40.22,
        "Cash_and_Equivalents_Cr": 52.00,
        "Total_Debt_Cr": 50.00,
        "Total_Assets_Cr": 355.00,
        "Net_Worth_Equity_Cr": 240.22
    },
    {
        "Fiscal_Year": "FY2023",
        "Period_Type": "Historical",
        "Data_Classification": "Synthetic - Simulated Benchmark",
        "Genomics_Revenue_Cr": 118.50,
        "Molecular_Revenue_Cr": 94.80,
        "Routine_Revenue_Cr": 134.30,
        "Clinical_Research_Revenue_Cr": 47.40,
        "Total_Revenue_Cr": 395.00,
        "COGS_Reagents_Consumables_Cr": 124.80,
        "Gross_Profit_Cr": 270.20,
        "Personnel_Expenses_Cr": 74.50,
        "Logistics_Collection_Costs_Cr": 33.20,
        "Lab_Operating_Expenses_Cr": 19.80,
        "Selling_Admin_Expenses_Cr": 14.70,
        "Total_Opex_Cr": 142.20,
        "EBITDA_Cr": 128.00,
        "Depreciation_Amortization_Cr": 26.00,
        "EBIT_Cr": 102.00,
        "Interest_Expense_Cr": 5.20,
        "Other_Income_Cr": 2.80,
        "EBT_Cr": 99.60,
        "Tax_Expense_Cr": 25.07,
        "Net_Profit_Cr": 74.53,
        "Operating_Cash_Flow_Cr": 98.53,
        "Capital_Expenditure_Cr": 42.00,
        "Free_Cash_Flow_Cr": 56.53,
        "Cash_and_Equivalents_Cr": 78.00,
        "Total_Debt_Cr": 48.00,
        "Total_Assets_Cr": 445.00,
        "Net_Worth_Equity_Cr": 314.75
    },
    {
        "Fiscal_Year": "FY2024",
        "Period_Type": "Historical",
        "Data_Classification": "Synthetic - Simulated Benchmark",
        "Genomics_Revenue_Cr": 164.30,
        "Molecular_Revenue_Cr": 114.50,
        "Routine_Revenue_Cr": 154.40,
        "Clinical_Research_Revenue_Cr": 64.80,
        "Total_Revenue_Cr": 498.00,
        "COGS_Reagents_Consumables_Cr": 154.40,
        "Gross_Profit_Cr": 343.60,
        "Personnel_Expenses_Cr": 91.00,
        "Logistics_Collection_Costs_Cr": 41.80,
        "Lab_Operating_Expenses_Cr": 24.80,
        "Selling_Admin_Expenses_Cr": 18.50,
        "Total_Opex_Cr": 176.10,
        "EBITDA_Cr": 167.50,
        "Depreciation_Amortization_Cr": 32.00,
        "EBIT_Cr": 135.50,
        "Interest_Expense_Cr": 5.50,
        "Other_Income_Cr": 3.50,
        "EBT_Cr": 133.50,
        "Tax_Expense_Cr": 33.60,
        "Net_Profit_Cr": 99.90,
        "Operating_Cash_Flow_Cr": 129.90,
        "Capital_Expenditure_Cr": 48.00,
        "Free_Cash_Flow_Cr": 81.90,
        "Cash_and_Equivalents_Cr": 110.00,
        "Total_Debt_Cr": 45.00,
        "Total_Assets_Cr": 565.00,
        "Net_Worth_Equity_Cr": 414.65
    }
]

df_hist = pd.DataFrame(hist_financials_data)
hist_path = os.path.join(DATA_DIR, "historical_financials.csv")
df_hist.to_csv(hist_path, index=False)
print(f"Created: {hist_path}")

# 2. OPERATIONAL DATA (Segment volumes, ARPT, lab infrastructure, quality)
operational_records = []
segments = ["Routine Biochemistry & Hematology", "Molecular & Infectious", "Genomics & Next-Gen Sequencing", "Clinical Research Services"]

op_specs = {
    "FY2021": {
        "Routine Biochemistry & Hematology": {"vol": 1850000, "arpt": 530, "gm": 0.58},
        "Molecular & Infectious": {"vol": 310000, "arpt": 1974, "gm": 0.64},
        "Genomics & Next-Gen Sequencing": {"vol": 45000, "arpt": 13067, "gm": 0.72},
        "Clinical Research Services": {"vol": 5200, "arpt": 51923, "gm": 0.76},
        "ref_labs": 1, "reg_labs": 6, "centers": 85, "b2b_hosp": 140, "rejection": 1.85, "tat_hrs": 48
    },
    "FY2022": {
        "Routine Biochemistry & Hematology": {"vol": 2120000, "arpt": 542, "gm": 0.59},
        "Molecular & Infectious": {"vol": 380000, "arpt": 2053, "gm": 0.65},
        "Genomics & Next-Gen Sequencing": {"vol": 63000, "arpt": 13365, "gm": 0.73},
        "Clinical Research Services": {"vol": 6500, "arpt": 53846, "gm": 0.77},
        "ref_labs": 1, "reg_labs": 9, "centers": 130, "b2b_hosp": 210, "rejection": 1.45, "tat_hrs": 40
    },
    "FY2023": {
        "Routine Biochemistry & Hematology": {"vol": 2440000, "arpt": 550, "gm": 0.60},
        "Molecular & Infectious": {"vol": 450000, "arpt": 2107, "gm": 0.66},
        "Genomics & Next-Gen Sequencing": {"vol": 87000, "arpt": 13621, "gm": 0.74},
        "Clinical Research Services": {"vol": 8600, "arpt": 55116, "gm": 0.78},
        "ref_labs": 2, "reg_labs": 14, "centers": 195, "b2b_hosp": 320, "rejection": 1.05, "tat_hrs": 32
    },
    "FY2024": {
        "Routine Biochemistry & Hematology": {"vol": 2750000, "arpt": 561, "gm": 0.61},
        "Molecular & Infectious": {"vol": 530000, "arpt": 2160, "gm": 0.67},
        "Genomics & Next-Gen Sequencing": {"vol": 118000, "arpt": 13924, "gm": 0.75},
        "Clinical Research Services": {"vol": 11500, "arpt": 56348, "gm": 0.79},
        "ref_labs": 2, "reg_labs": 20, "centers": 280, "b2b_hosp": 460, "rejection": 0.72, "tat_hrs": 26
    }
}

for year, data in op_specs.items():
    for seg in segments:
        s_data = data[seg]
        revenue_cr = round((s_data["vol"] * s_data["arpt"]) / 10000000, 2)
        operational_records.append({
            "Fiscal_Year": year,
            "Segment": seg,
            "Data_Classification": "Synthetic - Simulated Benchmark",
            "Test_Volume_Number": s_data["vol"],
            "Avg_Realization_Per_Test_INR": s_data["arpt"],
            "Segment_Revenue_Cr": revenue_cr,
            "Gross_Margin_Pct": s_data["gm"],
            "Active_Reference_Labs": data["ref_labs"],
            "Active_Regional_Labs": data["reg_labs"],
            "Active_Collection_Centers": data["centers"],
            "B2B_Hospital_Ties": data["b2b_hosp"],
            "Sample_Rejection_Rate_Pct": data["rejection"],
            "Avg_Turnaround_Time_Hours": data["tat_hrs"]
        })

df_op = pd.DataFrame(operational_records)
op_path = os.path.join(DATA_DIR, "operational_data.csv")
df_op.to_csv(op_path, index=False)
print(f"Created: {op_path}")

# 3. ASSUMPTIONS FILE (Parameters for 3-statement forecast, DCF & M&A)
assumptions_data = [
    # Data Integrity & Labeling
    {"Category": "Data Governance", "Parameter": "Dataset_Classification", "Value": "Synthetic / Simulated", "Unit": "Label", "Description": "All metrics are synthetic simulations for corporate development evaluation"},
    
    # Macro & Valuation Inputs
    {"Category": "Valuation Parameters", "Parameter": "Risk_Free_Rate_Rf", "Value": 0.0710, "Unit": "Percentage", "Description": "10-Year Indian Government Benchmark Bond Yield (G-Sec)"},
    {"Category": "Valuation Parameters", "Parameter": "Equity_Risk_Premium_ERP", "Value": 0.0600, "Unit": "Percentage", "Description": "Long-term emerging market equity risk premium"},
    {"Category": "Valuation Parameters", "Parameter": "Unlevered_Industry_Beta", "Value": 0.8500, "Unit": "Ratio", "Description": "Healthcare Diagnostics comparable median asset beta"},
    {"Category": "Valuation Parameters", "Parameter": "Target_Debt_Weight", "Value": 0.1500, "Unit": "Percentage", "Description": "Target Debt / (Debt + Equity) capital structure"},
    {"Category": "Valuation Parameters", "Parameter": "Target_Equity_Weight", "Value": 0.8500, "Unit": "Percentage", "Description": "Target Equity / (Debt + Equity) capital structure"},
    {"Category": "Valuation Parameters", "Parameter": "Levered_Beta", "Value": 0.9622, "Unit": "Ratio", "Description": "Beta levered via CAPM Hamada equation: Beta_U * [1 + (1-t)*(D/E)]"},
    {"Category": "Valuation Parameters", "Parameter": "Cost_of_Equity_Ke", "Value": 0.1287, "Unit": "Percentage", "Description": "Ke = Rf + Beta * ERP (7.10% + 0.9622 * 6.00%)"},
    {"Category": "Valuation Parameters", "Parameter": "Pre_Tax_Cost_of_Debt_Kd", "Value": 0.0900, "Unit": "Percentage", "Description": "Weighted average borrowing facility interest rate"},
    {"Category": "Valuation Parameters", "Parameter": "Effective_Tax_Rate", "Value": 0.2517, "Unit": "Percentage", "Description": "Indian corporate tax rate under Section 115BAA (25.17% inclusive of surcharge/cess)"},
    {"Category": "Valuation Parameters", "Parameter": "After_Tax_Cost_of_Debt", "Value": 0.0673, "Unit": "Percentage", "Description": "Kd * (1 - Tax Rate) = 9.0% * (1 - 0.2517)"},
    {"Category": "Valuation Parameters", "Parameter": "WACC", "Value": 0.1195, "Unit": "Percentage", "Description": "Weighted Average Cost of Capital: (85% * 12.87%) + (15% * 6.73%) = 11.95%"},
    {"Category": "Valuation Parameters", "Parameter": "Terminal_Growth_Rate_g", "Value": 0.0500, "Unit": "Percentage", "Description": "Perpetual terminal growth rate aligned with GDP & healthcare trends"},
    {"Category": "Valuation Parameters", "Parameter": "Exit_EV_EBITDA_Multiple", "Value": 18.00, "Unit": "Multiple", "Description": "Exit Multiple for Terminal Value (median peer diagnostic transaction multiple)"},

    # Growth & Operational Drivers - Base Case Forecast (FY25E - FY29E)
    {"Category": "Base Case Forecast", "Parameter": "Genomics_Revenue_CAGR", "Value": 0.2240, "Unit": "Percentage", "Description": "22.4% 5-Yr CAGR expanding mix from 33.0% to 38.0% of revenue"},
    {"Category": "Base Case Forecast", "Parameter": "Molecular_Revenue_CAGR", "Value": 0.1570, "Unit": "Percentage", "Description": "Molecular infectious disease panels & specialized RT-PCR"},
    {"Category": "Base Case Forecast", "Parameter": "Routine_Revenue_CAGR", "Value": 0.1486, "Unit": "Percentage", "Description": "Routine biochemistry expansion through regional spoke labs"},
    {"Category": "Base Case Forecast", "Parameter": "Clinical_Research_CAGR", "Value": 0.2400, "Unit": "Percentage", "Description": "Pharma biomarker discovery & contract research genomic services"},
    {"Category": "Base Case Forecast", "Parameter": "Blended_Revenue_Growth_FY25", "Value": 0.2200, "Unit": "Percentage", "Description": "FY25E YoY Top-line growth (Revenue: ₹607.56 Cr)"},
    {"Category": "Base Case Forecast", "Parameter": "Blended_Revenue_Growth_FY26", "Value": 0.2050, "Unit": "Percentage", "Description": "FY26E YoY Top-line growth (Revenue: ₹732.11 Cr)"},
    {"Category": "Base Case Forecast", "Parameter": "Blended_Revenue_Growth_FY27", "Value": 0.1900, "Unit": "Percentage", "Description": "FY27E YoY Top-line growth (Revenue: ₹871.21 Cr)"},
    {"Category": "Base Case Forecast", "Parameter": "Blended_Revenue_Growth_FY28", "Value": 0.1750, "Unit": "Percentage", "Description": "FY28E YoY Top-line growth (Revenue: ₹1,023.67 Cr)"},
    {"Category": "Base Case Forecast", "Parameter": "Blended_Revenue_Growth_FY29", "Value": 0.1600, "Unit": "Percentage", "Description": "FY29E YoY Top-line growth (Revenue: ₹1,187.46 Cr)"},

    # Cost & Working Capital Assumptions
    {"Category": "Operating Cost Ratios", "Parameter": "COGS_Pct_Revenue", "Value": 0.3000, "Unit": "Percentage", "Description": "Reagents, test kits, sequencers flow cells (bulk procurement economies)"},
    {"Category": "Operating Cost Ratios", "Parameter": "Personnel_Cost_Pct_Revenue", "Value": 0.1750, "Unit": "Percentage", "Description": "Pathologists, geneticists, lab technologists & bioinformaticians (steady state)"},
    {"Category": "Operating Cost Ratios", "Parameter": "Logistics_Cost_Pct_Revenue", "Value": 0.0800, "Unit": "Percentage", "Description": "Temperature-controlled cold-chain specimen couriers & transport"},
    {"Category": "Operating Cost Ratios", "Parameter": "Lab_Opex_Pct_Revenue", "Value": 0.0500, "Unit": "Percentage", "Description": "NABL/CAP accreditations, machine calibration, laboratory consumables"},
    {"Category": "Operating Cost Ratios", "Parameter": "SG&A_Pct_Revenue", "Value": 0.0350, "Unit": "Percentage", "Description": "Hospital B2B marketing, enterprise LIMS IT infrastructure, corporate overhead"},
    {"Category": "Working Capital", "Parameter": "Debtor_Days_DSO", "Value": 45.00, "Unit": "Days", "Description": "Days Sales Outstanding (B2B hospital & pharma billing cycles)"},
    {"Category": "Working Capital", "Parameter": "Inventory_Days_DIO", "Value": 35.00, "Unit": "Days", "Description": "Days Inventory Outstanding for reagents and chemical supplies"},
    {"Category": "Working Capital", "Parameter": "Creditor_Days_DPO", "Value": 50.00, "Unit": "Days", "Description": "Days Payable Outstanding for sequencer and reagent vendors"},

    # M&A Acquisition & Synergy Modeling (Reconciled & Accretive)
    {"Category": "M&A Acquisition", "Parameter": "Target_Standalone_EV_Cr", "Value": 2800.46, "Unit": "INR Crore", "Description": "Standalone DCF intrinsic Enterprise Value (Gordon Growth at 11.95% WACC)"},
    {"Category": "M&A Acquisition", "Parameter": "Proposed_Acquisition_EV_Cr", "Value": 3350.00, "Unit": "INR Crore", "Description": "Agreed Transaction Offer Enterprise Value (20.0x FY24 Actual EBITDA)"},
    {"Category": "M&A Acquisition", "Parameter": "Acquisition_Premium_Pct", "Value": 0.1962, "Unit": "Percentage", "Description": "19.6% control premium over standalone DCF value (14.9% vs base scenario)"},
    {"Category": "M&A Acquisition", "Parameter": "Takeover_Control_Premium_Paid_Cr", "Value": 549.54, "Unit": "INR Crore", "Description": "Total monetary premium paid to AuraGen shareholders: ₹3,350.00 - ₹2,800.46 Cr"},
    {"Category": "M&A Acquisition", "Parameter": "Annual_Reagent_Procurement_Synergies_Cr", "Value": 17.50, "Unit": "INR Crore", "Description": "Global reagent volume procurement savings (1.8% of combined COGS by Y5)"},
    {"Category": "M&A Acquisition", "Parameter": "Annual_IT_Admin_Synergies_Cr", "Value": 13.00, "Unit": "INR Crore", "Description": "Consolidation of LIMS IT software, corporate administration & licenses"},
    {"Category": "M&A Acquisition", "Parameter": "Annual_Logistics_Synergies_Cr", "Value": 8.50, "Unit": "INR Crore", "Description": "Cold-chain courier route density & regional processing hub optimization"},
    {"Category": "M&A Acquisition", "Parameter": "Cross_Selling_Revenue_Synergy_Annual_Cr", "Value": 48.00, "Unit": "INR Crore", "Description": "Cross-selling specialized oncology & NIPT panels across Acquirer network"},
    {"Category": "M&A Acquisition", "Parameter": "Cross_Selling_EBITDA_Contribution_Cr", "Value": 31.20, "Unit": "INR Crore", "Description": "EBITDA from cross-selling at 65% contribution margin: ₹48.0 Cr * 65%"},
    {"Category": "M&A Acquisition", "Parameter": "Total_Combined_EBITDA_Synergies_Y5_Cr", "Value": 70.20, "Unit": "INR Crore", "Description": "Total annual operating EBITDA synergies run-rate: ₹39.0 Cr cost + ₹31.2 Cr revenue"},
    {"Category": "M&A Acquisition", "Parameter": "NPV_of_Net_Synergies_Cr", "Value": 564.06, "Unit": "INR Crore", "Description": "Net Present Value of post-tax synergies at 11.95% WACC (Explicit ₹112.95 Cr + Terminal ₹451.11 Cr)"},
    {"Category": "M&A Acquisition", "Parameter": "Net_Acquirer_Value_Creation_Cr", "Value": 14.52, "Unit": "INR Crore", "Description": "Accretive deal value created: NPV Synergies (₹564.06 Cr) - Premium Paid (₹549.54 Cr) = +₹14.52 Cr (+₹129.26 Cr vs Base Scenario)"},
    {"Category": "M&A Acquisition", "Parameter": "Post_Synergies_Combined_EV_Cr", "Value": 3364.52, "Unit": "INR Crore", "Description": "Pro-forma value of target under Acquirer ownership: Offer Price ₹3,350 Cr + Net Value ₹14.52 Cr"}
]

df_assump = pd.DataFrame(assumptions_data)
df_assump["Data_Classification"] = "Synthetic - Simulated Benchmark"
assump_path = os.path.join(DATA_DIR, "assumptions.csv")
df_assump.to_csv(assump_path, index=False)
print(f"Created: {assump_path}")

# 4. POWER BI DASHBOARD DATASET (Comprehensive 9-year dataset: FY21 - FY29E)
years_all = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025E", "FY2026E", "FY2027E", "FY2028E", "FY2029E"]
regions = ["South", "West", "North", "East", "International"]

pbi_records = []

# Financial forecast baseline numbers in INR Cr (Reconciled with DCF and IS)
proj_fin = {
    "FY2021": {"rev": 245.00, "ebitda": 73.00, "pat": 40.41, "cogs": 81.50, "fcff": 27.41, "capex": 28.00, "type": "Historical", "tests": 2210200},
    "FY2022": {"rev": 312.00, "ebitda": 97.00, "pat": 55.22, "cogs": 101.40, "fcff": 40.22, "capex": 34.00, "type": "Historical", "tests": 2569500},
    "FY2023": {"rev": 395.00, "ebitda": 128.00, "pat": 74.53, "cogs": 124.80, "fcff": 56.53, "capex": 42.00, "type": "Historical", "tests": 2985600},
    "FY2024": {"rev": 498.00, "ebitda": 167.50, "pat": 99.90, "cogs": 154.40, "fcff": 81.90, "capex": 48.00, "type": "Historical", "tests": 3409500},
    "FY2025E": {"rev": 607.56, "ebitda": 206.57, "pat": 125.36, "cogs": 182.27, "fcff": 104.89, "capex": 45.00, "type": "Forecast", "tests": 3949119},
    "FY2026E": {"rev": 732.11, "ebitda": 252.58, "pat": 155.26, "cogs": 219.63, "fcff": 134.08, "capex": 50.00, "type": "Forecast", "tests": 4510252},
    "FY2027E": {"rev": 871.21, "ebitda": 304.92, "pat": 189.90, "cogs": 261.36, "fcff": 168.51, "capex": 55.00, "type": "Forecast", "tests": 5122509},
    "FY2028E": {"rev": 1023.67, "ebitda": 363.40, "pat": 229.13, "cogs": 307.10, "fcff": 209.53, "capex": 58.00, "type": "Forecast", "tests": 5698658},
    "FY2029E": {"rev": 1187.46, "ebitda": 427.49, "pat": 272.56, "cogs": 356.24, "fcff": 256.25, "capex": 60.00, "type": "Forecast", "tests": 6354108}
}

reg_weights = {
    "South": 0.45,
    "West": 0.25,
    "North": 0.15,
    "East": 0.10,
    "International": 0.05
}

# Segment proportions aligned with executive summary (Genomics 33% -> 38%)
seg_proportions = {
    "FY2021": {"Genomics & NGS": 0.2400, "Molecular": 0.2500, "Routine": 0.4000, "Clinical Research": 0.1100},
    "FY2022": {"Genomics & NGS": 0.2700, "Molecular": 0.2500, "Routine": 0.3680, "Clinical Research": 0.1120},
    "FY2023": {"Genomics & NGS": 0.3000, "Molecular": 0.2400, "Routine": 0.3400, "Clinical Research": 0.1200},
    "FY2024": {"Genomics & NGS": 0.3300, "Molecular": 0.2300, "Routine": 0.3100, "Clinical Research": 0.1300},
    "FY2025E": {"Genomics & NGS": 0.3400, "Molecular": 0.2200, "Routine": 0.3000, "Clinical Research": 0.1400},
    "FY2026E": {"Genomics & NGS": 0.3500, "Molecular": 0.2100, "Routine": 0.2900, "Clinical Research": 0.1500},
    "FY2027E": {"Genomics & NGS": 0.3600, "Molecular": 0.2100, "Routine": 0.2800, "Clinical Research": 0.1500},
    "FY2028E": {"Genomics & NGS": 0.3700, "Molecular": 0.2000, "Routine": 0.2700, "Clinical Research": 0.1600},
    "FY2029E": {"Genomics & NGS": 0.3800, "Molecular": 0.2000, "Routine": 0.2600, "Clinical Research": 0.1600}
}

for year in years_all:
    yr_spec = proj_fin[year]
    total_rev = yr_spec["rev"]
    total_ebitda = yr_spec["ebitda"]
    total_pat = yr_spec["pat"]
    total_cogs = yr_spec["cogs"]
    total_fcff = yr_spec["fcff"]
    total_capex = yr_spec["capex"]
    period_type = yr_spec["type"]
    total_tests = yr_spec["tests"]
    
    seg_mix = seg_proportions[year]
    
    for reg, r_wt in reg_weights.items():
        for seg, s_wt in seg_mix.items():
            cell_share = r_wt * s_wt
            rev_cr = round(total_rev * cell_share, 4)
            cogs_cr = round(total_cogs * cell_share, 4)
            gp_cr = round(rev_cr - cogs_cr, 4)
            gp_pct = round((gp_cr / rev_cr) * 100, 2) if rev_cr > 0 else 0
            
            ebitda_cr = round(total_ebitda * cell_share, 4)
            ebitda_pct = round((ebitda_cr / rev_cr) * 100, 2) if rev_cr > 0 else 0
            
            pat_cr = round(total_pat * cell_share, 4)
            pat_pct = round((pat_cr / rev_cr) * 100, 2) if rev_cr > 0 else 0
            
            cell_tests = int(round(total_tests * cell_share))
            arpt_inr = round((rev_cr * 10000000) / cell_tests, 1) if cell_tests > 0 else 0
            
            capex_cr = round(total_capex * cell_share, 4)
            fcff_cr = round(total_fcff * cell_share, 4)
            
            pbi_records.append({
                "Fiscal_Year": year,
                "Period_Type": period_type,
                "Data_Classification": "Synthetic - Simulated Benchmark",
                "Region": reg,
                "Segment": seg,
                "Revenue_Cr": rev_cr,
                "COGS_Cr": cogs_cr,
                "Gross_Profit_Cr": gp_cr,
                "Gross_Margin_Pct": gp_pct,
                "EBITDA_Cr": ebitda_cr,
                "EBITDA_Margin_Pct": ebitda_pct,
                "Net_Profit_Cr": pat_cr,
                "Net_Profit_Margin_Pct": pat_pct,
                "Test_Volume": cell_tests,
                "ARPT_INR": arpt_inr,
                "Capex_Allocated_Cr": capex_cr,
                "FCFF_Allocated_Cr": fcff_cr
            })

df_pbi = pd.DataFrame(pbi_records)
pbi_path = os.path.join(POWERBI_DIR, "dashboard_data.csv")
df_pbi.to_csv(pbi_path, index=False)
print(f"Created: {pbi_path} ({df_pbi.shape[0]} rows)")

print("\n[SUCCESS] Datasets generated successfully with full mathematical reconciliation and clear synthetic labels.")
