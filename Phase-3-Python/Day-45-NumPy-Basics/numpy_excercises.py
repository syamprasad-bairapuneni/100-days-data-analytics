# Day 45 - NumPy Practice Exercises
# Hands-on problem solving

import numpy as np

print("="*60)
print("NUMPY PRACTICE EXERCISES")
print("="*60)

# EXERCISE 1: Customer Purchase Analysis
print("\n--- EXERCISE 1: Customer Purchase Analysis ---")

# Monthly purchases by 8 customers (in rupees)
purchases = np.array([1200, 850, 2100, 950, 3200, 1100, 1800, 1400])

# Tasks:
print(f"Customer purchases: {purchases}")
print(f"1. Average purchase: ₹{np.mean(purchases):.2f}")
print(f"2. Customers above average: {np.sum(purchases > np.mean(purchases))}")
print(f"3. Top 3 spenders: ₹{np.sort(purchases)[-3:]}")
print(f"4. Purchase range: ₹{np.ptp(purchases)}")  # ptp = peak-to-peak (max-min)

# Segment customers
low_spenders = purchases[purchases < 1000]
mid_spenders = purchases[(purchases >= 1000) & (purchases < 2000)]
high_spenders = purchases[purchases >= 2000]

print(f"5. Customer segments:")
print(f"   Low (<1000): {len(low_spenders)} customers")
print(f"   Mid (1000-2000): {len(mid_spenders)} customers")
print(f"   High (>2000): {len(high_spenders)} customers")

# EXERCISE 2: Revenue Forecasting
print("\n--- EXERCISE 2: Revenue Forecasting ---")

# Last 6 months revenue
revenue = np.array([450, 480, 510, 530, 560, 590])

print(f"Historical revenue: {revenue}")

# Calculate month-over-month growth rates
mom_growth = np.diff(revenue) / revenue[:-1] * 100
avg_growth = np.mean(mom_growth)

print(f"Month-over-month growth rates: {mom_growth}")
print(f"Average growth rate: {avg_growth:.2f}%")

# Forecast next 3 months (simple linear projection)
last_value = revenue[-1]
forecast = []
for i in range(1, 4):
    forecast.append(last_value * (1 + avg_growth/100)**i)

forecast = np.array(forecast)
print(f"Forecasted next 3 months: {forecast.astype(int)}")

# EXERCISE 3: A/B Test Analysis
print("\n--- EXERCISE 3: A/B Test Analysis ---")

# Conversion rates for two variants (100 users each)
variant_a = np.array([1, 0, 0, 1, 1, 0, 1, 0, 0, 1] * 10)  # 40% conversion
variant_b = np.array([1, 1, 0, 1, 1, 0, 1, 1, 0, 1] * 10)  # 60% conversion

conv_rate_a = np.mean(variant_a) * 100
conv_rate_b = np.mean(variant_b) * 100
improvement = ((conv_rate_b - conv_rate_a) / conv_rate_a) * 100

print(f"Variant A conversion rate: {conv_rate_a:.1f}%")
print(f"Variant B conversion rate: {conv_rate_b:.1f}%")
print(f"Improvement: {improvement:+.1f}%")
print(f"Winner: Variant {'B' if conv_rate_b > conv_rate_a else 'A'}")

# EXERCISE 4: Outlier Detection
print("\n--- EXERCISE 4: Outlier Detection ---")

# Daily website visitors
visitors = np.array([1200, 1150, 1180, 1220, 1190, 3500, 1210, 1175, 1195, 1230])

mean_visitors = np.mean(visitors)
std_visitors = np.std(visitors)

# Outliers: values beyond 2 standard deviations
outliers = visitors[np.abs(visitors - mean_visitors) > 2 * std_visitors]

print(f"Daily visitors: {visitors}")
print(f"Mean: {mean_visitors:.0f}, Std: {std_visitors:.0f}")
print(f"Outliers detected: {outliers}")

# Clean data (remove outliers)
clean_visitors = visitors[np.abs(visitors - mean_visitors) <= 2 * std_visitors]
print(f"Clean data (no outliers): {clean_visitors}")
print(f"Clean data mean: {np.mean(clean_visitors):.0f}")

print("\n" + "="*60)
print("ALL EXERCISES COMPLETE ✅")
print("="*60)