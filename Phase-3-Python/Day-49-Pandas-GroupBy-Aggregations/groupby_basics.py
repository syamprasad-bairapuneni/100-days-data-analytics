# Day 49 - GroupBy Fundamentals
# Author: Syamprasad
# Date: February 19, 2026

import pandas as pd
import numpy as np

print("="*70)
print("GROUPBY FUNDAMENTALS - SPLIT-APPLY-COMBINE")
print("="*70)

# Create sample sales dataset
np.random.seed(42)
n = 100

data = {
    'Date': pd.date_range('2026-01-01', periods=n, freq='D'),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'Salesperson': np.random.choice(['Rahul', 'Priya', 'Amit', 'Sneha', 'Raj'], n),
    'Quantity': np.random.randint(1, 20, n),
    'Unit_Price': np.random.choice([500, 1200, 15000, 45000, 2500], n)
}

df = pd.DataFrame(data)
df['Revenue'] = df['Quantity'] * df['Unit_Price']

print("Sample Sales Data:")
print(df.head(10))
print(f"\nTotal records: {len(df)}")

print("\n" + "="*70)
print("PART 1: SIMPLE GROUPBY - SINGLE COLUMN")
print("="*70)

# Group by Product and get total revenue
product_revenue = df.groupby('Product')['Revenue'].sum()
print("Total Revenue by Product:")
print(product_revenue.sort_values(ascending=False))

# With more readable formatting
print("\nFormatted:")
for product, revenue in product_revenue.sort_values(ascending=False).items():
    print(f"{product:15} ₹{revenue:>12,}")

# Group by Region
region_revenue = df.groupby('Region')['Revenue'].sum()
print("\nTotal Revenue by Region:")
for region, revenue in region_revenue.sort_values(ascending=False).items():
    print(f"{region:10} ₹{revenue:>12,}")

print("\n" + "="*70)
print("PART 2: MULTIPLE AGGREGATIONS")
print("="*70)

# Multiple aggregations on same column
product_stats = df.groupby('Product')['Revenue'].agg(['sum', 'mean', 'count', 'min', 'max'])
product_stats.columns = ['Total_Revenue', 'Avg_Revenue', 'Transactions', 'Min_Sale', 'Max_Sale']
product_stats = product_stats.sort_values('Total_Revenue', ascending=False)

print("Product Statistics:")
print(product_stats)

# Custom aggregations
product_custom = df.groupby('Product')['Revenue'].agg([
    ('Total', 'sum'),
    ('Average', 'mean'),
    ('Count', 'count'),
    ('Std_Dev', 'std'),
    ('Median', 'median')
]).round(2)

print("\nCustom Aggregation Names:")
print(product_custom)

print("\n" + "="*70)
print("PART 3: AGGREGATING MULTIPLE COLUMNS")
print("="*70)

# Different aggregations on different columns
region_analysis = df.groupby('Region').agg({
    'Revenue': ['sum', 'mean'],
    'Quantity': ['sum', 'mean'],
    'Unit_Price': 'mean'
})

print("Multiple Columns Aggregation:")
print(region_analysis)

# Flatten column names for easier access
region_analysis.columns = ['_'.join(col).strip() for col in region_analysis.columns.values]
print("\nFlattened column names:")
print(region_analysis)

print("\n" + "="*70)
print("PART 4: GROUPBY WITH MULTIPLE COLUMNS")
print("="*70)

# Group by Region AND Product
region_product = df.groupby(['Region', 'Product'])['Revenue'].sum()
print("Revenue by Region and Product:")
print(region_product.head(20))

# Convert to DataFrame for better viewing
region_product_df = region_product.reset_index()
region_product_df = region_product_df.sort_values('Revenue', ascending=False)
print("\nAs DataFrame (sorted):")
print(region_product_df.head(15))

# Top product in each region
top_in_region = df.groupby(['Region', 'Product'])['Revenue'].sum()
top_in_region = top_in_region.groupby(level=0).nlargest(1)
print("\nTop product in each region:")
print(top_in_region)

print("\n" + "="*70)
print("PART 5: GROUPBY ITERATION")
print("="*70)

# Iterate through groups
print("Iterating through Region groups:")
for region, group_df in df.groupby('Region'):
    total = group_df['Revenue'].sum()
    count = len(group_df)
    print(f"\n{region}:")
    print(f"  Transactions: {count}")
    print(f"  Total Revenue: ₹{total:,}")
    print(f"  Top Product: {group_df.groupby('Product')['Revenue'].sum().idxmax()}")

print("\n" + "="*70)
print("PART 6: GETTING SPECIFIC GROUPS")
print("="*70)

# Get specific group
grouped = df.groupby('Region')
north_data = grouped.get_group('North')
print("North Region Data (first 10):")
print(north_data.head(10))

# Size of each group
group_sizes = df.groupby('Region').size()
print("\nNumber of transactions per region:")
print(group_sizes)

print("\n" + "="*70)
print("GROUPBY BASICS COMPLETE ✅")
print("="*70)