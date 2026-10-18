# Superstore End-to-End Analytics Dashboard

An end-to-end business intelligence project that transforms Superstore transactional data into an interactive Power BI report. The workflow combines Python-based data preparation, Microsoft SQL Server, Excel/SQL exploration, and Power BI data modeling and visualization.

## Project at a Glance

| Area | Details |
|---|---|
| Objective | Explore sales, profitability, regional performance, products, and customers |
| Tools | Python, Pandas, SQL Server, SQL, Excel, Power Query, Power BI, DAX |
| Workflow | Prepare data → load and model data → analyze → visualize |
| Dashboard | Executive overview, regional performance, category/product analysis, customer insights |

## Business Questions

This project explores questions such as:

- How do sales and profit change over time?
- Which regions contribute most to sales and profitability?
- Which categories and sub-categories combine high sales with weak or negative profit?
- How are sales distributed across customers, and what does the distribution suggest about customer concentration?
- How can business users investigate performance through interactive filters and drill-downs?

## Workflow

### 1. Data preparation with Python
- Loaded and cleaned the source data.
- Standardized data structures and prepared tables for downstream analysis.

### 2. SQL Server and data modeling
- Loaded prepared data into Microsoft SQL Server using Python.
- Used SQL to explore and validate the data.
- Organized data into fact and dimension tables for analytical reporting.

### 3. Analysis and metrics
- Explored transactional data with SQL and Excel.
- Created Power BI measures for sales, profit, profit margin, repeat customer rate, and average order value.
- Used relationships between fact and dimension tables to support consistent filtering.

### 4. Power BI dashboard
The report contains four analytical views:

1. **Executive Overview** — high-level performance metrics and trends.
2. **Regional Performance** — comparisons across regions and states.
3. **Category & Product Analysis** — product performance and profitability.
4. **Customer Insights** — customer-level sales patterns and contribution.

## Selected Dashboard Metrics

The current project documentation reports the following values. Recalculate them from the final model before using them in a presentation or interview.

| Metric | Reported value |
|---|---:|
| Total sales | $2.30M |
| Total profit | $286.40K |
| Profit margin | 12.47% |
| Total quantity | 38K |
| Unique customers | 793 |
| Average order value | $458.61 |

> **Metric definitions matter:** document the exact DAX formula and filter context for each KPI. In particular, define what counts as an order, a repeat customer, and ROI before interpreting those measures.

## Repository Structure

```text
.
├── Data/
├── Python_Scripts/
├── SQL_Schema/
├── ScreenShots/
├── pbix/
└── README.md
```

Folder names above reflect the current repository layout.

## How to Explore the Project

1. Review the screenshots in `ScreenShots/` for a quick dashboard overview.
2. Read the scripts in `Python_Scripts/` to understand data preparation and loading.
3. Review `SQL_Schema/` to inspect the database design.
4. Open the Power BI report in `pbix/` if you have Power BI Desktop and the required data access.

### Reproducibility Notes

The loading scripts may depend on a local SQL Server configuration. Before running them, review connection settings and replace machine-specific values with your own configuration. Do not commit passwords, access tokens, or other secrets.

## Key Takeaways to Validate

Use the report to investigate whether:

- Certain sub-categories generate sales but weaken overall profitability.
- Results vary meaningfully by region, product, and discount level.
- Revenue is concentrated among a relatively small number of customers.

These are analysis questions, not conclusions that should be accepted without checking the underlying data, definitions, and filters.

## Author

**Shahim Rhahleh** — Data Analyst

- GitHub: [@Shahim04](https://github.com/Shahim04)
- Email: shhmrhahlh8@gmail.com
