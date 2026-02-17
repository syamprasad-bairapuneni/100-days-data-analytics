# Day 47 - Real Sales Analysis Project
# Author: Syamprasad
# Date: February 17, 2026

import pandas as pd
import numpy as np

print("="*70)
print("SALES PERFORMANCE ANALYSIS - EXECUTIVE REPORT")
print("="*70)

# Load data
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print(f"\nDataset Overview:")
print(f"Total Transactions: {len(df):,}")
print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Products: {df['Product'].nunique()}")
print(f"Regions: {df['Region'].nunique()}")

print("\n" + "="*70)
print("SECTION 1: REVENUE ANALYSIS")
print("="*70)

total_revenue = df['Revenue'].sum()
avg_revenue = df['Revenue'].mean()
median_revenue = df['Revenue'].median()

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Transaction Value: ₹{avg_revenue:,.2f}")
print(f"Median Transaction Value: ₹{median_revenue:,.2f}")

# Revenue distribution
print(f"\nRevenue Distribution:")
print(f"Min: ₹{df['Revenue'].min():,.2f}")
print(f"25th Percentile: ₹{df['Revenue'].quantile(0.25):,.2f}")
print(f"50th Percentile (Median): ₹{df['Revenue'].quantile(0.50):,.2f}")
print(f"75th Percentile: ₹{df['Revenue'].quantile(0.75):,.2f}")
print(f"Max: ₹{df['Revenue'].max():,.2f}")

# High value transactions (top 10%)
high_value_threshold = df['Revenue'].quantile(0.90)
high_value_count = len(df[df['Revenue'] >= high_value_threshold])
high_value_revenue = df[df['Revenue'] >= high_value_threshold]['Revenue'].sum()

print(f"\nHigh-Value Transactions (Top 10%):")
print(f"Threshold: ₹{high_value_threshold:,.2f}")
print(f"Count: {high_value_count} ({high_value_count/len(df)*100:.1f}% of transactions)")
print(f"Revenue: ₹{high_value_revenue:,.2f} ({high_value_revenue/total_revenue*100:.1f}% of total)")

print("\n" + "="*70)
print("SECTION 2: PRODUCT ANALYSIS")
print("="*70)

# Revenue by product
product_analysis = df.groupby('Product').agg({
    'Revenue': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
}).round(2)

product_analysis.columns = ['Total_Revenue', 'Avg_Revenue', 'Transactions', 'Total_Quantity']
product_analysis = product_analysis.sort_values('Total_Revenue', ascending=False)

print("Product Performance Summary:")
print(product_analysis)

# Best and worst products
best_product = product_analysis.index[0]
worst_product = product_analysis.index[-1]

print(f"\n🏆 Best Product: {best_product}")
print(f"   Total Revenue: ₹{product_analysis.loc[best_product, 'Total_Revenue']:,.2f}")
print(f"   Transactions: {product_analysis.loc[best_product, 'Transactions']:.0f}")

print(f"\n⚠️  Worst Product: {worst_product}")
print(f"   Total Revenue: ₹{product_analysis.loc[worst_product, 'Total_Revenue']:,.2f}")
print(f"   Transactions: {product_analysis.loc[worst_product, 'Transactions']:.0f}")

print("\n" + "="*70)
print("SECTION 3: REGIONAL ANALYSIS")
print("="*70)

# Revenue by region
region_analysis = df.groupby('Region').agg({
    'Revenue': ['sum', 'mean', 'count']
}).round(2)

region_analysis.columns = ['Total_Revenue', 'Avg_Revenue', 'Transactions']
region_analysis = region_analysis.sort_values('Total_Revenue', ascending=False)

print("Regional Performance Summary:")
print(region_analysis)

# Market share by region
region_analysis['Market_Share_%'] = (region_analysis['Total_Revenue'] / total_revenue * 100).round(2)
print("\nMarket Share by Region:")
print(region_analysis[['Total_Revenue', 'Market_Share_%']])

