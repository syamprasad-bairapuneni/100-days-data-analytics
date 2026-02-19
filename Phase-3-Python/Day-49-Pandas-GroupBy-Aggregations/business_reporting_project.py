# Day 49 - Complete Business Reporting Project
# Author: Syamprasad
# Date: February 19, 2026

import pandas as pd
import numpy as np

print("="*70)
print("EXECUTIVE BUSINESS ANALYTICS REPORT")
print("Scenario: Quarterly Sales Performance Analysis")
print("="*70)

# Generate comprehensive dataset
np.random.seed(42)
n = 500

df = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=n, freq='D'),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam'], n),
    'Category': np.random.choice(['Computing', 'Accessories'], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n),
    'City': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata'], n),
    'Salesperson': np.random.choice(['Rahul', 'Priya', 'Amit', 'Sneha', 'Raj', 'Anita', 'Vikram'], n),
    'Customer_Type': np.random.choice(['New', 'Returning', 'VIP'], n),
    'Quantity': np.random.randint(1, 25, n),
    'Unit_Price': np.random.choice([500, 800, 1200, 2500, 15000, 45000], n),
    'Discount_Pct': np.random.choice([0, 5, 10, 15, 20], n)
})

# Calculate derived columns
df['Gross_Revenue'] = df['Quantity'] * df['Unit_Price']
df['Discount_Amount'] = df['Gross_Revenue'] * (df['Discount_Pct'] / 100)
df['Net_Revenue'] = df['Gross_Revenue'] - df['Discount_Amount']
df['Month'] = df['Date'].dt.to_period('M')
df['Quarter'] = df['Date'].dt.to_period('Q')
df['Week'] = df['Date'].dt.isocalendar().week

print(f"\nDataset Overview:")
print(f"Total Transactions: {len(df):,}")
print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Total Revenue: ₹{df['Net_Revenue'].sum():,.2f}")

print("\n" + "="*70)
print("SECTION 1: REGIONAL PERFORMANCE ANALYSIS")
print("="*70)

region_perf = df.groupby('Region').agg(
    Total_Revenue=('Net_Revenue', 'sum'),
    Avg_Order_Value=('Net_Revenue', 'mean'),
    Total_Transactions=('Net_Revenue', 'count'),
    Total_Quantity=('Quantity', 'sum'),
    Avg_Discount=('Discount_Pct', 'mean'),
    Unique_Customers=('Customer_Type', 'nunique')
).round(2)

region_perf = region_perf.sort_values('Total_Revenue', ascending=False)
region_perf['Market_Share_%'] = (region_perf['Total_Revenue'] / region_perf['Total_Revenue'].sum() * 100).round(2)

print("\nRegional Performance Summary:")
print(region_perf)

# Top and bottom regions
print(f"\n🏆 Best Region: {region_perf.index[0]}")
print(f"   Revenue: ₹{region_perf.iloc[0]['Total_Revenue']:,.2f}")
print(f"   Market Share: {region_perf.iloc[0]['Market_Share_%']:.1f}%")

print(f"\n⚠️  Weakest Region: {region_perf.index[-1]}")
print(f"   Revenue: ₹{region_perf.iloc[-1]['Total_Revenue']:,.2f}")
print(f"   Needs improvement")

print("\n" + "="*70)
print("SECTION 2: PRODUCT PERFORMANCE ANALYSIS")
print("="*70)

product_perf = df.groupby('Product').agg(
    Total_Revenue=('Net_Revenue', 'sum'),
    Total_Quantity=('Quantity', 'sum'),
    Avg_Price=('Unit_Price', 'mean'),
    Transaction_Count=('Net_Revenue', 'count'),
    Avg_Discount=('Discount_Pct', 'mean')
).round(2)

product_perf = product_perf.sort_values('Total_Revenue', ascending=False)
product_perf['Revenue_Share_%'] = (product_perf['Total_Revenue'] / product_perf['Total_Revenue'].sum() * 100).round(2)

print("Product Performance:")
print(product_perf)

# 80/20 analysis
cumulative_revenue = product_perf['Revenue_Share_%'].cumsum()
top_20_pct_products = cumulative_revenue[cumulative_revenue <= 80].index.tolist()

print(f"\n📊 80/20 Analysis:")
print(f"Top {len(top_20_pct_products)} products generate 80% of revenue:")
for product in top_20_pct_products:
    rev = product_perf.loc[product, 'Total_Revenue']
    share = product_perf.loc[product, 'Revenue_Share_%']
    print(f"  {product}: ₹{rev:,.2f} ({share:.1f}%)")

print("\n" + "="*70)
print("SECTION 3: CUSTOMER SEGMENTATION ANALYSIS")
print("="*70)

customer_analysis = df.groupby('Customer_Type').agg(
    Total_Revenue=('Net_Revenue', 'sum'),
    Avg_Order_Value=('Net_Revenue', 'mean'),
    Transaction_Count=('Net_Revenue', 'count'),
    Avg_Quantity=('Quantity', 'mean')
).round(2)

customer_analysis = customer_analysis.sort_values('Total_Revenue', ascending=False)
customer_analysis['Revenue_Share_%'] = (customer_analysis['Total_Revenue'] / customer_analysis['Total_Revenue'].sum() * 100).round(2)

print("Customer Type Analysis:")
print(customer_analysis)

print("\n💎 Customer Insights:")
for ctype in customer_analysis.index:
    rev = customer_analysis.loc[ctype, 'Total_Revenue']
    aov = customer_analysis.loc[ctype, 'Avg_Order_Value']
    count = customer_analysis.loc[ctype, 'Transaction_Count']
    print(f"\n{ctype} Customers:")
    print(f"  Total Revenue: ₹{rev:,.2f}")
    print(f"  Avg Order: ₹{aov:,.2f}")
    print(f"  Transactions: {count}")

