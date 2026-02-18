# Day 48 - Handling Missing Data in Pandas
# Author: Syamprasad
# Date: February 18, 2026

import pandas as pd
import numpy as np

print("="*70)
print("HANDLING MISSING DATA IN PANDAS")
print("="*70)

# Create dataset with missing values (realistic scenario)
data = {
    'Customer_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Rahul', 'Priya', None, 'Sneha', 'Raj', 'Anita', None, 'Vikram', 'Pooja', 'Arjun'],
    'Age': [25, 30, None, 28, 35, None, 29, 32, None, 27],
    'City': ['Mumbai', 'Delhi', 'Bangalore', None, 'Hyderabad', 'Chennai', 'Mumbai', None, 'Pune', 'Delhi'],
    'Purchase_Amount': [1200, None, 2100, 950, None, 1800, 3200, 1500, None, 2800],
    'Loyalty_Score': [85, 90, None, 78, 92, None, 88, None, 95, 82]
}

df = pd.DataFrame(data)
print("Dataset with missing values:")
print(df)

print("\n" + "="*70)
print("PART 1: DETECTING MISSING VALUES")
print("="*70)

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Percentage of missing values
print("\nMissing value percentage:")
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
print(missing_pct)

# Total missing values
print(f"\nTotal missing values: {df.isnull().sum().sum()}")
print(f"Total cells: {df.size}")
print(f"Missing percentage: {(df.isnull().sum().sum() / df.size * 100):.2f}%")

# Check if any value in a row is missing
df['Has_Missing'] = df.isnull().any(axis=1)
print("\nRows with missing values:")
print(df[df['Has_Missing'] == True][['Customer_ID', 'Name', 'Has_Missing']])

# Drop the helper column
df = df.drop('Has_Missing', axis=1)

print("\n" + "="*70)
print("PART 2: REMOVING MISSING VALUES")
print("="*70)

df_clean = df.copy()

# Drop rows with ANY missing value
df_no_missing = df_clean.dropna()
print(f"Original rows: {len(df_clean)}")
print(f"After dropping ANY missing: {len(df_no_missing)} rows")

# Drop rows where ALL values are missing
df_not_all_missing = df_clean.dropna(how='all')
print(f"After dropping ALL missing: {len(df_not_all_missing)} rows")

# Drop rows where specific columns have missing values
df_required_cols = df_clean.dropna(subset=['Name', 'Purchase_Amount'])
print(f"After dropping missing Name/Purchase: {len(df_required_cols)} rows")
print(df_required_cols)

# Drop columns with too many missing values (> 30%)
threshold = len(df_clean) * 0.7
df_dropped_cols = df_clean.dropna(axis=1, thresh=threshold)
print(f"\nColumns after dropping high-missing columns:")
print(df_dropped_cols.columns.tolist())

print("\n" + "="*70)
print("PART 3: FILLING MISSING VALUES")
print("="*70)

df_fill = df.copy()

# Fill with a constant value
df_fill['Name'] = df_fill['Name'].fillna('Unknown')
df_fill['City'] = df_fill['City'].fillna('Not Specified')
print("After filling Name and City:")
print(df_fill[['Customer_ID', 'Name', 'City']])

# Fill numeric with mean
age_mean = df_fill['Age'].mean()
df_fill['Age'] = df_fill['Age'].fillna(age_mean).round(0)
print(f"\nFilled Age with mean ({age_mean:.1f}):")
print(df_fill[['Customer_ID', 'Age']])

# Fill numeric with median (better for skewed data)
purchase_median = df_fill['Purchase_Amount'].median()
df_fill['Purchase_Amount'] = df_fill['Purchase_Amount'].fillna(purchase_median)
print(f"\nFilled Purchase_Amount with median (₹{purchase_median}):")
print(df_fill[['Customer_ID', 'Purchase_Amount']])

# Fill with mode (most frequent value)
loyalty_mode = df_fill['Loyalty_Score'].mode()[0]
df_fill['Loyalty_Score'] = df_fill['Loyalty_Score'].fillna(loyalty_mode)
print(f"\nFilled Loyalty_Score with mode ({loyalty_mode}):")
print(df_fill[['Customer_ID', 'Loyalty_Score']])

# Forward fill (use previous value)
sample = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=7),
    'Sales': [100, None, None, 200, None, 300, None]
})
print("\nForward fill (use previous value):")
print(sample['Sales'].ffill())

# Backward fill (use next value)
print("\nBackward fill (use next value):")
print(sample['Sales'].bfill())

print("\n" + "="*70)
print("PART 4: STRATEGY DECISION")
print("="*70)

print("""
WHEN TO USE WHICH STRATEGY:

1. DROP ROWS:
   ✅ When missing data is < 5% of total
   ✅ When you have large dataset
   ✅ When missing data is random
   ❌ When dropping causes bias

2. FILL WITH MEAN:
   ✅ Normally distributed numerical data
   ✅ When outliers are minimal
   Example: Age, Height, Weight

3. FILL WITH MEDIAN:
   ✅ Skewed numerical data
   ✅ When outliers exist
   Example: Salary, House Price, Revenue

4. FILL WITH MODE:
   ✅ Categorical data
   ✅ Low-cardinality columns
   Example: City, Category, Status

5. FORWARD/BACKWARD FILL:
   ✅ Time-series data
   ✅ Sequential data
   Example: Stock prices, Daily sales

6. FILL WITH CONSTANT:
   ✅ When "missing" has meaning
   Example: 'Unknown', 'N/A', 0
""")

print("\n" + "="*70)
print("COMPLETE CLEANED DATASET")
print("="*70)

print(df_fill)
print("\nMissing values remaining:", df_fill.isnull().sum().sum())

print("\n" + "="*70)
print("MISSING DATA HANDLING COMPLETE ✅")
print("="*70)