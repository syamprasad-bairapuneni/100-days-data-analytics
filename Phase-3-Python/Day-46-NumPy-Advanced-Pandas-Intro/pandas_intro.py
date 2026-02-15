# Day 46 - Introduction to Pandas
# Author: Syamprasad
# Date: February 15-16, 2026

import numpy as np
import pandas as pd

print("="*70)
print("WELCOME TO PANDAS! 🐼")
print("="*70)

print("""
WHY PANDAS?

NumPy is great for numerical arrays, but real data has:
- Column names (not just indices)
- Mixed data types (text, numbers, dates)
- Missing values
- Need for labels and indexes

Pandas solves this! Think: NumPy + Excel superpowers
""")

print("="*70)
print("PART 1: PANDAS SERIES (1D labeled array)")
print("="*70)

# Create a Series (like a single column in Excel with row labels)
sales = pd.Series([1200, 1500, 980, 2100, 1750])
print("Simple Series:")
print(sales)
print(f"Type: {type(sales)}")

# Series with custom index (labels)
sales_labeled = pd.Series(
    [1200, 1500, 980, 2100, 1750],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
)
print("\nSeries with custom index:")
print(sales_labeled)

# Access by label
print(f"\nMonday sales: {sales_labeled['Mon']}")
print(f"Wednesday sales: {sales_labeled['Wed']}")

# Series from dictionary
product_prices = {
    'Laptop': 45000,
    'Mouse': 500,
    'Keyboard': 1200,
    'Monitor': 15000
}
price_series = pd.Series(product_prices)
print("\nSeries from dictionary:")
print(price_series)

# Series operations
print(f"\nAverage price: ₹{price_series.mean():,.2f}")
print(f"Max price: ₹{price_series.max():,.2f}")
print(f"Products > ₹1000:")
print(price_series[price_series > 1000])

print("\n" + "="*70)
print("PART 2: PANDAS DATAFRAME (2D labeled array - like Excel)")
print("="*70)

# Create DataFrame from dictionary
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [45000, 500, 1200, 15000, 2500],
    'Stock': [50, 200, 150, 75, 120],
    'Category': ['Computer', 'Accessory', 'Accessory', 'Computer', 'Accessory']
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)

print(f"\nDataFrame shape: {df.shape}")  # (rows, columns)
print(f"Column names: {list(df.columns)}")
print(f"Index: {list(df.index)}")

print("\n" + "="*70)
print("PART 3: VIEWING & INSPECTING DATA")
print("="*70)

# Create larger dataset
sales_data = {
    'Date': pd.date_range('2026-01-01', periods=10),
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'] * 2,
    'Quantity': [2, 15, 8, 3, 5, 1, 20, 10, 2, 7],
    'Revenue': [80000, 7500, 9600, 45000, 12500, 40000, 10000, 12000, 30000, 17500],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
}

sales_df = pd.DataFrame(sales_data)

# Head - first 5 rows
print("First 5 rows (head):")
print(sales_df.head())

# Tail - last 3 rows
print("\nLast 3 rows (tail):")
print(sales_df.tail(3))

# Info - structure of DataFrame
print("\nDataFrame Info:")
print(sales_df.info())

# Describe - statistical summary
print("\nStatistical Summary:")
print(sales_df.describe())

print("\n" + "="*70)
print("PART 4: SELECTING DATA")
print("="*70)

# Select single column (returns Series)
products = sales_df['Product']
print("Product column (Series):")
print(products)
print(f"Type: {type(products)}")

# Select multiple columns (returns DataFrame)
subset = sales_df[['Product', 'Revenue']]
print("\nProduct and Revenue columns:")
print(subset)

# Select rows by position (iloc)
print("\nFirst 3 rows (iloc):")
print(sales_df.iloc[:3])

# Select specific row
print("\nRow index 5:")
print(sales_df.iloc[5])

# Select rows by label (loc) - will explore more in next days
print("\nRows 0 to 2 (loc):")
print(sales_df.loc[0:2])

print("\n" + "="*70)
print("PART 5: FILTERING DATA (Boolean Indexing)")
print("="*70)

# Filter high revenue sales
high_revenue = sales_df[sales_df['Revenue'] > 15000]
print("Sales with Revenue > 15000:")
print(high_revenue)

# Multiple conditions
north_laptops = sales_df[(sales_df['Region'] == 'North') & (sales_df['Product'] == 'Laptop')]
print("\nNorth region Laptop sales:")
print(north_laptops)

# Filter by multiple values
east_west = sales_df[sales_df['Region'].isin(['East', 'West'])]
print("\nEast and West region sales:")
print(east_west)

print("\n" + "="*70)
print("PART 6: ADDING/MODIFYING COLUMNS")
print("="*70)

# Add new column
sales_df['Profit_Margin'] = sales_df['Revenue'] * 0.2  # 20% profit margin
print("After adding Profit_Margin column:")
print(sales_df[['Product', 'Revenue', 'Profit_Margin']].head())

# Calculate column based on conditions
sales_df['Performance'] = sales_df['Revenue'].apply(
    lambda x: 'High' if x > 20000 else 'Medium' if x > 10000 else 'Low'
)
print("\nWith Performance category:")
print(sales_df[['Product', 'Revenue', 'Performance']])

print("\n" + "="*70)
print("PART 7: BASIC AGGREGATIONS")
print("="*70)

# Total revenue
total_revenue = sales_df['Revenue'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Average revenue
avg_revenue = sales_df['Revenue'].mean()
print(f"Average Revenue: ₹{avg_revenue:,.2f}")

# Revenue by region (groupby - we'll deep dive later)
revenue_by_region = sales_df.groupby('Region')['Revenue'].sum()
print("\nRevenue by Region:")
print(revenue_by_region)

# Count by product
product_counts = sales_df['Product'].value_counts()
print("\nSales count by Product:")
print(product_counts)

print("\n" + "="*70)
print("PART 8: WHY PANDAS > NUMPY FOR ANALYTICS")
print("="*70)

print("""
PANDAS ADVANTAGES:

1. LABELED DATA
   - NumPy: array[0, 2] ❌ (what does this mean?)
   - Pandas: df.loc['Product A', 'Revenue'] ✅ (clear!)

2. MIXED TYPES
   - NumPy: All elements same type
   - Pandas: Text, numbers, dates in same table ✅

3. MISSING DATA
   - NumPy: Hard to handle
   - Pandas: Built-in NaN handling ✅

4. REAL-WORLD DATA
   - NumPy: Great for math/arrays
   - Pandas: Great for CSV, Excel, SQL, APIs ✅

5. EASY ANALYSIS
   - NumPy: df.mean(axis=0) 
   - Pandas: df.groupby('Category').mean() ✅

BOTH ARE IMPORTANT:
- Pandas is BUILT ON NumPy
- Pandas uses NumPy arrays under the hood
- Master both for data analytics!
""")

print("="*70)
print("PANDAS INTRODUCTION COMPLETE ✅")
print("="*70)
print("\nNext: Deep dive into DataFrames, cleaning, and manipulation!")