"""
visualizations.py
=================
Generates executive-level, publication-quality financial charts and dashboards
for Healthcare Diagnostics Financial Modelling & M&A Valuation (AuraGen Diagnostics Ltd.).

Outputs:
1. outputs/revenue_trend.png (Revenue breakdown, EBITDA/PAT margin curves, ARPT, regional mix)
2. outputs/financial_analysis.png (ROIC/ROCE/ROE Dupont, Cost structure, FCF conversion, Valuation Heatmap)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
POWERBI_DIR = os.path.join(PROJECT_ROOT, "powerbi")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Styling Configuration
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#CCCCCC"
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["grid.color"] = "#EBEBEB"
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.alpha"] = 0.7

NAVY = "#1F4E78"
TEAL = "#2E75B6"
LIGHT_BLUE = "#5B9BD5"
CORAL = "#ED7D31"
GREEN = "#70AD47"
PURPLE = "#7030A0"
GOLD = "#FFC000"
DARK_GRAY = "#333333"


def create_revenue_trend_dashboard():
    """Generate 4-panel revenue trend, margin progression, ARPT and regional dashboard."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    # 9-Year Horizon (FY21 - FY29E)
    years = ["FY21", "FY22", "FY23", "FY24", "FY25E", "FY26E", "FY27E", "FY28E", "FY29E"]
    
    # Segment data in INR Cr
    genomics = [58.8, 84.2, 118.5, 164.3, 206.6, 256.2, 313.6, 378.8, 451.2]
    molecular = [61.2, 78.0, 94.8, 114.5, 133.7, 153.7, 182.9, 204.7, 237.5]
    routine = [98.0, 114.8, 134.3, 154.4, 182.3, 212.3, 243.9, 276.4, 308.7]
    clin_res = [27.0, 35.0, 47.4, 64.8, 85.0, 109.9, 130.8, 163.8, 190.0]
    total_rev = [245.0, 312.0, 395.0, 498.0, 607.6, 732.1, 871.2, 1023.7, 1187.5]
    yoy_growth = [0.0, 27.3, 26.6, 26.1, 22.0, 20.5, 19.0, 17.5, 16.0]
    
    # Panel 1: Stacked Segment Revenue & YoY Growth
    ax1 = axes[0, 0]
    x = np.arange(len(years))
    w = 0.55
    
    p1 = ax1.bar(x, routine, w, label="Routine Pathology", color="#BDD7EE", edgecolor="#2E75B6", linewidth=0.6)
    p2 = ax1.bar(x, molecular, w, bottom=routine, label="Molecular & Infectious", color="#9DC3E6", edgecolor="#1F4E78", linewidth=0.6)
    p3 = ax1.bar(x, genomics, w, bottom=np.array(routine)+np.array(molecular), label="Genomics & NGS", color="#2E75B6", edgecolor="#1B365D", linewidth=0.6)
    p4 = ax1.bar(x, clin_res, w, bottom=np.array(routine)+np.array(molecular)+np.array(genomics), label="Clinical Research", color="#1F4E78", edgecolor="#0B1C33", linewidth=0.6)
    
    ax1.set_title("A. Revenue Progression by Test Segment (FY21 - FY29E)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax1.set_ylabel("Revenue (INR Crore)", fontsize=10, fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(years, fontsize=9)
    ax1.legend(loc="upper left", frameon=True, fontsize=8)
    
    # Secondary axis for YoY growth
    ax1_twin = ax1.twinx()
    ax1_twin.plot(x[1:], yoy_growth[1:], color=CORAL, marker="o", linewidth=2.2, markersize=5, label="YoY Growth %")
    ax1_twin.set_ylabel("YoY Growth (%)", fontsize=10, fontweight="bold", color=CORAL)
    ax1_twin.tick_params(axis="y", labelcolor=CORAL)
    ax1_twin.set_ylim(10, 35)
    ax1_twin.grid(False)
    
    # Panel 2: EBITDA & Net Profit Margins
    ax2 = axes[0, 1]
    ebitda = [73.0, 97.0, 128.0, 167.5, 206.6, 252.6, 304.9, 363.4, 427.5]
    pat = [40.4, 55.2, 74.5, 99.9, 123.6, 154.5, 190.2, 230.7, 276.0]
    ebitda_margin = [29.8, 31.1, 32.4, 33.6, 34.0, 34.5, 35.0, 35.5, 36.0]
    pat_margin = [16.5, 17.7, 18.9, 20.1, 20.3, 21.1, 21.8, 22.5, 23.2]
    
    b1 = ax2.bar(x - 0.18, ebitda, width=0.35, label="EBITDA (INR Cr)", color=TEAL, alpha=0.9)
    b2 = ax2.bar(x + 0.18, pat, width=0.35, label="Net Profit (PAT) (INR Cr)", color=GREEN, alpha=0.9)
    
    ax2.set_title("B. EBITDA & Net Profit Expansion with Margins", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax2.set_ylabel("Profitability (INR Crore)", fontsize=10, fontweight="bold")
    ax2.set_xticks(x)
    ax2.set_xticklabels(years, fontsize=9)
    ax2.legend(loc="upper left", frameon=True, fontsize=8)
    
    ax2_twin = ax2.twinx()
    ax2_twin.plot(x, ebitda_margin, color=NAVY, linestyle="--", marker="s", linewidth=2.0, label="EBITDA Margin %")
    ax2_twin.plot(x, pat_margin, color="#385723", linestyle=":", marker="^", linewidth=2.0, label="PAT Margin %")
    ax2_twin.set_ylabel("Margin (%)", fontsize=10, fontweight="bold", color=NAVY)
    ax2_twin.set_ylim(10, 42)
    ax2_twin.grid(False)
    ax2_twin.legend(loc="upper center", frameon=True, fontsize=8)
    
    # Panel 3: Test Volumes vs Blended Realization (ARPT)
    ax3 = axes[1, 0]
    test_vol_mil = [2.21, 2.57, 2.99, 3.41, 3.95, 4.55, 5.20, 5.88, 6.55]
    blended_arpt = [1108, 1214, 1323, 1461, 1538, 1609, 1675, 1741, 1813]
    
    bars_vol = ax3.bar(x, test_vol_mil, width=0.5, color="#A6A6A6", edgecolor=DARK_GRAY, label="Total Tests (Millions)")
    ax3.set_title("C. Diagnostic Test Volume vs Realization Per Test (ARPT)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax3.set_ylabel("Annual Test Volume (Millions)", fontsize=10, fontweight="bold")
    ax3.set_xticks(x)
    ax3.set_xticklabels(years, fontsize=9)
    ax3.set_ylim(0, 8.0)
    ax3.legend(loc="upper left", frameon=True, fontsize=8)
    
    ax3_twin = ax3.twinx()
    ax3_twin.plot(x, blended_arpt, color=PURPLE, marker="D", linewidth=2.2, markersize=6, label="Blended ARPT (INR)")
    ax3_twin.set_ylabel("Average Realization Per Test (INR)", fontsize=10, fontweight="bold", color=PURPLE)
    ax3_twin.tick_params(axis="y", labelcolor=PURPLE)
    ax3_twin.set_ylim(800, 2200)
    ax3_twin.grid(False)
    ax3_twin.legend(loc="lower right", frameon=True, fontsize=8)
    
    # Panel 4: Regional Revenue Diversification (FY21 vs FY24 vs FY29E)
    ax4 = axes[1, 1]
    regions = ["South Hub", "West Hub", "North Hub", "East Hub", "International"]
    fy21_reg = [110.3, 61.3, 36.8, 24.5, 12.3]
    fy24_reg = [224.1, 124.5, 74.7, 49.8, 24.9]
    fy29_reg = [475.0, 296.9, 201.9, 130.6, 83.1]
    
    rx = np.arange(len(regions))
    rw = 0.25
    ax4.bar(rx - rw, fy21_reg, rw, label="FY21 Actual (INR 245 Cr)", color="#BDD7EE")
    ax4.bar(rx, fy24_reg, rw, label="FY24 Actual (INR 498 Cr)", color=TEAL)
    ax4.bar(rx + rw, fy29_reg, rw, label="FY29E Projected (INR 1,187 Cr)", color=NAVY)
    
    ax4.set_title("D. Regional Hub Revenue Expansion (INR Crore)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax4.set_ylabel("Regional Revenue (INR Crore)", fontsize=10, fontweight="bold")
    ax4.set_xticks(rx)
    ax4.set_xticklabels(regions, fontsize=9, fontweight="bold")
    ax4.legend(loc="upper right", frameon=True, fontsize=8)
    
    plt.suptitle("AURAGEN DIAGNOSTICS - REVENUE, MARGIN & OPERATIONAL GROWTH METRICS", fontsize=15, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    
    out_file = os.path.join(OUTPUTS_DIR, "revenue_trend.png")
    plt.savefig(out_file, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[EXPORT] Generated Revenue Dashboard: {out_file}")


def create_financial_analysis_dashboard():
    """Generate 4-panel financial deep-dive: ROIC/ROCE, Cost Structure, FCF Conversion, Valuation Sensitivity."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    # Panel 1: Return on Capital Metrics (FY21 - FY24 Historical Actuals)
    ax1 = axes[0, 0]
    hist_years = ["FY21", "FY22", "FY23", "FY24"]
    hx = np.arange(len(hist_years))
    
    roic = [21.12, 24.03, 26.80, 29.00]
    roce = [24.05, 26.36, 28.12, 29.48]
    roe =  [21.84, 22.99, 23.68, 24.09]
    
    ax1.plot(hx, roic, marker="o", color=NAVY, linewidth=2.5, markersize=7, label="ROIC (Return on Invested Capital)")
    ax1.plot(hx, roce, marker="s", color=TEAL, linewidth=2.2, markersize=7, label="ROCE (Return on Capital Employed)")
    ax1.plot(hx, roe, marker="^", color=CORAL, linewidth=2.0, markersize=7, label="ROE (Return on Equity)")
    
    for i in range(len(hist_years)):
        ax1.annotate(f"{roic[i]:.1f}%", (hx[i], roic[i] + 0.6), ha="center", fontsize=8, fontweight="bold", color=NAVY)
        ax1.annotate(f"{roce[i]:.1f}%", (hx[i], roce[i] - 1.1), ha="center", fontsize=8, color=TEAL)
        ax1.annotate(f"{roe[i]:.1f}%", (hx[i], roe[i] + 0.6), ha="center", fontsize=8, color=CORAL)
        
    ax1.set_title("A. Capital Efficiency & Return Ratios (FY21 - FY24 Actuals)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax1.set_ylabel("Return Metric (%)", fontsize=10, fontweight="bold")
    ax1.set_xticks(hx)
    ax1.set_xticklabels(hist_years, fontsize=9, fontweight="bold")
    ax1.set_ylim(18, 33)
    ax1.legend(loc="lower right", frameon=True, fontsize=8)
    
    # Panel 2: Cost Structure Optimization (% of Revenue)
    ax2 = axes[0, 1]
    years_all = ["FY21", "FY22", "FY23", "FY24", "FY25E", "FY27E", "FY29E"]
    ax2_x = np.arange(len(years_all))
    
    cogs_pct = [33.3, 32.5, 31.6, 31.0, 30.0, 30.0, 30.0]
    personnel_pct = [19.6, 19.2, 18.9, 18.3, 17.5, 17.5, 17.5]
    logistics_pct = [8.6, 8.5, 8.4, 8.4, 8.0, 8.0, 8.0]
    lab_opex_pct = [5.1, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    sga_pct = [3.7, 3.7, 3.7, 3.7, 3.5, 3.5, 3.5]
    
    ax2.plot(ax2_x, cogs_pct, marker="o", color=NAVY, linewidth=2.2, label="COGS / Reagents %")
    ax2.plot(ax2_x, personnel_pct, marker="s", color=TEAL, linewidth=2.0, label="Personnel / Pathologists %")
    ax2.plot(ax2_x, logistics_pct, marker="^", color=CORAL, linewidth=1.8, label="Cold-Chain Logistics %")
    ax2.plot(ax2_x, lab_opex_pct, marker="D", color=GOLD, linewidth=1.8, label="Lab Opex & Quality %")
    ax2.plot(ax2_x, sga_pct, marker="v", color="#7030A0", linewidth=1.8, label="SG&A Corporate %")
    
    ax2.set_title("B. Cost Structure Efficiency (% of Revenue)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax2.set_ylabel("% of Operating Revenue", fontsize=10, fontweight="bold")
    ax2.set_xticks(ax2_x)
    ax2.set_xticklabels(years_all, fontsize=9)
    ax2.set_ylim(0, 38)
    ax2.legend(loc="center right", frameon=True, fontsize=8)
    
    # Panel 3: Cash Flow Bridge & Cash Conversion
    ax3 = axes[1, 0]
    cf_years = ["FY21", "FY22", "FY23", "FY24", "FY25E", "FY26E", "FY27E", "FY28E", "FY29E"]
    cx = np.arange(len(cf_years))
    
    ebitda_cf = [73.0, 97.0, 128.0, 167.5, 206.6, 252.6, 304.9, 363.4, 427.5]
    cfo = [55.4, 74.2, 98.5, 129.9, 151.0, 178.5, 207.2, 237.5, 269.2]
    fcff = [27.4, 40.2, 56.5, 81.9, 104.9, 134.1, 168.5, 209.5, 256.3]
    
    ax3.bar(cx - 0.22, ebitda_cf, width=0.22, label="EBITDA", color="#BDD7EE")
    ax3.bar(cx, cfo, width=0.22, label="Cash from Operations (CFO)", color=TEAL)
    ax3.bar(cx + 0.22, fcff, width=0.22, label="Free Cash Flow (FCFF)", color=NAVY)
    
    ax3.set_title("C. Cash Flow Generation: EBITDA vs CFO vs FCFF (INR Cr)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax3.set_ylabel("Cash Flow (INR Crore)", fontsize=10, fontweight="bold")
    ax3.set_xticks(cx)
    ax3.set_xticklabels(cf_years, fontsize=9)
    ax3.legend(loc="upper left", frameon=True, fontsize=8)
    
    # Panel 4: Valuation Sensitivity Heatmap (WACC vs Perpetual Terminal Growth)
    ax4 = axes[1, 1]
    wacc_labels = ["10.50%", "11.00%", "11.50%", "11.89%", "12.50%", "13.00%"]
    growth_labels = ["4.0%", "4.5%", "5.0%", "5.5%", "6.0%"]
    
    # Matrix values calculated in DCFModel
    ev_heatmap_data = np.array([
        [3114.5, 3334.8, 3595.2, 3907.8, 4289.7],
        [2876.0, 3061.5, 3277.9, 3533.7, 3840.6],
        [2669.7, 2827.6, 3009.8, 3222.3, 3473.5],
        [2527.0, 2667.2, 2827.8, 3013.5, 3230.7],
        [2330.4, 2448.1, 2581.4, 2733.8, 2909.6],
        [2189.4, 2292.1, 2407.7, 2538.7, 2688.4]
    ])
    
    sns.heatmap(ev_heatmap_data, ax=ax4, annot=True, fmt=".1f", cmap="YlGnBu",
                xticklabels=growth_labels, yticklabels=wacc_labels, cbar_kws={"label": "Enterprise Value (INR Cr)"})
    ax4.set_title("D. Enterprise Value Sensitivity Heatmap (WACC vs g)", fontsize=12, fontweight="bold", color=NAVY, pad=10)
    ax4.set_xlabel("Terminal Perpetuity Growth Rate (g)", fontsize=10, fontweight="bold")
    ax4.set_ylabel("WACC Discount Rate", fontsize=10, fontweight="bold")
    
    plt.suptitle("AURAGEN DIAGNOSTICS - FINANCIAL RATIOS, CASH CONVERSION & VALUATION SENSITIVITY", fontsize=15, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    
    out_file = os.path.join(OUTPUTS_DIR, "financial_analysis.png")
    plt.savefig(out_file, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[EXPORT] Generated Financial Analysis Dashboard: {out_file}")


def main():
    create_revenue_trend_dashboard()
    create_financial_analysis_dashboard()


if __name__ == "__main__":
    main()

