# Day 46 - NumPy vs Pandas: When to use which?
# Author: Syamprasad

import numpy as np
import pandas as pd
import time

print("="*70)
print("NUMPY VS PANDAS - PRACTICAL COMPARISON")
print("="*70)

# Same data in both formats
data_list = [
    ['Laptop', 45000, 50],
    ['Mouse', 500, 200],
    ['Keyboard', 1200, 150],
    ['Monitor', 15000, 75]
]

# NumPy version
np_array = np.array(data_list)
print("NumPy Array:")
print(np_array)
print(f"Problem: All elements are strings! {np_array.dtype}")

# Pandas version
df = pd.DataFrame(data_list, columns=['Product', 'Price', 'Stock'])
print("\nPandas DataFrame:")
print(df)
print(f"\nData types:")
print(df.dtypes)

print("\n" + "="*70)
print("TASK 1: Calculate total inventory value")
print("="*70)

# NumPy way (harder with mixed types)
# Have to extract numeric columns manually
prices = np.array([45000, 500, 1200, 15000])
stocks = np.array([50, 200, 150, 75])
np_inventory = np.sum(prices * stocks)
print(f"NumPy result: ₹{np_inventory:,.2f}")

# Pandas way (natural!)
df['Inventory_Value'] = df['Price'] * df['Stock']
pd_inventory = df['Inventory_Value'].sum()
print(f"Pandas result: ₹{pd_inventory:,.2f}")
print("\nPandas DataFrame with new column:")
print(df)

print("\n" + "="*70)
print("TASK 2: Find products with stock < 100")
print("="*70)

# NumPy way
low_stock_indices = np.where(stocks < 100)[0]
print(f"NumPy - indices: {low_stock_indices}")
print("(Still need to map back to product names manually)")

# Pandas way
low_stock_products = df[df['Stock'] < 100]
print("\nPandas - complete info:")
print(low_stock_products)

print("\n" + "="*70)
print("TASK 3: Add new row")
print("="*70)

# NumPy way - have to recreate array
new_row = np.array([['Headphones', '2500', '120']])
np_array_new = np.vstack([np_array, new_row])
print("NumPy (recreated array):")
print(np_array_new)

# Pandas way - simple append
new_product = pd.DataFrame({
    'Product': ['Headphones'],
    'Price': [2500],
    'Stock': [120]
})
df_new = pd.concat([df, new_product], ignore_index=True)
print("\nPandas (concatenated):")
print(df_new)

print("\n" + "="*70)
print("WHEN TO USE WHICH?")
print("="*70)

print("""
USE NUMPY WHEN:
✅ Pure numerical calculations
✅ Matrix operations
✅ Performance-critical math
✅ All data is same type
✅ Array manipulation

Examples:
- Image processing
- Scientific computing
- Linear algebra
- Signal processing

USE PANDAS WHEN:
✅ Mixed data types (text + numbers)
✅ Labeled data (row/column names)
✅ Missing data handling
✅ Real-world datasets (CSV, Excel, SQL)
✅ Data cleaning & transformation
✅ Time series analysis
✅ Grouping & aggregation

Examples:
- Sales analysis (what we're doing!)
- Customer data
- Financial reports
- Any Excel-like data

BEST PRACTICE FOR DATA ANALYSTS:
1. Learn NumPy fundamentals first ✅ (Days 45-46)
2. Master Pandas for day-to-day work ✅ (Days 47-50+)
3. Use NumPy inside Pandas when needed ✅
""")

print("="*70)
print("COMPARISON COMPLETE ✅")
print("="*70)