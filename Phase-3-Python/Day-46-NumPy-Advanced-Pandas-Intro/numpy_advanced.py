# Day 46 - NumPy Advanced Operations
# Author: Syamprasad
# Date: February 15-16, 2026

import numpy as np

print("="*70)
print("PART 1: MULTI-DIMENSIONAL ARRAYS")
print("="*70)

# 2D Array (Matrix) - like Excel spreadsheet
sales_2d = np.array([
    [100, 150, 200],  # Product A: Jan, Feb, Mar
    [120, 140, 160],  # Product B: Jan, Feb, Mar
    [90, 110, 130]    # Product C: Jan, Feb, Mar
])

print("2D Sales Array:")
print(sales_2d)
print(f"Shape: {sales_2d.shape}")  # (3 rows, 3 columns)
print(f"Dimensions: {sales_2d.ndim}")

# 3D Array - like multiple Excel sheets
# Shape: (2 regions, 3 products, 3 months)
sales_3d = np.array([
    # Region 1
    [[100, 150, 200],  # Product A
     [120, 140, 160],  # Product B
     [90, 110, 130]],  # Product C
    # Region 2
    [[110, 160, 210],  # Product A
     [130, 150, 170],  # Product B
     [95, 115, 135]]   # Product C
])

print("\n3D Sales Array:")
print(sales_3d)
print(f"Shape: {sales_3d.shape}")  # (2 regions, 3 products, 3 months)

# Accessing 3D array
print(f"\nRegion 1, Product A, February: {sales_3d[0, 0, 1]}")
print(f"All months for Region 2, Product B: {sales_3d[1, 1, :]}")

print("\n" + "="*70)
print("PART 2: ARRAY RESHAPING")
print("="*70)

# Original 1D array
data = np.arange(1, 13)  # [1, 2, 3, ..., 12]
print(f"Original 1D: {data}")
print(f"Shape: {data.shape}")

# Reshape to 3x4 (3 rows, 4 columns)
matrix_3x4 = data.reshape(3, 4)
print(f"\nReshaped to 3x4:")
print(matrix_3x4)

# Reshape to 4x3
matrix_4x3 = data.reshape(4, 3)
print(f"\nReshaped to 4x3:")
print(matrix_4x3)

# Reshape to 2x2x3 (3D)
tensor_2x2x3 = data.reshape(2, 2, 3)
print(f"\nReshaped to 2x2x3:")
print(tensor_2x2x3)

# Flatten back to 1D
flattened = matrix_3x4.flatten()
print(f"\nFlattened back to 1D: {flattened}")

# Real use case: Monthly sales to quarterly
monthly_sales = np.array([100, 120, 110, 150, 140, 160, 170, 180, 175, 200, 190, 210])
quarterly = monthly_sales.reshape(4, 3)  # 4 quarters, 3 months each

print("\nReal example - Monthly to Quarterly:")
print("Quarterly sales (each row = 1 quarter):")
print(quarterly)
print(f"Q1 Total: {np.sum(quarterly[0])}")
print(f"Q2 Total: {np.sum(quarterly[1])}")

print("\n" + "="*70)
print("PART 3: ARRAY STACKING & COMBINING")
print("="*70)

# Two separate arrays
jan_sales = np.array([100, 120, 90])
feb_sales = np.array([150, 140, 110])
mar_sales = np.array([200, 160, 130])

# Stack vertically (vstack) - stack as rows
vertical = np.vstack([jan_sales, feb_sales, mar_sales])
print("Vertical stack (vstack) - each month as row:")
print(vertical)

# Stack horizontally (hstack) - side by side
horizontal = np.hstack([jan_sales, feb_sales, mar_sales])
print(f"\nHorizontal stack (hstack): {horizontal}")

# Column stack - create columns
column = np.column_stack([jan_sales, feb_sales, mar_sales])
print("\nColumn stack - each month as column:")
print(column)

# Concatenate with axis
concat_axis0 = np.concatenate([jan_sales.reshape(1, -1), 
                                feb_sales.reshape(1, -1)], axis=0)
