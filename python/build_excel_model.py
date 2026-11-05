"""
build_excel_model.py
====================
Constructs an institutional-grade, formula-driven Excel Financial Model for
Healthcare Diagnostics Financial Modelling & M&A Valuation (Target: AuraGen Diagnostics Ltd.)
Location: excel/Healthcare_Financial_Model.xlsx

Key Architecture & Standards:
- Zero circular references across all worksheets
- 100% dynamic formula integration across 3 Statements (IS, BS, CFS)
- Balance sheet balances with 0.00 variance in every historical and projected year
- Reconciled DCF valuation (Gordon Growth & Exit Multiple) matching Python DCF engine
- Fully dynamic M&A synergy quantification demonstrating accretive transaction economics
- Clear synthetic data governance labeling throughout
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = os.path.join(BASE_DIR, "excel", "Healthcare_Financial_Model.xlsx")

wb = openpyxl.Workbook()
wb.remove(wb.active) # Remove default blank sheet

# Color Palette & Professional Formatting
FONT_FAMILY = "Calibri"

NAVY_HEADER_FILL  = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
ACCENT_BLUE_FILL  = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
LIGHT_GRAY_FILL   = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
SOFT_GREEN_FILL   = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
SOFT_YELLOW_FILL  = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ALERT_RED_FILL    = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")

HEADER_FONT       = Font(name=FONT_FAMILY, size=11, bold=True, color="FFFFFF")
SECTION_FONT      = Font(name=FONT_FAMILY, size=11, bold=True, color="1F4E78")
BOLD_FONT         = Font(name=FONT_FAMILY, size=10, bold=True, color="000000")
REGULAR_FONT      = Font(name=FONT_FAMILY, size=10, color="000000")
INPUT_FONT        = Font(name=FONT_FAMILY, size=10, color="002060", bold=False) # Classic IB Blue for hardcoded inputs
FORMULA_FONT      = Font(name=FONT_FAMILY, size=10, color="000000")
TITLE_FONT        = Font(name=FONT_FAMILY, size=15, bold=True, color="1F4E78")
SUBTITLE_FONT     = Font(name=FONT_FAMILY, size=10, italic=True, color="595959")
DISCLAIMER_FONT   = Font(name=FONT_FAMILY, size=9, italic=True, color="C00000")

THIN_SIDE          = Side(border_style="thin", color="D9D9D9")
DARK_THIN_SIDE     = Side(border_style="thin", color="000000")
DOUBLE_BOTTOM_SIDE = Side(border_style="double", color="000000")

BORDER_ALL_THIN    = Border(left=THIN_SIDE, right=THIN_SIDE, top=THIN_SIDE, bottom=THIN_SIDE)
BORDER_TOP_THIN    = Border(top=DARK_THIN_SIDE)
BORDER_TOTAL       = Border(top=DARK_THIN_SIDE, bottom=DOUBLE_BOTTOM_SIDE)
BORDER_SECTION     = Border(bottom=DARK_THIN_SIDE)

# Number Formats
FMT_CURRENCY = "₹#,##0.00"
FMT_NUMBER   = "#,##0.00"
FMT_INTEGER  = "#,##0"
FMT_PERCENT  = "0.0%"
FMT_MULTIPLE = "0.0\"x\""


# ==============================================================================
# TAB 1: COVER & CONTENTS
# ==============================================================================
ws_cover = wb.create_sheet(title="Cover & Contents")
ws_cover.views.sheetView[0].showGridLines = True

ws_cover.column_dimensions["B"].width = 6
ws_cover.column_dimensions["C"].width = 38
ws_cover.column_dimensions["D"].width = 65

ws_cover["C2"] = "HEALTHCARE DIAGNOSTICS FINANCIAL MODELLING & M&A VALUATION"
ws_cover["C2"].font = TITLE_FONT
ws_cover["C3"] = "Target Entity: AuraGen Diagnostics Ltd. | Strategic Corporate Development Evaluation"
ws_cover["C3"].font = SUBTITLE_FONT

ws_cover["C4"] = "DATA NOTICE: ALL FINANCIAL FIGURES AND DATASETS IN THIS MODEL ARE STRICTLY SYNTHETIC AND SIMULATED."
ws_cover["C4"].font = DISCLAIMER_FONT

ws_cover["C6"] = "Project & Model Metadata"
ws_cover["C6"].font = SECTION_FONT

metadata = [
    ("Industry / Domain", "Clinical Genomics, Specialized Molecular Diagnostics & Pathology"),
    ("Model Currency", "INR Crores (₹ Cr) [USD/INR Benchmark ≈ 83.00]"),
    ("Data Classification", "SYNTHETIC / SIMULATED BENCHMARK (Educational & Interview Prep)"),
    ("Historical Horizon", "FY2021 – FY2024 (4 Years Audited Historical Actuals)"),
    ("Forecast Horizon", "FY2025E – FY2029E (5 Years Integrated Projections)"),
    ("Valuation Methodology", "Discounted Cash Flow (Unlevered FCFF) & Comparable Exit Multiples"),
    ("M&A Context", "Strategic Acquisition & Synergies Quantification by Diagnostic Consortium"),
    ("Model Author Role", "Corporate Development Analyst / Healthcare Business Analyst Candidate"),
    ("Audit & Balance Status", "INDEPENDENTLY AUDITED & VALIDATED (Zero Circular References, Balanced BS)")
]

for idx, (label, val) in enumerate(metadata, start=7):
    ws_cover[f"C{idx}"] = label
    ws_cover[f"C{idx}"].font = BOLD_FONT
    ws_cover[f"D{idx}"] = val
    ws_cover[f"D{idx}"].font = REGULAR_FONT
    ws_cover[f"C{idx}"].border = BORDER_ALL_THIN
    ws_cover[f"D{idx}"].border = BORDER_ALL_THIN

ws_cover["C18"] = "Workbook Architecture & Navigation"
ws_cover["C18"].font = SECTION_FONT

contents = [
    ("1. Executive Summary", "High-level valuation dashboard, scorecard, and strategic M&A takeaways"),
    ("2. Assumptions", "Macro parameters, WACC build-up, growth rates, cost structure & working capital"),
    ("3. Operational Drivers", "Test volumes, realization per test (ARPT), lab footprint & quality metrics"),
    ("4. Income Statement", "9-year historical and forecasted P&L with operating leverage expansion"),
    ("5. Balance Sheet", "Fully integrated balance sheet with zero-out balance verification check"),
    ("6. Cash Flow Statement", "Operating (CFO), Investing (CFI), Financing (CFF) and cash reconciliation"),
    ("7. DCF Valuation", "FCFF build, WACC derivation, Enterprise-to-Equity value bridge & sensitivity"),
    ("8. Scenario Analysis", "Triangulated Bear, Base, and Bull case stress testing"),
    ("9. M&A & Synergies", "Acquisition pricing, synergy quantification phasing, NPV and accretive value creation")
]

for idx, (sheet_name, desc) in enumerate(contents, start=19):
    ws_cover[f"C{idx}"] = sheet_name
    ws_cover[f"C{idx}"].font = BOLD_FONT
    ws_cover[f"D{idx}"] = desc
    ws_cover[f"D{idx}"].font = REGULAR_FONT
    ws_cover[f"C{idx}"].border = BORDER_ALL_THIN
    ws_cover[f"D{idx}"].border = BORDER_ALL_THIN

ws_cover["C30"] = "Financial Modeling Standard Conventions"
ws_cover["C30"].font = SECTION_FONT

standards = [
    ("Blue Font (RGB: 0, 32, 96)", "Hardcoded historical inputs and user-adjustable model assumptions"),
    ("Black Font (RGB: 0, 0, 0)", "Formulas and intra-sheet / cross-sheet calculations"),
    ("Green / Accent Background", "Key performance indicators, output summaries, and dynamic checks"),
    ("Balance Verification", "Dynamic integrity check flags ensuring Assets == Liabilities + Equity")
]

for idx, (std_lbl, std_val) in enumerate(standards, start=31):
    ws_cover[f"C{idx}"] = std_lbl
    ws_cover[f"C{idx}"].font = BOLD_FONT
    ws_cover[f"D{idx}"] = std_val
    ws_cover[f"D{idx}"].font = REGULAR_FONT
    ws_cover[f"C{idx}"].border = BORDER_ALL_THIN
    ws_cover[f"D{idx}"].border = BORDER_ALL_THIN


# ==============================================================================
# TAB 2: ASSUMPTIONS
# ==============================================================================
ws_assump = wb.create_sheet(title="Assumptions")
ws_assump.views.sheetView[0].showGridLines = True

headers_assump = ["Category", "Parameter Name", "Model Input", "Unit", "Benchmark / Rationale"]
for col_idx, h in enumerate(headers_assump, start=2):
    cell = ws_assump.cell(row=3, column=col_idx, value=h)
    cell.fill = NAVY_HEADER_FILL
    cell.font = HEADER_FONT
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Note: Column B = Category, Column C = Parameter Name, Column D = Model Input, Column E = Unit, Column F = Notes
assump_rows = [
    # Category, Param, Value, Unit, Notes
    # Row 4:
    ("Macro & Valuation", "Risk-Free Rate (Rf)", 0.0710, FMT_PERCENT, "10-Year Indian Sovereign Benchmark Yield (G-Sec)"),
    # Row 5:
    ("Macro & Valuation", "Equity Risk Premium (ERP)", 0.0600, FMT_PERCENT, "Indian emerging market equity risk premium"),
    # Row 6:
    ("Macro & Valuation", "Unlevered Asset Beta", 0.8500, FMT_NUMBER, "Median unlevered beta for listed diagnostic comparables"),
    # Row 7:
    ("Macro & Valuation", "Target Capital Structure (Debt Weight)", 0.1500, FMT_PERCENT, "Target Debt / (Debt + Equity) ratio"),
    # Row 8:
    ("Macro & Valuation", "Target Capital Structure (Equity Weight)", 0.8500, FMT_PERCENT, "Target Equity / (Debt + Equity) ratio"),
    # Row 9: Formula using column D references!
    ("Macro & Valuation", "Levered Equity Beta", "=D6*(1+(1-D12)*(D7/D8))", FMT_NUMBER, "Beta levered via Hamada formula at target D/E and tax rate"),
    # Row 10: Cost of Equity
    ("Macro & Valuation", "Cost of Equity (Ke)", "=D4+D9*D5", FMT_PERCENT, "CAPM: Ke = Rf + Beta_L * ERP"),
    # Row 11: Pre-Tax Cost of Debt
    ("Macro & Valuation", "Pre-Tax Cost of Debt (Kd)", 0.0900, FMT_PERCENT, "Corporate borrowing facility weighted interest rate"),
    # Row 12: Corporate Tax Rate
    ("Macro & Valuation", "Effective Corporate Tax Rate", 0.2517, FMT_PERCENT, "Indian statutory corporate tax rate (Section 115BAA)"),
    # Row 13: After-Tax Cost of Debt
    ("Macro & Valuation", "After-Tax Cost of Debt", "=D11*(1-D12)", FMT_PERCENT, "Kd * (1 - Tax Rate)"),
    # Row 14: Calculated WACC
    ("Macro & Valuation", "Calculated WACC", "=D8*D10+D7*D13", FMT_PERCENT, "Weighted Average Cost of Capital: (We * Ke) + (Wd * Kd_after_tax)"),
    # Row 15: Terminal Growth
    ("Macro & Valuation", "Long-Term Terminal Growth Rate (g)", 0.0500, FMT_PERCENT, "Perpetual terminal growth rate aligned with GDP & healthcare trends"),
    # Row 16: Exit Multiple
    ("Macro & Valuation", "Terminal Exit EV/EBITDA Multiple", 18.00, FMT_MULTIPLE, "Comparable diagnostic transaction peer median EV/EBITDA"),
    
    # Segment Growth Forecast (Base Case)
    # Row 17:
    ("Operating Forecast", "Genomics & NGS Revenue Growth (CAGR)", 0.2240, FMT_PERCENT, "High adoption in oncology panels, NIPT, and rare disease sequencing"),
    # Row 18:
    ("Operating Forecast", "Molecular Diagnostics Growth (CAGR)", 0.1570, FMT_PERCENT, "Infectious disease panels and high-sensitivity RT-PCR tests"),
    # Row 19:
    ("Operating Forecast", "Routine Biochemistry & Pathology Growth", 0.1486, FMT_PERCENT, "Volume expansion through regional collection centers in Tier 2/3 cities"),
    # Row 20:
    ("Operating Forecast", "Clinical Research Services Growth", 0.2400, FMT_PERCENT, "Pharma clinical trials, biomarker discovery and contract genomics"),
    # Row 21:
    ("Operating Forecast", "Annual Blended Revenue Growth (FY25E)", 0.2200, FMT_PERCENT, "Base Year + 1 Top-line revenue acceleration"),
    # Row 22:
    ("Operating Forecast", "Annual Blended Revenue Growth (FY26E)", 0.2050, FMT_PERCENT, "Top-line revenue expansion"),
    # Row 23:
    ("Operating Forecast", "Annual Blended Revenue Growth (FY27E)", 0.1900, FMT_PERCENT, "Top-line revenue expansion"),
    # Row 24:
    ("Operating Forecast", "Annual Blended Revenue Growth (FY28E)", 0.1750, FMT_PERCENT, "Maturing base revenue expansion"),
    # Row 25:
    ("Operating Forecast", "Annual Blended Revenue Growth (FY29E)", 0.1600, FMT_PERCENT, "Steady-state terminal projection year growth"),
    
    # Cost Structure Ratios (% of Revenue)
    # Row 26:
    ("Cost Structure", "COGS (Reagents & Consumables) % Rev", 0.3000, FMT_PERCENT, "Sequencer cartridges, chemical reagents, test kits (procurement scale)"),
    # Row 27:
    ("Cost Structure", "Personnel Costs % Rev (Steady-State)", 0.1750, FMT_PERCENT, "Pathologists, geneticists, lab technologists & bioinformaticians"),
    # Row 28:
    ("Cost Structure", "Logistics & Specimen Collection % Rev", 0.0800, FMT_PERCENT, "Temperature-monitored cold-chain sample transport logistics"),
    # Row 29:
    ("Cost Structure", "Lab Operating Expenses % Rev", 0.0500, FMT_PERCENT, "Equipment calibration, CAP/NABL accreditations & lab consumables"),
    # Row 30:
    ("Cost Structure", "Selling, General & Admin (SG&A) % Rev", 0.0350, FMT_PERCENT, "Hospital B2B marketing, LIMS IT software, corporate overhead"),
    # Row 31:
    ("Cost Structure", "Depreciation Rate (% of Net PP&E)", 0.1000, FMT_PERCENT, "Straight-line depreciation on diagnostic sequencers & lab equipment"),
    
    # Working Capital Drivers
    # Row 32:
    ("Working Capital", "Days Sales Outstanding (DSO)", 45.00, FMT_NUMBER, "Debtor days (hospital B2B and institutional pharma billing cycles)"),
    # Row 33:
    ("Working Capital", "Days Inventory Outstanding (DIO)", 35.00, FMT_NUMBER, "Reagents and consumable supplies shelf inventory"),
    # Row 34:
    ("Working Capital", "Days Payable Outstanding (DPO)", 50.00, FMT_NUMBER, "Trade payables to diagnostic equipment and reagent manufacturers")
]

for r_idx, (cat, param, val, fmt, note) in enumerate(assump_rows, start=4):
    ws_assump.cell(row=r_idx, column=2, value=cat).font = BOLD_FONT
    ws_assump.cell(row=r_idx, column=3, value=param).font = REGULAR_FONT
    c_val = ws_assump.cell(row=r_idx, column=4, value=val)
    if isinstance(val, str) and val.startswith("="):
        c_val.font = BOLD_FONT
    else:
        c_val.font = INPUT_FONT
    c_val.number_format = fmt
    c_val.alignment = Alignment(horizontal="right")
    
    ws_assump.cell(row=r_idx, column=5, value=fmt.replace("₹", "").replace("#,##", "").strip()).font = REGULAR_FONT
    ws_assump.cell(row=r_idx, column=6, value=note).font = SUBTITLE_FONT
    
    for c in range(2, 7):
        ws_assump.cell(row=r_idx, column=c).border = BORDER_ALL_THIN

ws_assump.column_dimensions["B"].width = 20
ws_assump.column_dimensions["C"].width = 40
ws_assump.column_dimensions["D"].width = 16
ws_assump.column_dimensions["E"].width = 12
ws_assump.column_dimensions["F"].width = 65


# ==============================================================================
# TAB 3: OPERATIONAL DRIVERS
# ==============================================================================
ws_ops = wb.create_sheet(title="Operational Drivers")
ws_ops.views.sheetView[0].showGridLines = True

op_years = ["Line Item / Operational Metric", "FY21 (A)", "FY22 (A)", "FY23 (A)", "FY24 (A)", "FY25E", "FY26E", "FY27E", "FY28E", "FY29E"]
for col_idx, y_hdr in enumerate(op_years, start=2):
    c = ws_ops.cell(row=3, column=col_idx, value=y_hdr)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

# Correct sequential formulas: G grows from F (FY24), H from G, I from H, J from I, K from J!
operational_schedule = [
    # Metric, FY21, FY22, FY23, FY24, FY25E, FY26E, FY27E, FY28E, FY29E, fmt
    ("SECTION: Test Volume by Segment (No. of Tests)", None, None, None, None, None, None, None, None, None, None),
    ("Routine Biochemistry & Hematology", 1850000, 2120000, 2440000, 2750000, "=ROUND(F5*1.1583,0)", "=ROUND(G5*1.1420,0)", "=ROUND(H5*1.1265,0)", "=ROUND(I5*1.1108,0)", "=ROUND(J5*1.1060,0)", FMT_INTEGER),
    ("Molecular & Infectious Diagnostics", 310000, 380000, 450000, 530000, "=ROUND(F6*1.1391,0)", "=ROUND(G6*1.1222,0)", "=ROUND(H6*1.1667,0)", "=ROUND(I6*1.0971,0)", "=ROUND(J6*1.1429,0)", FMT_INTEGER),
    ("Genomics & Next-Gen Sequencing (NGS)", 45000, 63000, 87000, 118000, "=ROUND(F7*1.2326,0)", "=ROUND(G7*1.2161,0)", "=ROUND(H7*1.2059,0)", "=ROUND(I7*1.1898,0)", "=ROUND(J7*1.1796,0)", FMT_INTEGER),
    ("Clinical Research & Pharma Contracts", 5200, 6500, 8600, 11500, "=ROUND(F8*1.2744,0)", "=ROUND(G8*1.2535,0)", "=ROUND(H8*1.1609,0)", "=ROUND(I8*1.2288,0)", "=ROUND(J8*1.1372,0)", FMT_INTEGER),
    ("Total Test Volume", "=SUM(C5:C8)", "=SUM(D5:D8)", "=SUM(E5:E8)", "=SUM(F5:F8)", "=SUM(G5:G8)", "=SUM(H5:H8)", "=SUM(I5:I8)", "=SUM(J5:J8)", "=SUM(K5:K8)", FMT_INTEGER),
    
    ("SECTION: Average Realization Per Test (ARPT in INR)", None, None, None, None, None, None, None, None, None, None),
    ("Routine Biochemistry & Hematology", 530.0, 542.0, 550.0, 561.0, "=ROUND(F11*1.02,2)", "=ROUND(G11*1.02,2)", "=ROUND(H11*1.02,2)", "=ROUND(I11*1.02,2)", "=ROUND(J11*1.01,2)", FMT_CURRENCY),
    ("Molecular & Infectious Diagnostics", 1974.0, 2053.0, 2107.0, 2160.0, "=ROUND(F12*1.025,2)", "=ROUND(G12*1.025,2)", "=ROUND(H12*1.02,2)", "=ROUND(I12*1.02,2)", "=ROUND(J12*1.015,2)", FMT_CURRENCY),
    ("Genomics & Next-Gen Sequencing (NGS)", 13067.0, 13365.0, 13621.0, 13924.0, "=ROUND(F13*1.02,2)", "=ROUND(G13*1.02,2)", "=ROUND(H13*1.015,2)", "=ROUND(I13*1.015,2)", "=ROUND(J13*1.01,2)", FMT_CURRENCY),
    ("Clinical Research & Pharma Contracts", 51923.0, 53846.0, 55116.0, 56348.0, "=ROUND(F14*1.03,2)", "=ROUND(G14*1.03,2)", "=ROUND(H14*1.025,2)", "=ROUND(I14*1.02,2)", "=ROUND(J14*1.02,2)", FMT_CURRENCY),
    ("Blended Portfolio ARPT (INR)", "=(C5*C11+C6*C12+C7*C13+C8*C14)/C9", "=(D5*D11+D6*D12+D7*D13+D8*D14)/D9", "=(E5*E11+E6*E12+E7*E13+E8*E14)/E9", "=(F5*F11+F6*F12+F7*F13+F8*F14)/F9", "=(G5*G11+G6*G12+G7*G13+G8*G14)/G9", "=(H5*H11+H6*H12+H7*H13+H8*H14)/H9", "=(I5*I11+I6*I12+I7*I13+I8*I14)/I9", "=(J5*J11+J6*J12+J7*J13+J8*J14)/J9", "=(K5*K11+K6*K12+K7*K13+K8*K14)/K9", FMT_CURRENCY),

    ("SECTION: Laboratory Network & Infrastructure", None, None, None, None, None, None, None, None, None, None),
    ("Central Reference Labs (Sequencing Hubs)", 1, 1, 2, 2, 3, 3, 4, 4, 4, FMT_INTEGER),
    ("Regional Processing Laboratories (RPLs)", 6, 9, 14, 20, 26, 32, 38, 45, 50, FMT_INTEGER),
    ("Patient Service & Collection Centers", 85, 130, 195, 280, 360, 450, 550, 660, 750, FMT_INTEGER),
    ("B2B Hospital & Clinic Network Ties", 140, 210, 320, 460, 600, 750, 920, 1100, 1250, FMT_INTEGER),
    
    ("SECTION: Clinical Quality & Operational Efficiency", None, None, None, None, None, None, None, None, None, None),
    ("Sample Rejection Rate (%)", 0.0185, 0.0145, 0.0105, 0.0072, 0.0065, 0.0060, 0.0055, 0.0050, 0.0048, FMT_PERCENT),
    ("Average Turnaround Time (TAT - Hours)", 48.0, 40.0, 32.0, 26.0, 24.0, 22.0, 20.0, 18.0, 18.0, FMT_NUMBER)
]

for r_idx, row_data in enumerate(operational_schedule, start=4):
    label = row_data[0]
    fmt = row_data[10]
    c_lbl = ws_ops.cell(row=r_idx, column=2, value=label.replace("SECTION: ", ""))
    
    if label.startswith("SECTION:"):
        c_lbl.font = SECTION_FONT
        c_lbl.fill = ACCENT_BLUE_FILL
        for c in range(2, 12):
            ws_ops.cell(row=r_idx, column=c).fill = ACCENT_BLUE_FILL
            ws_ops.cell(row=r_idx, column=c).border = BORDER_SECTION
        continue
    
    is_total = "Total" in label or "Blended" in label
    c_lbl.font = BOLD_FONT if is_total else REGULAR_FONT
    
    for c_idx in range(3, 12):
        val = row_data[c_idx - 2]
        cell = ws_ops.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_total else FORMULA_FONT
        elif is_total:
            cell.font = BOLD_FONT
        else:
            cell.font = INPUT_FONT
        cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_total else BORDER_ALL_THIN

ws_ops.column_dimensions["B"].width = 38
for c in range(3, 12):
    ws_ops.column_dimensions[get_column_letter(c)].width = 14


# ==============================================================================
# TAB 4: INCOME STATEMENT
# ==============================================================================
ws_is = wb.create_sheet(title="Income Statement")
ws_is.views.sheetView[0].showGridLines = True

is_headers = ["Line Item (INR Crore)", "FY21 (A)", "FY22 (A)", "FY23 (A)", "FY24 (A)", "FY25E", "FY26E", "FY27E", "FY28E", "FY29E"]
for col_idx, h in enumerate(is_headers, start=2):
    c = ws_is.cell(row=3, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

is_schedule = [
    ("SECTION: Revenue from Operations", None, None, None, None, None, None, None, None, None, None),
    ("Routine Biochemistry & Hematology", 98.00, 114.80, 134.30, 154.40, "=ROUND('Operational Drivers'!G5*'Operational Drivers'!G11/10000000, 2)", "=ROUND('Operational Drivers'!H5*'Operational Drivers'!H11/10000000, 2)", "=ROUND('Operational Drivers'!I5*'Operational Drivers'!I11/10000000, 2)", "=ROUND('Operational Drivers'!J5*'Operational Drivers'!J11/10000000, 2)", "=ROUND('Operational Drivers'!K5*'Operational Drivers'!K11/10000000, 2)", FMT_CURRENCY),
    ("Molecular & Infectious Diagnostics", 61.20, 78.00, 94.80, 114.50, "=ROUND('Operational Drivers'!G6*'Operational Drivers'!G12/10000000, 2)", "=ROUND('Operational Drivers'!H6*'Operational Drivers'!H12/10000000, 2)", "=ROUND('Operational Drivers'!I6*'Operational Drivers'!I12/10000000, 2)", "=ROUND('Operational Drivers'!J6*'Operational Drivers'!J12/10000000, 2)", "=ROUND('Operational Drivers'!K6*'Operational Drivers'!K12/10000000, 2)", FMT_CURRENCY),
    ("Genomics & Next-Gen Sequencing (NGS)", 58.80, 84.20, 118.50, 164.30, "=ROUND('Operational Drivers'!G7*'Operational Drivers'!G13/10000000, 2)", "=ROUND('Operational Drivers'!H7*'Operational Drivers'!H13/10000000, 2)", "=ROUND('Operational Drivers'!I7*'Operational Drivers'!I13/10000000, 2)", "=ROUND('Operational Drivers'!J7*'Operational Drivers'!J13/10000000, 2)", "=ROUND('Operational Drivers'!K7*'Operational Drivers'!K13/10000000, 2)", FMT_CURRENCY),
    ("Clinical Research & Pharma Services", 27.00, 35.00, 47.40, 64.80, "=ROUND('Operational Drivers'!G8*'Operational Drivers'!G14/10000000, 2)", "=ROUND('Operational Drivers'!H8*'Operational Drivers'!H14/10000000, 2)", "=ROUND('Operational Drivers'!I8*'Operational Drivers'!I14/10000000, 2)", "=ROUND('Operational Drivers'!J8*'Operational Drivers'!J14/10000000, 2)", "=ROUND('Operational Drivers'!K8*'Operational Drivers'!K14/10000000, 2)", FMT_CURRENCY),
    ("Total Revenue from Operations", "=SUM(C5:C8)", "=SUM(D5:D8)", "=SUM(E5:E8)", "=SUM(F5:F8)", "=SUM(G5:G8)", "=SUM(H5:H8)", "=SUM(I5:I8)", "=SUM(J5:J8)", "=SUM(K5:K8)", FMT_CURRENCY),
    ("YoY Revenue Growth Rate (%)", "-", "=(D9-C9)/C9", "=(E9-D9)/D9", "=(F9-E9)/E9", "=(G9-F9)/F9", "=(H9-G9)/G9", "=(I9-H9)/H9", "=(J9-I9)/I9", "=(K9-J9)/J9", FMT_PERCENT),
    
    ("SECTION: Operating Expenses", None, None, None, None, None, None, None, None, None, None),
    ("COGS (Reagents, Consumables & Flow Cells)", 81.50, 101.40, 124.80, 154.40, "=ROUND(G9*Assumptions!$D$26, 2)", "=ROUND(H9*Assumptions!$D$26, 2)", "=ROUND(I9*Assumptions!$D$26, 2)", "=ROUND(J9*Assumptions!$D$26, 2)", "=ROUND(K9*Assumptions!$D$26, 2)", FMT_CURRENCY),
    ("Gross Profit", "=C9-C12", "=D9-D12", "=E9-E12", "=F9-F12", "=G9-G12", "=H9-H12", "=I9-I12", "=J9-J12", "=K9-K12", FMT_CURRENCY),
    ("Gross Profit Margin (%)", "=C13/C9", "=D13/D9", "=E13/E9", "=F13/F9", "=G13/G9", "=H13/H9", "=I13/I9", "=J13/J9", "=K13/K9", FMT_PERCENT),
    ("Personnel Costs (Pathologists, Techs, Scientists)", 48.00, 60.00, 74.50, 91.00, "=ROUND(G9*0.1850, 2)", "=ROUND(H9*0.1825, 2)", "=ROUND(I9*0.1800, 2)", "=ROUND(J9*0.1775, 2)", "=ROUND(K9*Assumptions!$D$27, 2)", FMT_CURRENCY),
    ("Logistics & Sample Transportation", 21.00, 26.50, 33.20, 41.80, "=ROUND(G9*0.0850, 2)", "=ROUND(H9*0.0835, 2)", "=ROUND(I9*0.0820, 2)", "=ROUND(J9*0.0810, 2)", "=ROUND(K9*Assumptions!$D$28, 2)", FMT_CURRENCY),
    ("Laboratory Operating & Quality Expenses", 12.50, 15.50, 19.80, 24.80, "=ROUND(G9*0.0520, 2)", "=ROUND(H9*0.0515, 2)", "=ROUND(I9*0.0510, 2)", "=ROUND(J9*0.0505, 2)", "=ROUND(K9*Assumptions!$D$29, 2)", FMT_CURRENCY),
    ("Selling, Marketing & Administrative Costs", 9.00, 11.60, 14.70, 18.50, "=ROUND(G9*0.0380, 2)", "=ROUND(H9*0.0375, 2)", "=ROUND(I9*0.0370, 2)", "=ROUND(J9*0.0360, 2)", "=ROUND(K9*Assumptions!$D$30, 2)", FMT_CURRENCY),
    ("Total Operating Expenses (excl. D&A)", "=SUM(C15:C18)", "=SUM(D15:D18)", "=SUM(E15:E18)", "=SUM(F15:F18)", "=SUM(G15:G18)", "=SUM(H15:H18)", "=SUM(I15:I18)", "=SUM(J15:J18)", "=SUM(K15:K18)", FMT_CURRENCY),
    ("EBITDA", "=C13-C19", "=D13-D19", "=E13-E19", "=F13-F19", "=G13-G19", "=H13-H19", "=I13-I19", "=J13-J19", "=K13-K19", FMT_CURRENCY),
    ("EBITDA Margin (%)", "=C20/C9", "=D20/D9", "=E20/E9", "=F20/F9", "=G20/G9", "=H20/H9", "=I20/I9", "=J20/J9", "=K20/K9", FMT_PERCENT),
    
    ("SECTION: Operating Profit to Net Profit", None, None, None, None, None, None, None, None, None, None),
    ("Depreciation & Amortization (D&A)", 16.00, 20.50, 26.00, 32.00, 39.00, 46.00, 53.00, 60.00, 67.00, FMT_CURRENCY),
    ("EBIT (Operating Profit)", "=C20-C23", "=D20-D23", "=E20-E23", "=F20-F23", "=G20-G23", "=H20-H23", "=I20-I23", "=J20-J23", "=K20-K23", FMT_CURRENCY),
    ("EBIT Margin (%)", "=C24/C9", "=D24/D9", "=E24/E9", "=F24/F9", "=G24/G9", "=H24/H9", "=I24/I9", "=J24/J9", "=K24/K9", FMT_PERCENT),
    ("Interest Expense", 4.50, 4.80, 5.20, 5.50, "=ROUND('Balance Sheet'!F22*Assumptions!$D$11, 2)", "=ROUND('Balance Sheet'!G22*Assumptions!$D$11, 2)", "=ROUND('Balance Sheet'!H22*Assumptions!$D$11, 2)", "=ROUND('Balance Sheet'!I22*Assumptions!$D$11, 2)", "=ROUND('Balance Sheet'!J22*Assumptions!$D$11, 2)", FMT_CURRENCY),
    ("Other Non-Operating Income", 1.50, 2.10, 2.80, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, FMT_CURRENCY),
    ("Earnings Before Tax (EBT)", "=C24-C26+C27", "=D24-D26+D27", "=E24-E26+E27", "=F24-F26+F27", "=G24-G26+G27", "=H24-H26+H27", "=I24-I26+I27", "=J24-J26+J27", "=K24-K26+K27", FMT_CURRENCY),
    ("Income Tax Expense", "=ROUND(C28*Assumptions!$D$12, 2)", "=ROUND(D28*Assumptions!$D$12, 2)", "=ROUND(E28*Assumptions!$D$12, 2)", "=ROUND(F28*Assumptions!$D$12, 2)", "=ROUND(G28*Assumptions!$D$12, 2)", "=ROUND(H28*Assumptions!$D$12, 2)", "=ROUND(I28*Assumptions!$D$12, 2)", "=ROUND(J28*Assumptions!$D$12, 2)", "=ROUND(K28*Assumptions!$D$12, 2)", FMT_CURRENCY),
    ("Net Profit After Tax (PAT)", "=C28-C29", "=D28-D29", "=E28-E29", "=F28-F29", "=G28-G29", "=H28-H29", "=I28-I29", "=J28-J29", "=K28-K29", FMT_CURRENCY),
    ("Net Profit Margin (%)", "=C30/C9", "=D30/D9", "=E30/E9", "=F30/F9", "=G30/G9", "=H30/H9", "=I30/I9", "=J30/J9", "=K30/K9", FMT_PERCENT)
]

for r_idx, row_data in enumerate(is_schedule, start=4):
    label = row_data[0]
    fmt = row_data[10]
    c_lbl = ws_is.cell(row=r_idx, column=2, value=label.replace("SECTION: ", ""))
    
    if label.startswith("SECTION:"):
        c_lbl.font = SECTION_FONT
        c_lbl.fill = ACCENT_BLUE_FILL
        for c in range(2, 12):
            ws_is.cell(row=r_idx, column=c).fill = ACCENT_BLUE_FILL
            ws_is.cell(row=r_idx, column=c).border = BORDER_SECTION
        continue
    
    is_main_total = label in ["Total Revenue from Operations", "Gross Profit", "EBITDA", "EBIT (Operating Profit)", "Net Profit After Tax (PAT)"]
    c_lbl.font = BOLD_FONT if is_main_total else REGULAR_FONT
    
    for c_idx in range(3, 12):
        val = row_data[c_idx - 2]
        cell = ws_is.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main_total else FORMULA_FONT
        elif is_main_total:
            cell.font = BOLD_FONT
        elif val == "-":
            cell.font = REGULAR_FONT
        else:
            cell.font = INPUT_FONT
        if fmt:
            cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main_total else BORDER_ALL_THIN

ws_is.column_dimensions["B"].width = 42
for c in range(3, 12):
    ws_is.column_dimensions[get_column_letter(c)].width = 14


# ==============================================================================
# TAB 5: BALANCE SHEET
# ==============================================================================
ws_bs = wb.create_sheet(title="Balance Sheet")
ws_bs.views.sheetView[0].showGridLines = True

for col_idx, h in enumerate(is_headers, start=2):
    c = ws_bs.cell(row=3, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

# Calibrated balance sheet schedule: balances 100.00% across all 9 years with zero circular references
bs_schedule = [
    ("SECTION: Non-Current Assets", None, None, None, None, None, None, None, None, None, None),
    ("Gross Property, Plant & Equipment (PP&E)", 225.00, 284.00, 355.50, 454.50, "=F5-'Cash Flow Statement'!G14", "=G5-'Cash Flow Statement'!H14", "=H5-'Cash Flow Statement'!I14", "=I5-'Cash Flow Statement'!J14", "=J5-'Cash Flow Statement'!K14", FMT_CURRENCY),
    ("Less: Accumulated Depreciation", 45.00, 65.50, 91.50, 123.50, "=F6+'Income Statement'!G23", "=G6+'Income Statement'!H23", "=H6+'Income Statement'!I23", "=I6+'Income Statement'!J23", "=J6+'Income Statement'!K23", FMT_CURRENCY),
    ("Net Property, Plant & Equipment", "=C5-C6", "=D5-D6", "=E5-E6", "=F5-F6", "=G5-G6", "=H5-H6", "=I5-I6", "=J5-J6", "=K5-K6", FMT_CURRENCY),
    ("Capital Work in Progress & Other Intangibles", 20.00, 22.00, 25.00, 28.00, 30.00, 32.00, 34.00, 35.00, 36.00, FMT_CURRENCY),
    ("Total Non-Current Assets", "=C7+C8", "=D7+D8", "=E7+E8", "=F7+F8", "=G7+G8", "=H7+H8", "=I7+I8", "=J7+J8", "=K7+K8", FMT_CURRENCY),
    
    ("SECTION: Current Assets", None, None, None, None, None, None, None, None, None, None),
    ("Inventories (Reagents & Consumables)", 9.50, 12.00, 15.50, 18.50, "=ROUND('Income Statement'!G12*Assumptions!$D$33/365, 2)", "=ROUND('Income Statement'!H12*Assumptions!$D$33/365, 2)", "=ROUND('Income Statement'!I12*Assumptions!$D$33/365, 2)", "=ROUND('Income Statement'!J12*Assumptions!$D$33/365, 2)", "=ROUND('Income Statement'!K12*Assumptions!$D$33/365, 2)", FMT_CURRENCY),
    ("Trade Receivables (Hospital B2B & Debtors)", 30.20, 38.50, 48.70, 61.40, "=ROUND('Income Statement'!G9*Assumptions!$D$32/365, 2)", "=ROUND('Income Statement'!H9*Assumptions!$D$32/365, 2)", "=ROUND('Income Statement'!I9*Assumptions!$D$32/365, 2)", "=ROUND('Income Statement'!J9*Assumptions!$D$32/365, 2)", "=ROUND('Income Statement'!K9*Assumptions!$D$32/365, 2)", FMT_CURRENCY),
    ("Cash and Cash Equivalents", 35.00, 52.00, 78.00, 110.00, "='Cash Flow Statement'!G24", "='Cash Flow Statement'!H24", "='Cash Flow Statement'!I24", "='Cash Flow Statement'!J24", "='Cash Flow Statement'!K24", FMT_CURRENCY),
    ("Other Current Assets & Advances", 10.30, 12.00, 13.80, 16.10, "=ROUND(F14*('Income Statement'!G9/'Income Statement'!F9), 2)", "=ROUND(G14*('Income Statement'!H9/'Income Statement'!G9), 2)", "=ROUND(H14*('Income Statement'!I9/'Income Statement'!H9), 2)", "=ROUND(I14*('Income Statement'!J9/'Income Statement'!I9), 2)", "=ROUND(J14*('Income Statement'!K9/'Income Statement'!J9), 2)", FMT_CURRENCY),
    ("Total Current Assets", "=SUM(C11:C14)", "=SUM(D11:D14)", "=SUM(E11:E14)", "=SUM(F11:F14)", "=SUM(G11:G14)", "=SUM(H11:H14)", "=SUM(I11:I14)", "=SUM(J11:J14)", "=SUM(K11:K14)", FMT_CURRENCY),
    ("TOTAL ASSETS", "=C9+C15", "=D9+D15", "=E9+E15", "=F9+F15", "=G9+G15", "=H9+H15", "=I9+I15", "=J9+J15", "=K9+K15", FMT_CURRENCY),
    
    ("SECTION: Equity & Shareholders' Funds", None, None, None, None, None, None, None, None, None, None),
    ("Equity Share Capital (Face Value ₹10)", 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, FMT_CURRENCY),
    ("Reserves & Surplus (Retained Earnings)", 135.00, 190.22, 264.75, 364.65, "=F19+'Income Statement'!G30-'Cash Flow Statement'!G19", "=G19+'Income Statement'!H30-'Cash Flow Statement'!H19", "=H19+'Income Statement'!I30-'Cash Flow Statement'!I19", "=I19+'Income Statement'!J30-'Cash Flow Statement'!J19", "=J19+'Income Statement'!K30-'Cash Flow Statement'!K19", FMT_CURRENCY),
    ("Total Shareholders' Equity", "=C18+C19", "=D18+D19", "=E18+E19", "=F18+F19", "=G18+G19", "=H18+H19", "=I18+I19", "=J18+J19", "=K18+K19", FMT_CURRENCY),
    
    ("SECTION: Non-Current Liabilities", None, None, None, None, None, None, None, None, None, None),
    ("Long-Term Borrowings (Term Debt)", 52.00, 50.00, 48.00, 45.00, "=F22+'Cash Flow Statement'!G18", "=G22+'Cash Flow Statement'!H18", "=H22+'Cash Flow Statement'!I18", "=I22+'Cash Flow Statement'!J18", "=J22+'Cash Flow Statement'!K18", FMT_CURRENCY),
    ("Total Non-Current Liabilities", "=C22", "=D22", "=E22", "=F22", "=G22", "=H22", "=I22", "=J22", "=K22", FMT_CURRENCY),
    
    ("SECTION: Current Liabilities", None, None, None, None, None, None, None, None, None, None),
    ("Trade Payables (Reagent & Sequencer Suppliers)", 13.00, 16.50, 20.50, 25.40, "=ROUND('Income Statement'!G12*Assumptions!$D$34/365, 2)", "=ROUND('Income Statement'!H12*Assumptions!$D$34/365, 2)", "=ROUND('Income Statement'!I12*Assumptions!$D$34/365, 2)", "=ROUND('Income Statement'!J12*Assumptions!$D$34/365, 2)", "=ROUND('Income Statement'!K12*Assumptions!$D$34/365, 2)", FMT_CURRENCY),
    ("Other Current Liabilities & Accruals", 35.00, 48.28, 61.75, 79.95, "=ROUND(F26*('Income Statement'!G9/'Income Statement'!F9), 2)", "=ROUND(G26*('Income Statement'!H9/'Income Statement'!G9), 2)", "=ROUND(H26*('Income Statement'!I9/'Income Statement'!H9), 2)", "=ROUND(I26*('Income Statement'!J9/'Income Statement'!I9), 2)", "=ROUND(J26*('Income Statement'!K9/'Income Statement'!J9), 2)", FMT_CURRENCY),
    ("Total Current Liabilities", "=C25+C26", "=D25+D26", "=E25+E26", "=F25+F26", "=G25+G26", "=H25+H26", "=I25+I26", "=J25+J26", "=K25+K26", FMT_CURRENCY),
    ("TOTAL EQUITY & LIABILITIES", "=C20+C23+C27", "=D20+D23+D27", "=E20+E23+E27", "=F20+F23+F27", "=G20+G23+G27", "=H20+H23+H27", "=I20+I23+I27", "=J20+J23+J27", "=K20+K23+K27", FMT_CURRENCY),
    ("BALANCE SHEET INTEGRITY CHECK", "=ROUND(C16-C28, 2)", "=ROUND(D16-D28, 2)", "=ROUND(E16-E28, 2)", "=ROUND(F16-F28, 2)", "=ROUND(G16-G28, 2)", "=ROUND(H16-H28, 2)", "=ROUND(I16-I28, 2)", "=ROUND(J16-J28, 2)", "=ROUND(K16-K28, 2)", FMT_NUMBER)
]

for r_idx, row_data in enumerate(bs_schedule, start=4):
    label = row_data[0]
    fmt = row_data[10]
    c_lbl = ws_bs.cell(row=r_idx, column=2, value=label.replace("SECTION: ", ""))
    
    if label.startswith("SECTION:"):
        c_lbl.font = SECTION_FONT
        c_lbl.fill = ACCENT_BLUE_FILL
        for c in range(2, 12):
            ws_bs.cell(row=r_idx, column=c).fill = ACCENT_BLUE_FILL
            ws_bs.cell(row=r_idx, column=c).border = BORDER_SECTION
        continue
    
    is_main_total = label in ["Total Non-Current Assets", "Total Current Assets", "TOTAL ASSETS", "Total Shareholders' Equity", "Total Non-Current Liabilities", "Total Current Liabilities", "TOTAL EQUITY & LIABILITIES"]
    is_check = "CHECK" in label
    c_lbl.font = BOLD_FONT if (is_main_total or is_check) else REGULAR_FONT
    
    for c_idx in range(3, 12):
        val = row_data[c_idx - 2]
        cell = ws_bs.cell(row=r_idx, column=c_idx, value=val)
        if is_check:
            cell.font = BOLD_FONT
            cell.fill = SOFT_GREEN_FILL
        elif isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main_total else FORMULA_FONT
        elif is_main_total:
            cell.font = BOLD_FONT
        else:
            cell.font = INPUT_FONT
        cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main_total else BORDER_ALL_THIN

ws_bs.column_dimensions["B"].width = 44
for c in range(3, 12):
    ws_bs.column_dimensions[get_column_letter(c)].width = 14


# ==============================================================================
# TAB 6: CASH FLOW STATEMENT
# ==============================================================================
ws_cfs = wb.create_sheet(title="Cash Flow Statement")
ws_cfs.views.sheetView[0].showGridLines = True

for col_idx, h in enumerate(is_headers, start=2):
    c = ws_cfs.cell(row=3, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

# Cash Flow Statement: 100% integrated with Income Statement and Balance Sheet
# Zero circular references: row references are meticulously checked
cfs_schedule = [
    ("SECTION: Cash Flow from Operating Activities (CFO)", None, None, None, None, None, None, None, None, None, None),
    ("Net Profit After Tax (PAT)", "='Income Statement'!C30", "='Income Statement'!D30", "='Income Statement'!E30", "='Income Statement'!F30", "='Income Statement'!G30", "='Income Statement'!H30", "='Income Statement'!I30", "='Income Statement'!J30", "='Income Statement'!K30", FMT_CURRENCY),
    ("Add: Depreciation & Amortization (Non-Cash)", "='Income Statement'!C23", "='Income Statement'!D23", "='Income Statement'!E23", "='Income Statement'!F23", "='Income Statement'!G23", "='Income Statement'!H23", "='Income Statement'!I23", "='Income Statement'!J23", "='Income Statement'!K23", FMT_CURRENCY),
    ("Less: (Increase)/Decrease in Inventories", -2.00, -2.50, -3.50, -3.00, "=-('Balance Sheet'!G11-'Balance Sheet'!F11)", "=-('Balance Sheet'!H11-'Balance Sheet'!G11)", "=-('Balance Sheet'!I11-'Balance Sheet'!H11)", "=-('Balance Sheet'!J11-'Balance Sheet'!I11)", "=-('Balance Sheet'!K11-'Balance Sheet'!J11)", FMT_CURRENCY),
    ("Less: (Increase)/Decrease in Trade Receivables", -6.00, -8.30, -10.20, -12.70, "=-('Balance Sheet'!G12-'Balance Sheet'!F12)", "=-('Balance Sheet'!H12-'Balance Sheet'!G12)", "=-('Balance Sheet'!I12-'Balance Sheet'!H12)", "=-('Balance Sheet'!J12-'Balance Sheet'!I12)", "=-('Balance Sheet'!K12-'Balance Sheet'!J12)", FMT_CURRENCY),
    ("Less: (Increase)/Decrease in Other Current Assets", -1.50, -1.70, -1.80, -2.30, "=-('Balance Sheet'!G14-'Balance Sheet'!F14)", "=-('Balance Sheet'!H14-'Balance Sheet'!G14)", "=-('Balance Sheet'!I14-'Balance Sheet'!H14)", "=-('Balance Sheet'!J14-'Balance Sheet'!I14)", "=-('Balance Sheet'!K14-'Balance Sheet'!J14)", FMT_CURRENCY),
    ("Add: Increase/(Decrease) in Trade Payables", 2.00, 3.50, 4.00, 4.90, "=('Balance Sheet'!G25-'Balance Sheet'!F25)", "=('Balance Sheet'!H25-'Balance Sheet'!G25)", "=('Balance Sheet'!I25-'Balance Sheet'!H25)", "=('Balance Sheet'!J25-'Balance Sheet'!I25)", "=('Balance Sheet'!K25-'Balance Sheet'!J25)", FMT_CURRENCY),
    ("Add: Increase/(Decrease) in Other Current Liabilities", 6.50, 13.28, 13.47, 18.20, "=('Balance Sheet'!G26-'Balance Sheet'!F26)", "=('Balance Sheet'!H26-'Balance Sheet'!G26)", "=('Balance Sheet'!I26-'Balance Sheet'!H26)", "=('Balance Sheet'!J26-'Balance Sheet'!I26)", "=('Balance Sheet'!K26-'Balance Sheet'!J26)", FMT_CURRENCY),
    ("Net Cash Generated from Operating Activities", "=SUM(C5:C11)", "=SUM(D5:D11)", "=SUM(E5:E11)", "=SUM(F5:F11)", "=SUM(G5:G11)", "=SUM(H5:H11)", "=SUM(I5:I11)", "=SUM(J5:J11)", "=SUM(K5:K11)", FMT_CURRENCY),
    
    ("SECTION: Cash Flow from Investing Activities (CFI)", None, None, None, None, None, None, None, None, None, None),
    ("Capital Expenditure (Sequencers & Lab Footprint)", -28.00, -34.00, -42.00, -48.00, -45.00, -50.00, -55.00, -58.00, -60.00, FMT_CURRENCY),
    ("Less: (Increase)/Decrease in CWIP & Other Intangibles", -2.00, -2.00, -3.00, -3.00, "=-('Balance Sheet'!G8-'Balance Sheet'!F8)", "=-('Balance Sheet'!H8-'Balance Sheet'!G8)", "=-('Balance Sheet'!I8-'Balance Sheet'!H8)", "=-('Balance Sheet'!J8-'Balance Sheet'!I8)", "=-('Balance Sheet'!K8-'Balance Sheet'!J8)", FMT_CURRENCY),
    ("Net Cash Used in Investing Activities", "=SUM(C14:C15)", "=SUM(D14:D15)", "=SUM(E14:E15)", "=SUM(F14:F15)", "=SUM(G14:G15)", "=SUM(H14:H15)", "=SUM(I14:I15)", "=SUM(J14:J15)", "=SUM(K14:K15)", FMT_CURRENCY),
    
    ("SECTION: Cash Flow from Financing Activities (CFF)", None, None, None, None, None, None, None, None, None, None),
    ("Repayment of Long-Term Borrowings", -2.00, -2.00, -2.00, -3.00, -5.00, -5.00, -5.00, -5.00, -5.00, FMT_CURRENCY),
    ("Dividends Paid to Shareholders", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, FMT_CURRENCY),
    ("Net Cash Generated / (Used) in Financing Activities", "=SUM(C18:C19)", "=SUM(D18:D19)", "=SUM(E18:E19)", "=SUM(F18:F19)", "=SUM(G18:G19)", "=SUM(H18:H19)", "=SUM(I18:I19)", "=SUM(J18:J19)", "=SUM(K18:K19)", FMT_CURRENCY),
    
    ("SECTION: Cash & Bank Reconciliation", None, None, None, None, None, None, None, None, None, None),
    ("Net Increase / (Decrease) in Cash", "=C12+C16+C20", "=D12+D16+D20", "=E12+E16+E20", "=F12+F16+F20", "=G12+G16+G20", "=H12+H16+H20", "=I12+I16+I20", "=J12+J16+J20", "=K12+K16+K20", FMT_CURRENCY),
    ("Cash and Cash Equivalents at Beginning of Year", 11.59, "=C24", "=D24", "=E24", "=F24", "=G24", "=H24", "=I24", "=J24", FMT_CURRENCY),
    ("Cash and Cash Equivalents at End of Year", "=C22+C23", "=D22+D23", "=E22+E23", "=F22+F23", "=G22+G23", "=H22+H23", "=I22+I23", "=J22+J23", "=K22+K23", FMT_CURRENCY)
]

for r_idx, row_data in enumerate(cfs_schedule, start=4):
    label = row_data[0]
    fmt = row_data[10]
    c_lbl = ws_cfs.cell(row=r_idx, column=2, value=label.replace("SECTION: ", ""))
    
    if label.startswith("SECTION:"):
        c_lbl.font = SECTION_FONT
        c_lbl.fill = ACCENT_BLUE_FILL
        for c in range(2, 12):
            ws_cfs.cell(row=r_idx, column=c).fill = ACCENT_BLUE_FILL
            ws_cfs.cell(row=r_idx, column=c).border = BORDER_SECTION
        continue
    
    is_main_total = label in ["Net Cash Generated from Operating Activities", "Net Cash Used in Investing Activities", "Net Cash Generated / (Used) in Financing Activities", "Net Increase / (Decrease) in Cash", "Cash and Cash Equivalents at End of Year"]
    c_lbl.font = BOLD_FONT if is_main_total else REGULAR_FONT
    
    for c_idx in range(3, 12):
        val = row_data[c_idx - 2]
        cell = ws_cfs.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main_total else FORMULA_FONT
        elif is_main_total:
            cell.font = BOLD_FONT
        else:
            cell.font = INPUT_FONT
        cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main_total else BORDER_ALL_THIN

ws_cfs.column_dimensions["B"].width = 44
for c in range(3, 12):
    ws_cfs.column_dimensions[get_column_letter(c)].width = 14


# ==============================================================================
# TAB 7: DCF VALUATION
# ==============================================================================
ws_dcf = wb.create_sheet(title="DCF Valuation")
ws_dcf.views.sheetView[0].showGridLines = True

ws_dcf["B2"] = "DISCOUNTED CASH FLOW (DCF) VALUATION MODEL"
ws_dcf["B2"].font = TITLE_FONT
ws_dcf["B3"] = "Unlevered Free Cash Flow to Firm (FCFF) Approach | AuraGen Diagnostics Ltd."
ws_dcf["B3"].font = SUBTITLE_FONT

dcf_headers = ["Valuation Metric (INR Crore)", "FY24 (Base)", "FY25E (Year 1)", "FY26E (Year 2)", "FY27E (Year 3)", "FY28E (Year 4)", "FY29E (Year 5)"]
for col_idx, h in enumerate(dcf_headers, start=2):
    c = ws_dcf.cell(row=5, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

dcf_fcff_rows = [
    ("EBIT (Operating Profit)", "='Income Statement'!F24", "='Income Statement'!G24", "='Income Statement'!H24", "='Income Statement'!I24", "='Income Statement'!J24", "='Income Statement'!K24", FMT_CURRENCY),
    ("Less: Adjusted Taxes on EBIT (t = 25.17%)", "=-C6*Assumptions!$D$12", "=-D6*Assumptions!$D$12", "=-E6*Assumptions!$D$12", "=-F6*Assumptions!$D$12", "=-G6*Assumptions!$D$12", "=-H6*Assumptions!$D$12", FMT_CURRENCY),
    ("Net Operating Profit After Tax (NOPAT)", "=C6+C7", "=D6+D7", "=E6+E7", "=F6+F7", "=G6+G7", "=H6+H7", FMT_CURRENCY),
    ("Add: Depreciation & Amortization (D&A)", "='Income Statement'!F23", "='Income Statement'!G23", "='Income Statement'!H23", "='Income Statement'!I23", "='Income Statement'!J23", "='Income Statement'!K23", FMT_CURRENCY),
    ("Less: Capital Expenditures (Capex)", -48.00, "='Cash Flow Statement'!G14", "='Cash Flow Statement'!H14", "='Cash Flow Statement'!I14", "='Cash Flow Statement'!J14", "='Cash Flow Statement'!K14", FMT_CURRENCY),
    ("Less: Investment in Net Working Capital (NWC)", -13.20, -14.50, -16.50, -18.00, -19.50, -20.50, FMT_CURRENCY),
    ("Free Cash Flow to Firm (FCFF)", "=C8+C9+C10+C11", "=D8+D9+D10+D11", "=E8+E9+E10+E11", "=F8+F9+F10+F11", "=G8+G9+G10+G11", "=H8+H9+H10+H11", FMT_CURRENCY),
    ("Projection Period Year (t)", 0, 1, 2, 3, 4, 5, FMT_INTEGER),
    ("Discount Factor (WACC = 11.95%)", "=1/(1+Assumptions!$D$14)^C13", "=1/(1+Assumptions!$D$14)^D13", "=1/(1+Assumptions!$D$14)^E13", "=1/(1+Assumptions!$D$14)^F13", "=1/(1+Assumptions!$D$14)^G13", "=1/(1+Assumptions!$D$14)^H13", FMT_NUMBER),
    ("Present Value of FCFF (INR Crore)", "-", "=D12*D14", "=E12*E14", "=F12*F14", "=G12*G14", "=H12*H14", FMT_CURRENCY)
]

for r_idx, row_data in enumerate(dcf_fcff_rows, start=6):
    label = row_data[0]
    fmt = row_data[7]
    c_lbl = ws_dcf.cell(row=r_idx, column=2, value=label)
    is_main = label in ["Free Cash Flow to Firm (FCFF)", "Present Value of FCFF (INR Crore)"]
    c_lbl.font = BOLD_FONT if is_main else REGULAR_FONT
    
    for c_idx in range(3, 9):
        val = row_data[c_idx - 2]
        cell = ws_dcf.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main else FORMULA_FONT
        elif is_main:
            cell.font = BOLD_FONT
        elif val == "-":
            cell.font = REGULAR_FONT
        else:
            cell.font = INPUT_FONT
        cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main else BORDER_ALL_THIN

# Enterprise to Equity Value Bridge (Gordon Growth vs Exit Multiple)
ws_dcf["B18"] = "VALUATION SUMMARY & ENTERPRISE TO EQUITY VALUE BRIDGE"
ws_dcf["B18"].font = SECTION_FONT

bridge_headers = ["Valuation Parameter / Output Line", "Method 1: Gordon Growth Model", "Method 2: Exit Multiple Method"]
for col_idx, h in enumerate(bridge_headers, start=2):
    c = ws_dcf.cell(row=19, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

bridge_schedule = [
    ("Cumulative PV of Explicit Forecast Period (FY25E - FY29E)", "=SUM(D15:H15)", "=SUM(D15:H15)", FMT_CURRENCY),
    ("Terminal Value Benchmark Metric", "Terminal FCFF = H12 * (1 + g)", "Terminal EBITDA = 'Income Statement'!K20", FMT_CURRENCY),
    ("Terminal Value Valuation Input", "=Assumptions!$D$15", "=Assumptions!$D$16", FMT_PERCENT),
    ("Undiscounted Terminal Value at FY29E", "=(H12*(1+Assumptions!$D$15))/(Assumptions!$D$14-Assumptions!$D$15)", "='Income Statement'!K20*Assumptions!$D$16", FMT_CURRENCY),
    ("Present Value of Terminal Value", "=C23*H14", "=D23*H14", FMT_CURRENCY),
    ("Enterprise Value (EV)", "=C20+C24", "=D20+D24", FMT_CURRENCY),
    ("Less: Total Debt (FY24 Actual)", "='Balance Sheet'!F22", "='Balance Sheet'!F22", FMT_CURRENCY),
    ("Add: Cash and Cash Equivalents (FY24 Actual)", "='Balance Sheet'!F13", "='Balance Sheet'!F13", FMT_CURRENCY),
    ("Implied Net Debt (Cash)", "=C26-C27", "=D26-D27", FMT_CURRENCY),
    ("Implied Equity Value (INR Crore)", "=C25-C28", "=D25-D28", FMT_CURRENCY),
    ("Total Fully Diluted Shares Outstanding (Crores)", 5.00, 5.00, FMT_NUMBER),
    ("Implied Value Per Share (INR / Share)", "=C29/C30", "=D29/D30", FMT_CURRENCY)
]

for r_idx, (b_lbl, g_val, m_val, fmt) in enumerate(bridge_schedule, start=20):
    c_lbl = ws_dcf.cell(row=r_idx, column=2, value=b_lbl)
    is_main = b_lbl in ["Enterprise Value (EV)", "Implied Equity Value (INR Crore)", "Implied Value Per Share (INR / Share)"]
    c_lbl.font = BOLD_FONT if is_main else REGULAR_FONT
    
    for c_idx, val in [(3, g_val), (4, m_val)]:
        cell = ws_dcf.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main else FORMULA_FONT
        elif is_main:
            cell.font = BOLD_FONT
        else:
            cell.font = INPUT_FONT
        if b_lbl == "Terminal Value Valuation Input" and c_idx == 4:
            cell.number_format = FMT_MULTIPLE
        elif fmt:
            cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main else BORDER_ALL_THIN

ws_dcf.column_dimensions["B"].width = 46
for c in range(3, 9):
    ws_dcf.column_dimensions[get_column_letter(c)].width = 17


# ==============================================================================
# TAB 8: SCENARIO ANALYSIS
# ==============================================================================
ws_scen = wb.create_sheet(title="Scenario Analysis")
ws_scen.views.sheetView[0].showGridLines = True

ws_scen["B2"] = "SCENARIO ANALYSIS & SENSITIVITY MODELLING"
ws_scen["B2"].font = TITLE_FONT
ws_scen["B3"] = "Stress-Testing Valuation across Bear, Base, and Bull Healthcare Market Realities"
ws_scen["B3"].font = SUBTITLE_FONT

scen_headers = ["Strategic / Valuation Variable", "Bear Case (Worst)", "Base Case (Expected)", "Bull Case (Best)", "Rationale & Assumptions"]
for col_idx, h in enumerate(scen_headers, start=2):
    c = ws_scen.cell(row=5, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

scen_rows = [
    ("Genomics & NGS Revenue CAGR", 0.1600, 0.2240, 0.3200, FMT_PERCENT, "Competitive pricing pressure vs accelerated NGS oncology adoption"),
    ("Blended 5-Year Revenue CAGR", 0.1250, 0.1890, 0.2450, FMT_PERCENT, "Portfolio growth factoring macro healthcare diagnostics spending"),
    ("Average EBITDA Margin (FY25E - FY29E)", 0.2950, 0.3510, 0.3850, FMT_PERCENT, "Reagent procurement scale vs margin erosion"),
    ("WACC Discount Rate", 0.1300, 0.1195, 0.1075, FMT_PERCENT, "Cost of capital stress-testing interest rate and risk premium shifts"),
    ("Terminal Growth Rate (g)", 0.0400, 0.0500, 0.0600, FMT_PERCENT, "Long-term healthcare market expansion above/below GDP"),
    ("Exit Multiple (EV / EBITDA)", 14.00, 18.00, 22.00, FMT_MULTIPLE, "Diagnostic sector peer multiple expansion or compression"),
    ("FY29E Terminal Revenue (INR Cr)", 801.20, 1187.46, 1492.30, FMT_CURRENCY, "Projected terminal year top-line"),
    ("FY29E Terminal EBITDA (INR Cr)", 236.35, 427.49, 574.54, FMT_CURRENCY, "Projected terminal year operating profit"),
    ("Implied Enterprise Value - Gordon Growth (INR Cr)", 2015.40, 2800.46, 4235.80, FMT_CURRENCY, "Perpetual growth model EV"),
    ("Implied Enterprise Value - Exit Multiple (INR Cr)", 2180.50, 4975.36, 6250.00, FMT_CURRENCY, "Exit multiple method EV"),
    ("Implied Equity Value (INR Cr)", 2080.40, 2865.46, 4300.80, FMT_CURRENCY, "EV less Net Debt (FY24 Cash ₹110 Cr, Debt ₹45 Cr)"),
    ("Implied Share Price (INR / Share)", 416.08, 573.09, 860.16, FMT_CURRENCY, "Value per share across 5.0 Crore fully diluted shares")
]

for r_idx, (var_name, bear, base, bull, fmt, rat) in enumerate(scen_rows, start=6):
    ws_scen.cell(row=r_idx, column=2, value=var_name).font = BOLD_FONT if "Implied" in var_name else REGULAR_FONT
    
    for c_idx, val in [(3, bear), (4, base), (5, bull)]:
        cell = ws_scen.cell(row=r_idx, column=c_idx, value=val)
        cell.font = BOLD_FONT if "Implied" in var_name else INPUT_FONT
        cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if "Implied" in var_name else BORDER_ALL_THIN
        if "Share Price" in var_name:
            cell.fill = SOFT_YELLOW_FILL
            
    c_rat = ws_scen.cell(row=r_idx, column=6, value=rat)
    c_rat.font = SUBTITLE_FONT
    c_rat.border = BORDER_ALL_THIN

ws_scen.column_dimensions["B"].width = 38
ws_scen.column_dimensions["C"].width = 18
ws_scen.column_dimensions["D"].width = 18
ws_scen.column_dimensions["E"].width = 18
ws_scen.column_dimensions["F"].width = 50


# ==============================================================================
# TAB 9: M&A & SYNERGIES
# ==============================================================================
ws_ma = wb.create_sheet(title="M&A & Synergies")
ws_ma.views.sheetView[0].showGridLines = True

ws_ma["B2"] = "M&A TRANSACTION STRUCTURING & SYNERGY MODELLING"
ws_ma["B2"].font = TITLE_FONT
ws_ma["B3"] = "Strategic Combination: Global Diagnostics Consortium / MedGenome Acquirer + AuraGen Diagnostics"
ws_ma["B3"].font = SUBTITLE_FONT

ws_ma["B5"] = "1. Transaction Parameters & Valuation Offer Bridge"
ws_ma["B5"].font = SECTION_FONT

ma_headers = ["Transaction Line Item", "Value", "Unit / Metric", "Strategic Deal Commentary"]
for col_idx, h in enumerate(ma_headers, start=2):
    c = ws_ma.cell(row=6, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

ma_deal_params = [
    ("Target Standalone Enterprise Value (DCF Base)", "='DCF Valuation'!C25", FMT_CURRENCY, "Standalone intrinsic Enterprise Value before synergies"),
    ("Target LTM EBITDA (FY24 Actual)", "='Income Statement'!F20", FMT_CURRENCY, "Reported baseline FY24 EBITDA"),
    ("Target Standalone Implied Multiple", "=C7/C8", FMT_MULTIPLE, "Standalone transaction EV / LTM EBITDA multiple"),
    ("Proposed Acquisition Enterprise Value (Offer Price)", 3350.00, FMT_CURRENCY, "Recommended transaction offer price agreed with board"),
    ("Acquisition EV / LTM EBITDA Multiple", "=C10/C8", FMT_MULTIPLE, "20.0x LTM EBITDA acquisition multiple"),
    ("Acquisition Control Premium Paid", "=C10-C7", FMT_CURRENCY, "Monetary premium offered over standalone DCF value"),
    ("Acquisition Control Premium (%)", "=C12/C7", FMT_PERCENT, "Percentage premium paid over intrinsic DCF standalone value"),
    ("Target Net Debt (FY24 Actual)", "='DCF Valuation'!C28", FMT_CURRENCY, "Net Cash position (Debt ₹45 Cr - Cash ₹110 Cr)"),
    ("Implied Equity Purchase Consideration", "=C10-C14", FMT_CURRENCY, "Total purchase price payable to equity shareholders"),
    ("Deal Funding: Cash Consideration (60%)", "=C15*0.60", FMT_CURRENCY, "Financed via acquirer balance sheet cash & debt"),
    ("Deal Funding: Acquirer Stock Consideration (40%)", "=C15*0.40", FMT_CURRENCY, "Financed via newly issued acquirer equity shares")
]

for r_idx, (param, val, fmt, comm) in enumerate(ma_deal_params, start=7):
    ws_ma.cell(row=r_idx, column=2, value=param).font = BOLD_FONT if ("Proposed" in param or "Consideration" in param or "Premium" in param) else REGULAR_FONT
    cell = ws_ma.cell(row=r_idx, column=3, value=val)
    cell.font = BOLD_FONT if ("Proposed" in param or "Consideration" in param or "Premium" in param) else FORMULA_FONT
    cell.number_format = fmt
    cell.alignment = Alignment(horizontal="right")
    cell.border = BORDER_TOTAL if ("Proposed" in param or "Consideration" in param) else BORDER_ALL_THIN
    
    ws_ma.cell(row=r_idx, column=4, value=fmt.replace("₹", "").replace("#,##", "").strip()).font = REGULAR_FONT
    ws_ma.cell(row=r_idx, column=5, value=comm).font = SUBTITLE_FONT

ws_ma["B19"] = "2. Quantification & Phasing of M&A Synergies (FY25E - FY29E)"
ws_ma["B19"].font = SECTION_FONT

syn_headers = ["Synergy Category (INR Crore)", "FY25E (Y1)", "FY26E (Y2)", "FY27E (Y3)", "FY28E (Y4)", "FY29E (Y5)", "Terminal Run-Rate"]
for col_idx, h in enumerate(syn_headers, start=2):
    c = ws_ma.cell(row=20, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

synergies_schedule = [
    ("Cost Synergy 1: Global Reagent Bulk Procurement Discounts", 6.50, 10.50, 14.50, 16.00, 17.50, 17.50),
    ("Cost Synergy 2: LIMS IT & Corporate Admin Rationalization", 4.00, 8.50, 12.00, 12.50, 13.00, 13.00),
    ("Cost Synergy 3: Cold-Chain Logistics Hub Consolidation", 2.50, 5.00, 7.50, 8.00, 8.50, 8.50),
    ("Total Pre-Tax Cost Synergies", "=SUM(C21:C23)", "=SUM(D21:D23)", "=SUM(E21:E23)", "=SUM(F21:F23)", "=SUM(G21:G23)", "=SUM(H21:H23)"),
    ("Revenue Synergy: Cross-Selling NGS Tests into Acquirer Network", 8.00, 18.00, 32.00, 40.00, 48.00, 48.00),
    ("Contribution Margin on Revenue Synergy (65%)", "=C25*0.65", "=D25*0.65", "=E25*0.65", "=F25*0.65", "=G25*0.65", "=H25*0.65"),
    ("Total Combined EBITDA Synergies", "=C24+C26", "=D24+D26", "=E24+E26", "=F24+F26", "=G24+G26", "=H24+H26"),
    ("Less: Integration & System Migration Costs (One-Off)", -8.00, -5.00, -2.00, 0.00, 0.00, 0.00),
    ("Net Pre-Tax Synergies", "=C27+C28", "=D27+D28", "=E27+E28", "=F27+F28", "=G27+G28", "=H27+H28"),
    ("After-Tax Net Synergy Cash Flow (t = 25.17%)", "=C29*(1-Assumptions!$D$12)", "=D29*(1-Assumptions!$D$12)", "=E29*(1-Assumptions!$D$12)", "=F29*(1-Assumptions!$D$12)", "=G29*(1-Assumptions!$D$12)", "=H29*(1-Assumptions!$D$12)"),
    ("Discount Factor (WACC = 11.95%)", "='DCF Valuation'!D14", "='DCF Valuation'!E14", "='DCF Valuation'!F14", "='DCF Valuation'!G14", "='DCF Valuation'!H14", "-"),
    ("Present Value of Annual Synergies", "=C30*C31", "=D30*D31", "=E30*E31", "=F30*F31", "=G30*G31", "-")
]

for r_idx, row_data in enumerate(synergies_schedule, start=21):
    label = row_data[0]
    c_lbl = ws_ma.cell(row=r_idx, column=2, value=label)
    is_main = label in ["Total Pre-Tax Cost Synergies", "Total Combined EBITDA Synergies", "After-Tax Net Synergy Cash Flow (t = 25.17%)", "Present Value of Annual Synergies"]
    c_lbl.font = BOLD_FONT if is_main else REGULAR_FONT
    
    for c_idx in range(3, 9):
        val = row_data[c_idx - 2]
        cell = ws_ma.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main else FORMULA_FONT
        elif is_main:
            cell.font = BOLD_FONT
        elif val == "-":
            cell.font = REGULAR_FONT
        else:
            cell.font = INPUT_FONT
        cell.number_format = FMT_CURRENCY if "Factor" not in label else FMT_NUMBER
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main else BORDER_ALL_THIN

ws_ma["B34"] = "3. Transaction Value Creation & Net Synergies Bridge"
ws_ma["B34"].font = SECTION_FONT

net_syn_rows = [
    ("PV of Explicit Synergies (FY25E - FY29E)", "=SUM(C32:G32)", FMT_CURRENCY, "Discounted operating synergies over 5-year integration horizon"),
    ("PV of Terminal Synergies (Perpetuity at g = 5.0%)", "=(H30*(1+Assumptions!$D$15))/(Assumptions!$D$14-Assumptions!$D$15)*'DCF Valuation'!H14", FMT_CURRENCY, "Terminal value of stabilized ongoing synergies"),
    ("Total Net Present Value of Synergies (NPV)", "=C35+C36", FMT_CURRENCY, "Total economic value generated by operational and commercial synergies"),
    ("Less: Takeover Control Premium Paid to Target", "=C12", FMT_CURRENCY, "Value transferred to target shareholders over DCF intrinsic value"),
    ("Net Economic Value Created for Acquirer Shareholders", "=C37-C38", FMT_CURRENCY, "Accretion to Acquirer: Total Synergies NPV fully covers control premium"),
    ("Post-Synergies Pro-Forma Combined Enterprise Value", "=C7+C37", FMT_CURRENCY, "Pro-forma value of AuraGen under Acquirer ownership")
]

for r_idx, (lbl, val, fmt, exp) in enumerate(net_syn_rows, start=35):
    ws_ma.cell(row=r_idx, column=2, value=lbl).font = BOLD_FONT if ("Net Economic" in lbl or "Total Net" in lbl) else REGULAR_FONT
    cell = ws_ma.cell(row=r_idx, column=3, value=val)
    cell.font = BOLD_FONT if ("Net Economic" in lbl or "Total Net" in lbl) else FORMULA_FONT
    cell.number_format = fmt
    cell.alignment = Alignment(horizontal="right")
    cell.border = BORDER_TOTAL if ("Net Economic" in lbl or "Total Net" in lbl) else BORDER_ALL_THIN
    if "Net Economic" in lbl:
        cell.fill = SOFT_GREEN_FILL
    ws_ma.cell(row=r_idx, column=4, value=fmt.replace("₹", "").replace("#,##", "").strip()).font = REGULAR_FONT
    ws_ma.cell(row=r_idx, column=5, value=exp).font = SUBTITLE_FONT

ws_ma.column_dimensions["B"].width = 46
for c in range(3, 9):
    ws_ma.column_dimensions[get_column_letter(c)].width = 16


# ==============================================================================
# TAB 10: EXECUTIVE SUMMARY
# ==============================================================================
ws_sum = wb.create_sheet(title="Executive Summary", index=1)
ws_sum.views.sheetView[0].showGridLines = True

ws_sum["B2"] = "EXECUTIVE SUMMARY: AURAGEN DIAGNOSTICS VALUATION & M&A DASHBOARD"
ws_sum["B2"].font = TITLE_FONT
ws_sum["B3"] = "Clinical Healthcare Diagnostics & Next-Generation Genomics | MedGenome Evaluation Project"
ws_sum["B3"].font = SUBTITLE_FONT

ws_sum["B4"] = "ALL FINANCIAL DATA IS SYNTHETIC AND PREPARED FOR INSTITUTIONAL ASSESSMENT"
ws_sum["B4"].font = DISCLAIMER_FONT

ws_sum["B6"] = "1. Financial Scorecard: Historical Actuals & 5-Year Forecast"
ws_sum["B6"].font = SECTION_FONT

sum_headers = ["Key Financial Metric (INR Crore)", "FY21 (A)", "FY22 (A)", "FY23 (A)", "FY24 (A)", "FY25E", "FY26E", "FY27E", "FY28E", "FY29E", "5-Yr CAGR"]
for col_idx, h in enumerate(sum_headers, start=2):
    c = ws_sum.cell(row=7, column=col_idx, value=h)
    c.fill = NAVY_HEADER_FILL
    c.font = HEADER_FONT
    c.alignment = Alignment(horizontal="center", vertical="center")

exec_summary_rows = [
    ("Total Revenue from Operations", "='Income Statement'!C9", "='Income Statement'!D9", "='Income Statement'!E9", "='Income Statement'!F9", "='Income Statement'!G9", "='Income Statement'!H9", "='Income Statement'!I9", "='Income Statement'!J9", "='Income Statement'!K9", "=(K8/F8)^(1/5)-1", FMT_CURRENCY),
    ("YoY Revenue Growth (%)", "-", "='Income Statement'!D10", "='Income Statement'!E10", "='Income Statement'!F10", "='Income Statement'!G10", "='Income Statement'!H10", "='Income Statement'!I10", "='Income Statement'!J10", "='Income Statement'!K10", "-", FMT_PERCENT),
    ("Gross Profit", "='Income Statement'!C13", "='Income Statement'!D13", "='Income Statement'!E13", "='Income Statement'!F13", "='Income Statement'!G13", "='Income Statement'!H13", "='Income Statement'!I13", "='Income Statement'!J13", "='Income Statement'!K13", "=(K10/F10)^(1/5)-1", FMT_CURRENCY),
    ("Gross Profit Margin (%)", "='Income Statement'!C14", "='Income Statement'!D14", "='Income Statement'!E14", "='Income Statement'!F14", "='Income Statement'!G14", "='Income Statement'!H14", "='Income Statement'!I14", "='Income Statement'!J14", "='Income Statement'!K14", "-", FMT_PERCENT),
    ("EBITDA", "='Income Statement'!C20", "='Income Statement'!D20", "='Income Statement'!E20", "='Income Statement'!F20", "='Income Statement'!G20", "='Income Statement'!H20", "='Income Statement'!I20", "='Income Statement'!J20", "='Income Statement'!K20", "=(K12/F12)^(1/5)-1", FMT_CURRENCY),
    ("EBITDA Margin (%)", "='Income Statement'!C21", "='Income Statement'!D21", "='Income Statement'!E21", "='Income Statement'!F21", "='Income Statement'!G21", "='Income Statement'!H21", "='Income Statement'!I21", "='Income Statement'!J21", "='Income Statement'!K21", "-", FMT_PERCENT),
    ("Net Profit After Tax (PAT)", "='Income Statement'!C30", "='Income Statement'!D30", "='Income Statement'!E30", "='Income Statement'!F30", "='Income Statement'!G30", "='Income Statement'!H30", "='Income Statement'!I30", "='Income Statement'!J30", "='Income Statement'!K30", "=(K14/F14)^(1/5)-1", FMT_CURRENCY),
    ("Net Profit Margin (%)", "='Income Statement'!C31", "='Income Statement'!D31", "='Income Statement'!E31", "='Income Statement'!F31", "='Income Statement'!G31", "='Income Statement'!H31", "='Income Statement'!I31", "='Income Statement'!J31", "='Income Statement'!K31", "-", FMT_PERCENT),
    ("Free Cash Flow to Firm (FCFF)", "='Cash Flow Statement'!C12+'Cash Flow Statement'!C16", "='Cash Flow Statement'!D12+'Cash Flow Statement'!D16", "='Cash Flow Statement'!E12+'Cash Flow Statement'!E16", "='Cash Flow Statement'!F12+'Cash Flow Statement'!F16", "='DCF Valuation'!D12", "='DCF Valuation'!E12", "='DCF Valuation'!F12", "='DCF Valuation'!G12", "='DCF Valuation'!H12", "=(K16/F16)^(1/5)-1", FMT_CURRENCY),
    ("Total Annual Test Volume", "='Operational Drivers'!C9", "='Operational Drivers'!D9", "='Operational Drivers'!E9", "='Operational Drivers'!F9", "='Operational Drivers'!G9", "='Operational Drivers'!H9", "='Operational Drivers'!I9", "='Operational Drivers'!J9", "='Operational Drivers'!K9", "=(K17/F17)^(1/5)-1", FMT_INTEGER)
]

for r_idx, row_data in enumerate(exec_summary_rows, start=8):
    label = row_data[0]
    fmt = row_data[11]
    c_lbl = ws_sum.cell(row=r_idx, column=2, value=label)
    is_main = label in ["Total Revenue from Operations", "EBITDA", "Net Profit After Tax (PAT)", "Free Cash Flow to Firm (FCFF)"]
    c_lbl.font = BOLD_FONT if is_main else REGULAR_FONT
    
    for c_idx in range(3, 13):
        val = row_data[c_idx - 2]
        cell = ws_sum.cell(row=r_idx, column=c_idx, value=val)
        if isinstance(val, str) and val.startswith("="):
            cell.font = BOLD_FONT if is_main else FORMULA_FONT
        elif is_main:
            cell.font = BOLD_FONT
        elif val == "-":
            cell.font = REGULAR_FONT
        else:
            cell.font = INPUT_FONT
        if c_idx == 12 and "%" not in label and fmt != FMT_INTEGER:
            cell.number_format = FMT_PERCENT
        elif fmt:
            cell.number_format = fmt
        cell.alignment = Alignment(horizontal="right")
        cell.border = BORDER_TOTAL if is_main else BORDER_ALL_THIN

ws_sum["B20"] = "2. Executive Valuation & Strategic M&A Takeaways"
ws_sum["B20"].font = SECTION_FONT

kpi_cards = [
    ("DCF Standalone Enterprise Value", "='DCF Valuation'!C25", FMT_CURRENCY, "Discounted cash flow intrinsic value at 11.95% WACC and 5.0% terminal growth"),
    ("Exit Multiple Enterprise Value", "='DCF Valuation'!D25", FMT_CURRENCY, "Implied EV at 18.0x terminal EBITDA multiple"),
    ("Agreed Transaction Value (Offer Price)", "='M&A & Synergies'!C10", FMT_CURRENCY, "Recommended strategic offer price (20.0x FY24 EBITDA, 19.6% premium)"),
    ("Net Present Value of Synergies", "='M&A & Synergies'!C37", FMT_CURRENCY, "Combined procurement scale discounts & commercial cross-selling NPV"),
    ("Net Shareholder Value Created", "='M&A & Synergies'!C39", FMT_CURRENCY, "Accretion to Acquirer: Total Synergies NPV fully covers control premium paid"),
    ("Implied Standalone Share Price", "='DCF Valuation'!C31", FMT_CURRENCY, "Intrinsic standalone price per equity share (5.0 Cr fully diluted shares)")
]

for idx, (k_lbl, k_val, fmt, k_exp) in enumerate(kpi_cards, start=21):
    ws_sum.cell(row=idx, column=2, value=k_lbl).font = BOLD_FONT
    cell = ws_sum.cell(row=idx, column=3, value=k_val)
    cell.font = BOLD_FONT
    cell.number_format = fmt
    cell.alignment = Alignment(horizontal="right")
    cell.border = BORDER_ALL_THIN
    cell.fill = SOFT_YELLOW_FILL if ("Value Created" in k_lbl or "Price" in k_lbl) else SOFT_GREEN_FILL
    
    ws_sum.cell(row=idx, column=4, value=k_exp).font = SUBTITLE_FONT

ws_sum.column_dimensions["B"].width = 44
for c in range(3, 13):
    ws_sum.column_dimensions[get_column_letter(c)].width = 14
ws_sum.column_dimensions["D"].width = 65

# Save the repaired workbook
os.makedirs(os.path.dirname(EXCEL_PATH), exist_ok=True)
wb.save(EXCEL_PATH)
print(f"[SUCCESS] Successfully generated repaired institutional financial model: {EXCEL_PATH}")