print("\n" + "="*70)
print("SECTION 4: TIME-BASED TRENDS")
print("="*70)

# Monthly trend
monthly_trend = df.groupby('Month').agg(
    Revenue=('Net_Revenue', 'sum'),
    Transactions=('Net_Revenue', 'count'),
    Avg_Order=('Net_Revenue', 'mean')
).round(2)

monthly_trend['Growth_%'] = monthly_trend['Revenue'].pct_change() * 100

print("Monthly Performance Trend:")
print(monthly_trend)

# Best and worst months
best_month = monthly_trend['Revenue'].idxmax()
worst_month = monthly_trend['Revenue'].idxmin()

print(f"\n🏆 Best Month: {best_month}")
print(f"   Revenue: ₹{monthly_trend.loc[best_month, 'Revenue']:,.2f}")

print(f"\n⚠️  Weakest Month: {worst_month}")
print(f"   Revenue: ₹{monthly_trend.loc[worst_month, 'Revenue']:,.2f}")

print("\n" + "="*70)
print("SECTION 5: REGIONAL PRODUCT MATRIX")
print("="*70)

# Pivot table: Region × Product
region_product_matrix = pd.pivot_table(
    df,
    values='Net_Revenue',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
).round(0)

print("Revenue by Region × Product:")
print(region_product_matrix)

# Find best product per region
print("\nBest product in each region:")
for region in region_product_matrix.index:
    best_product = region_product_matrix.loc[region].idxmax()
    revenue = region_product_matrix.loc[region, best_product]
    print(f"  {region}: {best_product} (₹{revenue:,.0f})")

print("\n" + "="*70)
print("SECTION 6: SALESPERSON PERFORMANCE")
print("="*70)

salesperson_perf = df.groupby('Salesperson').agg(
    Total_Revenue=('Net_Revenue', 'sum'),
    Transactions=('Net_Revenue', 'count'),
    Avg_Deal_Size=('Net_Revenue', 'mean'),
    Total_Customers=('Customer_Type', 'count')
).round(2)

salesperson_perf = salesperson_perf.sort_values('Total_Revenue', ascending=False)
salesperson_perf['Revenue_Share_%'] = (salesperson_perf['Total_Revenue'] / salesperson_perf['Total_Revenue'].sum() * 100).round(2)

print("Salesperson Rankings:")
print(salesperson_perf)

# Top 3 performers
print("\n🏆 Top 3 Performers:")
for i, salesperson in enumerate(salesperson_perf.head(3).index, 1):
    rev = salesperson_perf.loc[salesperson, 'Total_Revenue']
    deals = salesperson_perf.loc[salesperson, 'Transactions']
    avg = salesperson_perf.loc[salesperson, 'Avg_Deal_Size']
    print(f"\n{i}. {salesperson}")
    print(f"   Revenue: ₹{rev:,.2f}")
    print(f"   Deals: {deals:.0f}")
    print(f"   Avg Deal: ₹{avg:,.2f}")

print("\n" + "="*70)
print("SECTION 7: EXECUTIVE SUMMARY & RECOMMENDATIONS")
print("="*70)

# Calculate key metrics
total_revenue = df['Net_Revenue'].sum()
total_transactions = len(df)
avg_order_value = df['Net_Revenue'].mean()
total_quantity = df['Quantity'].sum()

# Growth metrics
first_month_rev = monthly_trend.iloc[0]['Revenue']
last_month_rev = monthly_trend.iloc[-1]['Revenue']
overall_growth = ((last_month_rev - first_month_rev) / first_month_rev * 100)

print("\n📊 KEY PERFORMANCE INDICATORS:")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Transactions: {total_transactions:,}")
print(f"Average Order Value: ₹{avg_order_value:,.2f}")
print(f"Total Units Sold: {total_quantity:,}")
print(f"Growth (First to Last Month): {overall_growth:+.2f}%")

print("\n💡 STRATEGIC RECOMMENDATIONS:")

# Recommendation 1: Focus on best region
best_region = region_perf.index[0]
print(f"\n1. REGIONAL EXPANSION:")
print(f"   ✅ {best_region} is the strongest market")
print(f"   → Increase marketing budget by 20%")
print(f"   → Add 2 more sales reps")

# Recommendation 2: Product focus
top_3_products = product_perf.head(3).index.tolist()
print(f"\n2. PRODUCT STRATEGY:")
print(f"   ✅ Top 3 products: {', '.join(top_3_products)}")
print(f"   → Bundle these for cross-selling")
print(f"   → Increase inventory by 15%")

# Recommendation 3: Customer retention
vip_revenue_share = customer_analysis.loc['VIP', 'Revenue_Share_%']
print(f"\n3. CUSTOMER RETENTION:")
print(f"   ✅ VIP customers = {vip_revenue_share:.1f}% of revenue")
print(f"   → Launch VIP loyalty program")
print(f"   → Personalized offers for returning customers")

# Recommendation 4: Salesperson training
print(f"\n4. SALES TEAM:")
print(f"   ✅ Top performer generates {salesperson_perf.iloc[0]['Revenue_Share_%']:.1f}% of revenue")
print(f"   → Conduct training with best practices from top performer")
print(f"   → Implement peer mentoring program")

print("\n" + "="*70)
print("BUSINESS REPORTING PROJECT COMPLETE ✅")
print("="*70)

# Save report
print("\nSaving analysis to CSV files...")
region_perf.to_csv('regional_performance.csv')
product_perf.to_csv('product_performance.csv')
salesperson_perf.to_csv('salesperson_rankings.csv')
print("✅ Reports saved!")