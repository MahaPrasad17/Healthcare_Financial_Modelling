-- ==============================================================================
-- PROJECT: Healthcare Diagnostics Financial Modelling & M&A Valuation
-- TARGET ENTITY: AuraGen Diagnostics Ltd.
-- FILE: financial_analysis.sql
-- DIALECT: Microsoft SQL Server (T-SQL) / ANSI SQL Compatible
-- DATA CLASSIFICATION: Synthetic Financial & Operational Benchmark Data
-- NOTICE: All financial records, test counts, metrics, and operational data
--         contained herein are simulated benchmarks compiled for financial
--         modelling, M&A valuation, and diagnostic analytics case studies.
-- OBJECTIVE: 15 Institutional-Grade Financial & Operational Queries Covering
--            Revenue Trends, Profitability, Segment Mix, Working Capital & M&A.
-- ==============================================================================

USE HealthcareDiagnosticsDW;
GO

-- ==============================================================================
-- QUERY 1: Multi-Year Revenue, EBITDA & Profitability Margin Progression
-- Objective: Evaluate top-line acceleration, EBITDA margin expansion, and net profit growth.
-- ==============================================================================
SELECT 
    FiscalYear,
    PeriodType,
    TotalRevenue_Cr,
    LAG(TotalRevenue_Cr, 1) OVER (ORDER BY FinancialRecordID) AS PriorYear_Revenue_Cr,
    ROUND(((TotalRevenue_Cr - LAG(TotalRevenue_Cr, 1) OVER (ORDER BY FinancialRecordID)) 
           / NULLIF(LAG(TotalRevenue_Cr, 1) OVER (ORDER BY FinancialRecordID), 0)) * 100, 2) AS YoY_Revenue_Growth_Pct,
    EBITDA_Cr,
    EBITDAMargin_Pct,
    NetProfit_PAT_Cr,
    NetProfitMargin_Pct,
    FreeCashFlow_FCFF_Cr,
    ROUND((FreeCashFlow_FCFF_Cr / NULLIF(EBITDA_Cr, 0)) * 100, 2) AS FCF_to_EBITDA_Conversion_Pct
FROM Fact_Financial_Annual
ORDER BY FinancialRecordID;
GO


-- ==============================================================================
-- QUERY 2: Diagnostic Segment Contribution & Gross Margin Mix
-- Objective: Track the portfolio shift from routine biochemistry to high-value genomics.
-- ==============================================================================
WITH SegmentAggregates AS (
    SELECT 
        c.CategoryName,
        c.ClinicalSpecialty,
        c.IsGenomicsSpecialized,
        SUM(f.TestVolume) AS Total_Test_Volume,
        ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Total_Revenue_Cr,
        ROUND(SUM(f.DirectCOGS_INR) / 10000000.0, 2) AS Total_COGS_Cr,
        ROUND(SUM(f.GrossProfit_INR) / 10000000.0, 2) AS Total_GrossProfit_Cr
    FROM Fact_Monthly_Revenues f
    INNER JOIN Dim_Test_Category c ON f.CategoryID = c.CategoryID
    GROUP BY c.CategoryName, c.ClinicalSpecialty, c.IsGenomicsSpecialized
)
SELECT 
    CategoryName,
    ClinicalSpecialty,
    Total_Test_Volume,
    Total_Revenue_Cr,
    ROUND((Total_Revenue_Cr / SUM(Total_Revenue_Cr) OVER()) * 100, 2) AS Revenue_Contribution_Pct,
    Total_COGS_Cr,
    Total_GrossProfit_Cr,
    ROUND((Total_GrossProfit_Cr / NULLIF(Total_Revenue_Cr, 0)) * 100, 2) AS Gross_Margin_Pct,
    CASE WHEN IsGenomicsSpecialized = 1 THEN 'High-Growth Core Engine' ELSE 'Cash Cow Volume' END AS StrategicRole
FROM SegmentAggregates
ORDER BY Total_Revenue_Cr DESC;
GO


