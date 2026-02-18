# Day 48 - Applying Functions in Pandas
# Author: Syamprasad
# Date: February 18, 2026

import pandas as pd
import numpy as np

print("="*70)
print("APPLYING FUNCTIONS IN PANDAS")
print("="*70)

# Sample sales dataset
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [45000, 500, 1200, 15000, 2500],
    'Quantity': [10, 150, 80, 25, 60],
    'Category': ['computer', 'accessory', 'accessory', 'computer', 'accessory'],
    'Customer_Name': ['rahul sharma', 'priya singh', 'amit kumar', 'sneha patel', 'raj verma']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\n" + "="*70)
print("PART 1: APPLY ON SERIES (SINGLE COLUMN)")
print("="*70)

# apply() with lambda function
df['Revenue'] = df['Price'] * df['Quantity']
df['Revenue_Category'] = df['Revenue'].apply(
    lambda x: 'High' if x > 100000
    else 'Medium' if x > 50000
    else 'Low'
)
print("Revenue Categories:")
print(df[['Product', 'Revenue', 'Revenue_Category']])

# apply() with custom function
def calculate_profit_margin(price):
    """Calculate profit margin based on price range"""
    if price > 20000:
        return 0.25   # 25% margin
    elif price > 5000:
        return 0.20   # 20% margin
    elif price > 1000:
        return 0.15   # 15% margin
    else:
        return 0.10   # 10% margin

df['Profit_Margin'] = df['Price'].apply(calculate_profit_margin)
df['Profit'] = df['Price'] * df['Profit_Margin'] * df['Quantity']

print("\nWith Profit Margins:")
print(df[['Product', 'Price', 'Profit_Margin', 'Profit']])

print("\n" + "="*70)
print("PART 2: APPLY ON DATAFRAME (MULTIPLE COLUMNS)")
print("="*70)

# apply() on entire DataFrame row (axis=1)
def classify_product(row):
    """Classify product based on price and quantity"""
    if row['Price'] > 10000 and row['Quantity'] < 50:
        return 'Premium Low Volume'
    elif row['Price'] < 2000 and row['Quantity'] > 50:
        return 'Budget High Volume'
    else:
        return 'Mid Range'

df['Product_Classification'] = df.apply(classify_product, axis=1)
print("Product Classification:")
print(df[['Product', 'Price', 'Quantity', 'Product_Classification']])

print("\n" + "="*70)
print("PART 3: MAP FUNCTION (VALUE REPLACEMENT)")
print("="*70)

# map() - replace values based on dictionary
category_mapping = {
    'computer': 'Computing Devices',
    'accessory': 'Accessories'
}
df['Category_Full'] = df['Category'].map(category_mapping)
print("Category mapping:")
print(df[['Category', 'Category_Full']])

# map() with function
df['Price_USD'] = df['Price'].map(lambda x: round(x / 83, 2))  # INR to USD
print("\nPrice in USD (1 USD = 83 INR):")
print(df[['Product', 'Price', 'Price_USD']])

print("\n" + "="*70)
print("PART 4: STRING OPERATIONS")
print("="*70)

# String operations with .str accessor
print("Original customer names:", df['Customer_Name'].tolist())

# Title case
df['Customer_Name'] = df['Customer_Name'].str.title()
print("\nTitle case:", df['Customer_Name'].tolist())

# Uppercase category
df['Category'] = df['Category'].str.upper()
print("Uppercase category:", df['Category'].tolist())

# Extract first name
df['First_Name'] = df['Customer_Name'].str.split(' ').str[0]
print("\nFirst names:", df['First_Name'].tolist())

# String length
df['Name_Length'] = df['Customer_Name'].str.len()
print("\nName lengths:")
print(df[['Customer_Name', 'Name_Length']])

# Replace string
df['Product_Code'] = df['Product'].str.replace(' ', '_').str.upper()
print("\nProduct codes:")
print(df[['Product', 'Product_Code']])

# Check contains
df['Is_Accessory'] = df['Category'].str.contains('ACCESSORY')
print("\nIs Accessory:")
print(df[['Product', 'Category', 'Is_Accessory']])

print("\n" + "="*70)
print("PART 5: APPLYMAP (ELEMENT-WISE OPERATIONS)")
print("="*70)

# Create numeric DataFrame
numeric_df = pd.DataFrame({
    'Q1': [100, 200, 150],
    'Q2': [120, 180, 160],
    'Q3': [130, 210, 170]
})

print("Original numeric data:")
print(numeric_df)

# Apply function to every element
# Round to nearest 50
formatted = numeric_df.map(lambda x: round(x / 50) * 50)
print("\nRounded to nearest 50:")
print(formatted)

print("\n" + "="*70)
print("APPLYING FUNCTIONS COMPLETE ✅")
print("="*70)