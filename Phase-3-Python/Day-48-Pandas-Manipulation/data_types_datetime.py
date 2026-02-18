# Day 48 - Data Types and Datetime Operations
# Author: Syamprasad
# Date: February 18, 2026

import pandas as pd
import numpy as np

print("="*70)
print("DATA TYPES AND DATETIME OPERATIONS")
print("="*70)

# Create dataset with mixed types (messy real-world data)
raw_data = {
    'Transaction_ID': ['T001', 'T002', 'T003', 'T004', 'T005'],
    'Date': ['2026-01-15', '2026-01-16', '2026-01-17', '2026-01-18', '2026-01-19'],
    'Amount': ['1200.50', '850.00', '2100.75', '950.25', '3200.00'],
    'Quantity': ['2', '5', '1', '3', '4'],
    'Is_Premium': ['True', 'False', 'True', 'False', 'True'],
    'Category_Code': [1, 2, 1, 3, 2]
}

df = pd.DataFrame(raw_data)
print("Raw DataFrame:")
print(df)
print("\nData types BEFORE conversion:")
print(df.dtypes)

print("\n" + "="*70)
print("PART 1: DATA TYPE CONVERSIONS")
print("="*70)

# Convert string to numeric
df['Amount'] = pd.to_numeric(df['Amount'])
df['Quantity'] = df['Quantity'].astype(int)
print("\nAfter converting Amount and Quantity:")
print(df[['Amount', 'Quantity']].dtypes)

# Convert string to boolean
df['Is_Premium'] = df['Is_Premium'].map({'True': True, 'False': False})
print("\nAfter converting Is_Premium to boolean:")
print(df[['Is_Premium']].dtypes)
print(df['Is_Premium'])

# Convert to category (saves memory for low-cardinality columns)
df['Category_Code'] = df['Category_Code'].astype('category')
print("\nCategory_Code as category type:")
print(df['Category_Code'])
print(f"Categories: {df['Category_Code'].cat.categories.tolist()}")

print("\n" + "="*70)
print("PART 2: DATETIME OPERATIONS")
print("="*70)

# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])
print("Date column type:", df['Date'].dtype)
print(df['Date'])

# Create richer datetime dataset
date_data = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=30, freq='D'),
    'Sales': np.random.randint(10000, 50000, 30)
})

print("\nDatetime-rich dataset:")
print(date_data.head())

# Extract datetime components
date_data['Year'] = date_data['Date'].dt.year
date_data['Month'] = date_data['Date'].dt.month
date_data['Month_Name'] = date_data['Date'].dt.month_name()
date_data['Day'] = date_data['Date'].dt.day
date_data['Day_Name'] = date_data['Date'].dt.day_name()
date_data['Week'] = date_data['Date'].dt.isocalendar().week
date_data['Quarter'] = date_data['Date'].dt.quarter
date_data['Is_Weekend'] = date_data['Date'].dt.dayofweek >= 5

print("\nWith extracted datetime features:")
print(date_data.head(10))

# Analysis using datetime features
print("\n" + "="*70)
print("PART 3: DATETIME ANALYTICS")
print("="*70)

# Sales by day of week
dow_sales = date_data.groupby('Day_Name')['Sales'].mean().round(2)
print("Average sales by day of week:")
print(dow_sales)

# Weekend vs weekday sales
weekend_sales = date_data[date_data['Is_Weekend']]['Sales'].mean()
weekday_sales = date_data[~date_data['Is_Weekend']]['Sales'].mean()
print(f"\nAverage weekend sales: ₹{weekend_sales:,.2f}")
print(f"Average weekday sales: ₹{weekday_sales:,.2f}")

# Weekly totals
weekly_sales = date_data.groupby('Week')['Sales'].sum()
print("\nWeekly sales totals:")
print(weekly_sales)

# Date arithmetic
date_data['Days_Since_Start'] = (date_data['Date'] - date_data['Date'].min()).dt.days
date_data['Days_Until_End'] = (date_data['Date'].max() - date_data['Date']).dt.days

print("\nDate arithmetic:")
print(date_data[['Date', 'Days_Since_Start', 'Days_Until_End']].head())

# Filter by date range
jan_first_week = date_data[
    (date_data['Date'] >= '2026-01-01') &
    (date_data['Date'] <= '2026-01-07')
]
print("\nFirst week of January:")
print(jan_first_week[['Date', 'Day_Name', 'Sales']])

# Rolling average (7-day)
date_data['7_Day_Avg'] = date_data['Sales'].rolling(window=7).mean().round(2)
print("\nWith 7-day rolling average:")
print(date_data[['Date', 'Sales', '7_Day_Avg']].tail(10))

print("\n" + "="*70)
print("DATA TYPES & DATETIME COMPLETE ✅")
print("="*70)