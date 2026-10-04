# FinSight 360 — Banking Operations & Risk Intelligence

An end-to-end Data Analytics project that analyzes banking customers, accounts, transactions, fraud alerts, and customer-support data to generate actionable business insights.

## Project Overview

FinSight 360 is a synthetic banking analytics project designed to simulate the work of a Data Analyst in a banking environment.

The project follows a complete analytics workflow:

**Raw Data → Data Validation → SQL Analysis → Python EDA → Tableau Dashboard → Business Insights → Business Recommendations**

The objective is to demonstrate how raw operational data can be transformed into meaningful information that supports data-driven business decisions.

## Business Problem

Banks generate large volumes of data through customer accounts, financial transactions, branch operations, fraud monitoring, and customer-support activities.

Simply storing this data is not enough. Businesses need to understand:

- How customers are using different transaction channels
- Which transaction types have the highest activity
- How much transaction value is being generated
- How many transactions succeed, fail, or get reversed
- How transaction activity changes over time
- What patterns exist in fraud alerts
- Which customer-support areas require attention
- Whether the underlying data is complete and reliable

FinSight 360 addresses these requirements through SQL analysis, Python-based exploratory data analysis, and Tableau visualization.

## Project Objectives

The main objectives of the project are:

- Analyze customer and account information
- Study transaction volume and transaction value
- Identify the most frequently used transaction types
- Measure transaction success and failure rates
- Analyze monthly transaction trends
- Analyze customer segments
- Evaluate branch-level performance
- Analyze fraud alerts and severity
- Analyze customer-support activity
- Identify data-quality and record-count discrepancies
- Build visualizations that communicate important findings
- Convert analytical results into business recommendations

## Dataset

The project uses synthetic banking datasets representing realistic banking operations.

The datasets include:

1. Customers
2. Accounts
3. Branches
4. Transactions
5. Fraud Alerts
6. Support Tickets

### Dataset Size

- Customers — 5,000 records
- Accounts — 6,500 records
- Branches — 20 records
- Transactions — 50,035 source records
- Support Tickets — 8,000 records
- Fraud Alerts — 2,500 source records

The transaction and fraud-alert source counts are intentionally compared with the records imported into MySQL as part of the data-quality validation process.

## Technologies Used

- **MySQL** — Database creation, data import, validation and SQL analysis
- **SQL** — Business analysis and aggregation
- **Python** — Exploratory Data Analysis and data processing
- **Pandas** — Data manipulation and cleaning
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Tableau** — Business intelligence dashboard
- **GitHub** — Version control and project documentation

## Project Workflow

The project follows an end-to-end Data Analyst workflow:

### 1. Data Collection

Synthetic banking datasets were prepared for customers, accounts, branches, transactions, fraud alerts and support tickets.

### 2. Data Understanding

The datasets were inspected to understand:

- Number of records
- Available columns
- Data types
- Relationships between datasets
- Missing values
- Duplicate records
- Important business fields

### 3. Database Creation

A MySQL database named `finsight360` was created.

The database contains six major tables:

- `customers`
- `accounts`
- `branches`
- `transactions`
- `fraud_alerts`
- `support_tickets`

Relationships between these tables allow customer, account, transaction, fraud and support information to be analyzed together.

### 4. Data Validation

The imported data was checked for:

- Missing values
- Duplicate records
- Duplicate transaction IDs
- Invalid transaction records
- Date formatting
- Record-count consistency
- Source CSV versus database record counts

### 5. SQL Analysis

SQL was used to answer business questions using:

- `SELECT`
- `WHERE`
- `GROUP BY`
- `ORDER BY`
- `COUNT()`
- `SUM()`
- `AVG()`
- `ROUND()`
- Filtering
- Table relationships
- Aggregation

### 6. Python Analysis

Python and Pandas were used for exploratory data analysis.

The Python workflow included:

- Loading CSV files
- Inspecting datasets
- Checking dimensions
- Checking missing values
- Checking duplicates
- Converting transaction dates
- Cleaning invalid records
- Calculating KPIs
- Analyzing transaction types
- Analyzing transaction statuses
- Studying monthly trends
- Analyzing customer segments
- Exploring fraud data
- Exploring support data
- Creating visualizations

### 7. Tableau Dashboard

Tableau was used to convert analytical results into an interactive business dashboard.

The dashboard contains:

- Transaction Volume
- Transaction Value
- Transaction Status
- Monthly Transaction Trend

### 8. Business Insights

The final stage was to interpret the analysis and convert numerical findings into useful business insights and recommendations.

## SQL Analysis

The SQL analysis covered multiple areas of banking operations.

### Customer Analysis

Customer records were analyzed to understand the customer base and available customer segments.

### Customer Segmentation

Customer segments were analyzed to understand differences in customer activity.

### Account Analysis

Account types were analyzed to understand the distribution of banking products.

### Transaction Analysis

Transactions were analyzed by:

- Transaction type
- Transaction volume
- Transaction value
- Average transaction value
- Transaction status
- Channel
- Time period

### Branch Analysis

Branch-level transaction activity was analyzed to identify differences in operational performance.

### Fraud Analysis

Fraud alerts were analyzed based on:

- Fraud activity
- Severity
- Risk type

### Customer Support Analysis

Support tickets were analyzed to understand customer issues and support priorities.

## Python Analysis

Python was used as the exploratory analysis layer of the project.

Pandas provided the main data manipulation functionality.

