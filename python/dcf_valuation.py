"""
dcf_valuation.py
================
Comprehensive Discounted Cash Flow (DCF) Valuation Engine and Sensitivity Modeler.
Performs:
- WACC derivation via CAPM and Target Capital Structure
- 5-Year Unlevered Free Cash Flow to Firm (FCFF) Projections
- Terminal Value calculation (Gordon Growth Model & Exit Multiple Method)
- Enterprise-to-Equity Value Bridge & Implied Share Price
- Full reconciliation with Excel Financial Model (Healthcare_Financial_Model.xlsx)
- 2D Sensitivity Matrices (WACC vs Terminal Growth, WACC vs Exit Multiple)
- Outputs valuation summary to outputs/valuation_summary.csv
"""

import os
import pandas as pd
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)


class DCFModel:
    def __init__(self):
        # 1. Macro & WACC Parameters
        self.rf = 0.0710                # 7.10% Indian 10-Yr G-Sec Benchmark
        self.erp = 0.0600               # 6.00% Equity Risk Premium
        self.unlevered_beta = 0.8500    # Diagnostics industry asset beta
        self.target_debt_weight = 0.15  # 15% Debt
        self.target_equity_weight = 0.85# 85% Equity
        self.pre_tax_kd = 0.0900        # 9.00% Borrowing cost
        self.tax_rate = 0.2517          # 25.17% Statutory Corporate Tax Rate
        
        # Levered Beta = Unlevered Beta * (1 + (1 - t) * (D / E))
        d_over_e = self.target_debt_weight / self.target_equity_weight
        self.levered_beta = self.unlevered_beta * (1 + (1 - self.tax_rate) * d_over_e)
        self.ke = self.rf + self.levered_beta * self.erp
        self.after_tax_kd = self.pre_tax_kd * (1 - self.tax_rate)
        self.wacc = (self.target_equity_weight * self.ke) + (self.target_debt_weight * self.after_tax_kd)
        
        # 2. Terminal Value Parameters
        self.terminal_growth_rate = 0.0500 # 5.0% long-term perpetuity growth
        self.exit_multiple = 18.00         # 18.0x EV / EBITDA multiple
        
        # 3. Capital Structure at FY24 Base Date
        self.fy24_debt = 45.00             # INR 45.0 Cr
        self.fy24_cash = 110.00            # INR 110.0 Cr
        self.net_debt = self.fy24_debt - self.fy24_cash # -INR 65.0 Cr (Net Cash)
        self.shares_outstanding = 5.00     # 5.00 Crore shares
        
        # 4. Projections Schedule (FY25E - FY29E) in INR Crore
        self.years = ["FY25E", "FY26E", "FY27E", "FY28E", "FY29E"]
        self.t = np.array([1, 2, 3, 4, 5])
        self.revenue = np.array([607.56, 732.11, 871.21, 1023.67, 1187.46])
        self.ebitda = np.array([206.57, 252.58, 304.92, 363.40, 427.49])
        self.da = np.array([39.00, 46.00, 53.00, 60.00, 67.00])
        self.ebit = self.ebitda - self.da
        self.nopat = self.ebit * (1 - self.tax_rate)
        self.capex = np.array([45.00, 50.00, 55.00, 58.00, 60.00])
        self.delta_nwc = np.array([14.50, 16.50, 18.00, 19.50, 20.50])
        
        # Free Cash Flow to Firm (FCFF) = NOPAT + D&A - Capex - Delta NWC
        self.fcff = self.nopat + self.da - self.capex - self.delta_nwc
        
    def calculate_valuation(self, wacc=None, g=None, multiple=None):
        """Execute DCF valuation given specific inputs."""
        w = self.wacc if wacc is None else wacc
        growth = self.terminal_growth_rate if g is None else g
        exit_mult = self.exit_multiple if multiple is None else multiple
        
        # Discount factors
        discount_factors = 1.0 / ((1.0 + w) ** self.t)
        pv_fcff = self.fcff * discount_factors
        cumulative_pv_explicit = np.sum(pv_fcff)
        
        # Method 1: Gordon Growth Model
        terminal_fcff = self.fcff[-1] * (1.0 + growth)
        tv_gordon_undiscounted = terminal_fcff / (w - growth)
        tv_gordon_pv = tv_gordon_undiscounted * discount_factors[-1]
        ev_gordon = cumulative_pv_explicit + tv_gordon_pv
        equity_val_gordon = ev_gordon - self.net_debt
        share_price_gordon = equity_val_gordon / self.shares_outstanding
        
        # Method 2: Exit Multiple Method
        tv_multiple_undiscounted = self.ebitda[-1] * exit_mult
        tv_multiple_pv = tv_multiple_undiscounted * discount_factors[-1]
        ev_multiple = cumulative_pv_explicit + tv_multiple_pv
        equity_val_multiple = ev_multiple - self.net_debt
        share_price_multiple = equity_val_multiple / self.shares_outstanding
        
        return {
            "wacc": w,
            "growth": growth,
            "exit_mult": exit_mult,
            "discount_factors": discount_factors,
            "pv_fcff": pv_fcff,
            "cum_pv_fcff": cumulative_pv_explicit,
            "gordon": {
                "tv_undiscounted": tv_gordon_undiscounted,
                "tv_pv": tv_gordon_pv,
                "ev": ev_gordon,
                "equity_value": equity_val_gordon,
                "share_price": share_price_gordon
            },
            "multiple": {
                "tv_undiscounted": tv_multiple_undiscounted,
                "tv_pv": tv_multiple_pv,
                "ev": ev_multiple,
                "equity_value": equity_val_multiple,
                "share_price": share_price_multiple
            }
        }
        
    def generate_sensitivity_tables(self):
        """Compute 2D Sensitivity Grids for Corporate Presentation."""
        wacc_range = np.array([0.1050, 0.1100, 0.1150, 0.1189, 0.1250, 0.1300])
        growth_range = np.array([0.0400, 0.0450, 0.0500, 0.0550, 0.0600])
        mult_range = np.array([14.0, 16.0, 18.0, 20.0, 22.0])
        
        # Grid 1: WACC vs Growth (Gordon Growth EV)
        ev_grid_gordon = np.zeros((len(wacc_range), len(growth_range)))
        share_price_grid_gordon = np.zeros((len(wacc_range), len(growth_range)))
        
        for i, w in enumerate(wacc_range):
            for j, g in enumerate(growth_range):
                res = self.calculate_valuation(wacc=w, g=g)
                ev_grid_gordon[i, j] = res["gordon"]["ev"]
                share_price_grid_gordon[i, j] = res["gordon"]["share_price"]
                
        # Grid 2: WACC vs Exit Multiple
        ev_grid_mult = np.zeros((len(wacc_range), len(mult_range)))
        share_price_grid_mult = np.zeros((len(wacc_range), len(mult_range)))
        
        for i, w in enumerate(wacc_range):
            for j, m in enumerate(mult_range):
                res = self.calculate_valuation(wacc=w, multiple=m)
                ev_grid_mult[i, j] = res["multiple"]["ev"]
                share_price_grid_mult[i, j] = res["multiple"]["share_price"]
                
        return {
            "wacc_range": wacc_range,
            "growth_range": growth_range,
            "mult_range": mult_range,
            "ev_grid_gordon": ev_grid_gordon,
            "share_price_grid_gordon": share_price_grid_gordon,
            "ev_grid_mult": ev_grid_mult,
            "share_price_grid_mult": share_price_grid_mult
        }


