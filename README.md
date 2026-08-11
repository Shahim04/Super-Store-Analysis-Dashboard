# Superstore End-to-End Data Pipeline & Executive Analytics Dashboard

A comprehensive end-to-end business intelligence project analyzing sales, profitability, customer segmentation, and regional performance for the Superstore dataset. The project demonstrates an complete ETL pipeline starting from raw data ingestion to database modeling and interactive visual reporting.

---

## 📋 Executive Summary

This project transforms raw transactional data into actionable operational insights. By leveraging **Python**, **SQL Server**, **Power Query Editor**, and **Power BI**, the resulting four-page dynamic dashboard enables stakeholders to trace revenue growth, analyze discount impacts on margins, identify top-value customers, and pinpoint underperforming product categories across geographic markets.

---

## 🛠 Tech Stack & Tools

* **Data Processing & ETL:** Python (`pandas`, `sqlalchemy`), Excel, Power Query Editor
* **Database & Storage:** Microsoft SQL Server
* **Data Visualization:** Power BI (DAX, Interactive Slicers, Custom Page Navigation)
* **Documentation & Version Control:** Git, Markdown

---

## ⚙️ Data Architecture & Pipeline Steps

1. **Data Ingestion & Cleaning:**
   * Ingested raw Excel datasets containing order details, shipping information, customer segments, and regional hierarchy.
   * Standardized schema types, fixed missing attributes, and verified cross-table normalization rules.

2. **Database Ingestion & Schema Transformation (Python & SQL):**
   * Built an ETL pipeline script (`python_Scripts`) leveraging **SQLAlchemy** and **Pandas** to programmatically push clean transaction data into an **MS SQL Server** instance.
   * De-normalized flat tables into a optimized **Star Schema** relational design using SQL scripts (`SQL_Schema`) to separate transactional events from core business dimensions.

3. **Data Modeling & DAX (Power Query & Power BI):**
   * Imported schema tables into Power BI and validated `1:N` single-direction relationships across dimensions and the fact table.
   * Transformed dynamic parameters using **Power Query Editor**.
   * Formulated DAX measures for core KPIs: Total Sales, Total Profit, Profit Margin %, Repeat Customer Rate %, and Average Order Value (AOV).
---

## 📊 Dashboard Overview

The dashboard comprises **four distinct view pages**, styled with a custom high-contrast executive theme and custom icon navigation:

### 1. Executive Summary (Home Page)
Provides a high-level strategic snapshot of aggregate business health across years and product divisions.
* **Key Metrics:** Total Sales ($2.30M), Total Quantity (38K), Total Profit ($286.40K), Profit Margin % (12.47%).
* **Visual Highlights:** Multi-year trend analysis, sales distribution by category, and regional profit distribution.

![Home Page](C:\Users\ASUS\Desktop\ScreenShots\Home.png)

---

### 2. Regional Performance
Breaks down revenue, orders, and shipping mode preferences across 4 primary regions and 49 states.
* **Key Insights:** Identifies California and New York as primary revenue drivers; evaluates profit margins by state map boundaries and ship mode volume.

![Regions Page](docs/screenshots/Regions.jpg)

---

### 3. Category & Product Performance
Delivers deep granularity on product performance, discount sensitivities, and line-item profitability.
* **Key Insights:** Highlights high-volume items vs. margin-draining categories (e.g., negative profit lines in select sub-categories).

![Category Page](docs/screenshots/Category.jpg)

---

### 4. Customer Analysis
Monitors buyer trends, order frequencies, and customer lifetime concentration.
* **Key Metrics:** Total Unique Customers (793), Average Sales per Customer ($2.90K), Top Customer Revenue ($25.04K), Average Order Value ($458.61).
* **Visual Highlights:** Top 5 customers by profit, decomposition trees for profit origin, and state breakdown per segment.

![Customer Page](docs/screenshots/Customer.png)
## ✉️ Author
* **Developer:** Shahm
* **Contact:** [shhmrhahlh8@gmail.com](mailto:shhmrhahlh8@gmail.com)