-- ==============================================================================
-- QUERY 3: Revenue Run-Rate with 3-Period Trailing Moving Average
-- Objective: Smooth out seasonal diagnostic volume spikes using window functions.
-- ==============================================================================
SELECT 
    d.FiscalYear,
    d.FiscalQuarter,
    d.FullDate,
    ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Quarterly_Revenue_Cr,
    ROUND(AVG(SUM(f.GrossRevenue_INR) / 10000000.0) OVER (
        ORDER BY d.DateKey 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS Trailing_3Quarter_MovingAvg_Cr,
    SUM(f.TestVolume) AS Quarterly_Test_Volume,
    ROUND(SUM(f.GrossRevenue_INR) / NULLIF(SUM(f.TestVolume), 0), 2) AS Quarterly_Blended_ARPT_INR
FROM Fact_Monthly_Revenues f
INNER JOIN Dim_Date d ON f.DateKey = d.DateKey
GROUP BY d.FiscalYear, d.FiscalQuarter, d.FullDate, d.DateKey
ORDER BY d.DateKey;
GO


-- ==============================================================================
-- QUERY 4: Regional Hub Benchmarking: Revenue, Volumes & Realization (ARPT)
-- Objective: Compare geographic diagnostic penetration, test mix, and ARPT.
-- ==============================================================================
SELECT 
    r.RegionName,
    r.Zone,
    r.TierClassification,
    SUM(f.TestVolume) AS Total_Tests_Conducted,
    ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Regional_Revenue_Cr,
    ROUND((SUM(f.GrossRevenue_INR) / SUM(SUM(f.GrossRevenue_INR)) OVER()) * 100, 2) AS Regional_Share_Pct,
    ROUND(SUM(f.GrossRevenue_INR) / NULLIF(SUM(f.TestVolume), 0), 2) AS Average_Realization_Per_Test_INR,
    ROUND((SUM(f.GrossProfit_INR) / NULLIF(SUM(f.GrossRevenue_INR), 0)) * 100, 2) AS Regional_Gross_Margin_Pct
FROM Fact_Monthly_Revenues f
INNER JOIN Dim_Region r ON f.RegionID = r.RegionID
GROUP BY r.RegionName, r.Zone, r.TierClassification
ORDER BY Regional_Revenue_Cr DESC;
GO


-- ==============================================================================
-- QUERY 5: Laboratory Center Profitability Ranking using DENSE_RANK()
-- Objective: Rank individual processing hubs by gross margin generation and throughput.
-- ==============================================================================
WITH LabPerformance AS (
    SELECT 
        l.CenterCode,
        l.CenterName,
        l.CenterType,
        r.RegionName,
        l.SequencerCapacityCount,
        SUM(f.TestVolume) AS Total_Volume,
        ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Revenue_Generated_Cr,
        ROUND(SUM(f.GrossProfit_INR) / 10000000.0, 2) AS Gross_Profit_Cr,
        ROUND((SUM(f.GrossProfit_INR) / NULLIF(SUM(f.GrossRevenue_INR), 0)) * 100, 2) AS Gross_Margin_Pct
    FROM Fact_Monthly_Revenues f
    INNER JOIN Dim_Lab_Center l ON f.CenterID = l.CenterID
    INNER JOIN Dim_Region r ON l.RegionID = r.RegionID
    GROUP BY l.CenterCode, l.CenterName, l.CenterType, r.RegionName, l.SequencerCapacityCount
)
SELECT 
    DENSE_RANK() OVER (ORDER BY Gross_Profit_Cr DESC) AS Profit_Rank,
    CenterCode,
    CenterName,
    CenterType,
    RegionName,
    SequencerCapacityCount,
    Total_Volume,
    Revenue_Generated_Cr,
    Gross_Profit_Cr,
    Gross_Margin_Pct
FROM LabPerformance
ORDER BY Profit_Rank;
GO


-- ==============================================================================
-- QUERY 6: Operating Cost Structure Decomposition (% of Total Revenue)
-- Objective: Analyze structural cost levers: Reagents, Personnel, Logistics, and SG&A.
-- ==============================================================================
SELECT 
    FiscalYear,
    PeriodType,
    TotalRevenue_Cr,
    ROUND((COGS_Cr / TotalRevenue_Cr) * 100, 2) AS Reagents_COGS_Pct,
    ROUND((PersonnelExpenses_Cr / TotalRevenue_Cr) * 100, 2) AS Personnel_Expense_Pct,
    ROUND((LogisticsExpenses_Cr / TotalRevenue_Cr) * 100, 2) AS ColdChain_Logistics_Pct,
    ROUND((LabOperatingExpenses_Cr / TotalRevenue_Cr) * 100, 2) AS Lab_Operations_Pct,
    ROUND((SGAExpenses_Cr / TotalRevenue_Cr) * 100, 2) AS Corporate_SGA_Pct,
    ROUND(((COGS_Cr + PersonnelExpenses_Cr + LogisticsExpenses_Cr + LabOperatingExpenses_Cr + SGAExpenses_Cr) 
           / TotalRevenue_Cr) * 100, 2) AS Total_Opex_Pct,
    EBITDAMargin_Pct
FROM Fact_Financial_Annual
ORDER BY FinancialRecordID;
GO


-- ==============================================================================
-- QUERY 7: Price-Volume Variance Analysis (Top-line Growth Attribution)
-- Objective: Deconstruct quarterly revenue changes into Volume Effect vs Price Effect.
-- ==============================================================================
WITH PeriodMetrics AS (
    SELECT 
        d.DateKey,
        d.FiscalQuarter,
        c.CategoryName,
        SUM(f.TestVolume) AS Qty,
        ROUND(SUM(f.GrossRevenue_INR) / NULLIF(SUM(f.TestVolume), 0), 2) AS UnitPrice,
        ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Revenue_Cr
    FROM Fact_Monthly_Revenues f
    INNER JOIN Dim_Date d ON f.DateKey = d.DateKey
    INNER JOIN Dim_Test_Category c ON f.CategoryID = c.CategoryID
    GROUP BY d.DateKey, d.FiscalQuarter, c.CategoryName
),
VarianceCalc AS (
    SELECT 
        DateKey,
        FiscalQuarter,
        CategoryName,
        Qty,
        LAG(Qty, 1) OVER (PARTITION BY CategoryName ORDER BY DateKey) AS Prior_Qty,
        UnitPrice,
        LAG(UnitPrice, 1) OVER (PARTITION BY CategoryName ORDER BY DateKey) AS Prior_Price,
        Revenue_Cr,
        LAG(Revenue_Cr, 1) OVER (PARTITION BY CategoryName ORDER BY DateKey) AS Prior_Revenue_Cr
    FROM PeriodMetrics
)
SELECT 
    FiscalQuarter,
    CategoryName,
    Revenue_Cr,
    Prior_Revenue_Cr,
    ROUND(Revenue_Cr - Prior_Revenue_Cr, 2) AS Total_Revenue_Variance_Cr,
    -- Volume Effect = (Current Qty - Prior Qty) * Prior Price / 1e7
    ROUND(((Qty - Prior_Qty) * Prior_Price) / 10000000.0, 2) AS Volume_Effect_Cr,
    -- Price Effect = Current Qty * (Current Price - Prior Price) / 1e7
    ROUND((Qty * (UnitPrice - Prior_Price)) / 10000000.0, 2) AS Price_Realization_Effect_Cr
FROM VarianceCalc
WHERE Prior_Qty IS NOT NULL
ORDER BY CategoryName, FiscalQuarter;
GO


-- ==============================================================================
-- QUERY 8: Clinical Quality Control & Operational Risk Analysis
-- Objective: Monitor specimen rejection rates and turnaround times across labs.
-- ==============================================================================
SELECT 
    l.CenterName,
    r.RegionName,
    COUNT(o.OperationID) AS Total_Reporting_Periods,
    SUM(o.SamplesReceived) AS Total_Samples_Received,
    SUM(o.SamplesTested) AS Total_Samples_Tested,
    SUM(o.SamplesRejected) AS Total_Samples_Rejected,
    ROUND((CAST(SUM(o.SamplesRejected) AS DECIMAL(12,2)) / NULLIF(SUM(o.SamplesReceived), 0)) * 100, 3) AS Blended_Rejection_Rate_Pct,
    ROUND(AVG(o.AverageTurnaroundHours), 1) AS Mean_Turnaround_Time_Hours,
    CASE 
        WHEN AVG(o.AverageTurnaroundHours) <= 24.0 THEN 'World-Class Efficiency (TAT <= 24h)'
        WHEN AVG(o.AverageTurnaroundHours) <= 36.0 THEN 'Standard Clinical Benchmark'
        ELSE 'Attention Required: TAT Lag'
    END AS Quality_Assessment
FROM Fact_Lab_Operations o
INNER JOIN Dim_Lab_Center l ON o.CenterID = l.CenterID
INNER JOIN Dim_Region r ON l.RegionID = r.RegionID
GROUP BY l.CenterName, r.RegionName
ORDER BY Blended_Rejection_Rate_Pct ASC;
GO


-- ==============================================================================
-- QUERY 9: Free Cash Flow Conversion & Capital Intensity
-- Objective: Assess conversion of operating EBITDA into free cash flow and Capex intensity.
-- ==============================================================================
SELECT 
    FiscalYear,
    PeriodType,
    EBITDA_Cr,
    OperatingCashFlow_CFO_Cr,
    CapitalExpenditure_Capex_Cr,
    FreeCashFlow_FCFF_Cr,
    ROUND((OperatingCashFlow_CFO_Cr / NULLIF(EBITDA_Cr, 0)) * 100, 2) AS CFO_to_EBITDA_Pct,
    ROUND((FreeCashFlow_FCFF_Cr / NULLIF(EBITDA_Cr, 0)) * 100, 2) AS FCFF_to_EBITDA_Pct,
    ROUND((CapitalExpenditure_Capex_Cr / NULLIF(TotalRevenue_Cr, 0)) * 100, 2) AS Capex_as_Pct_of_Revenue
FROM Fact_Financial_Annual
ORDER BY FinancialRecordID;
GO


-- ==============================================================================
-- QUERY 10: Advanced Genomics (NGS) Penetration Index Across Geographies
-- Objective: Identify regional under-penetration for targeted expansion by Corporate Development.
-- ==============================================================================
WITH RegionalTotal AS (
    SELECT 
        RegionID,
        SUM(GrossRevenue_INR) AS Total_Regional_Rev
    FROM Fact_Monthly_Revenues
    GROUP BY RegionID
),
GenomicsTotal AS (
    SELECT 
        f.RegionID,
        SUM(f.GrossRevenue_INR) AS Genomics_Rev,
        SUM(f.TestVolume) AS Genomics_Volume
    FROM Fact_Monthly_Revenues f
    INNER JOIN Dim_Test_Category c ON f.CategoryID = c.CategoryID
    WHERE c.IsGenomicsSpecialized = 1
    GROUP BY f.RegionID
)
SELECT 
    r.RegionName,
    r.Zone,
    ROUND(rt.Total_Regional_Rev / 10000000.0, 2) AS Total_Revenue_Cr,
    ROUND(COALESCE(gt.Genomics_Rev, 0) / 10000000.0, 2) AS Genomics_Revenue_Cr,
    ROUND((COALESCE(gt.Genomics_Rev, 0) / NULLIF(rt.Total_Regional_Rev, 0)) * 100, 2) AS Genomics_Penetration_Pct,
    COALESCE(gt.Genomics_Volume, 0) AS Genomics_Volume,
    CASE 
        WHEN (COALESCE(gt.Genomics_Rev, 0) / NULLIF(rt.Total_Regional_Rev, 0)) >= 0.40 THEN 'Genomics Dominant'
        WHEN (COALESCE(gt.Genomics_Rev, 0) / NULLIF(rt.Total_Regional_Rev, 0)) >= 0.25 THEN 'Balanced Portfolio'
        ELSE 'High Expansion Opportunity'
    END AS M_and_A_Opportunity_Rating
FROM Dim_Region r
LEFT JOIN RegionalTotal rt ON r.RegionID = rt.RegionID
LEFT JOIN GenomicsTotal gt ON r.RegionID = gt.RegionID
ORDER BY Genomics_Penetration_Pct DESC;
GO


-- ==============================================================================
-- QUERY 11: High-Margin B2B Clinical Research Revenue Concentration
-- Objective: Monitor B2B recurring revenue from global biotech and pharma trials.
-- ==============================================================================
SELECT 
    c.CategoryName,
    r.RegionName,
    SUM(f.TestVolume) AS Contract_Sample_Volume,
    ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Revenue_Cr,
    ROUND(SUM(f.GrossProfit_INR) / 10000000.0, 2) AS Gross_Profit_Cr,
    ROUND(SUM(f.GrossRevenue_INR) / NULLIF(SUM(f.TestVolume), 0), 2) AS ARPT_INR
FROM Fact_Monthly_Revenues f
INNER JOIN Dim_Test_Category c ON f.CategoryID = c.CategoryID
INNER JOIN Dim_Region r ON f.RegionID = r.RegionID
WHERE c.CategoryCode = 'CLN-RES'
GROUP BY c.CategoryName, r.RegionName
ORDER BY Revenue_Cr DESC;
GO


-- ==============================================================================
-- QUERY 12: Operating Leverage Metric (Incremental EBITDA / Incremental Revenue)
-- Objective: Measure fixed cost absorption and operational leverage scaling.
-- ==============================================================================
WITH IncrementalCalc AS (
    SELECT 
        FiscalYear,
        PeriodType,
        TotalRevenue_Cr,
        TotalRevenue_Cr - LAG(TotalRevenue_Cr, 1) OVER (ORDER BY FinancialRecordID) AS Delta_Revenue_Cr,
        EBITDA_Cr,
        EBITDA_Cr - LAG(EBITDA_Cr, 1) OVER (ORDER BY FinancialRecordID) AS Delta_EBITDA_Cr
    FROM Fact_Financial_Annual
)
SELECT 
    FiscalYear,
    PeriodType,
    TotalRevenue_Cr,
    Delta_Revenue_Cr,
    EBITDA_Cr,
    Delta_EBITDA_Cr,
    ROUND((Delta_EBITDA_Cr / NULLIF(Delta_Revenue_Cr, 0)) * 100, 2) AS Incremental_EBITDA_Margin_Pct,
    ROUND((Delta_EBITDA_Cr / NULLIF(LAG(EBITDA_Cr, 1) OVER (ORDER BY FiscalYear), 0)) 
          / NULLIF((Delta_Revenue_Cr / NULLIF(LAG(TotalRevenue_Cr, 1) OVER (ORDER BY FiscalYear), 0)), 0), 2) AS Degree_Of_Operating_Leverage
FROM IncrementalCalc
ORDER BY FiscalYear;
GO


-- ==============================================================================
-- QUERY 13: Laboratory Capacity Utilization & Throughput Efficiency
-- Objective: Calculate daily test runs per sequencing unit to guide Capex timing.
-- ==============================================================================
SELECT 
    l.CenterName,
    l.SequencerCapacityCount,
    SUM(o.SamplesTested) AS Samples_Tested_Reported,
    ROUND(SUM(o.ReagentCost_INR) / NULLIF(SUM(o.SamplesTested), 0), 2) AS Reagent_Cost_Per_Sample_INR,
    ROUND(SUM(o.EquipmentMaintenance_INR) / NULLIF(SUM(o.SamplesTested), 0), 2) AS Maintenance_Cost_Per_Sample_INR,
    CASE 
        WHEN l.SequencerCapacityCount > 0 
        THEN ROUND(CAST(SUM(o.SamplesTested) AS DECIMAL(14,2)) / (l.SequencerCapacityCount * 365.0), 1)
        ELSE NULL 
    END AS Daily_Samples_Per_Sequencer
FROM Fact_Lab_Operations o
INNER JOIN Dim_Lab_Center l ON o.CenterID = l.CenterID
GROUP BY l.CenterName, l.SequencerCapacityCount
ORDER BY Samples_Tested_Reported DESC;
GO


-- ==============================================================================
-- QUERY 14: Cumulative Revenue Run-Rate vs Annual Corporate Target
-- Objective: Running total revenue tracking with window partition.
-- ==============================================================================
SELECT 
    d.FiscalYear,
    d.FiscalQuarter,
    d.FullDate,
    ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Quarter_Revenue_Cr,
    ROUND(SUM(SUM(f.GrossRevenue_INR) / 10000000.0) OVER (
        PARTITION BY d.FiscalYear 
        ORDER BY d.DateKey
    ), 2) AS Cumulative_YTD_Revenue_Cr
FROM Fact_Monthly_Revenues f
INNER JOIN Dim_Date d ON f.DateKey = d.DateKey
GROUP BY d.FiscalYear, d.FiscalQuarter, d.FullDate, d.DateKey
ORDER BY d.DateKey;
GO


-- ==============================================================================
-- QUERY 15: M&A Strategic Synergies: Regional Overlap & Procurement Potential
-- Objective: Simulate Acquirer synergy capture across reagent procurement and volume tiering.
-- ==============================================================================
WITH RegionalProfile AS (
    SELECT 
        r.RegionName,
        SUM(f.TestVolume) AS Target_Volume,
        ROUND(SUM(f.GrossRevenue_INR) / 10000000.0, 2) AS Target_Revenue_Cr,
        ROUND(SUM(f.DirectCOGS_INR) / 10000000.0, 2) AS Target_COGS_Cr
    FROM Fact_Monthly_Revenues f
    INNER JOIN Dim_Region r ON f.RegionID = r.RegionID
    GROUP BY r.RegionName
)
SELECT 
    RegionName,
    Target_Volume,
    Target_Revenue_Cr,
    Target_COGS_Cr,
    -- Synergy Assumption 1: 1.8% Reagent Procurement Discount from Combined Purchasing
    ROUND(Target_COGS_Cr * 0.018, 2) AS Estimated_Annual_Procurement_Synergy_Cr,
    -- Synergy Assumption 2: 5.0% Cross-Selling Revenue Expansion from Acquirer Network
    ROUND(Target_Revenue_Cr * 0.050, 2) AS Potential_CrossSell_Revenue_Cr,
    -- Contribution margin 65% on cross-sold revenue
    ROUND(Target_Revenue_Cr * 0.050 * 0.65, 2) AS EBITDA_from_CrossSelling_Cr
FROM RegionalProfile
ORDER BY Target_Revenue_Cr DESC;
GO

PRINT 'Successfully executed 15 financial analysis queries for HealthcareDiagnosticsDW.';
GO