print("\nConcatenate along axis 0 (rows):")
print(concat_axis0)

print("\n" + "="*70)
print("PART 4: ADVANCED INDEXING")
print("="*70)

sales = np.array([
    [100, 150, 200, 250],
    [120, 140, 160, 180],
    [90, 110, 130, 150]
])

print("Sales matrix:")
print(sales)

# Fancy indexing - select specific rows
selected_rows = sales[[0, 2]]  # Select row 0 and row 2
print(f"\nRows 0 and 2:")
print(selected_rows)

# Fancy indexing - specific elements
# Get sales[0,1], sales[1,2], sales[2,3]
rows = np.array([0, 1, 2])
cols = np.array([1, 2, 3])
specific_elements = sales[rows, cols]
print(f"\nSpecific elements [0,1], [1,2], [2,3]: {specific_elements}")

# Boolean mask with multiple conditions
mask = (sales >= 120) & (sales <= 160)
filtered = sales[mask]
print(f"\nSales between 120 and 160: {filtered}")

print("\n" + "="*70)
print("PART 5: BROADCASTING")
print("="*70)

# Broadcasting: operating on arrays of different shapes
sales = np.array([
    [100, 150, 200],
    [120, 140, 160],
    [90, 110, 130]
])

# Add 10% to all values (scalar broadcasting)
increased = sales * 1.1
print("Original:")
print(sales)
print("\nAfter 10% increase (broadcasting):")
print(increased.astype(int))

# Add different value to each column (1D to 2D broadcasting)
column_adjustments = np.array([5, 10, 15])  # Add 5 to col1, 10 to col2, 15 to col3
adjusted = sales + column_adjustments
print(f"\nColumn adjustments {column_adjustments}:")
print(adjusted)

# Add different value to each row
row_adjustments = np.array([[10], [20], [30]])  # Must be column vector
adjusted_rows = sales + row_adjustments
print(f"\nRow adjustments:")
print(adjusted_rows)

print("\n" + "="*70)
print("PART 6: PRACTICAL ANALYTICS SCENARIO")
print("="*70)

# Scenario: 6-month sales data for 4 products across 3 regions
# Shape: (3 regions, 4 products, 6 months)

np.random.seed(42)  # For reproducibility
sales_data = np.random.randint(80, 200, size=(3, 4, 6))

print("Sales data shape:", sales_data.shape)
print("(3 regions × 4 products × 6 months)")

# Analysis 1: Total sales per region
region_totals = np.sum(sales_data, axis=(1, 2))  # Sum over products and months
print(f"\nTotal sales per region: {region_totals}")

# Analysis 2: Total sales per product (across all regions and months)
product_totals = np.sum(sales_data, axis=(0, 2))  # Sum over regions and months
print(f"Total sales per product: {product_totals}")

# Analysis 3: Monthly totals (across all regions and products)
monthly_totals = np.sum(sales_data, axis=(0, 1))  # Sum over regions and products
print(f"Monthly totals: {monthly_totals}")

# Analysis 4: Average sales per product per region
avg_per_product_region = np.mean(sales_data, axis=2)  # Average over months
print("\nAverage sales per product per region:")
print(avg_per_product_region.astype(int))

# Analysis 5: Find best performing region-product combo
max_value = np.max(sales_data)
max_position = np.unravel_index(np.argmax(sales_data), sales_data.shape)
print(f"\nBest sale: {max_value}")
print(f"Region {max_position[0]}, Product {max_position[1]}, Month {max_position[2]}")

# Analysis 6: Growth analysis - first vs last month
first_month = sales_data[:, :, 0]  # All regions, all products, first month
last_month = sales_data[:, :, -1]  # All regions, all products, last month
growth = ((last_month - first_month) / first_month * 100)

print("\nGrowth % (First month vs Last month):")
print(growth.astype(int))

print("\n" + "="*70)
print("NUMPY ADVANCED COMPLETE ✅")
print("="*70)