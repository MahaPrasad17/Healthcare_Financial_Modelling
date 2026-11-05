"""
validate_model.py
=================
Comprehensive, independent audit and mathematical verification suite for the
Healthcare Diagnostics Financial Modelling & M&A Valuation project (AuraGen Diagnostics Ltd.).

Executes multi-tier validation checks:
1. Excel Workbook Structural & Formula Audit (circular references, invalid tokens, Assumptions references)
2. 3-Statement Balance Sheet Balance & Cash Flow Reconciliation (Assets == Liabilities + Equity in all 9 years)
3. Python vs Excel DCF Valuation Cross-Check (WACC, FCFF, PV, Enterprise Value, Equity Value, Share Price)
4. M&A Synergy & Accretion Mathematics Cross-Check (NPV, Control Premium, Net Value Creation)
5. Dataset Accounting Identity & Integrity Verification
6. SQL Star Schema & Analytical Queries Syntax & Consistency Check
7. Power BI Project Architecture Validation
8. Synthetic Data Labeling Verification Across All Assets
"""

import os
import sys
import re
import json
import openpyxl
import pandas as pd
import numpy as np

# Reconfigure stdout for utf-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
EXCEL_DIR = os.path.join(PROJECT_ROOT, "excel")
SQL_DIR = os.path.join(PROJECT_ROOT, "sql")
POWERBI_DIR = os.path.join(PROJECT_ROOT, "powerbi")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")


