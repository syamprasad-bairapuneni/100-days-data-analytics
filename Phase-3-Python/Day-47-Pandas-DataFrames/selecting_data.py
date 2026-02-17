# Day 47 - Selecting and Indexing Data
# Author: Syamprasad
# Date: February 17, 2026

import pandas as pd
import numpy as np

# Load the sample data we created
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime

print("="*70)
print("SALES DATA OVERVIEW")
print("="*70)
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"\nData types:")
print(df.dtypes)

print("\n" + "="*70)
print("PART 1: SELECTING COLUMNS")
print("="*70)

# Select single column (returns Series)
products = df['Product']
print("Product column (Series):")
print(products.head())
print(f"Type: {type(products)}")

# Select single column (returns DataFrame)
products_df = df[['Product']]
print("\nProduct column (DataFrame):")
print(products_df.head())
print(f"Type: {type(products_df)}")

# Select multiple columns
subset = df[['Product', 'Region', 'Revenue']]
print("\nMultiple columns:")
print(subset.head())

# Select columns by position
first_three_cols = df.iloc[:, :3]
print("\nFirst 3 columns (by position):")
print(first_three_cols.head())

print("\n" + "="*70)
print("PART 2: SELECTING ROWS")
print("="*70)

# First 5 rows
print("First 5 rows:")
print(df.head())

# Last 3 rows
print("\nLast 3 rows:")
print(df.tail(3))

# Random sample of 5 rows
print("\nRandom sample of 5 rows:")
print(df.sample(5))

# Specific rows by position (iloc)
print("\nRows 10 to 15 (iloc):")
print(df.iloc[10:15])

# Specific rows by index (loc)
print("\nRows with index 5, 10, 15 (loc):")
print(df.loc[[5, 10, 15]])

print("\n" + "="*70)
print("PART 3: SELECTING SPECIFIC CELLS")
print("="*70)

# Single cell - row 5, column 'Product'
cell_value = df.loc[5, 'Product']
print(f"Row 5, Product column: {cell_value}")

# Single cell by position
cell_by_position = df.iloc[5, 1]  # Row 5, Column 1
print(f"Row 5, Column 1: {cell_by_position}")

# Multiple cells
subset_cells = df.loc[5:8, ['Product', 'Revenue']]
print("\nRows 5-8, Product and Revenue:")
print(subset_cells)

# Cells by position
subset_by_position = df.iloc[5:8, [1, 5]]  # Rows 5-8, Columns 1 and 5
print("\nRows 5-8, Columns 1 and 5:")
print(subset_by_position)

print("\n" + "="*70)
print("PART 4: CONDITIONAL SELECTION (BOOLEAN INDEXING)")
print("="*70)

# Single condition - high revenue sales
high_revenue = df[df['Revenue'] > 100000]
print(f"Sales with Revenue > 100,000:")
print(high_revenue.head())
print(f"Count: {len(high_revenue)}")

# Multiple conditions - AND
north_laptops = df[(df['Region'] == 'North') & (df['Product'] == 'Laptop')]
print(f"\nNorth region Laptop sales:")
print(north_laptops)

# Multiple conditions - OR
laptop_or_monitor = df[(df['Product'] == 'Laptop') | (df['Product'] == 'Monitor')]
print(f"\nLaptop OR Monitor sales (first 5):")
print(laptop_or_monitor.head())

# NOT condition
not_north = df[df['Region'] != 'North']
print(f"\nSales NOT in North region (first 5):")
print(not_north.head())

# Between condition
mid_revenue = df[(df['Revenue'] >= 50000) & (df['Revenue'] <= 150000)]
print(f"\nRevenue between 50k and 150k:")
print(mid_revenue.head())
print(f"Count: {len(mid_revenue)}")

# isin() - multiple values
regions_of_interest = df[df['Region'].isin(['North', 'South'])]
print(f"\nNorth or South regions (using isin):")
print(regions_of_interest.head())

print("\n" + "="*70)
print("PART 5: STRING OPERATIONS IN SELECTION")
print("="*70)

# Contains
products_with_o = df[df['Product'].str.contains('o', case=False)]
print("Products containing 'o':")
print(products_with_o['Product'].unique())

# Starts with
products_start_h = df[df['Product'].str.startswith('H')]
print("\nProducts starting with 'H':")
print(products_start_h['Product'].unique())

# Ends with
products_end_e = df[df['Product'].str.endswith('e')]
print("\nProducts ending with 'e':")
print(products_end_e['Product'].unique())

print("\n" + "="*70)
print("PART 6: QUERY METHOD (SQL-LIKE SYNTAX)")
print("="*70)

# Using query() method - cleaner syntax
high_revenue_query = df.query('Revenue > 100000')
print("Revenue > 100,000 (using query):")
print(high_revenue_query.head())

# Multiple conditions with query
complex_query = df.query('Region == "North" and Product == "Laptop" and Revenue > 50000')
print("\nComplex query (North Laptops > 50k):")
print(complex_query)

# Query with variables
min_revenue = 80000
filtered = df.query('Revenue > @min_revenue')
print(f"\nRevenue > {min_revenue} (using variable in query):")
print(filtered.head())

print("\n" + "="*70)
print("SELECTING & INDEXING COMPLETE ✅")
print("="*70)