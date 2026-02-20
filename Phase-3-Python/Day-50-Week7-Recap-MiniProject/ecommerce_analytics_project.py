# Day 50 - Complete E-Commerce Analytics Project
# Author: Syamprasad
# Date: February 20, 2026
# 
# PROJECT: E-Commerce Customer Analytics
# Combining all Week 7 skills in one complete pipeline

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("="*80)
print("E-COMMERCE CUSTOMER ANALYTICS PLATFORM")
print("Complete End-to-End Python Analytics Project")
print("="*80)

# ============================================================================
# SECTION 1: DATA GENERATION (Simulating Real E-Commerce Data)
# ============================================================================

print("\n" + "="*80)
print("SECTION 1: DATA GENERATION & LOADING")
print("="*80)

np.random.seed(42)

# Generate realistic e-commerce data
n_customers = 200
n_transactions = 1000

# Customer data
customer_ids = [f'CUST{i:04d}' for i in range(1, n_customers + 1)]
customer_data = {
    'customer_id': customer_ids,
    'customer_name': [f'Customer_{i}' for i in range(1, n_customers + 1)],
    'signup_date': pd.date_range('2025-01-01', periods=n_customers, freq='D'),
    'city': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata'], n_customers),
    'customer_segment': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], n_customers, p=[0.4, 0.3, 0.2, 0.1])
}

customers_df = pd.DataFrame(customer_data)

# Transaction data
transaction_data = {
    'transaction_id': [f'TXN{i:06d}' for i in range(1, n_transactions + 1)],
    'transaction_date': pd.date_range('2025-01-01', periods=n_transactions, freq='12H'),
    'customer_id': np.random.choice(customer_ids, n_transactions),
    'product_category': np.random.choice(
        ['Electronics', 'Fashion', 'Home & Kitchen', 'Books', 'Sports', 'Beauty'],
        n_transactions
    ),
    'product_name': np.random.choice(
        ['Laptop', 'Smartphone', 'Headphones', 'Shirt', 'Jeans', 'Watch', 
         'Mixer', 'Bedsheet', 'Novel', 'Textbook', 'Football', 'Cricket Bat',
         'Perfume', 'Lipstick'],
        n_transactions
    ),
    'quantity': np.random.randint(1, 5, n_transactions),
    'unit_price': np.random.choice([299, 499, 999, 1499, 2999, 4999, 9999, 19999, 49999], n_transactions),
    'discount_percent': np.random.choice([0, 5, 10, 15, 20, 25, 30], n_transactions),
    'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'COD'], n_transactions),
    'delivery_status': np.random.choice(['Delivered', 'In Transit', 'Cancelled', 'Returned'], n_transactions, p=[0.75, 0.15, 0.07, 0.03])
}

transactions_df = pd.DataFrame(transaction_data)

print(f"✅ Generated {len(customers_df)} customers")
print(f"✅ Generated {len(transactions_df)} transactions")

print("\nCustomer Data Sample:")
print(customers_df.head())

print("\nTransaction Data Sample:")
print(transactions_df.head())

# ============================================================================
# SECTION 2: DATA CLEANING & TRANSFORMATION
# ============================================================================

print("\n" + "="*80)
print("SECTION 2: DATA CLEANING & TRANSFORMATION")
print("="*80)

# Calculate revenue metrics
transactions_df['gross_amount'] = transactions_df['quantity'] * transactions_df['unit_price']
transactions_df['discount_amount'] = transactions_df['gross_amount'] * (transactions_df['discount_percent'] / 100)
transactions_df['net_amount'] = transactions_df['gross_amount'] - transactions_df['discount_amount']

# Extract datetime features
transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'])
transactions_df['year'] = transactions_df['transaction_date'].dt.year
transactions_df['month'] = transactions_df['transaction_date'].dt.month
transactions_df['month_name'] = transactions_df['transaction_date'].dt.month_name()
transactions_df['day_of_week'] = transactions_df['transaction_date'].dt.day_name()
transactions_df['hour'] = transactions_df['transaction_date'].dt.hour
transactions_df['is_weekend'] = transactions_df['transaction_date'].dt.dayofweek >= 5

# Merge customer and transaction data
df = transactions_df.merge(customers_df, on='customer_id', how='left')

print("✅ Revenue calculations complete")
print("✅ Datetime features extracted")
print("✅ Customer data merged")