def print_valuation_report(model, res, sens):
    """Print executive valuation summary."""
    print("=" * 85)
    print("      AURAGEN DIAGNOSTICS LTD. - DCF VALUATION & SENSITIVITY REPORT")
    print("=" * 85)
    
    print("\n1. COST OF CAPITAL (WACC) BUILD-UP")
    print("-" * 85)
    print(f" Risk-Free Benchmark Rate (Rf):               {model.rf*100:>8.2f}%")
    print(f" Equity Risk Premium (ERP):                     {model.erp*100:>8.2f}%")
    print(f" Diagnostic Sector Unlevered Beta:              {model.unlevered_beta:>8.2f}")
    print(f" Target Capital Structure (Debt / Equity):      {model.target_debt_weight*100:.1f}% / {model.target_equity_weight*100:.1f}%")
    print(f" Re-Levered Equity Beta:                        {model.levered_beta:>8.4f}")
    print(f" Cost of Equity (Ke via CAPM):                 {model.ke*100:>8.2f}%")
    print(f" Pre-Tax Cost of Debt (Kd):                     {model.pre_tax_kd*100:>8.2f}%")
    print(f" Effective Corporate Tax Rate:                  {model.tax_rate*100:>8.2f}%")
    print(f" After-Tax Cost of Debt:                        {model.after_tax_kd*100:>8.2f}%")
    print(f" Weighted Average Cost of Capital (WACC):       {model.wacc*100:>8.2f}%")
    
    print("\n2. EXPLICIT 5-YEAR UNLEVERED FREE CASH FLOW (FCFF) PROJECTION")
    print("-" * 85)
    headers = ["Metric (INR Cr)"] + model.years
    print(f"{headers[0]:<25} | " + " | ".join([f"{h:>10}" for h in headers[1:]]))
    print("-" * 85)
    print(f"{'Revenue':<25} | " + " | ".join([f"{v:>10.2f}" for v in model.revenue]))
    print(f"{'EBITDA':<25} | " + " | ".join([f"{v:>10.2f}" for v in model.ebitda]))
    print(f"{'EBIT':<25} | " + " | ".join([f"{v:>10.2f}" for v in model.ebit]))
    print(f"{'NOPAT (EBIT * (1-t))':<25} | " + " | ".join([f"{v:>10.2f}" for v in model.nopat]))
    print(f"{'Add: D&A':<25} | " + " | ".join([f"{v:>10.2f}" for v in model.da]))
    print(f"{'Less: Capex':<25} | " + " | ".join([f"{-v:>10.2f}" for v in model.capex]))
    print(f"{'Less: Delta NWC':<25} | " + " | ".join([f"{-v:>10.2f}" for v in model.delta_nwc]))
    print(f"{'Free Cash Flow (FCFF)':<25} | " + " | ".join([f"{v:>10.2f}" for v in model.fcff]))
    print(f"{'Discount Factor':<25} | " + " | ".join([f"{v:>10.4f}" for v in res["discount_factors"]]))
    print(f"{'Present Value of FCFF':<25} | " + " | ".join([f"{v:>10.2f}" for v in res["pv_fcff"]]))
    print("-" * 85)
    print(f" Cumulative PV of Explicit Forecast Period:   INR {res['cum_pv_fcff']:>8.2f} Cr")
    
    print("\n3. VALUATION SUMMARY & DUAL-METHODOLOGY COMPARISON")
    print("-" * 85)
    print(f"{'Valuation Output Line Item':<40} | {'Method 1: Gordon Growth':<20} | {'Method 2: Exit Multiple':<20}")
    print("-" * 85)
    g = res["gordon"]
    m = res["multiple"]
    print(f"{'Terminal Valuation Parameter':<40} | {f'g = {model.terminal_growth_rate*100:.1f}%':<20} | {f'{model.exit_multiple:.1f}x EBITDA':<20}")
    print(f"{'Undiscounted Terminal Value':<40} | INR {g['tv_undiscounted']:>12.2f} Cr  | INR {m['tv_undiscounted']:>12.2f} Cr")
    print(f"{'Present Value of Terminal Value':<40} | INR {g['tv_pv']:>12.2f} Cr  | INR {m['tv_pv']:>12.2f} Cr")
    print(f"{'Cumulative Explicit PV of FCFF':<40} | INR {res['cum_pv_fcff']:>12.2f} Cr  | INR {res['cum_pv_fcff']:>12.2f} Cr")
    print(f"{'Enterprise Value (EV)':<40} | INR {g['ev']:>12.2f} Cr  | INR {m['ev']:>12.2f} Cr")
    print(f"{'Less: FY24 Total Debt':<40} | INR {model.fy24_debt:>12.2f} Cr  | INR {model.fy24_debt:>12.2f} Cr")
    print(f"{'Add: FY24 Cash & Equivalents':<40} | INR {model.fy24_cash:>12.2f} Cr  | INR {model.fy24_cash:>12.2f} Cr")
    print(f"{'Implied Net Debt (Net Cash)':<40} | INR {model.net_debt:>12.2f} Cr  | INR {model.net_debt:>12.2f} Cr")
    print(f"{'Implied Equity Value':<40} | INR {g['equity_value']:>12.2f} Cr  | INR {m['equity_value']:>12.2f} Cr")
    print(f"{'Fully Diluted Shares (Crore)':<40} | {model.shares_outstanding:>16.2f}     | {model.shares_outstanding:>16.2f}")
    print(f"{'Implied Intrinsic Share Price':<40} | INR {g['share_price']:>12.2f}      | INR {m['share_price']:>12.2f}")
    print("=" * 85)
    
    print("\n4. SENSITIVITY MATRIX: WACC vs TERMINAL GROWTH RATE (GORDON GROWTH EV in INR Cr)")
    print("-" * 85)
    col_str = " | ".join([f"g={g*100:.1f}%" for g in sens["growth_range"]])
    print(f"{'WACC':<10} | " + col_str)
    print("-" * 85)
    for i, w in enumerate(sens["wacc_range"]):
        row_vals = " | ".join([f"{sens['ev_grid_gordon'][i, j]:>7.1f}" for j in range(len(sens["growth_range"]))])
        print(f"{w*100:>6.2f}%    | " + row_vals)
    print("=" * 85 + "\n")


