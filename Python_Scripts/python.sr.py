import pandas as pd
from sqlalchemy import create_engine, text
import urllib

# 1. Load raw data from Excel/CSV
df = pd.read_csv(r"C:\Users\ASUS\Desktop\Superstore.xlsx")

# Clean up column names
df.columns = df.columns.str.strip()

# 2. MSSQL Connection Setup
SERVER = 'DESKTOP-28092IC'
DATABASE = 'Project'
DRIVER = 'ODBC Driver 17 for SQL Server'

# Windows Authentication connection string:
params = urllib.parse.quote_plus(
    f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 3. Create Tables Schema (DDL for MSSQL)
create_tables_sql = """
IF OBJECT_ID('dbo.Fact_Sales', 'U') IS NOT NULL DROP TABLE dbo.Fact_Sales;
IF OBJECT_ID('dbo.Dim_Customer', 'U') IS NOT NULL DROP TABLE dbo.Dim_Customer;
IF OBJECT_ID('dbo.Dim_Product', 'U') IS NOT NULL DROP TABLE dbo.Dim_Product;
IF OBJECT_ID('dbo.Dim_Location', 'U') IS NOT NULL DROP TABLE dbo.Dim_Location;
IF OBJECT_ID('dbo.Dim_Order', 'U') IS NOT NULL DROP TABLE dbo.Dim_Order;

CREATE TABLE Dim_Customer (
    Customer_ID VARCHAR(50) PRIMARY KEY,
    Customer_Name NVARCHAR(100),
    Segment VARCHAR(50)
);

CREATE TABLE Dim_Product (
    Product_ID VARCHAR(50) PRIMARY KEY,
    Product_Name NVARCHAR(255),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50)
);

CREATE TABLE Dim_Location (
    Postal_Code VARCHAR(20) PRIMARY KEY,
    City NVARCHAR(100),
    State NVARCHAR(100),
    Region VARCHAR(50),
    Country NVARCHAR(100)
);

CREATE TABLE Dim_Order (
    Order_ID VARCHAR(50) PRIMARY KEY,
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(50)
);

CREATE TABLE Fact_Sales (
    Row_ID INT PRIMARY KEY,
    Order_ID VARCHAR(50),
    Customer_ID VARCHAR(50),
    Product_ID VARCHAR(50),
    Postal_Code VARCHAR(20),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    Profit FLOAT,
    CONSTRAINT FK_Fact_Order FOREIGN KEY (Order_ID) REFERENCES Dim_Order(Order_ID),
    CONSTRAINT FK_Fact_Customer FOREIGN KEY (Customer_ID) REFERENCES Dim_Customer(Customer_ID),
    CONSTRAINT FK_Fact_Product FOREIGN KEY (Product_ID) REFERENCES Dim_Product(Product_ID),
    CONSTRAINT FK_Fact_Location FOREIGN KEY (Postal_Code) REFERENCES Dim_Location(Postal_Code)
);
"""

print("Creating tables in MSSQL...")
with engine.connect() as conn:
    # Execute table schema creation
    for statement in create_tables_sql.split(';'):
        if statement.strip():
            conn.execute(text(statement))
    conn.commit()

# 4. Extract and Deduplicate Dimensions

# --- Dim_Customer ---
dim_customer = df[['Customer ID', 'Customer Name', 'Segment']].drop_duplicates(subset=['Customer ID'])
dim_customer.columns = ['Customer_ID', 'Customer_Name', 'Segment']

# --- Dim_Product ---
dim_product = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']].drop_duplicates(subset=['Product ID'])
dim_product.columns = ['Product_ID', 'Product_Name', 'Category', 'Sub_Category']

# --- Dim_Location ---
dim_location = df[['Postal Code', 'City', 'State', 'Region', 'Country']].copy()
# Standardize Postal Code to prevent NULL issues on Primary Key
dim_location['Postal Code'] = dim_location['Postal Code'].fillna(0).astype(int).astype(str)
dim_location = dim_location.drop_duplicates(subset=['Postal Code'])
dim_location.columns = ['Postal_Code', 'City', 'State', 'Region', 'Country']

# --- Dim_Order ---
dim_order = df[['Order ID', 'Order Date', 'Ship Date', 'Ship Mode']].drop_duplicates(subset=['Order ID']).copy()
dim_order['Order Date'] = pd.to_datetime(dim_order['Order Date'])
dim_order['Ship Date'] = pd.to_datetime(dim_order['Ship Date'])
dim_order.columns = ['Order_ID', 'Order_Date', 'Ship_Date', 'Ship_Mode']

# 5. Extract Fact Table
fact_sales = df[['Row ID', 'Order ID', 'Customer ID', 'Product ID', 'Postal Code', 'Sales', 'Quantity', 'Discount', 'Profit']].copy()
fact_sales['Postal Code'] = fact_sales['Postal Code'].fillna(0).astype(int).astype(str)
fact_sales.columns = ['Row_ID', 'Order_ID', 'Customer_ID', 'Product_ID', 'Postal_Code', 'Sales', 'Quantity', 'Discount', 'Profit']

# 6. Load Data into MSSQL using fast_executemany
print("Loading Dimension tables...")

dim_customer.to_sql('Dim_Customer', con=engine, if_exists='append', index=False, chunksize=1000)
dim_product.to_sql('Dim_Product', con=engine, if_exists='append', index=False, chunksize=1000)
dim_location.to_sql('Dim_Location', con=engine, if_exists='append', index=False, chunksize=1000)
dim_order.to_sql('Dim_Order', con=engine, if_exists='append', index=False, chunksize=1000)

print("Loading Fact table...")
fact_sales.to_sql('Fact_Sales', con=engine, if_exists='append', index=False, chunksize=1000)

print("ETL Process Completed Successfully! Star Schema tables loaded into SQL Server.")