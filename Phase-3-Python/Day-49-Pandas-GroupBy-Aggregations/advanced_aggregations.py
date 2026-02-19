# Day 49 - Advanced Aggregations
# Author: Syamprasad
# Date: February 19, 2026

import pandas as pd
import numpy as np

# Load or create data
np.random.seed(42)
n = 100

df = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=n, freq='D'),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'Category': np.random.choice(['Electronics', 'Accessories'], n),
    'Salesperson': np.random.choice(['Rahul', 'Priya', 'Amit', 'Sneha', 'Raj'], n),
    'Quantity': np.random.randint(1, 20, n),
    'Unit_Price': np.random.choice([500, 1200, 15000, 45000, 2500], n)
})
df['Revenue'] = df['Quantity'] * df['Unit_Price']
df['Month'] = df['Date'].dt.to_period('M')

print("="*70)
print("ADVANCED AGGREGATIONS")
print("="*70)

print("\n" + "="*70)
print("PART 1: CUSTOM AGGREGATION FUNCTIONS")
print("="*70)

# Custom function
def revenue_range(series):
    """Calculate range (max - min)"""
    return series.max() - series.min()

def top_25_pct(series):
    """Get 75th percentile"""
    return series.quantile(0.75)

# Apply custom functions
region_custom = df.groupby('Region')['Revenue'].agg([
    ('Total', 'sum'),
    ('Average', 'mean'),
    ('Range', revenue_range),
    ('Top_25%', top_25_pct),
    ('Count', 'count')
]).round(2)

print("Custom Aggregation Functions:")
print(region_custom)

print("\n" + "="*70)
print("PART 2: NAMED AGGREGATIONS (CLEANER SYNTAX)")
print("="*70)

# Named aggregations (Pandas 0.25+)
product_analysis = df.groupby('Product').agg(
    Total_Revenue=('Revenue', 'sum'),
    Avg_Revenue=('Revenue', 'mean'),
    Total_Quantity=('Quantity', 'sum'),
    Transaction_Count=('Revenue', 'count'),
    Revenue_Std=('Revenue', 'std')
).round(2)

print("Named Aggregations:")
print(product_analysis.sort_values('Total_Revenue', ascending=False))

print("\n" + "="*70)
print("PART 3: TRANSFORM - ADD AGGREGATED VALUES TO ORIGINAL DF")
print("="*70)

# Add group statistics back to original dataframe
df['Region_Total_Revenue'] = df.groupby('Region')['Revenue'].transform('sum')
df['Region_Avg_Revenue'] = df.groupby('Region')['Revenue'].transform('mean')
df['Product_Total_Revenue'] = df.groupby('Product')['Revenue'].transform('sum')

# Calculate percentage of region total
df['Pct_of_Region'] = (df['Revenue'] / df['Region_Total_Revenue'] * 100).round(2)

print("DataFrame with transformed columns:")
print(df[['Product', 'Region', 'Revenue', 'Region_Total_Revenue', 'Pct_of_Region']].head(10))

print("\n" + "="*70)
print("PART 4: FILTER - KEEP ONLY CERTAIN GROUPS")
print("="*70)

# Keep only regions with total revenue > 100,000
high_revenue_regions = df.groupby('Region').filter(
    lambda x: x['Revenue'].sum() > 100000
)

print(f"Original data: {len(df)} rows")
print(f"After filtering high-revenue regions: {len(high_revenue_regions)} rows")
print("\nRegions kept:")
print(high_revenue_regions['Region'].unique())

# Keep products with more than 15 transactions
popular_products = df.groupby('Product').filter(
    lambda x: len(x) > 15
)

print(f"\nProducts with >15 transactions:")
print(popular_products['Product'].value_counts())

print("\n" + "="*70)
print("PART 5: APPLY - COMPLEX CUSTOM OPERATIONS")
print("="*70)

# Apply custom function to each group
def analyze_region(group_df):
    """Custom analysis function"""
    return pd.Series({
        'Total_Revenue': group_df['Revenue'].sum(),
        'Avg_Revenue': group_df['Revenue'].mean(),
        'Top_Product': group_df.groupby('Product')['Revenue'].sum().idxmax(),
        'Top_Product_Revenue': group_df.groupby('Product')['Revenue'].sum().max(),
        'Transaction_Count': len(group_df),
        'Unique_Products': group_df['Product'].nunique()
    })

region_analysis = df.groupby('Region').apply(analyze_region)
print("Custom Apply Function Results:")
print(region_analysis)

print("\n" + "="*70)
print("PART 6: GROUPBY WITH TIME SERIES")
print("="*70)

# Monthly aggregations
monthly_revenue = df.groupby('Month').agg({
    'Revenue': 'sum',
    'Quantity': 'sum',
    'Product': 'count'
})
monthly_revenue.columns = ['Total_Revenue', 'Total_Quantity', 'Transactions']

print("Monthly Performance:")
print(monthly_revenue)

# Week over week growth
monthly_revenue['Revenue_Growth'] = monthly_revenue['Total_Revenue'].pct_change() * 100
print("\nWith Growth Rate:")
print(monthly_revenue)

# Multiple time groupings
df['Year'] = df['Date'].dt.year
df['Month_Num'] = df['Date'].dt.month
df['Week'] = df['Date'].dt.isocalendar().week

weekly_by_product = df.groupby(['Week', 'Product'])['Revenue'].sum()
print("\nWeekly revenue by product (first 20):")
print(weekly_by_product.head(20))

print("\n" + "="*70)
print("ADVANCED AGGREGATIONS COMPLETE ✅")
print("="*70)