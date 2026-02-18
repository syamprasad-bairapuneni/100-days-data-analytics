# Day 48 - Real Business Data Transformation Project
# Author: Syamprasad
# Date: February 18, 2026

import pandas as pd
import numpy as np

print("="*70)
print("BUSINESS DATA TRANSFORMATION PROJECT")
print("Scenario: E-commerce Raw Data → Analytics-Ready Dataset")
print("="*70)

# Create MESSY raw data (realistic scenario)
np.random.seed(42)
n = 50

raw_data = {
    'order_id': range(1001, 1001 + n),
    'customer_name': [
        'rahul sharma', 'PRIYA SINGH', 'Amit Kumar',
        'sneha patel', 'RAJ VERMA', 'anita gupta',
        'VIKRAM RAO', 'pooja mehta', 'arjun kapoor', 'NISHA JOSHI'
    ] * 5,
    'order_date': (
        pd.date_range('2026-01-01', periods=n, freq='D').astype(str).tolist()
    ),
    'product': np.random.choice(
        ['Laptop', 'mouse', 'KEYBOARD', 'Monitor', 'headphones'], n
    ),
    'quantity': np.random.randint(1, 10, n),
    'unit_price': np.random.choice(
        ['45000', '500', '1200', '15000', '2500'], n
    ),
    'region': np.random.choice(['north', 'SOUTH', 'East', 'west'], n),
    'payment_method': np.random.choice(
        ['Credit Card', 'UPI', None, 'Net Banking', 'Debit Card'], n
    ),
    'discount_pct': np.random.choice([0, 5, 10, None, 15, 20], n),
    'customer_rating': np.random.choice([1, 2, 3, 4, 5, None], n)
}

df_raw = pd.DataFrame(raw_data)

print("RAW MESSY DATA (first 10 rows):")
print(df_raw.head(10))
print(f"\nShape: {df_raw.shape}")
print(f"\nData types:")
print(df_raw.dtypes)
print(f"\nMissing values:")
print(df_raw.isnull().sum())

print("\n" + "="*70)
print("STEP 1: DATA CLEANING")
print("="*70)

df = df_raw.copy()

# 1. Standardize text columns
df['customer_name'] = df['customer_name'].str.title()
df['product'] = df['product'].str.title()
df['region'] = df['region'].str.title()

print("✅ Text standardized (Title Case)")

# 2. Convert data types
df['order_date'] = pd.to_datetime(df['order_date'])
df['unit_price'] = pd.to_numeric(df['unit_price'])

print("✅ Data types converted")

# 3. Handle missing values
df['payment_method'] = df['payment_method'].fillna('Unknown')
df['discount_pct'] = df['discount_pct'].fillna(0)
df['customer_rating'] = df['customer_rating'].fillna(
    df['customer_rating'].median()
)

print("✅ Missing values handled")
print(f"   Remaining missing: {df.isnull().sum().sum()}")

print("\n" + "="*70)
print("STEP 2: FEATURE ENGINEERING")
print("="*70)

# Add calculated columns
df['gross_revenue'] = df['quantity'] * df['unit_price']
df['discount_amount'] = df['gross_revenue'] * (df['discount_pct'] / 100)
df['net_revenue'] = df['gross_revenue'] - df['discount_amount']

# Datetime features
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['month_name'] = df['order_date'].dt.month_name()
df['day_of_week'] = df['order_date'].dt.day_name()
df['week_number'] = df['order_date'].dt.isocalendar().week
df['is_weekend'] = df['order_date'].dt.dayofweek >= 5

# Customer segments
df['customer_segment'] = df['net_revenue'].apply(
    lambda x: 'Premium' if x > 30000
    else 'Standard' if x > 10000
    else 'Basic'
)

# Rating category
df['rating_category'] = df['customer_rating'].apply(
    lambda x: 'Excellent' if x >= 4.5
    else 'Good' if x >= 3.5
    else 'Average' if x >= 2.5
    else 'Poor'
)

# Product code
df['product_code'] = df['product'].str[:3].str.upper() + '-' + \
    df['order_id'].astype(str)

print("✅ Features engineered:")
print("   - gross_revenue, discount_amount, net_revenue")
print("   - year, month, month_name, day_of_week, week_number, is_weekend")
print("   - customer_segment, rating_category, product_code")

print("\n" + "="*70)
print("STEP 3: DATA VALIDATION")
print("="*70)

# Check for business logic errors
negative_revenue = df[df['net_revenue'] < 0]
print(f"Orders with negative revenue: {len(negative_revenue)}")

invalid_discount = df[df['discount_pct'] > 50]
print(f"Orders with > 50% discount: {len(invalid_discount)}")

invalid_rating = df[(df['customer_rating'] < 1) | (df['customer_rating'] > 5)]
print(f"Orders with invalid rating: {len(invalid_rating)}")

print("✅ Data validation complete")

print("\n" + "="*70)
print("STEP 4: FINAL CLEAN DATASET")
print("="*70)

print("Cleaned and transformed data (first 10 rows):")
print(df[[
    'order_id', 'customer_name', 'order_date',
    'product', 'region', 'quantity',
    'unit_price', 'net_revenue', 'customer_segment'
]].head(10))

print(f"\nFinal dataset info:")
print(f"Total orders: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Missing values: {df.isnull().sum().sum()}")

print("\n" + "="*70)
print("STEP 5: BUSINESS INSIGHTS FROM CLEAN DATA")
print("="*70)

# Revenue by product
print("Revenue by Product:")
product_rev = df.groupby('product')['net_revenue'].sum().sort_values(ascending=False)
for product, rev in product_rev.items():
    print(f"  {product}: ₹{rev:,.2f}")

# Revenue by region
print("\nRevenue by Region:")
region_rev = df.groupby('region')['net_revenue'].sum().sort_values(ascending=False)
for region, rev in region_rev.items():
    print(f"  {region}: ₹{rev:,.2f}")

# Customer segments
print("\nCustomer Segments:")
segments = df['customer_segment'].value_counts()
for segment, count in segments.items():
    pct = count/len(df)*100
    seg_rev = df[df['customer_segment'] == segment]['net_revenue'].sum()
    print(f"  {segment}: {count} orders ({pct:.1f}%) | Revenue: ₹{seg_rev:,.2f}")

# Payment methods
print("\nPayment Methods:")
payment = df['payment_method'].value_counts()
print(payment)

# Average discount by product
print("\nAverage Discount by Product:")
avg_discount = df.groupby('product')['discount_pct'].mean().round(2)
print(avg_discount)

# Save clean data
df.to_csv('clean_ecommerce_data.csv', index=False)
print("\n✅ Clean data saved to 'clean_ecommerce_data.csv'")

print("\n" + "="*70)
print("BUSINESS TRANSFORMATION PROJECT COMPLETE ✅")
print("="*70)
print("\nRAW DATA → CLEAN DATA → BUSINESS INSIGHTS")
print("This is the core workflow of a Data Analyst! 🎯")