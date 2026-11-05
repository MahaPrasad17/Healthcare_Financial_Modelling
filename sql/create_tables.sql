-- ==============================================================================
-- PROJECT: Healthcare Diagnostics Financial Modelling & M&A Valuation
-- TARGET ENTITY: AuraGen Diagnostics Ltd.
-- FILE: create_tables.sql
-- DIALECT: Microsoft SQL Server (T-SQL)
-- DATA CLASSIFICATION: Synthetic Financial & Operational Benchmark Data
-- NOTICE: All financial records, test counts, metrics, and operational data
--         contained herein are simulated benchmarks compiled for financial
--         modelling, M&A valuation, and diagnostic analytics case studies.
-- OBJECTIVE: Establishes the Relational Star Schema for Diagnostics Financial,
--            Operational, and Segment Reporting.
-- ==============================================================================

-- 1. Create Database (Conditional Execution)
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'HealthcareDiagnosticsDW')
BEGIN
    CREATE DATABASE HealthcareDiagnosticsDW;
END
GO

USE HealthcareDiagnosticsDW;
GO

-- 2. Drop Existing Tables in Reverse Dependency Order
DROP TABLE IF EXISTS Fact_Lab_Operations;
DROP TABLE IF EXISTS Fact_Monthly_Revenues;
DROP TABLE IF EXISTS Fact_Financial_Annual;
DROP TABLE IF EXISTS Dim_Lab_Center;
DROP TABLE IF EXISTS Dim_Test_Category;
DROP TABLE IF EXISTS Dim_Region;
DROP TABLE IF EXISTS Dim_Date;
GO

-- ==============================================================================
-- DIMENSION TABLES
-- ==============================================================================

-- Dim_Date: Master Calendar Dimension
CREATE TABLE Dim_Date (
    DateKey INT PRIMARY KEY,                       -- Format: YYYYMMDD
    FullDate DATE NOT NULL,
    CalendarYear INT NOT NULL,
    CalendarQuarter INT NOT NULL,
    MonthNumber INT NOT NULL,
    MonthName NVARCHAR(20) NOT NULL,
    FiscalYear NVARCHAR(10) NOT NULL,              -- e.g. 'FY2021', 'FY2022'
    FiscalQuarter NVARCHAR(10) NOT NULL            -- e.g. 'FY21-Q1'
);
GO

-- Dim_Region: Geographic Hubs and Zones
CREATE TABLE Dim_Region (
    RegionID INT IDENTITY(1,1) PRIMARY KEY,
    RegionCode NVARCHAR(10) NOT NULL UNIQUE,       -- e.g. 'REG-SO', 'REG-WE'
    RegionName NVARCHAR(50) NOT NULL,              -- 'South Hub', 'West Hub'
    Zone NVARCHAR(30) NOT NULL,                    -- 'Domestic South', 'International'
    TierClassification NVARCHAR(20) NOT NULL,      -- 'Metro Tier-1', 'Tier-2 Hub'
    RegionalHeadquarters NVARCHAR(50) NOT NULL     -- 'Bangalore', 'Mumbai', 'Delhi'
);
GO

-- Dim_Test_Category: Diagnostic Modalities and Clinical Segments
CREATE TABLE Dim_Test_Category (
    CategoryID INT IDENTITY(1,1) PRIMARY KEY,
    CategoryCode NVARCHAR(10) NOT NULL UNIQUE,     -- 'GEN-NGS', 'MOL-INF', 'ROU-BIO', 'CLN-RES'
    CategoryName NVARCHAR(80) NOT NULL,            -- 'Genomics & Next-Generation Sequencing'
    ClinicalSpecialty NVARCHAR(50) NOT NULL,       -- 'Oncology & Rare Diseases', 'Biochemistry'
    MarginTier NVARCHAR(20) NOT NULL,              -- 'Super-Premium', 'High-Margin', 'Standard'
    TargetTurnaroundHours INT NOT NULL,            -- Standard Benchmark TAT in Hours
    IsGenomicsSpecialized BIT NOT NULL DEFAULT 0   -- Flag for Specialized Genomics
);
GO

