# Day 45 - NumPy Fundamentals
# Author: Syamprasad
# Date: February 14, 2026

import numpy as np

print("="*60)
print("PART 1: CREATING NUMPY ARRAYS")
print("="*60)

# 1. From Python list
sales = [1200, 1500, 980, 2100, 1750]
sales_array = np.array(sales)
print(f"From list: {sales_array}")
print(f"Type: {type(sales_array)}")
print(f"Data type: {sales_array.dtype}")

# 2. Using arange (like range, but returns array)
numbers = np.arange(0, 10, 2)  # start, stop, step
print(f"\narange(0, 10, 2): {numbers}")

# 3. Using linspace (evenly spaced values)
even_spacing = np.linspace(0, 100, 5)  # start, stop, count
print(f"linspace(0, 100, 5): {even_spacing}")

# 4. Arrays of zeros, ones
zeros = np.zeros(5)
ones = np.ones(5)
print(f"\nZeros: {zeros}")
print(f"Ones: {ones}")

# 5. Random arrays (useful for testing)
random_sales = np.random.randint(1000, 5000, size=10)
print(f"Random sales (10 values): {random_sales}")

print("\n" + "="*60)
print("PART 2: ARRAY PROPERTIES")
print("="*60)

# Create a 2D array (like Excel table)
monthly_sales = np.array([
    [1200, 1500, 1800],  # Product A
    [980, 1100, 1250],   # Product B
    [2100, 2300, 2500]   # Product C
])

print(f"Monthly Sales:\n{monthly_sales}")
print(f"\nShape (rows, cols): {monthly_sales.shape}")
print(f"Dimensions: {monthly_sales.ndim}")
print(f"Total elements: {monthly_sales.size}")
print(f"Data type: {monthly_sales.dtype}")

print("\n" + "="*60)
print("PART 3: ARRAY INDEXING & SLICING")
print("="*60)

sales = np.array([1200, 1500, 980, 2100, 1750, 1300, 1900])

# Indexing (same as lists)
print(f"First sale: {sales[0]}")
print(f"Last sale: {sales[-1]}")

# Slicing
print(f"First 3 sales: {sales[:3]}")
print(f"Last 3 sales: {sales[-3:]}")
print(f"Every other sale: {sales[::2]}")

# 2D indexing
print(f"\nProduct B, Month 2: {monthly_sales[1, 1]}")
print(f"All sales for Product A: {monthly_sales[0, :]}")
print(f"All sales for Month 1: {monthly_sales[:, 0]}")

print("\n" + "="*60)
print("PART 4: BOOLEAN INDEXING (POWERFUL FOR ANALYTICS)")
print("="*60)

sales = np.array([1200, 1500, 980, 2100, 1750, 1300, 1900])

# Filter sales > 1500
high_sales = sales[sales > 1500]
print(f"Sales > 1500: {high_sales}")

# Filter sales between 1000 and 1800
mid_sales = sales[(sales >= 1000) & (sales <= 1800)]
print(f"Sales 1000-1800: {mid_sales}")

# Count how many sales > 1500
count_high = np.sum(sales > 1500)
print(f"Count of high sales: {count_high}")

print("\n" + "="*60)
print("PART 5: ARRAY OPERATIONS (VECTORIZATION)")
print("="*60)

prices = np.array([100, 200, 150, 300, 250])

# Apply 10% discount to ALL prices (no loop needed!)
discounted = prices * 0.9
print(f"Original prices: {prices}")
print(f"After 10% discount: {discounted}")

# Add GST (18%)
with_gst = prices * 1.18
print(f"With 18% GST: {with_gst}")

# Operations between arrays
jan_sales = np.array([1000, 1500, 1200])
feb_sales = np.array([1100, 1400, 1300])

# Month-over-month growth
growth = feb_sales - jan_sales
growth_pct = (growth / jan_sales) * 100

print(f"\nJan Sales: {jan_sales}")
print(f"Feb Sales: {feb_sales}")
print(f"Growth: {growth}")
print(f"Growth %: {growth_pct}")

print("\n" + "="*60)
print("PART 6: STATISTICAL FUNCTIONS")
print("="*60)

sales = np.array([1200, 1500, 980, 2100, 1750, 1300, 1900, 1600])

print(f"Sales data: {sales}")
print(f"\nMean (Average): {np.mean(sales):.2f}")
print(f"Median: {np.median(sales):.2f}")
print(f"Standard Deviation: {np.std(sales):.2f}")
print(f"Min: {np.min(sales)}")
print(f"Max: {np.max(sales)}")
print(f"Sum: {np.sum(sales)}")

# Percentiles
print(f"\n25th Percentile: {np.percentile(sales, 25):.2f}")
print(f"75th Percentile: {np.percentile(sales, 75):.2f}")

# Cumulative sum (running total)
cumsum = np.cumsum(sales)
print(f"\nCumulative Sales: {cumsum}")

print("\n" + "="*60)
print("NUMPY BASICS COMPLETE ✅")
print("="*60)