The analysis included:

### Data Inspection

The datasets were loaded and inspected to understand their structure and dimensions.

### Data Quality

Missing values and duplicate records were checked before performing analysis.

### Data Cleaning

Transaction dates were converted into appropriate date formats and invalid or incomplete transaction records were handled during the analysis.

### KPI Analysis

Important transaction KPIs were calculated, including:

- Total transactions
- Total transaction value
- Average transaction value
- Transaction status distribution

### Trend Analysis

Transaction activity was grouped by month to identify changes in transaction volume over time.

### Visualization

Matplotlib was used to create charts for important transaction patterns and distributions.

## Tableau Dashboard

The Tableau dashboard is titled:

**FinSight 360 — Banking Transaction Intelligence**

The dashboard provides a management-level view of transaction activity.

It contains four major analytical views:

### Transaction Volume

Shows transaction counts across transaction types.

### Transaction Value

Shows the total financial value associated with transaction types.

### Transaction Status

Shows the distribution of successful, failed and reversed transactions.

### Monthly Transaction Trend

Shows how transaction activity changes over time.

## Key Findings

### Transaction Volume

UPI recorded the highest transaction volume with:

**14,033 transactions**

This indicates strong usage of digital payment channels in the synthetic banking dataset.

### Transaction Value

UPI also generated the highest total transaction value:

**₹42,017,108.28**

Card transactions generated approximately:

**₹29,864,652.52**

### Transaction Status

The MySQL database contained:

**49,915 transactions**

Among them:

- Successful — 46,955
- Failed — 1,983
- Reversed — 977

The successful transaction rate was approximately:

**94%**

### Data Quality Findings

The source transaction CSV contained:

**50,035 records**

while the MySQL database contained:

**49,915 records**

This represents a difference of:

**120 records**

The source fraud-alert dataset contained:

**2,500 records**

while MySQL contained:

**2,492 records**

This represents a difference of:

**8 records**

These differences were documented as data-quality/import discrepancies rather than being ignored.

## Business Recommendations

### 1. Improve Digital Payment Reliability

UPI represents a major portion of transaction activity. Monitoring UPI transaction performance and failure patterns can help improve customer experience.

### 2. Monitor Failed Transactions

Failed transactions should be monitored by transaction type, channel and time period to identify recurring operational issues.

### 3. Strengthen Risk Monitoring

Fraud alerts can be analyzed by severity and risk type to help prioritize potentially high-risk activities.

### 4. Improve Customer Support

Support tickets can be analyzed by issue type and priority to identify recurring customer problems and improve service quality.

### 5. Monitor Transaction Trends

Monthly transaction trends can help business teams understand changes in customer behavior and plan operational resources.

### 6. Strengthen Data Validation

Differences between source files and database records demonstrate the importance of validating data during data ingestion and ETL processes.

## Data Quality Validation

Data quality is an important part of the project.

The following checks were performed:

- Missing-value checks
- Duplicate checks
- Transaction ID validation
- Date validation
- Record-count validation
- Source-versus-database comparison

The project demonstrates that data analysis is not only about creating charts. Reliable analysis depends on ensuring that the underlying data is valid and consistent.

## Project Structure

```text
FinSight360/
│
├── data/
│   └── raw/
│
├── documentation/
│   ├── business_questions.md
│   ├── data_dictionary.csv
│   ├── README_STARTER.md
│   ├── methodology.md
│   └── insights.md
│
├── python/
│   └── finsight360_analysis.py
│
├── sql/
│   └── 01_create_schema.sql
│
├── screenshots/
│
├── tableau/
│   └── FinSight360_Banking_Analytics.twbx
│
└── README.md
Project Deliverables
The project includes:
- Raw banking datasets
- MySQL database schema
- SQL analysis
- Python exploratory analysis
- Python visualizations
- Tableau dashboard
- Tableau workbook
- Data dictionary
- Business questions
- Methodology documentation
- Business insights documentation
- GitHub repository
Skills Demonstrated
This project demonstrates practical skills in:
- Data Analysis
- SQL
- MySQL
- Python
- Pandas
- Exploratory Data Analysis
- Data Cleaning
- Data Validation
- Data Visualization
- Tableau
- Business Intelligence
- KPI Analysis
- Business Problem Solving
- GitHub
- Business Communication


What This Project Demonstrates
FinSight 360 demonstrates a practical Data Analyst workflow rather than focusing only on technical tools.

The project shows how to:
Understand the business problem → Understand the data → Validate the data → Analyze the data → Visualize the results → Identify insights → Recommend business actions
This mirrors the type of workflow used in real-world analytics environments.
Business Value

FinSight 360 can support business teams by providing insights into:
- Customer activity
- Transaction performance
- Digital payment usage
- Operational issues
- Fraud monitoring
- Customer support
- Data quality


The project demonstrates how analytical findings can support data-driven decision-making.
Project Status
Completed

Author

Chiranthan S
Information Science & Engineering
Jawaharlal Nehru New College of Engineering (JNNCE), Shivamogga, Karnataka


Conclusion


FinSight 360 demonstrates an end-to-end banking analytics workflow using SQL, Python and Tableau.
The project begins with raw operational datasets, validates and analyzes the data using SQL and Python, and presents the results through a Tableau dashboard.
The final outcome is a portfolio project that demonstrates practical Data Analyst skills including data cleaning, SQL analysis, exploratory data analysis, visualization, business intelligence and insight generation.
