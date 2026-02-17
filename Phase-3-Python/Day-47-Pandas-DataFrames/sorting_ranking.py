# Day 47 - Sorting and Ranking Data
# Author: Syamprasad
# Date: February 17, 2026

import pandas as pd

# Load data
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("="*70)
print("PART 1: SORTING BY SINGLE COLUMN")
print("="*70)

# Sort by Revenue (ascending)
sorted_asc = df.sort_values('Revenue')
print("Sorted by Revenue (ascending) - first 5:")
print(sorted_asc[['Product', 'Revenue']].head())

# Sort by Revenue (descending)
sorted_desc = df.sort_values('Revenue', ascending=False)
print("\nSorted by Revenue (descending) - top 5:")
print(sorted_desc[['Product', 'Revenue']].head())

# Sort by Date
sorted_by_date = df.sort_values('Date')
print("\nSorted by Date (first 5):")
print(sorted_by_date[['Date', 'Product', 'Revenue']].head())

print("\n" + "="*70)
print("PART 2: SORTING BY MULTIPLE COLUMNS")
print("="*70)

# Sort by Region, then by Revenue
sorted_multi = df.sort_values(['Region', 'Revenue'], ascending=[True, False])
print("Sorted by Region (asc), then Revenue (desc):")
print(sorted_multi[['Region', 'Product', 'Revenue']].head(10))

# Sort by Product and Date
sorted_product_date = df.sort_values(['Product', 'Date'])
print("\nSorted by Product, then Date:")
print(sorted_product_date[['Product', 'Date', 'Revenue']].head(10))

print("\n" + "="*70)
print("PART 3: SORTING INDEX")
print("="*70)

# Sort by index
df_shuffled = df.sample(frac=1)  # Shuffle
print("Shuffled data (index out of order):")
print(df_shuffled.head())

df_sorted_index = df_shuffled.sort_index()
print("\nSorted by index:")
print(df_sorted_index.head())

print("\n" + "="*70)
print("PART 4: RANKING DATA")
print("="*70)

# Add rank column based on Revenue
df['Revenue_Rank'] = df['Revenue'].rank(ascending=False)
print("With revenue rank:")
print(df[['Product', 'Revenue', 'Revenue_Rank']].sort_values('Revenue_Rank').head(10))

# Rank within groups
df['Rank_Within_Region'] = df.groupby('Region')['Revenue'].rank(ascending=False)
print("\nRank within each region:")
print(df[['Region', 'Product', 'Revenue', 'Rank_Within_Region']].sort_values(['Region', 'Rank_Within_Region']).head(15))

# Percentage rank
df['Percentile_Rank'] = df['Revenue'].rank(pct=True)
print("\nPercentile rank:")
print(df[['Product', 'Revenue', 'Percentile_Rank']].sort_values('Revenue', ascending=False).head(10))

print("\n" + "="*70)
print("PART 5: FINDING TOP N AND BOTTOM N")
print("="*70)

# Top 10 revenue sales
top_10 = df.nlargest(10, 'Revenue')
print("Top 10 revenue sales:")
print(top_10[['Date', 'Product', 'Region', 'Revenue']])

# Bottom 10 revenue sales
bottom_10 = df.nsmallest(10, 'Revenue')
print("\nBottom 10 revenue sales:")
print(bottom_10[['Date', 'Product', 'Region', 'Revenue']])

# Top 5 by Revenue for each Region
top_per_region = df.groupby('Region', group_keys=False).apply(
    lambda x: x.nlargest(5, 'Revenue')
)
print("\nTop 5 sales per region:")
print(top_per_region[['Region', 'Product', 'Revenue']])

print("\n" + "="*70)
print("PART 6: PRACTICAL ANALYTICS SCENARIOS")
print("="*70)

# Scenario 1: Find best performing product by total revenue
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("Total revenue by product:")
print(product_revenue)
print(f"\n🏆 Best product: {product_revenue.index[0]} (₹{product_revenue.iloc[0]:,.2f})")

# Scenario 2: Find best performing region
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print("\nTotal revenue by region:")
print(region_revenue)
print(f"\n🏆 Best region: {region_revenue.index[0]} (₹{region_revenue.iloc[0]:,.2f})")

# Scenario 3: Identify underperforming sales (bottom 25%)
threshold = df['Revenue'].quantile(0.25)
underperforming = df[df['Revenue'] < threshold]
print(f"\nUnderperforming sales (bottom 25%, Revenue < ₹{threshold:,.2f}):")
print(f"Count: {len(underperforming)}")
print(underperforming[['Product', 'Region', 'Revenue']].head(10))

# Scenario 4: Monthly best sellers
df['Month'] = df['Date'].dt.to_period('M')
monthly_best = df.groupby('Month').apply(
    lambda x: x.nlargest(1, 'Revenue')[['Date', 'Product', 'Revenue']]
)
print("\nBest sale each month:")
print(monthly_best)

print("\n" + "="*70)
print("SORTING & RANKING COMPLETE ✅")
print("="*70)