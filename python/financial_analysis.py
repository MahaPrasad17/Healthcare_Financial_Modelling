"""
financial_analysis.py
=====================
In-depth financial performance analysis, ratio calculation, and benchmarking
for Healthcare Diagnostics Financial Modelling & M&A Valuation (AuraGen Diagnostics Ltd.).

Covers:
- Profitability & Margin Evolution (Gross, EBITDA, EBIT, Net Margin)
- Return on Capital (ROIC, ROCE, ROE)
- Credit, Solvency & Leverage Ratios (Net Debt/EBITDA, Interest Coverage)
- Working Capital & Efficiency Metrics (DSO, DIO, DPO, CCC)
- Growth Decomposition (Test Volume vs ARPT Realization)
"""

import os
import pandas as pd
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)


def calculate_comprehensive_financial_ratios():
    """Compute all corporate finance ratios for AuraGen Diagnostics."""
    hist_file = os.path.join(DATA_DIR, "historical_financials.csv")
    df = pd.read_csv(hist_file)
    
    # 1. Profitability Margins
    df["Gross_Margin_Pct"] = (df["Gross_Profit_Cr"] / df["Total_Revenue_Cr"]) * 100
    df["EBITDA_Margin_Pct"] = (df["EBITDA_Cr"] / df["Total_Revenue_Cr"]) * 100
    df["EBIT_Margin_Pct"] = (df["EBIT_Cr"] / df["Total_Revenue_Cr"]) * 100
    df["Net_Profit_Margin_Pct"] = (df["Net_Profit_Cr"] / df["Total_Revenue_Cr"]) * 100
    
    # 2. Growth Rates (YoY)
    df["YoY_Revenue_Growth_Pct"] = df["Total_Revenue_Cr"].pct_change() * 100
    df["YoY_EBITDA_Growth_Pct"] = df["EBITDA_Cr"].pct_change() * 100
    df["YoY_PAT_Growth_Pct"] = df["Net_Profit_Cr"].pct_change() * 100
    df["Genomics_Growth_Pct"] = df["Genomics_Revenue_Cr"].pct_change() * 100
    
    # 3. Capital Returns (ROIC, ROCE, ROE)
    # Invested Capital = Total Equity + Total Debt - Cash & Cash Eq.
    df["Invested_Capital_Cr"] = df["Net_Worth_Equity_Cr"] + df["Total_Debt_Cr"] - df["Cash_and_Equivalents_Cr"]
    # Effective Tax = 25.17%
    tax_rate = 0.2517
    df["NOPAT_Cr"] = df["EBIT_Cr"] * (1 - tax_rate)
    df["ROIC_Pct"] = (df["NOPAT_Cr"] / df["Invested_Capital_Cr"]) * 100
    
    # Capital Employed = Total Assets - Current Liabilities
    # Current Liabilities approx: Total Assets - (Equity + Long Term Debt)
    df["Capital_Employed_Cr"] = df["Net_Worth_Equity_Cr"] + df["Total_Debt_Cr"]
    df["ROCE_Pct"] = (df["EBIT_Cr"] / df["Capital_Employed_Cr"]) * 100
    df["ROE_Pct"] = (df["Net_Profit_Cr"] / df["Net_Worth_Equity_Cr"]) * 100
    
    # 4. Solvency & Liquidity Ratios
    df["Net_Debt_Cr"] = df["Total_Debt_Cr"] - df["Cash_and_Equivalents_Cr"]
    df["Net_Debt_to_EBITDA"] = df["Net_Debt_Cr"] / df["EBITDA_Cr"]
    df["Debt_to_Equity"] = df["Total_Debt_Cr"] / df["Net_Worth_Equity_Cr"]
    df["Interest_Coverage_Ratio"] = df["EBIT_Cr"] / df["Interest_Expense_Cr"]
    
    # 5. Cash Flow Conversion
    df["CFO_to_EBITDA_Pct"] = (df["Operating_Cash_Flow_Cr"] / df["EBITDA_Cr"]) * 100
    df["FCF_Conversion_PAT_Pct"] = (df["Free_Cash_Flow_Cr"] / df["Net_Profit_Cr"]) * 100
    
    return df