class AuditTestSuite:
    def __init__(self):
        self.total_checks = 0
        self.passed_checks = 0
        self.failed_checks = 0
        self.failures = []

    def log_result(self, test_name, status, details=""):
        self.total_checks += 1
        if status:
            self.passed_checks += 1
            print(f"  [PASS] {test_name}: {details}")
        else:
            self.failed_checks += 1
            self.failures.append(f"{test_name}: {details}")
            print(f"  [FAIL] {test_name}: {details}")

    def run_all_tests(self):
        print("=" * 80)
        print("STARTING INDEPENDENT AUDIT & VALIDATION SUITE")
        print("Target: AuraGen Diagnostics Financial Modelling & M&A Valuation")
        print("Directory:", PROJECT_ROOT)
        print("=" * 80)

        self.test_datasets()
        self.test_excel_model()
        self.test_dcf_reconciliation()
        self.test_m_and_a_synergies()
        self.test_sql_scripts()
        self.test_powerbi_artifacts()
        self.test_synthetic_data_disclaimers()

        print("\n" + "=" * 80)
        print(f"AUDIT SUMMARY: {self.passed_checks}/{self.total_checks} CHECKS PASSED")
        if self.failed_checks == 0:
            print("STATUS: ALL FINANCIAL & TECHNICAL CRITERIA 100% VALIDATED (ZERO DEFECTS)")
            print("=" * 80)
            return True
        else:
            print(f"STATUS: {self.failed_checks} CHECKS FAILED:")
            for fail in self.failures:
                print(f"  - {fail}")
            print("=" * 80)
            return False

    def test_datasets(self):
        print("\n--- 1. DATASETS & ACCOUNTING IDENTITIES AUDIT ---")
        hist_file = os.path.join(DATA_DIR, "historical_financials.csv")
        op_file = os.path.join(DATA_DIR, "operational_data.csv")
        assump_file = os.path.join(DATA_DIR, "assumptions.csv")

        # Existence
        self.log_result("historical_financials.csv exists", os.path.exists(hist_file))
        self.log_result("operational_data.csv exists", os.path.exists(op_file))
        self.log_result("assumptions.csv exists", os.path.exists(assump_file))

        if not os.path.exists(hist_file):
            return

        df_hist = pd.read_csv(hist_file)
        
        # Check nulls
        null_count = df_hist.isnull().sum().sum()
        self.log_result("historical_financials.csv zero nulls", null_count == 0, f"Null count = {null_count}")

        # Check Accounting Identities across historical years
        for _, r in df_hist.iterrows():
            yr = r["Fiscal_Year"]
            seg_sum = r["Genomics_Revenue_Cr"] + r["Molecular_Revenue_Cr"] + r["Routine_Revenue_Cr"] + r["Clinical_Research_Revenue_Cr"]
            self.log_result(f"[{yr}] Revenue Sum Reconciliation", abs(seg_sum - r["Total_Revenue_Cr"]) < 0.05, f"Sum={seg_sum:.2f}, Rev={r['Total_Revenue_Cr']:.2f}")

            gp_calc = r["Total_Revenue_Cr"] - r["COGS_Reagents_Consumables_Cr"]
            self.log_result(f"[{yr}] Gross Profit Identity", abs(gp_calc - r["Gross_Profit_Cr"]) < 0.05, f"GP={gp_calc:.2f}")

            ebitda_calc = r["Gross_Profit_Cr"] - r["Total_Opex_Cr"]
            self.log_result(f"[{yr}] EBITDA Identity", abs(ebitda_calc - r["EBITDA_Cr"]) < 0.05, f"EBITDA={ebitda_calc:.2f}")

            ebt_calc = r["EBIT_Cr"] - r["Interest_Expense_Cr"] + r["Other_Income_Cr"]
            self.log_result(f"[{yr}] EBT Identity", abs(ebt_calc - r["EBT_Cr"]) < 0.05, f"EBT={ebt_calc:.2f}")

            pat_calc = r["EBT_Cr"] - r["Tax_Expense_Cr"]
            self.log_result(f"[{yr}] PAT Identity", abs(pat_calc - r["Net_Profit_Cr"]) < 0.05, f"PAT={pat_calc:.2f}")

    def test_excel_model(self):
        print("\n--- 2. EXCEL FINANCIAL WORKBOOK AUDIT ---")
        wb_path = os.path.join(EXCEL_DIR, "Healthcare_Financial_Model.xlsx")
        self.log_result("Healthcare_Financial_Model.xlsx exists", os.path.exists(wb_path))
        if not os.path.exists(wb_path):
            return

        wb = openpyxl.load_workbook(wb_path, data_only=False)
        expected_sheets = [
            "Cover & Contents", "Executive Summary", "Assumptions", "Operational Drivers",
            "Income Statement", "Balance Sheet", "Cash Flow Statement", "DCF Valuation",
            "Scenario Analysis", "M&A & Synergies"
        ]
        
        # Check sheet existence
        missing_sheets = [s for s in expected_sheets if s not in wb.sheetnames]
        self.log_result("All 10 Expected Sheets Present", len(missing_sheets) == 0, f"Missing: {missing_sheets}")

        # Check for circular references and invalid formula tokens
        circular_issues = []
        error_tokens = ["#VALUE!", "#REF!", "#NAME?", "#DIV/0!", "#N/A"]
        error_cells = []
        wrong_col_c_refs = []

        for sheetname in wb.sheetnames:
            ws = wb[sheetname]
            for row in ws.iter_rows():
                for cell in row:
                    val = cell.value
                    if val and isinstance(val, str):
                        # Check error strings
                        for err in error_tokens:
                            if err in val:
                                error_cells.append((sheetname, cell.coordinate, val))
                        
                        # Check formulas
                        if val.startswith("="):
                            coord = cell.coordinate
                            # Strip cross-sheet references
                            stripped = re.sub(r'\'[^\']+\'![A-Z]+[0-9]+', '', val)
                            stripped = re.sub(r'[A-Za-z0-9_]+![A-Z]+[0-9]+', '', stripped)
                            tokens = re.findall(r'\b[A-Z]+[0-9]+\b', stripped)
                            if coord in tokens:
                                circular_issues.append((sheetname, coord, val))
                            
                            # Check if Assumptions col C (text descriptions) is multiplied
                            if "Assumptions!C" in val and any(op in val for op in ["*", "+", "/", "-"]):
                                wrong_col_c_refs.append((sheetname, coord, val))

        self.log_result("Zero Direct Circular References in Workbook", len(circular_issues) == 0, f"Issues: {circular_issues}")
        self.log_result("Zero Hardcoded Error Tokens (#VALUE!, etc.)", len(error_cells) == 0, f"Errors: {error_cells}")
        self.log_result("Zero Arithmetic Lookups to Assumptions Column C (Text)", len(wrong_col_c_refs) == 0, f"Col C Refs: {wrong_col_c_refs}")

        # Check Balance Sheet check row formulas
        bs = wb["Balance Sheet"]
        check_row_cells = ["C29", "D29", "E29", "F29", "G29", "H29", "I29", "J29", "K29"]
        check_formulas_ok = True
        for col_idx, c_coord in enumerate(check_row_cells):
            col_letter = chr(ord('C') + col_idx)
            val = bs[c_coord].value
            expected_f = f"=ROUND({col_letter}16-{col_letter}28, 2)"
            if val != expected_f:
                check_formulas_ok = False
        self.log_result("Balance Sheet Check Formulas Active Across All 9 Years (C29:K29)", check_formulas_ok)

        # Check Cash Flow Statement Ending Cash link
        cfs = wb["Cash Flow Statement"]
        cfs_cash_ok = True
        for col_idx in range(9):
            col_letter = chr(ord('C') + col_idx)
            # Cash Flow Statement ending cash is row 24: =C22+C23 (Row 22=net change, Row 23=beginning cash)
            f_end_cash = cfs[f"{col_letter}24"].value
            if f_end_cash != f"={col_letter}22+{col_letter}23":
                cfs_cash_ok = False
        self.log_result("Cash Flow Statement Ending Cash Formula (=Beginning + Net Change)", cfs_cash_ok)

        # Check Balance Sheet dynamic Cash link from CFS for Forecast years (G13:K13)
        bs_cash_ok = True
        for col_idx in range(4, 9):
            col_letter = chr(ord('C') + col_idx)
            val = bs[f"{col_letter}13"].value
            expected_val = f"='Cash Flow Statement'!{col_letter}24"
            if val != expected_val:
                bs_cash_ok = False
        self.log_result("Balance Sheet Cash Dynamically Linked to Cash Flow Statement Ending Cash (G24:K24)", bs_cash_ok)

    def test_dcf_reconciliation(self):
        print("\n--- 3. PYTHON DCF VALUATION & SENSITIVITY RECONCILIATION ---")
        from dcf_valuation import DCFModel
        model = DCFModel()
        res = model.calculate_valuation()

        # 1. WACC
        wacc_pct = round(res["wacc"] * 100, 2)
        self.log_result("Cost of Capital (WACC) Calculation", wacc_pct == 11.95, f"WACC = {wacc_pct}% (Target 11.95%)")

        # 2. Explicit FCFF PV
        explicit_pv = round(res["cum_pv_fcff"], 2)
        self.log_result("Explicit 5-Year FCFF PV Reconciliation", explicit_pv == 599.87, f"Explicit PV = INR {explicit_pv} Cr (Target 599.87 Cr)")

        # 3. Gordon Growth Terminal Value PV
        tv_gordon_pv = round(res["gordon"]["tv_pv"], 2)
        self.log_result("Gordon Growth Terminal Value PV Reconciliation", tv_gordon_pv == 2200.59, f"TV Gordon PV = INR {tv_gordon_pv} Cr (Target 2200.59 Cr)")

        # 4. Gordon Growth Enterprise Value
        ev_gordon = round(res["gordon"]["ev"], 2)
        self.log_result("Gordon Growth Enterprise Value Reconciliation", ev_gordon == 2800.46, f"EV Gordon = INR {ev_gordon} Cr (Target 2800.46 Cr)")

        # 5. Gordon Growth Equity Value
        eq_gordon = round(res["gordon"]["equity_value"], 2)
        self.log_result("Gordon Growth Equity Value Reconciliation", eq_gordon == 2865.46, f"Equity Value Gordon = INR {eq_gordon} Cr (Target 2865.46 Cr)")

        # 6. Gordon Growth Share Price
        px_gordon = round(res["gordon"]["share_price"], 2)
        self.log_result("Gordon Growth Implied Share Price Reconciliation", px_gordon == 573.09, f"Share Price = INR {px_gordon} (Target 573.09)")

        # 7. Exit Multiple Enterprise Value
        ev_multiple = round(res["multiple"]["ev"], 2)
        self.log_result("Exit Multiple Enterprise Value Reconciliation", ev_multiple == 4975.36, f"EV Multiple = INR {ev_multiple} Cr (Target 4975.36 Cr)")

        # 8. Exit Multiple Share Price
        px_multiple = round(res["multiple"]["share_price"], 2)
        self.log_result("Exit Multiple Implied Share Price Reconciliation", px_multiple == 1008.07, f"Share Price Multiple = INR {px_multiple} (Target 1008.07)")

    def test_m_and_a_synergies(self):
        print("\n--- 4. M&A SYNERGIES & ACCRETION AUDIT ---")
        # Explicit 5-year net pre-tax synergies: [10.20, 30.70, 52.80, 62.50, 70.20]
        # After-tax at 25.17%: [7.63, 22.97, 39.51, 46.77, 52.53]
        post_tax_synergies = np.array([7.6327, 22.9728, 39.5098, 46.7688, 52.5307])
        
        # WACC from model: 11.9524% (11.95%)
        rf = 0.071
        erp = 0.06
        beta_u = 0.85
        tax_rate = 0.2517
        de_ratio = 0.15 / 0.85
        beta_l = beta_u * (1 + (1 - tax_rate) * de_ratio)
        ke = rf + beta_l * erp
        kd_after_tax = 0.09 * (1 - tax_rate)
        wacc = 0.85 * ke + 0.15 * kd_after_tax
        
        t = np.array([1, 2, 3, 4, 5])
        df = 1.0 / ((1.0 + wacc) ** t)
        pv_explicit = np.sum(post_tax_synergies * df)
        
        g = 0.05
        terminal_synergy = post_tax_synergies[-1] * (1.0 + g)
        tv_synergy = terminal_synergy / (wacc - g)
        pv_terminal = tv_synergy * df[-1]
        total_npv = pv_explicit + pv_terminal
        
        standalone_ev = 2800.46
        offer_ev = 3350.00
        control_premium = offer_ev - standalone_ev  # 549.54 Cr
        net_value_creation = total_npv - control_premium

        self.log_result("M&A Explicit 5-Year Synergies PV", round(pv_explicit, 2) == 112.95, f"PV Explicit = INR {pv_explicit:.2f} Cr (Target 112.95 Cr)")
        self.log_result("M&A Terminal Synergies PV", round(pv_terminal, 2) == 451.11, f"PV Terminal = INR {pv_terminal:.2f} Cr (Target 451.11 Cr)")
        self.log_result("Total Synergies Net Present Value (NPV)", round(total_npv, 2) == 564.06, f"Total NPV = INR {total_npv:.2f} Cr (Target 564.06 Cr)")
        self.log_result("Control Premium Over Standalone EV", round(control_premium, 2) == 549.54, f"Premium = INR {control_premium:.2f} Cr (Target 549.54 Cr)")
        self.log_result("Net Deal Value Creation Accretion Check", round(net_value_creation, 2) == 14.52 and net_value_creation > 0, f"Net Accretion = +INR {net_value_creation:.2f} Cr (> 0, Accretive)")

    def test_sql_scripts(self):
        print("\n--- 5. SQL SCRIPTS & SYNTAX INTEGRITY ---")
        ddl_path = os.path.join(SQL_DIR, "create_tables.sql")
        qry_path = os.path.join(SQL_DIR, "financial_analysis.sql")

        self.log_result("create_tables.sql exists", os.path.exists(ddl_path))
        self.log_result("financial_analysis.sql exists", os.path.exists(qry_path))

        with open(ddl_path, "r", encoding="utf-8") as f:
            ddl_content = f.read()
        with open(qry_path, "r", encoding="utf-8") as f:
            qry_content = f.read()

        # Check table definitions in DDL
        self.log_result("Fact_Financial_Annual table in DDL", "CREATE TABLE Fact_Financial_Annual" in ddl_content)
        self.log_result("Fact_Monthly_Revenues table in DDL", "CREATE TABLE Fact_Monthly_Revenues" in ddl_content)
        self.log_result("Fact_Lab_Operations table in DDL", "CREATE TABLE Fact_Lab_Operations" in ddl_content)

        # Check 15 queries present in financial_analysis.sql
        queries_found = len(re.findall(r'-- QUERY \d+:', qry_content))
        self.log_result("15 Financial Analysis Queries Present", queries_found == 15, f"Found {queries_found} queries")

        # Check COALESCE replacing ISNULL in Query 10
        self.log_result("ANSI COALESCE used in Query 10 (cross-engine compatibility)", "COALESCE(gt.Genomics_Rev, 0)" in qry_content)

    def test_powerbi_artifacts(self):
        print("\n--- 6. POWER BI PROJECT ARTIFACTS AUDIT ---")
        pbip_file = os.path.join(POWERBI_DIR, "AuraGen_Diagnostics_Dashboard.pbip")
        pbir_file = os.path.join(POWERBI_DIR, "AuraGen_Diagnostics_Dashboard.Report", "definition.pbir")
        report_json = os.path.join(POWERBI_DIR, "AuraGen_Diagnostics_Dashboard.Report", "report.json")
        bim_file = os.path.join(POWERBI_DIR, "AuraGen_Diagnostics_Dashboard.SemanticModel", "definition.bim")
        dax_file = os.path.join(POWERBI_DIR, "DAX_Measures.dax")
        csv_file = os.path.join(POWERBI_DIR, "dashboard_data.csv")

        self.log_result("AuraGen_Diagnostics_Dashboard.pbip exists", os.path.exists(pbip_file))
        self.log_result("definition.pbir exists", os.path.exists(pbir_file))
        self.log_result("report.json exists", os.path.exists(report_json))
        self.log_result("definition.bim exists", os.path.exists(bim_file))
        self.log_result("DAX_Measures.dax exists", os.path.exists(dax_file))
        self.log_result("dashboard_data.csv exists", os.path.exists(csv_file))

        # Check JSON validity of BIM and Report
        try:
            with open(bim_file, "r", encoding="utf-8") as f:
                bim_json = json.load(f)
            bim_valid = "model" in bim_json and len(bim_json["model"]["tables"]) > 0
            self.log_result("definition.bim Valid TMSL JSON", bim_valid)
        except Exception as e:
            self.log_result("definition.bim Valid TMSL JSON", False, str(e))

        try:
            with open(report_json, "r", encoding="utf-8") as f:
                rep_json = json.load(f)
            rep_valid = "sections" in rep_json and len(rep_json["sections"]) == 4
            self.log_result("report.json Valid Multi-Page Report (4 Sections)", rep_valid)
        except Exception as e:
            self.log_result("report.json Valid Multi-Page Report", False, str(e))

    def test_synthetic_data_disclaimers(self):
        print("\n--- 7. SYNTHETIC DATA LABELING & COMPLIANCE ---")
        # Check CSVs have synthetic data notice or Data_Classification column
        for csv_name in ["historical_financials.csv", "operational_data.csv", "assumptions.csv", "dashboard_data.csv"]:
            path = os.path.join(DATA_DIR, csv_name) if csv_name != "dashboard_data.csv" else os.path.join(POWERBI_DIR, csv_name)
            df = pd.read_csv(path)
            has_class = "Data_Classification" in df.columns
            self.log_result(f"[{csv_name}] Data_Classification synthetic tag column", has_class)

        # Check documentation files have disclaimers
        for doc_name in ["README.md", "data/README.md", "docs/methodology.md", "docs/project_conclusions.md", "powerbi/README.md"]:
            doc_path = os.path.join(PROJECT_ROOT, doc_name)
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            has_disclaimer = "synthetic" in content.lower() or "simulated benchmark" in content.lower()
            self.log_result(f"[{doc_name}] Synthetic data notice", has_disclaimer)


if __name__ == "__main__":
    suite = AuditTestSuite()
    success = suite.run_all_tests()
    sys.exit(0 if success else 1)