print(f"\nFinal dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# ============================================================================
# SECTION 3: EXPLORATORY DATA ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 3: EXPLORATORY DATA ANALYSIS")
print("="*80)

# Overall business metrics
total_transactions = len(df)
total_revenue = df['net_amount'].sum()
total_customers = df['customer_id'].nunique()
avg_order_value = df['net_amount'].mean()
avg_items_per_order = df['quantity'].mean()

print("\n📊 BUSINESS OVERVIEW:")
print(f"Total Transactions: {total_transactions:,}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: ₹{avg_order_value:,.2f}")
print(f"Average Items/Order: {avg_items_per_order:.2f}")

# Delivery performance
delivery_stats = df['delivery_status'].value_counts()
delivery_rate = (delivery_stats.get('Delivered', 0) / total_transactions * 100)
cancellation_rate = (delivery_stats.get('Cancelled', 0) / total_transactions * 100)

print(f"\n📦 DELIVERY METRICS:")
print(f"Delivery Rate: {delivery_rate:.2f}%")
print(f"Cancellation Rate: {cancellation_rate:.2f}%")
print("\nDelivery Status Breakdown:")
print(delivery_stats)

# ============================================================================
# SECTION 4: CUSTOMER SEGMENTATION ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 4: CUSTOMER SEGMENTATION ANALYSIS")
print("="*80)

# Analyze by customer segment
segment_analysis = df.groupby('customer_segment').agg(
    Total_Revenue=('net_amount', 'sum'),
    Avg_Order_Value=('net_amount', 'mean'),
    Total_Transactions=('transaction_id', 'count'),
    Unique_Customers=('customer_id', 'nunique'),
    Avg_Discount=('discount_percent', 'mean')
).round(2)

segment_analysis = segment_analysis.sort_values('Total_Revenue', ascending=False)
segment_analysis['Revenue_Share_%'] = (segment_analysis['Total_Revenue'] / total_revenue * 100).round(2)

print("\nCustomer Segment Performance:")
print(segment_analysis)

# Top segment
top_segment = segment_analysis.index[0]
print(f"\n🏆 Most Valuable Segment: {top_segment}")
print(f"   Revenue: ₹{segment_analysis.loc[top_segment, 'Total_Revenue']:,.2f}")
print(f"   Share: {segment_analysis.loc[top_segment, 'Revenue_Share_%']:.1f}%")

# ============================================================================
# SECTION 5: PRODUCT CATEGORY ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 5: PRODUCT CATEGORY ANALYSIS")
print("="*80)

category_analysis = df.groupby('product_category').agg(
    Total_Revenue=('net_amount', 'sum'),
    Total_Quantity=('quantity', 'sum'),
    Avg_Price=('unit_price', 'mean'),
    Transaction_Count=('transaction_id', 'count')
).round(2)

category_analysis = category_analysis.sort_values('Total_Revenue', ascending=False)
category_analysis['Revenue_Share_%'] = (category_analysis['Total_Revenue'] / total_revenue * 100).round(2)

print("\nProduct Category Performance:")
print(category_analysis)

# Top 3 categories
print("\n🏆 Top 3 Categories by Revenue:")
for i, category in enumerate(category_analysis.head(3).index, 1):
    rev = category_analysis.loc[category, 'Total_Revenue']
    share = category_analysis.loc[category, 'Revenue_Share_%']
    print(f"{i}. {category}: ₹{rev:,.2f} ({share:.1f}%)")

# ============================================================================
# SECTION 6: GEOGRAPHIC ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 6: GEOGRAPHIC ANALYSIS")
print("="*80)

city_analysis = df.groupby('city').agg(
    Total_Revenue=('net_amount', 'sum'),
    Customer_Count=('customer_id', 'nunique'),
    Transaction_Count=('transaction_id', 'count'),
    Avg_Order_Value=('net_amount', 'mean')
).round(2)

city_analysis = city_analysis.sort_values('Total_Revenue', ascending=False)
city_analysis['Revenue_Share_%'] = (city_analysis['Total_Revenue'] / total_revenue * 100).round(2)

print("\nCity-wise Performance:")
print(city_analysis)

# Top city
top_city = city_analysis.index[0]
print(f"\n🏆 Top City: {top_city}")
print(f"   Revenue: ₹{city_analysis.loc[top_city, 'Total_Revenue']:,.2f}")
print(f"   Customers: {city_analysis.loc[top_city, 'Customer_Count']:.0f}")

# ============================================================================
# SECTION 7: TIME-BASED ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 7: TIME-BASED ANALYSIS")
print("="*80)

# Monthly trend
monthly_trend = df.groupby('month_name').agg(
    Revenue=('net_amount', 'sum'),
    Transactions=('transaction_id', 'count'),
    Avg_Order_Value=('net_amount', 'mean')
).round(2)

print("\nMonthly Performance:")
print(monthly_trend)

# Day of week analysis
dow_analysis = df.groupby('day_of_week').agg(
    Revenue=('net_amount', 'sum'),
    Transactions=('transaction_id', 'count')
).round(2)

# Reorder days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_analysis = dow_analysis.reindex([d for d in day_order if d in dow_analysis.index])

print("\nDay of Week Analysis:")
print(dow_analysis)

# Weekend vs Weekday
weekend_rev = df[df['is_weekend']]['net_amount'].sum()
weekday_rev = df[~df['is_weekend']]['net_amount'].sum()

print(f"\nWeekend Revenue: ₹{weekend_rev:,.2f} ({weekend_rev/total_revenue*100:.1f}%)")
print(f"Weekday Revenue: ₹{weekday_rev:,.2f} ({weekday_rev/total_revenue*100:.1f}%)")

# Peak shopping hours
hour_analysis = df.groupby('hour')['net_amount'].sum().sort_values(ascending=False)
print(f"\nPeak Shopping Hours (Top 5):")
for hour, revenue in hour_analysis.head(5).items():
    print(f"  {hour:02d}:00 - ₹{revenue:,.2f}")

# ============================================================================
# SECTION 8: CUSTOMER LIFETIME VALUE (CLV) ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 8: CUSTOMER LIFETIME VALUE ANALYSIS")
print("="*80)

customer_ltv = df.groupby('customer_id').agg(
    Total_Spent=('net_amount', 'sum'),
    Total_Transactions=('transaction_id', 'count'),
    Avg_Order_Value=('net_amount', 'mean'),
    First_Purchase=('transaction_date', 'min'),
    Last_Purchase=('transaction_date', 'max')
).round(2)

# Calculate days active
customer_ltv['Days_Active'] = (customer_ltv['Last_Purchase'] - customer_ltv['First_Purchase']).dt.days

# Sort by total spent
customer_ltv = customer_ltv.sort_values('Total_Spent', ascending=False)

print("\nTop 10 Customers by Lifetime Value:")
print(customer_ltv.head(10))

# VIP customers (top 10%)
vip_threshold = customer_ltv['Total_Spent'].quantile(0.90)
vip_customers = customer_ltv[customer_ltv['Total_Spent'] >= vip_threshold]

print(f"\n💎 VIP Customers (Top 10%):")
print(f"   Count: {len(vip_customers)}")
print(f"   Threshold: ₹{vip_threshold:,.2f}")
print(f"   Total Revenue: ₹{vip_customers['Total_Spent'].sum():,.2f}")
print(f"   Share of Total: {vip_customers['Total_Spent'].sum()/total_revenue*100:.1f}%")

# ============================================================================
# SECTION 9: PAYMENT METHOD ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SECTION 9: PAYMENT METHOD ANALYSIS")
print("="*80)

payment_analysis = df.groupby('payment_method').agg(
    Total_Revenue=('net_amount', 'sum'),
    Transaction_Count=('transaction_id', 'count'),
    Avg_Transaction=('net_amount', 'mean')
).round(2)

payment_analysis = payment_analysis.sort_values('Total_Revenue', ascending=False)
payment_analysis['Usage_%'] = (payment_analysis['Transaction_Count'] / total_transactions * 100).round(2)

print("\nPayment Method Preferences:")
print(payment_analysis)

# Most popular payment method
top_payment = payment_analysis.index[0]
print(f"\n🏆 Most Popular: {top_payment}")
print(f"   Usage: {payment_analysis.loc[top_payment, 'Usage_%']:.1f}%")

# ============================================================================
# SECTION 10: CROSS-SELL OPPORTUNITIES
# ============================================================================

print("\n" + "="*80)
print("SECTION 10: CROSS-SELL ANALYSIS")
print("="*80)

# Category × Segment matrix
cross_sell_matrix = pd.pivot_table(
    df,
    values='net_amount',
    index='product_category',
    columns='customer_segment',
    aggfunc='sum',
    fill_value=0
).round(0)

print("\nRevenue: Category × Customer Segment:")
print(cross_sell_matrix)

# Best category for each segment
print("\nBest Category per Segment:")
for segment in cross_sell_matrix.columns:
    best_category = cross_sell_matrix[segment].idxmax()
    revenue = cross_sell_matrix.loc[best_category, segment]
    print(f"  {segment}: {best_category} (₹{revenue:,.0f})")

# ============================================================================
# SECTION 11: KEY INSIGHTS & RECOMMENDATIONS
# ============================================================================

print("\n" + "="*80)
print("SECTION 11: EXECUTIVE SUMMARY & RECOMMENDATIONS")
print("="*80)

print("\n📊 KEY INSIGHTS:")

print(f"\n1. REVENUE CONCENTRATION:")
print(f"   • Top 10% customers generate {vip_customers['Total_Spent'].sum()/total_revenue*100:.1f}% of revenue")
print(f"   • {top_segment} segment is most valuable ({segment_analysis.loc[top_segment, 'Revenue_Share_%']:.1f}%)")

print(f"\n2. PRODUCT PERFORMANCE:")
top_category = category_analysis.index[0]
print(f"   • {top_category} leads with {category_analysis.loc[top_category, 'Revenue_Share_%']:.1f}% revenue share")
print(f"   • Top 3 categories generate {category_analysis.head(3)['Revenue_Share_%'].sum():.1f}% of revenue")

print(f"\n3. GEOGRAPHIC INSIGHTS:")
print(f"   • {top_city} is strongest market with ₹{city_analysis.loc[top_city, 'Total_Revenue']:,.2f}")
print(f"   • Top 3 cities: {', '.join(city_analysis.head(3).index)}")

print(f"\n4. DELIVERY PERFORMANCE:")
print(f"   • {delivery_rate:.1f}% successful delivery rate")
print(f"   • {cancellation_rate:.1f}% cancellation rate needs improvement")

print(f"\n5. SHOPPING BEHAVIOR:")
peak_hour = hour_analysis.index[0]
print(f"   • Peak shopping: {peak_hour:02d}:00 hours")
best_day = dow_analysis['Revenue'].idxmax()
print(f"   • Best day: {best_day}")

print("\n💡 STRATEGIC RECOMMENDATIONS:")

print("\n1. VIP CUSTOMER RETENTION:")
print("   ✅ Launch exclusive loyalty program for top 10%")
print("   ✅ Personalized offers and early access to sales")
print("   ✅ Dedicated customer support channel")

print("\n2. CATEGORY EXPANSION:")
print(f"   ✅ Increase {top_category} inventory by 20%")
print("   ✅ Cross-sell opportunities with complementary categories")
print("   ✅ Bundle deals for popular combinations")

print("\n3. GEOGRAPHIC FOCUS:")
print(f"   ✅ Strengthen presence in {top_city}")
print("   ✅ Launch targeted campaigns in underperforming cities")
print("   ✅ Optimize delivery network for top 3 cities")

print("\n4. DELIVERY OPTIMIZATION:")
print("   ✅ Investigate cancellation reasons")
print("   ✅ Improve delivery time estimates")
print("   ✅ Partner with reliable logistics providers")

print("\n5. PAYMENT & TIMING:")
print(f"   ✅ Promote {top_payment} (most popular)")
print(f"   ✅ Schedule flash sales during peak hours ({peak_hour:02d}:00)")
print(f"   ✅ Weekend-specific offers (currently {weekend_rev/total_revenue*100:.1f}% of revenue)")

# ============================================================================
# SECTION 12: SAVE OUTPUTS
# ============================================================================

print("\n" + "="*80)
print("SECTION 12: SAVING ANALYSIS OUTPUTS")
print("="*80)

# Save key reports
segment_analysis.to_csv('customer_segment_report.csv')
category_analysis.to_csv('product_category_report.csv')
city_analysis.to_csv('geographic_analysis.csv')
customer_ltv.head(100).to_csv('top_100_customers.csv')

print("✅ customer_segment_report.csv saved")
print("✅ product_category_report.csv saved")
print("✅ geographic_analysis.csv saved")
print("✅ top_100_customers.csv saved")

print("\n" + "="*80)
print("PROJECT COMPLETE ✅")
print("="*80)
print("\nThis project demonstrates:")
print("✅ Data generation and loading")
print("✅ Data cleaning and transformation")
print("✅ Datetime feature engineering")
print("✅ Exploratory data analysis")
print("✅ Customer segmentation")
print("✅ Product and geographic analysis")
print("✅ Time-based trends")
print("✅ Customer lifetime value")
print("✅ Cross-sell analysis")
print("✅ Business insights generation")
print("✅ Strategic recommendations")
print("✅ Report generation")
print("\n🎯 All Week 7 skills applied in one complete pipeline!")