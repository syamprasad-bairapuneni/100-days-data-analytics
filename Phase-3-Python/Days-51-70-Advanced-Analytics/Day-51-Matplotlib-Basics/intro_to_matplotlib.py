# Day 51 - Introduction to Matplotlib
# Data Visualization Basics
# Author: Syamprasad
# Date: February 21, 2026

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("="*60)
print("DAY 51 - MATPLOTLIB BASICS")
print("Learning Data Visualization")
print("="*60)

# ============================================================
# PART 1: LINE CHART - TREND ANALYSIS
# ============================================================

print("\n📈 Creating Line Chart...")

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [45000, 52000, 48000, 61000, 58000, 67000]

# Create figure
plt.figure(figsize=(10, 6))

# Plot line
plt.plot(months, sales, 
         marker='o',           # Add dots at data points
         linewidth=2,          # Line thickness
         markersize=8,         # Dot size
         color='steelblue',    # Line color
         markerfacecolor='coral')  # Dot color

# Add labels and title
plt.title('Monthly Sales Trend Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (₹)', fontsize=12)

# Add grid for better readability
plt.grid(True, alpha=0.3, linestyle='--')

# Format y-axis to show values in thousands
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{int(x/1000)}K'))

# Save the chart
plt.tight_layout()
plt.savefig('sales_trend_line.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Line chart saved: sales_trend_line.png")

# ============================================================
# PART 2: BAR CHART - COMPARISON
# ============================================================

print("\n📊 Creating Bar Chart...")

# Create figure
plt.figure(figsize=(10, 6))

# Create bars
bars = plt.bar(months, sales, 
               color='steelblue', 
               alpha=0.7,
               edgecolor='black',
               linewidth=1.2)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'₹{int(height/1000)}K',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# Labels and title
plt.title('Monthly Sales Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (₹)', fontsize=12)

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{int(x/1000)}K'))

# Save
plt.tight_layout()
plt.savefig('sales_comparison_bar.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Bar chart saved: sales_comparison_bar.png")

# ============================================================
# PART 3: SCATTER PLOT - RELATIONSHIP ANALYSIS
# ============================================================

print("\n🔵 Creating Scatter Plot...")

# Generate sample data
np.random.seed(51)
customers = np.random.randint(50, 150, 50)
revenue = customers * np.random.randint(300, 800, 50) + np.random.randint(-5000, 5000, 50)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(customers, revenue, 
            alpha=0.6,           # Transparency
            s=100,               # Size of dots
            c='coral',           # Color
            edgecolors='black',  # Dot border
            linewidth=1)

# Labels and title
plt.title('Customer Count vs Revenue Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Number of Customers', fontsize=12)
plt.ylabel('Revenue (₹)', fontsize=12)

# Add grid
plt.grid(True, alpha=0.3, linestyle='--')

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{int(x/1000)}K'))

# Save
plt.tight_layout()
plt.savefig('customer_revenue_scatter.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Scatter plot saved: customer_revenue_scatter.png")

# ============================================================
# PART 4: BONUS - ALL THREE IN ONE FIGURE
# ============================================================

print("\n📋 Creating Combined Dashboard...")

# Create figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Subplot 1: Line Chart
axes[0].plot(months, sales, marker='o', linewidth=2, markersize=8, color='steelblue')
axes[0].set_title('Sales Trend', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Sales (₹)')
axes[0].grid(True, alpha=0.3)

# Subplot 2: Bar Chart
axes[1].bar(months, sales, color='coral', alpha=0.7)
axes[1].set_title('Sales Comparison', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Sales (₹)')

# Subplot 3: Scatter Plot
axes[2].scatter(customers, revenue, alpha=0.6, s=50, c='green')
axes[2].set_title('Customers vs Revenue', fontsize=14, fontweight='bold')
axes[2].set_xlabel('Customers')
axes[2].set_ylabel('Revenue (₹)')
axes[2].grid(True, alpha=0.3)

# Overall title
fig.suptitle('Day 51 - Sales Analytics Dashboard', fontsize=18, fontweight='bold', y=1.02)

# Save combined dashboard
plt.tight_layout()
plt.savefig('combined_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Combined dashboard saved: combined_dashboard.png")

# ============================================================
# SUMMARY
# ============================================================

print("\n" + "="*60)
print("DAY 51 COMPLETE ✅")
print("="*60)
print("\n📊 Visualizations Created:")
print("  1. ✅ sales_trend_line.png - Line chart")
print("  2. ✅ sales_comparison_bar.png - Bar chart")
print("  3. ✅ customer_revenue_scatter.png - Scatter plot")
print("  4. ✅ combined_dashboard.png - All three combined")
print("\n🎯 Skills Learned:")
print("  • Creating figures and axes")
print("  • Line, bar, and scatter plots")
print("  • Customizing colors, markers, and styles")
print("  • Adding labels, titles, and grids")
print("  • Formatting axis values")
print("  • Saving high-quality images")
print("  • Creating multi-plot dashboards")
print("\n💡 Key Takeaway:")
print("  Matplotlib transforms raw data into visual insights!")
print("="*60)