-- Dim_Lab_Center: Laboratory Infrastructure and Network Footprint
CREATE TABLE Dim_Lab_Center (
    CenterID INT IDENTITY(1,1) PRIMARY KEY,
    CenterCode NVARCHAR(20) NOT NULL UNIQUE,
    CenterName NVARCHAR(100) NOT NULL,
    CenterType NVARCHAR(40) NOT NULL,              -- 'Central Reference Hub', 'Regional Lab (RPL)', 'Patient Service Center (PSC)'
    RegionID INT NOT NULL FOREIGN KEY REFERENCES Dim_Region(RegionID),
    AccreditationStatus NVARCHAR(50) NOT NULL,     -- 'NABL & CAP Accredited', 'NABL Accredited'
    SequencerCapacityCount INT NOT NULL DEFAULT 0, -- Number of high-throughput sequencers installed
    CommissionedYear INT NOT NULL
);
GO

-- ==============================================================================
-- FACT TABLES
-- ==============================================================================

-- Fact_Financial_Annual: High-Level Audited & Projected Corporate Financials
CREATE TABLE Fact_Financial_Annual (
    FinancialRecordID INT IDENTITY(1,1) PRIMARY KEY,
    FiscalYear NVARCHAR(10) NOT NULL UNIQUE,
    PeriodType NVARCHAR(20) NOT NULL,              -- 'Historical Actual' or 'Financial Forecast'
    TotalRevenue_Cr DECIMAL(14,2) NOT NULL,
    COGS_Cr DECIMAL(14,2) NOT NULL,
    GrossProfit_Cr DECIMAL(14,2) NOT NULL,
    GrossMargin_Pct DECIMAL(6,2) NOT NULL,
    PersonnelExpenses_Cr DECIMAL(14,2) NOT NULL,
    LogisticsExpenses_Cr DECIMAL(14,2) NOT NULL,
    LabOperatingExpenses_Cr DECIMAL(14,2) NOT NULL,
    SGAExpenses_Cr DECIMAL(14,2) NOT NULL,
    EBITDA_Cr DECIMAL(14,2) NOT NULL,
    EBITDAMargin_Pct DECIMAL(6,2) NOT NULL,
    DepreciationAmortization_Cr DECIMAL(14,2) NOT NULL,
    EBIT_Cr DECIMAL(14,2) NOT NULL,
    InterestExpense_Cr DECIMAL(14,2) NOT NULL,
    OtherIncome_Cr DECIMAL(14,2) NOT NULL,
    EBT_Cr DECIMAL(14,2) NOT NULL,
    TaxExpense_Cr DECIMAL(14,2) NOT NULL,
    NetProfit_PAT_Cr DECIMAL(14,2) NOT NULL,
    NetProfitMargin_Pct DECIMAL(6,2) NOT NULL,
    OperatingCashFlow_CFO_Cr DECIMAL(14,2) NOT NULL,
    CapitalExpenditure_Capex_Cr DECIMAL(14,2) NOT NULL,
    FreeCashFlow_FCFF_Cr DECIMAL(14,2) NOT NULL,
    CashAndEquivalents_Cr DECIMAL(14,2) NOT NULL,
    TotalDebt_Cr DECIMAL(14,2) NOT NULL,
    ShareholdersEquity_Cr DECIMAL(14,2) NOT NULL
);
GO

-- Fact_Monthly_Revenues: Granular Transaction & Segment Revenue Performance
CREATE TABLE Fact_Monthly_Revenues (
    RevenueID BIGINT IDENTITY(1,1) PRIMARY KEY,
    DateKey INT NOT NULL FOREIGN KEY REFERENCES Dim_Date(DateKey),
    CategoryID INT NOT NULL FOREIGN KEY REFERENCES Dim_Test_Category(CategoryID),
    RegionID INT NOT NULL FOREIGN KEY REFERENCES Dim_Region(RegionID),
    CenterID INT NOT NULL FOREIGN KEY REFERENCES Dim_Lab_Center(CenterID),
    TestVolume INT NOT NULL CHECK (TestVolume >= 0),
    GrossRevenue_INR DECIMAL(18,2) NOT NULL,
    DirectCOGS_INR DECIMAL(18,2) NOT NULL,
    GrossProfit_INR AS (GrossRevenue_INR - DirectCOGS_INR) PERSISTED,
    AvgRealizationPerTest_INR AS (CASE WHEN TestVolume > 0 THEN GrossRevenue_INR / TestVolume ELSE 0 END) PERSISTED
);
GO

