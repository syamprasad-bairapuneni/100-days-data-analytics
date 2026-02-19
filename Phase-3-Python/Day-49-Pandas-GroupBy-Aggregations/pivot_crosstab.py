# Day 49 - Pivot Tables and Cross-Tabulation
# Author: Syamprasad
# Date: February 19, 2026

import pandas as pd
import numpy as np

# Create data
np.random.seed(42)
n = 100

df = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=n, freq='D'),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'Category': np.random.choice(['Electronics', 'Accessories'], n),
    'Salesperson': np.random.choice(['Rahul', 'Priya', 'Amit', 'Sneha'], n),
    'Quantity': np.random.randint(1, 20, n),
    'Unit_Price': np.random.choice([500, 1200, 15000, 45000, 2500], n)
})
df['Revenue'] = df['Quantity'] * df['Unit_Price']
df['Month'] = df['Date'].dt.to_period('M').astype(str)

print("="*70)
print("PIVOT TABLES AND CROSS-TABULATION")
print("="*70)

print("\n" + "="*70)
print("PART 1: BASIC PIVOT TABLES")
print("="*70)

# Simple pivot: Region (rows) × Product (columns)
pivot_revenue = pd.pivot_table(
    df,
    values='Revenue',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)

print("Revenue by Region and Product:")
print(pivot_revenue)

# Add totals
pivot_revenue['Total'] = pivot_revenue.sum(axis=1)
pivot_revenue.loc['Total'] = pivot_revenue.sum()

print("\nWith row and column totals:")
print(pivot_revenue)

print("\n" + "="*70)
print("PART 2: MULTIPLE AGGREGATIONS IN PIVOT")
print("="*70)

# Multiple aggregation functions
pivot_multi = pd.pivot_table(
    df,
    values='Revenue',
    index='Region',
    columns='Product',
    aggfunc=['sum', 'mean', 'count'],
    fill_value=0
)

print("Multiple aggregations (sum, mean, count):")
print(pivot_multi)

print("\n" + "="*70)
print("PART 3: MULTIPLE VALUE COLUMNS")
print("="*70)

# Pivot with multiple value columns
pivot_multi_values = pd.pivot_table(
    df,
    values=['Revenue', 'Quantity'],
    index='Region',
    columns='Product',
    aggfunc={'Revenue': 'sum', 'Quantity': 'sum'},
    fill_value=0
)

print("Revenue AND Quantity pivot:")
print(pivot_multi_values)

print("\n" + "="*70)
print("PART 4: HIERARCHICAL INDEXES IN PIVOT")
print("="*70)

# Multiple row indexes
pivot_hierarchy = pd.pivot_table(
    df,
    values='Revenue',
    index=['Region', 'Category'],
    columns='Product',
    aggfunc='sum',
    fill_value=0
)

print("Hierarchical index (Region → Category):")
print(pivot_hierarchy)

print("\n" + "="*70)
print("PART 5: CROSS-TABULATION (FREQUENCY TABLES)")
print("="*70)

# Simple crosstab - count occurrences
crosstab_simple = pd.crosstab(
    df['Region'],
    df['Product']
)

print("Transaction count by Region and Product:")
print(crosstab_simple)

# Add row and column totals
crosstab_totals = pd.crosstab(
    df['Region'],
    df['Product'],
    margins=True,
    margins_name='Total'
)

print("\nWith totals:")
print(crosstab_totals)

# Crosstab with percentages
crosstab_pct = pd.crosstab(
    df['Region'],
    df['Product'],
    normalize='all'  # Can be 'all', 'index', 'columns'
) * 100

print("\nPercentage of total transactions:")
print(crosstab_pct.round(2))

# Percentage within rows (each region sums to 100%)
crosstab_row_pct = pd.crosstab(
    df['Region'],
    df['Product'],
    normalize='index'
) * 100

print("\nPercentage within each region (rows sum to 100%):")
print(crosstab_row_pct.round(2))

print("\n" + "="*70)
print("PART 6: CROSSTAB WITH AGGREGATION")
print("="*70)

# Crosstab with custom aggregation (not just count)
crosstab_revenue = pd.crosstab(
    df['Region'],
    df['Product'],
    values=df['Revenue'],
    aggfunc='sum'
)

print("Revenue crosstab (instead of count):")
print(crosstab_revenue.fillna(0).astype(int))

# Multiple aggregations in crosstab
crosstab_multi_agg = pd.crosstab(
    df['Region'],
    df['Product'],
    values=df['Revenue'],
    aggfunc=['sum', 'mean']
)

print("\nCrosstab with multiple aggregations:")
print(crosstab_multi_agg)

print("\n" + "="*70)
print("PART 7: PIVOT VS GROUPBY - WHEN TO USE WHICH")
print("="*70)

print("""
PIVOT TABLE vs GROUPBY:

USE PIVOT TABLE when:
✅ You want a 2D view (rows × columns)
✅ Creating reports for humans to read
✅ Need cross-sectional analysis
✅ Making Excel-like summaries
Example: "Show me revenue by Region (rows) and Product (columns)"

USE GROUPBY when:
✅ You want flexible aggregations
✅ Need to chain operations
✅ Working with single grouping dimension
✅ Further data processing needed
Example: "Group by region, calculate stats, filter, sort"

THEY'RE COMPLEMENTARY:
- Pivot is built on GroupBy
- Pivot = GroupBy + Reshaping
- Use what's clearer for your use case
""")

print("\n" + "="*70)
print("PIVOT TABLES & CROSSTAB COMPLETE ✅")
print("="*70)