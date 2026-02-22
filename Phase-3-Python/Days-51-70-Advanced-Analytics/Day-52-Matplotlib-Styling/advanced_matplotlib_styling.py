# Day 52 - Advanced Matplotlib Styling
# Professional Chart Customization
# Author: Syamprasad
# Date: February 22, 2026

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set style for all charts
plt.style.use('seaborn-v0_8-darkgrid')

print("="*70)
print("DAY 52 - ADVANCED MATPLOTLIB STYLING")
print("Creating Professional, Publication-Quality Visualizations")
print("="*70)

# =========================================================================
# PART 1: COLOR SCHEMES & PALETTES
# =========================================================================

print("\n🎨 PART 1: Professional Color Schemes")

# Sample data
categories = ['Q1', 'Q2', 'Q3', 'Q4']
revenue_2024 = [450, 520, 580, 640]
revenue_2025 = [480, 550, 620, 680]

# Professional color palette
colors_professional = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
colors_corporate = ['#003f5c', '#58508d', '#bc5090', '#ff6361']

# Create comparison of color schemes
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: Default colors
axes[0, 0].bar(categories, revenue_2024, alpha=0.8)
axes[0, 0].set_title('Default Colors', fontsize=14, fontweight='bold', pad=15)
axes[0, 0].set_ylabel('Revenue (₹ Lakhs)', fontsize=11)

# Chart 2: Professional palette
axes[0, 1].bar(categories, revenue_2024, color=colors_professional, alpha=0.8)
axes[0, 1].set_title('Professional Palette', fontsize=14, fontweight='bold', pad=15)
axes[0, 1].set_ylabel('Revenue (₹ Lakhs)', fontsize=11)

# Chart 3: Corporate palette
axes[1, 0].bar(categories, revenue_2024, color=colors_corporate, alpha=0.8)
axes[1, 0].set_title('Corporate Palette', fontsize=14, fontweight='bold', pad=15)
axes[1, 0].set_ylabel('Revenue (₹ Lakhs)', fontsize=11)

# Chart 4: Gradient effect
colors_gradient = plt.cm.viridis(np.linspace(0.3, 0.9, len(categories)))
axes[1, 1].bar(categories, revenue_2024, color=colors_gradient, alpha=0.8)
axes[1, 1].set_title('Gradient Palette', fontsize=14, fontweight='bold', pad=15)
axes[1, 1].set_ylabel('Revenue (₹ Lakhs)', fontsize=11)

plt.suptitle('Color Scheme Comparison', fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('01_color_schemes.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Color schemes comparison saved")

# =========================================================================
# PART 2: PROFESSIONAL STYLING - REVENUE COMPARISON
# =========================================================================

print("\n📊 PART 2: Professional Bar Chart with Full Styling")

fig, ax = plt.subplots(figsize=(12, 7))

# Set positions
x = np.arange(len(categories))
width = 0.35

# Create bars with professional styling
bars1 = ax.bar(x - width/2, revenue_2024, width, 
               label='2024', 
               color='#2E86AB',
               alpha=0.85,
               edgecolor='black',
               linewidth=1.2)

bars2 = ax.bar(x + width/2, revenue_2025, width,
               label='2025',
               color='#F18F01',
               alpha=0.85,
               edgecolor='black',
               linewidth=1.2)

# Add value labels on bars
def add_value_labels(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'₹{int(height)}L',
                ha='center', va='bottom',
                fontsize=10, fontweight='bold')

add_value_labels(bars1, ax)
add_value_labels(bars2, ax)

# Customize axes
ax.set_xlabel('Quarter', fontsize=13, fontweight='bold')
ax.set_ylabel('Revenue (₹ Lakhs)', fontsize=13, fontweight='bold')
ax.set_title('Quarterly Revenue Comparison: 2024 vs 2025',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11)

# Add legend with styling
ax.legend(loc='upper left', fontsize=11, framealpha=0.9,
          edgecolor='black', fancybox=True, shadow=True)

# Add grid for better readability
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)
ax.set_axisbelow(True)

# Set y-axis limits with padding
ax.set_ylim(0, max(revenue_2025) * 1.15)

# Add background color
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('white')

# Add subtle border
for spine in ax.spines.values():
    spine.set_edgecolor('#cccccc')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.savefig('02_professional_bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Professional bar chart saved")

# =========================================================================
# PART 3: ANNOTATED LINE CHART WITH HIGHLIGHTS
# =========================================================================

print("\n📈 PART 3: Annotated Line Chart with Key Highlights")

# Generate data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [420, 450, 480, 520, 490, 560, 590, 610, 580, 640, 680, 720]

fig, ax = plt.subplots(figsize=(14, 7))

# Main line plot
ax.plot(months, sales,
        color='#2E86AB',
        linewidth=3,
        marker='o',
        markersize=8,
        markerfacecolor='white',
        markeredgewidth=2,
        markeredgecolor='#2E86AB',
        label='Monthly Sales')

# Highlight highest and lowest points
max_idx = sales.index(max(sales))
min_idx = sales.index(min(sales))

# Highlight max point
ax.scatter(max_idx, sales[max_idx], 
          color='#27AE60', s=300, zorder=5, 
          edgecolor='black', linewidth=2)
ax.annotate(f'Peak: ₹{sales[max_idx]}L',
           xy=(max_idx, sales[max_idx]),
           xytext=(max_idx-1.5, sales[max_idx]+30),
           fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='#27AE60', alpha=0.8),
           arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3',
                          color='black', lw=2))