-- Fact_Lab_Operations: Quality Assurance, Sample TAT, and Efficiency Metrics
CREATE TABLE Fact_Lab_Operations (
    OperationID BIGINT IDENTITY(1,1) PRIMARY KEY,
    DateKey INT NOT NULL FOREIGN KEY REFERENCES Dim_Date(DateKey),
    CenterID INT NOT NULL FOREIGN KEY REFERENCES Dim_Lab_Center(CenterID),
    SamplesReceived INT NOT NULL,
    SamplesTested INT NOT NULL,
    SamplesRejected INT NOT NULL,
    RejectionRate_Pct AS (CASE WHEN SamplesReceived > 0 THEN (CAST(SamplesRejected AS DECIMAL(10,4)) / SamplesReceived) * 100 ELSE 0 END) PERSISTED,
    AverageTurnaroundHours DECIMAL(6,2) NOT NULL,
    ReagentCost_INR DECIMAL(16,2) NOT NULL,
    EquipmentMaintenance_INR DECIMAL(16,2) NOT NULL
);
GO

-- ==============================================================================
-- INDEXING STRATEGY FOR QUERY PERFORMANCE
-- ==============================================================================
CREATE NONCLUSTERED INDEX IX_FactMonthlyRevenues_Date_Category 
ON Fact_Monthly_Revenues (DateKey, CategoryID) 
INCLUDE (TestVolume, GrossRevenue_INR, DirectCOGS_INR);

CREATE NONCLUSTERED INDEX IX_FactMonthlyRevenues_Region_Center 
ON Fact_Monthly_Revenues (RegionID, CenterID) 
INCLUDE (GrossRevenue_INR, TestVolume);

CREATE NONCLUSTERED INDEX IX_FactLabOps_Center_Date 
ON Fact_Lab_Operations (CenterID, DateKey) 
INCLUDE (RejectionRate_Pct, AverageTurnaroundHours);
GO

-- ==============================================================================
-- SEED DATA INSERTION
-- ==============================================================================

-- 1. Insert Dimensions: Regions
INSERT INTO Dim_Region (RegionCode, RegionName, Zone, TierClassification, RegionalHeadquarters) VALUES
('REG-SO', 'South Hub (HQ)', 'South India', 'Tier-1 Metro Hub', 'Bangalore'),
('REG-WE', 'West Hub', 'West India', 'Tier-1 Metro Hub', 'Mumbai'),
('REG-NO', 'North Hub', 'North India', 'Tier-1 Metro Hub', 'New Delhi / NCR'),
('REG-EA', 'East Hub', 'East India', 'Tier-2 Emerging', 'Kolkata'),
('REG-IN', 'International Markets', 'Global Exports', 'Cross-Border', 'Dubai / Singapore');

-- 2. Insert Dimensions: Categories
INSERT INTO Dim_Test_Category (CategoryCode, CategoryName, ClinicalSpecialty, MarginTier, TargetTurnaroundHours, IsGenomicsSpecialized) VALUES
('ROU-BIO', 'Routine Biochemistry & Hematology', 'General Health & Routine Pathology', 'Standard Volume', 12, 0),
('MOL-INF', 'Molecular & Infectious Pathology', 'Virology, PCR & Infectious Disease', 'High-Margin', 24, 0),
('GEN-NGS', 'Genomics & Next-Generation Sequencing', 'Oncology, NIPT & Rare Genetic Diseases', 'Super-Premium', 48, 1),
('CLN-RES', 'Clinical Research & Pharma Biomarkers', 'Pharma Drug Trials & Genome Biobanking', 'High-Margin B2B', 72, 1);

-- 3. Insert Dimensions: Lab Centers
INSERT INTO Dim_Lab_Center (CenterCode, CenterName, CenterType, RegionID, AccreditationStatus, SequencerCapacityCount, CommissionedYear) VALUES
('LAB-BLR-01', 'AuraGen Central Reference Genomic Lab', 'Central Reference Hub', 1, 'NABL & CAP Accredited', 8, 2018),
('LAB-MUM-01', 'West India Regional Sequencing Center', 'Regional Lab (RPL)', 2, 'NABL & CAP Accredited', 4, 2020),
('LAB-DEL-01', 'North Capital Diagnostic Center', 'Regional Lab (RPL)', 3, 'NABL Accredited', 3, 2021),
('LAB-KOL-01', 'Eastern Diagnostic Processing Hub', 'Regional Lab (RPL)', 4, 'NABL Accredited', 2, 2022),
('LAB-DXB-01', 'International Specimen Receiving Center', 'Patient Service Center (PSC)', 5, 'ISO 15189 Certified', 0, 2023);

