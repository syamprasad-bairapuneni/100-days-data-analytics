# Day 45 - Real Sales Analytics with NumPy
# Practical business problem solving

import numpy as np

print("="*70)
print("SALES ANALYTICS - QUARTERLY PERFORMANCE ANALYSIS")
print("="*70)

# Scenario: You're analyzing quarterly sales for 5 products across 4 quarters
# Data: Sales in thousands of rupees

# Create sales data
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Sales data (5 products x 4 quarters)
sales_data = np.array([
    [450, 480, 520, 550],    # Laptop
    [120, 135, 128, 142],    # Mouse
    [85, 92, 88, 95],        # Keyboard
    [320, 310, 340, 360],    # Monitor
    [95, 105, 110, 120]      # Headphones
])

print(f"\nSales Data (in thousands):")
print(f"{'Product':<12} {'Q1':>8} {'Q2':>8} {'Q3':>8} {'Q4':>8}")
print("-" * 70)
for i, product in enumerate(products):
    print(f"{product:<12} {sales_data[i, 0]:>8.0f} {sales_data[i, 1]:>8.0f} "
          f"{sales_data[i, 2]:>8.0f} {sales_data[i, 3]:>8.0f}")

# ANALYSIS 1: Total sales per product
print("\n" + "="*70)
print("ANALYSIS 1: TOTAL SALES PER PRODUCT")
print("="*70)

product_totals = np.sum(sales_data, axis=1)  # axis=1 means sum across columns
for i, product in enumerate(products):
    print(f"{product:<12}: ₹{product_totals[i]:,.0f}k")

top_product_idx = np.argmax(product_totals)
print(f"\n🏆 Top Product: {products[top_product_idx]} "
      f"(₹{product_totals[top_product_idx]:,.0f}k)")

# ANALYSIS 2: Total sales per quarter
print("\n" + "="*70)
print("ANALYSIS 2: TOTAL SALES PER QUARTER")
print("="*70)

quarter_totals = np.sum(sales_data, axis=0)  # axis=0 means sum across rows
for i, quarter in enumerate(quarters):
    print(f"{quarter}: ₹{quarter_totals[i]:,.0f}k")

# Quarter-over-quarter growth
qoq_growth = np.diff(quarter_totals) / quarter_totals[:-1] * 100
print(f"\nQuarter-over-Quarter Growth:")
for i in range(len(qoq_growth)):
    print(f"{quarters[i]} → {quarters[i+1]}: {qoq_growth[i]:+.2f}%")

# ANALYSIS 3: Average sales per product
print("\n" + "="*70)
print("ANALYSIS 3: AVERAGE QUARTERLY SALES")
print("="*70)

product_avg = np.mean(sales_data, axis=1)
for i, product in enumerate(products):
    print(f"{product:<12}: ₹{product_avg[i]:,.2f}k per quarter")

# ANALYSIS 4: Performance consistency (using standard deviation)
print("\n" + "="*70)
print("ANALYSIS 4: SALES CONSISTENCY (Lower is more consistent)")
print("="*70)

product_std = np.std(sales_data, axis=1)
for i, product in enumerate(products):
    consistency = "High" if product_std[i] < 30 else "Medium" if product_std[i] < 50 else "Low"
    print(f"{product:<12}: Std Dev = {product_std[i]:6.2f} ({consistency} consistency)")

most_consistent_idx = np.argmin(product_std)
print(f"\n📊 Most Consistent: {products[most_consistent_idx]}")

# ANALYSIS 5: Products exceeding target (e.g., 400k total)
print("\n" + "="*70)
print("ANALYSIS 5: PRODUCTS EXCEEDING 400K TARGET")
print("="*70)

target = 400
exceeding_target = product_totals > target
for i, product in enumerate(products):
    if exceeding_target[i]:
        print(f"✅ {product}: ₹{product_totals[i]:,.0f}k "
              f"(+₹{product_totals[i] - target:,.0f}k above target)")

# ANALYSIS 6: Best and worst quarters per product
print("\n" + "="*70)
print("ANALYSIS 6: BEST & WORST QUARTERS PER PRODUCT")
print("="*70)

for i, product in enumerate(products):
    best_q_idx = np.argmax(sales_data[i])
    worst_q_idx = np.argmin(sales_data[i])
    
    print(f"\n{product}:")
    print(f"  Best:  {quarters[best_q_idx]} - ₹{sales_data[i, best_q_idx]:.0f}k")
    print(f"  Worst: {quarters[worst_q_idx]} - ₹{sales_data[i, worst_q_idx]:.0f}k")
    print(f"  Range: ₹{sales_data[i, best_q_idx] - sales_data[i, worst_q_idx]:.0f}k")

# ANALYSIS 7: Overall business metrics
print("\n" + "="*70)
print("ANALYSIS 7: OVERALL BUSINESS METRICS")
print("="*70)

total_revenue = np.sum(sales_data)
avg_quarterly_revenue = np.mean(quarter_totals)
growth_rate = ((quarter_totals[-1] - quarter_totals[0]) / quarter_totals[0]) * 100

print(f"Total Annual Revenue: ₹{total_revenue:,.0f}k")
print(f"Average Quarterly Revenue: ₹{avg_quarterly_revenue:,.2f}k")
print(f"Q1 to Q4 Growth Rate: {growth_rate:+.2f}%")
print(f"Best Quarter: {quarters[np.argmax(quarter_totals)]} "
      f"(₹{np.max(quarter_totals):,.0f}k)")
print(f"Worst Quarter: {quarters[np.argmin(quarter_totals)]} "
      f"(₹{np.min(quarter_totals):,.0f}k)")

print("\n" + "="*70)
print("ANALYSIS COMPLETE ✅")
print("="*70)