# Highlight min point
ax.scatter(min_idx, sales[min_idx],
          color='#E74C3C', s=300, zorder=5,
          edgecolor='black', linewidth=2)
ax.annotate(f'Low: ₹{sales[min_idx]}L',
           xy=(min_idx, sales[min_idx]),
           xytext=(min_idx+1, sales[min_idx]-40),
           fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='#E74C3C', alpha=0.8),
           arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.3',
                          color='black', lw=2))

# Add average line
avg_sales = np.mean(sales)
ax.axhline(y=avg_sales, color='#E67E22', linestyle='--', 
          linewidth=2, alpha=0.7, label=f'Average: ₹{avg_sales:.0f}L')

# Shade area under curve
ax.fill_between(range(len(months)), sales, alpha=0.2, color='#2E86AB')

# Styling
ax.set_xlabel('Month', fontsize=13, fontweight='bold')
ax.set_ylabel('Sales (₹ Lakhs)', fontsize=13, fontweight='bold')
ax.set_title('2025 Sales Performance - Monthly Analysis',
            fontsize=16, fontweight='bold', pad=20)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)
ax.set_axisbelow(True)

# Legend
ax.legend(loc='upper left', fontsize=11, framealpha=0.9,
         edgecolor='black', fancybox=True, shadow=True)

# Background
ax.set_facecolor('#f8f9fa')

# Y-axis formatting
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{int(x)}L'))

plt.tight_layout()
plt.savefig('03_annotated_line_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Annotated line chart saved")

# =========================================================================
# PART 4: MULTI-METRIC DASHBOARD
# =========================================================================

print("\n📋 PART 4: Professional Multi-Metric Dashboard")

# Generate sample data
np.random.seed(52)
regions = ['North', 'South', 'East', 'West', 'Central']
revenue = [850, 720, 680, 590, 450]
growth = [12.5, 8.3, 15.7, 6.2, 10.1]
customers = [1250, 980, 1100, 750, 620]

# Create dashboard with 4 panels
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# Panel 1: Revenue by Region (Bar Chart)
ax1 = fig.add_subplot(gs[0, 0])
colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(regions)))
bars = ax1.barh(regions, revenue, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, revenue)):
    ax1.text(val + 20, bar.get_y() + bar.get_height()/2,
            f'₹{val}L', va='center', fontweight='bold', fontsize=10)

ax1.set_xlabel('Revenue (₹ Lakhs)', fontsize=11, fontweight='bold')
ax1.set_title('Regional Revenue Distribution', fontsize=13, fontweight='bold', pad=15)
ax1.set_facecolor('#f8f9fa')
ax1.grid(axis='x', alpha=0.3, linestyle='--')

# Panel 2: Growth Rate (Line + Bar)
ax2 = fig.add_subplot(gs[0, 1])
x_pos = np.arange(len(regions))

# Bar chart for growth
bars2 = ax2.bar(x_pos, growth, color='#3498DB', alpha=0.7, edgecolor='black', linewidth=1.2)

# Add target line
target = 10
ax2.axhline(y=target, color='#E74C3C', linestyle='--', linewidth=2, label=f'Target: {target}%')

# Color bars based on target
for i, (bar, val) in enumerate(zip(bars2, growth)):
    if val >= target:
        bar.set_color('#27AE60')  # Green if above target
    else:
        bar.set_color('#E74C3C')  # Red if below target
    
    # Add value labels
    ax2.text(bar.get_x() + bar.get_width()/2, val + 0.5,
            f'{val}%', ha='center', fontweight='bold', fontsize=10)