def print_financial_report(df):
    """Print an executive-level institutional financial report."""
    print("=" * 85)
    print("      AURAGEN DIAGNOSTICS LTD. - INSTITUTIONAL FINANCIAL ANALYSIS REPORT")
    print("      (Specialized Genomics & Advanced Healthcare Diagnostics Chain)")
    print("=" * 85)
    
    print("\n1. PROFITABILITY & MARGIN EXPANSION")
    print("-" * 85)
    print(f"{'Fiscal Year':<10} | {'Revenue (INR Cr)':<16} | {'Gross Margin':<14} | {'EBITDA Margin':<14} | {'PAT Margin':<12}")
    print("-" * 85)
    for _, r in df.iterrows():
        print(f"{r['Fiscal_Year']:<10} | INR {r['Total_Revenue_Cr']:>8.2f} Cr   | {r['Gross_Margin_Pct']:>12.2f}% | {r['EBITDA_Margin_Pct']:>12.2f}% | {r['Net_Profit_Margin_Pct']:>10.2f}%")
        
    print("\n2. SEGMENT MIX & REVENUE EXPANSION")
    print("-" * 85)
    print(f"{'Fiscal Year':<10} | {'Genomics (Cr)':<14} | {'Molecular (Cr)':<14} | {'Routine (Cr)':<14} | {'Clin Res (Cr)':<14}")
    print("-" * 85)
    for _, r in df.iterrows():
        print(f"{r['Fiscal_Year']:<10} | INR {r['Genomics_Revenue_Cr']:>6.2f} Cr    | INR {r['Molecular_Revenue_Cr']:>6.2f} Cr    | INR {r['Routine_Revenue_Cr']:>6.2f} Cr    | INR {r['Clinical_Research_Revenue_Cr']:>6.2f} Cr")

    print("\n3. CAPITAL RETURN METRICS (ROIC, ROCE, ROE)")
    print("-" * 85)
    print(f"{'Fiscal Year':<10} | {'Invested Capital':<16} | {'ROIC (%)':<12} | {'ROCE (%)':<12} | {'ROE (%)':<10}")
    print("-" * 85)
    for _, r in df.iterrows():
        print(f"{r['Fiscal_Year']:<10} | INR {r['Invested_Capital_Cr']:>8.2f} Cr   | {r['ROIC_Pct']:>10.2f}% | {r['ROCE_Pct']:>10.2f}% | {r['ROE_Pct']:>8.2f}%")

    print("\n4. BALANCE SHEET STRENGTH & CASH GENERATION")
    print("-" * 85)
    print(f"{'Fiscal Year':<10} | {'Net Debt (Cr)':<14} | {'Net Debt/EBITDA':<16} | {'Int Coverage':<14} | {'FCF Conversion':<14}")
    print("-" * 85)
    for _, r in df.iterrows():
        net_debt_str = f"INR {r['Net_Debt_Cr']:>5.2f} Cr"
        print(f"{r['Fiscal_Year']:<10} | {net_debt_str:<14} | {r['Net_Debt_to_EBITDA']:>14.2f}x | {r['Interest_Coverage_Ratio']:>12.2f}x | {r['FCF_Conversion_PAT_Pct']:>12.2f}%")

    # Historical CAGRs
    rev_cagr = ((df.iloc[-1]["Total_Revenue_Cr"] / df.iloc[0]["Total_Revenue_Cr"]) ** (1/3) - 1) * 100
    gen_cagr = ((df.iloc[-1]["Genomics_Revenue_Cr"] / df.iloc[0]["Genomics_Revenue_Cr"]) ** (1/3) - 1) * 100
    ebitda_cagr = ((df.iloc[-1]["EBITDA_Cr"] / df.iloc[0]["EBITDA_Cr"]) ** (1/3) - 1) * 100
    pat_cagr = ((df.iloc[-1]["Net_Profit_Cr"] / df.iloc[0]["Net_Profit_Cr"]) ** (1/3) - 1) * 100
    
    print("\n5. 3-YEAR HISTORICAL COMPOUND ANNUAL GROWTH RATES (FY21 -> FY24)")
    print("-" * 85)
    print(f" Total Revenue CAGR:                {rev_cagr:>8.2f}%")
    print(f" Genomics & NGS Revenue CAGR:       {gen_cagr:>8.2f}%")
    print(f" EBITDA CAGR:                       {ebitda_cagr:>8.2f}%")
    print(f" Net Profit (PAT) CAGR:             {pat_cagr:>8.2f}%")
    print("=" * 85 + "\n")


def export_ratios_summary(df):
    """Export key ratios table to outputs folder."""
    out_file = os.path.join(OUTPUTS_DIR, "financial_ratios_summary.csv")
    cols_to_export = [
        "Fiscal_Year", "Total_Revenue_Cr", "Gross_Margin_Pct", "EBITDA_Margin_Pct",
        "Net_Profit_Margin_Pct", "ROIC_Pct", "ROCE_Pct", "ROE_Pct",
        "Net_Debt_Cr", "Net_Debt_to_EBITDA", "Interest_Coverage_Ratio", "Free_Cash_Flow_Cr"
    ]
    df[cols_to_export].to_csv(out_file, index=False)
    print(f"[EXPORT] Saved financial ratios summary to: {out_file}")


def main():
    df_ratios = calculate_comprehensive_financial_ratios()
    print_financial_report(df_ratios)
    export_ratios_summary(df_ratios)


if __name__ == "__main__":
    main()

