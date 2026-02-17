# Day 47 - Creating Pandas DataFrames
# Author: Syamprasad
# Date: February 17, 2026

import pandas as pd
import numpy as np

print("="*70)
print("PART 1: CREATING DATAFRAMES FROM DICTIONARIES")
print("="*70)

# Method 1: Dictionary with lists
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [45000, 500, 1200, 15000, 2500],
    'Stock': [50, 200, 150, 75, 120],
    'Category': ['Computer', 'Accessory', 'Accessory', 'Computer', 'Accessory']
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Method 2: List of dictionaries (each dict = one row)
sales_data = [
    {'Date': '2026-01-01', 'Product': 'Laptop', 'Revenue': 45000, 'Region': 'North'},
    {'Date': '2026-01-02', 'Product': 'Mouse', 'Revenue': 500, 'Region': 'South'},
    {'Date': '2026-01-03', 'Product': 'Keyboard', 'Revenue': 1200, 'Region': 'East'}
]

df_sales = pd.DataFrame(sales_data)
print("\nDataFrame from list of dictionaries:")
print(df_sales)

# Method 3: Dictionary of Series
product_series = pd.Series(['Laptop', 'Mouse', 'Keyboard'])
price_series = pd.Series([45000, 500, 1200])

df_series = pd.DataFrame({
    'Product': product_series,
    'Price': price_series
})
print("\nDataFrame from Series:")
print(df_series)

print("\n" + "="*70)
print("PART 2: CREATING FROM NUMPY ARRAYS")
print("="*70)

# Create DataFrame from NumPy array
np_data = np.array([
    [100, 150, 200],
    [120, 140, 160],
    [90, 110, 130]
])

df_numpy = pd.DataFrame(
    np_data,
    columns=['Jan', 'Feb', 'Mar'],
    index=['Product_A', 'Product_B', 'Product_C']
)

print("DataFrame from NumPy array:")
print(df_numpy)

print("\n" + "="*70)
print("PART 3: CREATING WITH DATE RANGES")
print("="*70)

# Create time-series data
dates = pd.date_range('2026-01-01', periods=10, freq='D')
revenue = np.random.randint(10000, 50000, size=10)

df_timeseries = pd.DataFrame({
    'Date': dates,
    'Revenue': revenue
})

print("Time-series DataFrame:")
print(df_timeseries)

# Set date as index
df_timeseries_indexed = df_timeseries.set_index('Date')
print("\nWith Date as index:")
print(df_timeseries_indexed.head())

print("\n" + "="*70)
print("PART 4: CREATING SAMPLE DATA FOR PRACTICE")
print("="*70)

# Generate realistic sales dataset
np.random.seed(42)

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
regions = ['North', 'South', 'East', 'West']
n_rows = 100

sample_data = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=n_rows, freq='D'),
    'Product': np.random.choice(products, n_rows),
    'Region': np.random.choice(regions, n_rows),
    'Quantity': np.random.randint(1, 20, n_rows),
    'Unit_Price': np.random.randint(500, 50000, n_rows),
})

# Calculate revenue
sample_data['Revenue'] = sample_data['Quantity'] * sample_data['Unit_Price']

print("Sample sales dataset (first 10 rows):")
print(sample_data.head(10))
print(f"\nDataset info:")
print(f"Total records: {len(sample_data)}")
print(f"Date range: {sample_data['Date'].min()} to {sample_data['Date'].max()}")
print(f"Total revenue: ₹{sample_data['Revenue'].sum():,.2f}")

# Save to CSV for future use
sample_data.to_csv('sales_data.csv', index=False)
print("\n✅ Sample data saved to 'sales_data.csv'")

print("\n" + "="*70)
print("DATAFRAME CREATION COMPLETE ✅")
print("="*70)