# Best and worst regions
best_region = region_analysis.index[0]
worst_region = region_analysis.index[-1]

print(f"\n🏆 Best Region: {best_region}")
print(f"   Revenue: ₹{region_analysis.loc[best_region, 'Total_Revenue']:,.2f}")
print(f"   Market Share: {region_analysis.loc[best_region, 'Market_Share_%']:.1f}%")

print(f"\n⚠️  Worst Region: {worst_region}")
print(f"   Revenue: ₹{region_analysis.loc[worst_region, 'Total_Revenue']:,.2f}")
print(f"   Market Share: {region_analysis.loc[worst_region, 'Market_Share_%']:.1f}%")

print("\n" + "="*70)
print("SECTION 4: PRODUCT-REGION COMBINATION ANALYSIS")
print("="*70)

# Best product-region combinations
product_region = df.groupby(['Product', 'Region'])['Revenue'].sum().sort_values(ascending=False)
print("Top 10 Product-Region Combinations:")
print(product_region.head(10))

print("\nWorst 5 Product-Region Combinations:")
print(product_region.tail(5))

print("\n" + "="*70)
print("SECTION 5: TIME-BASED ANALYSIS")
print("="*70)

# Add time features
df['Week'] = df['Date'].dt.isocalendar().week
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

# Weekly revenue trend
weekly_revenue = df.groupby('Week')['Revenue'].sum().sort_index()
print("Weekly Revenue Trend:")
print(weekly_revenue)

# Best and worst weeks
best_week = weekly_revenue.idxmax()
worst_week = weekly_revenue.idxmin()

print(f"\n🏆 Best Week: Week {best_week} (₹{weekly_revenue[best_week]:,.2f})")
print(f"⚠️  Worst Week: Week {worst_week} (₹{weekly_revenue[worst_week]:,.2f})")

# Day of week analysis
dow_analysis = df.groupby('DayOfWeek')['Revenue'].agg(['sum', 'mean', 'count'])
# Reorder days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_analysis = dow_analysis.reindex([d for d in day_order if d in dow_analysis.index])

print("\nDay of Week Analysis:")
print(dow_analysis)

print("\n" + "="*70)
print("SECTION 6: KEY INSIGHTS & RECOMMENDATIONS")
print("="*70)

print("\n📊 KEY INSIGHTS:")

print(f"\n1. REVENUE CONCENTRATION:")
print(f"   - Top 10% of transactions generate {high_value_revenue/total_revenue*100:.1f}% of revenue")
print(f"   - Focus on high-value customer segments")

print(f"\n2. PRODUCT PERFORMANCE:")
print(f"   - {best_product} is the clear winner (₹{product_analysis.loc[best_product, 'Total_Revenue']:,.2f})")
print(f"   - {worst_product} needs attention or phase-out consideration")

print(f"\n3. REGIONAL OPPORTUNITIES:")
print(f"   - {best_region} leads with {region_analysis.loc[best_region, 'Market_Share_%']:.1f}% market share")
print(f"   - {worst_region} shows growth potential")

best_combo = product_region.index[0]
print(f"\n4. WINNING COMBINATION:")
print(f"   - {best_combo[0]} in {best_combo[1]} region (₹{product_region.iloc[0]:,.2f})")

print(f"\n5. TIMING INSIGHTS:")
print(f"   - Week {best_week} had exceptional performance")
print(f"   - Consider weekly patterns for inventory planning")

print("\n💡 STRATEGIC RECOMMENDATIONS:")
print("   1. Expand high-performing product-region combinations")
print("   2. Investigate low-performing regions for improvement")
print("   3. Focus marketing budget on proven winners")
print("   4. Consider promotions during low-performing weeks")
print("   5. Optimize inventory based on weekly trends")

print("\n" + "="*70)
print("ANALYSIS COMPLETE ✅")
print("="*70)