-- 4. Insert Master Annual Financial Facts (FY21 - FY24 Actuals, FY25E - FY29E Forecast)
INSERT INTO Fact_Financial_Annual (
    FiscalYear, PeriodType, TotalRevenue_Cr, COGS_Cr, GrossProfit_Cr, GrossMargin_Pct,
    PersonnelExpenses_Cr, LogisticsExpenses_Cr, LabOperatingExpenses_Cr, SGAExpenses_Cr,
    EBITDA_Cr, EBITDAMargin_Pct, DepreciationAmortization_Cr, EBIT_Cr, InterestExpense_Cr,
    OtherIncome_Cr, EBT_Cr, TaxExpense_Cr, NetProfit_PAT_Cr, NetProfitMargin_Pct,
    OperatingCashFlow_CFO_Cr, CapitalExpenditure_Capex_Cr, FreeCashFlow_FCFF_Cr,
    CashAndEquivalents_Cr, TotalDebt_Cr, ShareholdersEquity_Cr
) VALUES
('FY2021', 'Historical Actual', 245.00,  81.50, 163.50, 66.73,  48.00, 21.00, 12.50,  9.00,  73.00, 29.80, 16.00,  57.00, 4.50, 1.50,  54.00, 13.59,  40.41, 16.49,  55.41, 28.00,  27.41,  35.00, 52.00, 185.00),
('FY2022', 'Historical Actual', 312.00, 101.40, 210.60, 67.50,  60.00, 26.50, 15.50, 11.60,  97.00, 31.09, 20.50,  76.50, 4.80, 2.10,  73.80, 18.58,  55.22, 17.70,  74.22, 34.00,  40.22,  52.00, 50.00, 240.22),
('FY2023', 'Historical Actual', 395.00, 124.80, 270.20, 68.41,  74.50, 33.20, 19.80, 14.70, 128.00, 32.41, 26.00, 102.00, 5.20, 2.80,  99.60, 25.07,  74.53, 18.87,  98.53, 42.00,  56.53,  78.00, 48.00, 314.75),
('FY2024', 'Historical Actual', 498.00, 154.40, 343.60, 69.00,  91.00, 41.80, 24.80, 18.50, 167.50, 33.63, 32.00, 135.50, 5.50, 3.50, 133.50, 33.60,  99.90, 20.06, 129.90, 48.00,  81.90, 110.00, 45.00, 414.65),
('FY2025E','Financial Forecast', 607.56, 182.27, 425.29, 70.00, 106.32, 48.60, 30.38, 21.26, 206.57, 34.00, 39.00, 167.57, 4.05, 4.00, 167.52, 42.16, 125.36, 20.63, 151.00, 45.00, 104.89, 145.00, 40.00, 538.28),
('FY2026E','Financial Forecast', 732.11, 219.63, 512.48, 70.00, 128.12, 58.57, 36.61, 25.62, 252.58, 34.50, 46.00, 206.58, 3.60, 4.50, 207.48, 52.22, 155.26, 21.21, 178.50, 50.00, 134.08, 188.00, 35.00, 688.54),
('FY2027E','Financial Forecast', 871.21, 261.36, 609.85, 70.00, 152.46, 69.70, 43.56, 30.49, 304.92, 35.00, 53.00, 251.92, 3.15, 5.00, 253.77, 63.87, 189.90, 21.80, 207.20, 55.00, 168.51, 238.00, 30.00, 873.44),
('FY2028E','Financial Forecast',1023.67, 307.10, 716.57, 70.00, 179.14, 81.89, 51.18, 35.83, 363.40, 35.50, 60.00, 303.40, 2.70, 5.50, 306.20, 77.07, 229.13, 22.38, 237.50, 58.00, 209.53, 295.00, 25.00, 1097.57),
('FY2029E','Financial Forecast',1187.46, 356.24, 831.22, 70.00, 207.81, 95.00, 59.37, 41.56, 427.49, 36.00, 67.00, 360.49, 2.25, 6.00, 364.24, 91.68, 272.56, 22.95, 269.20, 60.00, 256.25, 360.00, 20.00, 1365.13);