ax2.set_xticks(x_pos)
ax2.set_xticklabels(regions, fontsize=10)
ax2.set_ylabel('Growth Rate (%)', fontsize=11, fontweight='bold')
ax2.set_title('Year-over-Year Growth Rate', fontsize=13, fontweight='bold', pad=15)
ax2.legend(loc='upper right', fontsize=10)
ax2.set_facecolor('#f8f9fa')
ax2.grid(axis='y', alpha=0.3, linestyle='--')

# Panel 3: Customer Distribution (Pie Chart)
ax3 = fig.add_subplot(gs[1, 0])
colors_pie = ['#3498DB', '#E74C3C', '#F39C12', '#9B59B6', '#1ABC9C']
wedges, texts, autotexts = ax3.pie(customers, 
                                     labels=regions,
                                     autopct='%1.1f%%',
                                     colors=colors_pie,
                                     startangle=90,
                                     explode=(0.05, 0, 0, 0, 0),
                                     shadow=True,
                                     textprops={'fontsize': 10, 'fontweight': 'bold'})

# Make percentage text white and bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

ax3.set_title('Customer Distribution by Region', fontsize=13, fontweight='bold', pad=15)

# Panel 4: Revenue vs Customers (Scatter)
ax4 = fig.add_subplot(gs[1, 1])

# Scatter plot
scatter = ax4.scatter(customers, revenue, 
                     s=400, 
                     c=growth,
                     cmap='RdYlGn',
                     alpha=0.7,
                     edgecolor='black',
                     linewidth=2)

# Add region labels
for i, region in enumerate(regions):
    ax4.annotate(region, 
                (customers[i], revenue[i]),
                fontsize=10,
                fontweight='bold',
                ha='center',
                va='center')

# Colorbar for growth rate
cbar = plt.colorbar(scatter, ax=ax4)
cbar.set_label('Growth Rate (%)', fontsize=10, fontweight='bold')

ax4.set_xlabel('Number of Customers', fontsize=11, fontweight='bold')
ax4.set_ylabel('Revenue (₹ Lakhs)', fontsize=11, fontweight='bold')
ax4.set_title('Revenue vs Customer Base', fontsize=13, fontweight='bold', pad=15)
ax4.set_facecolor('#f8f9fa')
ax4.grid(True, alpha=0.3, linestyle='--')

# Overall title
fig.suptitle('Regional Performance Dashboard - Q4 2025', 
            fontsize=18, fontweight='bold', y=0.98)

plt.savefig('04_professional_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Professional dashboard saved")

# =========================================================================
# PART 5: BEFORE & AFTER COMPARISON
# =========================================================================

print("\n🔄 PART 5: Before & After - Styling Impact")

# Sample data
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales_data = [450, 380, 520, 290]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# BEFORE - Basic styling
ax1.bar(products, sales_data)
ax1.set_title('Before: Basic Chart')
ax1.set_ylabel('Sales')

# AFTER - Professional styling
bars = ax2.bar(products, sales_data,
              color=['#2E86AB', '#A23B72', '#F18F01', '#27AE60'],
              alpha=0.85,
              edgecolor='black',
              linewidth=1.5)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'₹{int(height)}L',
            ha='center', va='bottom',
            fontsize=11, fontweight='bold')

# Styling
ax2.set_ylabel('Sales (₹ Lakhs)', fontsize=12, fontweight='bold')
ax2.set_title('After: Professional Styling', fontsize=14, fontweight='bold', pad=15)
ax2.set_facecolor('#f8f9fa')
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.set_axisbelow(True)

# Spines
for spine in ax2.spines.values():
    spine.set_edgecolor('#cccccc')
    spine.set_linewidth(1.5)

plt.suptitle('Impact of Professional Styling', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('05_before_after.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Before/After comparison saved")

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 52 COMPLETE ✅")
print("="*70)
print("\n📊 Visualizations Created:")
print("  1. ✅ 01_color_schemes.png - Color palette comparison")
print("  2. ✅ 02_professional_bar_chart.png - Styled revenue chart")
print("  3. ✅ 03_annotated_line_chart.png - Highlighted trends")
print("  4. ✅ 04_professional_dashboard.png - Multi-metric dashboard")
print("  5. ✅ 05_before_after.png - Styling impact demonstration")
print("\n🎨 Styling Techniques Mastered:")
print("  • Professional color palettes")
print("  • Custom annotations and highlights")
print("  • Value labels on charts")
print("  • Grid and background styling")
print("  • Legend customization")
print("  • Multi-panel layouts")
print("  • Gradient effects")
print("  • Responsive sizing")
print("\n💡 Key Takeaway:")
print("  Professional styling transforms data from 'informative' to 'compelling'.")
print("  Good visualizations don't just show data - they tell stories!")
print("="*70)