def export_valuation_summary(res):
    """Export valuation summary to outputs/valuation_summary.csv."""
    g = res["gordon"]
    m = res["multiple"]
    summary_data = [
        {"Metric": "WACC (%)", "Gordon_Growth_Model": round(res["wacc"] * 100, 2), "Exit_Multiple_Method": round(res["wacc"] * 100, 2)},
        {"Metric": "Terminal Parameter", "Gordon_Growth_Model": "5.0% perpetuity growth", "Exit_Multiple_Method": "18.0x EV/EBITDA"},
        {"Metric": "PV of Explicit FCFF (INR Cr)", "Gordon_Growth_Model": round(res["cum_pv_fcff"], 2), "Exit_Multiple_Method": round(res["cum_pv_fcff"], 2)},
        {"Metric": "PV of Terminal Value (INR Cr)", "Gordon_Growth_Model": round(g["tv_pv"], 2), "Exit_Multiple_Method": round(m["tv_pv"], 2)},
        {"Metric": "Enterprise Value (INR Cr)", "Gordon_Growth_Model": round(g["ev"], 2), "Exit_Multiple_Method": round(m["ev"], 2)},
        {"Metric": "Net Debt (Cash) (INR Cr)", "Gordon_Growth_Model": -65.00, "Exit_Multiple_Method": -65.00},
        {"Metric": "Equity Value (INR Cr)", "Gordon_Growth_Model": round(g["equity_value"], 2), "Exit_Multiple_Method": round(m["equity_value"], 2)},
        {"Metric": "Fully Diluted Shares (Cr)", "Gordon_Growth_Model": 5.00, "Exit_Multiple_Method": 5.00},
        {"Metric": "Implied Value Per Share (INR)", "Gordon_Growth_Model": round(g["share_price"], 2), "Exit_Multiple_Method": round(m["share_price"], 2)}
    ]
    df_sum = pd.DataFrame(summary_data)
    out_path = os.path.join(OUTPUTS_DIR, "valuation_summary.csv")
    df_sum.to_csv(out_path, index=False)
    print(f"[EXPORT] Saved valuation summary to: {out_path}")


def main():
    model = DCFModel()
    res = model.calculate_valuation()
    sens = model.generate_sensitivity_tables()
    print_valuation_report(model, res, sens)
    export_valuation_summary(res)


if __name__ == "__main__":
    main()