-- 5. Insert Date Dimension (Quarterly Calendar Dates FY21 - FY24)
INSERT INTO Dim_Date (DateKey, FullDate, CalendarYear, CalendarQuarter, MonthNumber, MonthName, FiscalYear, FiscalQuarter) VALUES
(20210331, '2021-03-31', 2021, 1, 3, 'March', 'FY2021', 'FY21-Q4'),
(20210630, '2021-06-30', 2021, 2, 6, 'June', 'FY2022', 'FY22-Q1'),
(20210930, '2021-09-30', 2021, 3, 9, 'September', 'FY2022', 'FY22-Q2'),
(20211231, '2021-12-31', 2021, 4, 12, 'December', 'FY2022', 'FY22-Q3'),
(20220331, '2022-03-31', 2022, 1, 3, 'March', 'FY2022', 'FY22-Q4'),
(20220630, '2022-06-30', 2022, 2, 6, 'June', 'FY2023', 'FY23-Q1'),
(20220930, '2022-09-30', 2022, 3, 9, 'September', 'FY2023', 'FY23-Q2'),
(20221231, '2022-12-31', 2022, 4, 12, 'December', 'FY2023', 'FY23-Q3'),
(20230331, '2023-03-31', 2023, 1, 3, 'March', 'FY2023', 'FY23-Q4'),
(20230630, '2023-06-30', 2023, 2, 6, 'June', 'FY2024', 'FY24-Q1'),
(20230930, '2023-09-30', 2023, 3, 9, 'September', 'FY2024', 'FY24-Q2'),
(20231231, '2023-12-31', 2023, 4, 12, 'December', 'FY2024', 'FY24-Q3'),
(20240331, '2024-03-31', 2024, 1, 3, 'March', 'FY2024', 'FY24-Q4');

-- 6. Insert Representative Monthly/Quarterly Revenue Facts
INSERT INTO Fact_Monthly_Revenues (DateKey, CategoryID, RegionID, CenterID, TestVolume, GrossRevenue_INR, DirectCOGS_INR) VALUES
(20230331, 3, 1, 1, 28000, 392000000.00, 109760000.00), -- Genomics in Bangalore Reference Lab
(20230331, 2, 1, 1, 115000, 241500000.00, 79695000.00),  -- Molecular in Bangalore
(20230331, 1, 1, 1, 620000, 341000000.00, 132990000.00), -- Routine in South
(20230331, 4, 1, 1, 2900, 160000000.00, 35200000.00),    -- Clinical Research in South
(20231231, 3, 2, 2, 18500, 260850000.00, 73038000.00),   -- Genomics in Mumbai
(20231231, 2, 2, 2, 85000, 180200000.00, 59466000.00),   -- Molecular in Mumbai
(20240331, 3, 1, 1, 36000, 507600000.00, 142128000.00),  -- FY24 Q4 Genomics Bangalore
(20240331, 3, 2, 2, 25000, 352500000.00, 98700000.00),   -- FY24 Q4 Genomics Mumbai
(20240331, 3, 3, 3, 14500, 204450000.00, 57246000.00),   -- FY24 Q4 Genomics Delhi
(20240331, 4, 1, 1, 3800, 214000000.00, 47080000.00);    -- FY24 Q4 Clinical Research

-- 7. Insert Lab Operational Facts
INSERT INTO Fact_Lab_Operations (DateKey, CenterID, SamplesReceived, SamplesTested, SamplesRejected, AverageTurnaroundHours, ReagentCost_INR, EquipmentMaintenance_INR) VALUES
(20230331, 1, 850000, 843200, 6800, 31.5, 320000000.00, 18500000.00),
(20230331, 2, 420000, 415800, 4200, 33.2, 165000000.00, 9800000.00),
(20231231, 1, 940000, 934500, 5500, 26.8, 385000000.00, 21000000.00),
(20231231, 2, 480000, 476160, 3840, 28.1, 195000000.00, 11200000.00),
(20240331, 1, 1050000, 1044750, 5250, 24.2, 440000000.00, 24500000.00),
(20240331, 2, 530000, 526820, 3180, 25.5, 220000000.00, 12800000.00);
GO

PRINT 'Successfully created tables, indexes, and populated seed data for HealthcareDiagnosticsDW.';
GO

