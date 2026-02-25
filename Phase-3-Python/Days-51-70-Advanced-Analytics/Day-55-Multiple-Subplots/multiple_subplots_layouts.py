# Day 55 - Multiple Subplots & Custom Layouts
# Professional Dashboard Design
# Author: Syamprasad
# Date: February 26, 2026

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
sns.set_theme(style="whitegrid")

print("="*70)
print("DAY 55 - MULTIPLE SUBPLOTS & CUSTOM LAYOUTS")
print("Professional Multi-Panel Dashboard Design")
print("="*70)

# Generate sample data for all examples
np.random.seed(55)

sales_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] * 4,
    'Region': np.repeat(['North', 'South', 'East', 'West'], 6),
    'Sales': np.random.gamma(2, 50, 24),
    'Profit': np.random.gamma(1.5, 30, 24),
    'Customers': np.random.randint(50, 200, 24)
})

# =========================================================================
# PART 1: BASIC SUBPLOTS - GRID LAYOUTS
# =========================================================================

print("\n📊 PART 1: Basic Subplot Grids")

# Simple 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Flatten axes for easy iteration
axes = axes.flatten()

# Plot 1: Line chart
months_unique = sales_data['Month'].unique()
sales_by_month = sales_data.groupby('Month')['Sales'].mean()
axes[0].plot(months_unique, sales_by_month.values, marker='o', linewidth=2, color='#3498DB')
axes[0].set_title('Average Sales by Month', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Sales (₹K)')
axes[0].grid(True, alpha=0.3)

# Plot 2: Bar chart
region_sales = sales_data.groupby('Region')['Sales'].sum()
axes[1].bar(region_sales.index, region_sales.values, color='#E74C3C', alpha=0.7)
axes[1].set_title('Total Sales by Region', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Sales (₹K)')

# Plot 3: Scatter plot
axes[2].scatter(sales_data['Customers'], sales_data['Sales'], 
                alpha=0.6, s=100, c='#2ECC71')
axes[2].set_title('Customers vs Sales', fontsize=12, fontweight='bold')
axes[2].set_xlabel('Number of Customers')
axes[2].set_ylabel('Sales (₹K)')
axes[2].grid(True, alpha=0.3)

# Plot 4: Box plot
sns.boxplot(data=sales_data, x='Region', y='Profit', palette='Set2', ax=axes[3])
axes[3].set_title('Profit Distribution by Region', fontsize=12, fontweight='bold')
axes[3].set_ylabel('Profit (₹K)')

plt.suptitle('Basic 2×2 Subplot Grid', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('01_basic_grid_2x2.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Basic 2×2 grid saved")

# =========================================================================
# PART 2: DIFFERENT SIZED GRIDS
# =========================================================================

print("\n📊 PART 2: Various Grid Configurations")

# 3×2 grid
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

# Different plot types in each panel
plot_configs = [
    {'type': 'line', 'title': 'Sales Trend'},
    {'type': 'bar', 'title': 'Regional Performance'},
    {'type': 'scatter', 'title': 'Customer Analysis'},
    {'type': 'hist', 'title': 'Sales Distribution'},
    {'type': 'box', 'title': 'Profit by Region'},
    {'type': 'violin', 'title': 'Sales Variability'}
]

for idx, (ax, config) in enumerate(zip(axes.flatten(), plot_configs)):
    if config['type'] == 'line':
        ax.plot(months_unique, sales_by_month.values, marker='o', linewidth=2)
    elif config['type'] == 'bar':
        ax.bar(region_sales.index, region_sales.values, alpha=0.7)
    elif config['type'] == 'scatter':
        ax.scatter(sales_data['Customers'], sales_data['Sales'], alpha=0.6, s=80)
    elif config['type'] == 'hist':
        ax.hist(sales_data['Sales'], bins=15, alpha=0.7, edgecolor='black')
    elif config['type'] == 'box':
        sns.boxplot(data=sales_data, x='Region', y='Profit', ax=ax)
    elif config['type'] == 'violin':
        sns.violinplot(data=sales_data, x='Region', y='Sales', ax=ax)
    
    ax.set_title(config['title'], fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)

plt.suptitle('3×2 Subplot Grid - Mixed Chart Types', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('02_grid_3x2.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ 3×2 grid saved")

# =========================================================================
# PART 3: GRIDSPEC - CUSTOM LAYOUTS
# =========================================================================

print("\n🎨 PART 3: GridSpec - Custom Asymmetric Layouts")

# Create custom layout: Large plot on left, 3 small plots on right
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(3, 2, figure=fig, width_ratios=[2, 1], height_ratios=[1, 1, 1])

# Large plot (spans all rows in column 0)
ax_main = fig.add_subplot(gs[:, 0])
for region in sales_data['Region'].unique():
    region_data = sales_data[sales_data['Region'] == region]
    ax_main.scatter(region_data['Customers'], region_data['Sales'], 
                   label=region, s=100, alpha=0.6)
ax_main.set_title('Main Analysis: Customers vs Sales by Region', 
                  fontsize=13, fontweight='bold', pad=15)
ax_main.set_xlabel('Number of Customers', fontsize=11)
ax_main.set_ylabel('Sales (₹K)', fontsize=11)
ax_main.legend(title='Region', loc='upper left')
ax_main.grid(True, alpha=0.3)

# Small plot 1 (top right)
ax1 = fig.add_subplot(gs[0, 1])
region_sales = sales_data.groupby('Region')['Sales'].sum()
ax1.barh(region_sales.index, region_sales.values, color='#3498DB', alpha=0.7)
ax1.set_title('Total Sales', fontsize=11, fontweight='bold')
ax1.set_xlabel('Sales (₹K)')

# Small plot 2 (middle right)
ax2 = fig.add_subplot(gs[1, 1])
profit_sales = sales_data.groupby('Region')[['Profit', 'Sales']].mean()
x = np.arange(len(profit_sales.index))
width = 0.35
ax2.bar(x - width/2, profit_sales['Profit'], width, label='Profit', alpha=0.7)
ax2.bar(x + width/2, profit_sales['Sales'], width, label='Sales', alpha=0.7)
ax2.set_xticks(x)
ax2.set_xticklabels(profit_sales.index, rotation=45)
ax2.set_title('Avg Profit & Sales', fontsize=11, fontweight='bold')
ax2.legend()

# Small plot 3 (bottom right)
ax3 = fig.add_subplot(gs[2, 1])
sns.boxplot(data=sales_data, y='Customers', palette='Set2', ax=ax3)
ax3.set_title('Customer Distribution', fontsize=11, fontweight='bold')
ax3.set_ylabel('Customers')

plt.suptitle('Custom Layout: Large Main + 3 Supporting Charts', 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('03_gridspec_asymmetric.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ GridSpec asymmetric layout saved")

# =========================================================================
# PART 4: COMPLEX GRIDSPEC LAYOUTS
# =========================================================================

print("\n🎨 PART 4: Complex GridSpec - Dashboard Style")

# Create dashboard-style layout
fig = plt.figure(figsize=(18, 12))
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

# Top row: One large chart spanning 2 columns + 1 small
ax_top_main = fig.add_subplot(gs[0, :2])
monthly_trend = sales_data.groupby('Month')[['Sales', 'Profit']].sum()
ax_top_main.plot(months_unique, monthly_trend['Sales'].values, 
                marker='o', linewidth=3, label='Sales', color='#3498DB')
ax_top_main.plot(months_unique, monthly_trend['Profit'].values, 
                marker='s', linewidth=3, label='Profit', color='#E74C3C')
ax_top_main.set_title('Monthly Performance Trend', fontsize=13, fontweight='bold', pad=15)
ax_top_main.set_ylabel('Amount (₹K)')
ax_top_main.legend(loc='upper left', fontsize=11)
ax_top_main.grid(True, alpha=0.3)
ax_top_main.set_facecolor('#f8f9fa')

ax_top_right = fig.add_subplot(gs[0, 2])
total_sales = sales_data['Sales'].sum()
total_profit = sales_data['Profit'].sum()
profit_margin = (total_profit / total_sales * 100)
ax_top_right.text(0.5, 0.7, f'₹{total_sales:.0f}K', 
                 ha='center', va='center', fontsize=24, fontweight='bold', color='#3498DB')
ax_top_right.text(0.5, 0.4, 'Total Sales', 
                 ha='center', va='center', fontsize=12, color='gray')
ax_top_right.text(0.5, 0.2, f'{profit_margin:.1f}% Margin', 
                 ha='center', va='center', fontsize=11, color='#2ECC71')
ax_top_right.axis('off')
ax_top_right.set_facecolor('#f0f0f0')

# Middle row: Three equal charts
ax_mid_1 = fig.add_subplot(gs[1, 0])
sns.barplot(data=sales_data, x='Region', y='Sales', palette='viridis', ax=ax_mid_1)
ax_mid_1.set_title('Sales by Region', fontsize=12, fontweight='bold')
ax_mid_1.set_ylabel('Sales (₹K)')

ax_mid_2 = fig.add_subplot(gs[1, 1])
sns.violinplot(data=sales_data, x='Region', y='Profit', palette='muted', ax=ax_mid_2)
ax_mid_2.set_title('Profit Distribution', fontsize=12, fontweight='bold')
ax_mid_2.set_ylabel('Profit (₹K)')

ax_mid_3 = fig.add_subplot(gs[1, 2])
customer_counts = sales_data.groupby('Region')['Customers'].sum()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
ax_mid_3.pie(customer_counts.values, labels=customer_counts.index, 
            autopct='%1.1f%%', colors=colors, startangle=90)
ax_mid_3.set_title('Customer Distribution', fontsize=12, fontweight='bold')

# Bottom row: Two charts
ax_bot_1 = fig.add_subplot(gs[2, :2])
sns.scatterplot(data=sales_data, x='Customers', y='Sales', 
               hue='Region', style='Region', s=120, alpha=0.7, ax=ax_bot_1)
ax_bot_1.set_title('Customer Acquisition Analysis', fontsize=12, fontweight='bold')
ax_bot_1.set_xlabel('Number of Customers')
ax_bot_1.set_ylabel('Sales (₹K)')
ax_bot_1.grid(True, alpha=0.3)

ax_bot_2 = fig.add_subplot(gs[2, 2])
correlation = sales_data[['Sales', 'Profit', 'Customers']].corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
           center=0, square=True, linewidths=1, ax=ax_bot_2)
ax_bot_2.set_title('Correlation Matrix', fontsize=12, fontweight='bold')

plt.suptitle('Executive Dashboard - Complex GridSpec Layout', 
            fontsize=16, fontweight='bold')
plt.savefig('04_complex_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Complex dashboard layout saved")

# =========================================================================
# PART 5: SHARED AXES
# =========================================================================

print("\n🔗 PART 5: Shared Axes for Comparison")

# Create figure with shared axes
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex='col', sharey='row')

regions = sales_data['Region'].unique()

for idx, (ax, region) in enumerate(zip(axes.flatten(), regions)):
    region_data = sales_data[sales_data['Region'] == region]
    
    ax.scatter(region_data['Customers'], region_data['Sales'], 
              s=100, alpha=0.6, color=f'C{idx}')
    ax.set_title(f'{region} Region', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Only set labels on edge plots
    if idx >= 2:  # Bottom row
        ax.set_xlabel('Customers')
    if idx % 2 == 0:  # Left column
        ax.set_ylabel('Sales (₹K)')

plt.suptitle('Regional Analysis with Shared Axes', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('05_shared_axes.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Shared axes layout saved")

# =========================================================================
# PART 6: COMBINING MATPLOTLIB & SEABORN
# =========================================================================

print("\n🎨 PART 6: Matplotlib + Seaborn Integration")

fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.3, wspace=0.3)

# Matplotlib plots
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(months_unique, sales_by_month.values, marker='o', linewidth=2, color='#3498DB')
ax1.set_title('Line Plot (Matplotlib)', fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3)

ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(region_sales.index, region_sales.values, color='#E74C3C', alpha=0.7)
ax2.set_title('Bar Chart (Matplotlib)', fontsize=11, fontweight='bold')

ax3 = fig.add_subplot(gs[0, 2])
ax3.scatter(sales_data['Customers'], sales_data['Sales'], alpha=0.6, s=80, c='#2ECC71')
ax3.set_title('Scatter (Matplotlib)', fontsize=11, fontweight='bold')
ax3.grid(True, alpha=0.3)

# Seaborn plots
ax4 = fig.add_subplot(gs[1, 0])
sns.boxplot(data=sales_data, x='Region', y='Sales', palette='Set2', ax=ax4)
ax4.set_title('Box Plot (Seaborn)', fontsize=11, fontweight='bold')

ax5 = fig.add_subplot(gs[1, 1])
sns.violinplot(data=sales_data, x='Region', y='Profit', palette='muted', ax=ax5)
ax5.set_title('Violin Plot (Seaborn)', fontsize=11, fontweight='bold')

ax6 = fig.add_subplot(gs[1, 2])
sns.heatmap(sales_data[['Sales', 'Profit', 'Customers']].corr(), 
           annot=True, fmt='.2f', cmap='coolwarm', ax=ax6)
ax6.set_title('Heatmap (Seaborn)', fontsize=11, fontweight='bold')

plt.suptitle('Combining Matplotlib & Seaborn in One Figure', 
            fontsize=15, fontweight='bold')
plt.savefig('06_matplotlib_seaborn_combo.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Matplotlib + Seaborn combination saved")

# =========================================================================
# PART 7: FINAL PROFESSIONAL REPORT LAYOUT
# =========================================================================

print("\n💼 PART 7: Professional Executive Report Layout")

# Generate comprehensive data
report_data = pd.DataFrame({
    'Month': np.tile(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 4),
    'Region': np.repeat(['North', 'South', 'East', 'West'], 6),
    'Product': np.random.choice(['A', 'B', 'C'], 24),
    'Sales': np.random.gamma(2, 50, 24),
    'Profit': np.random.gamma(1.5, 30, 24),
    'Customers': np.random.randint(50, 200, 24),
    'Marketing_Spend': np.random.uniform(10, 50, 24)
})

# Create executive report layout
fig = plt.figure(figsize=(20, 14))
gs = gridspec.GridSpec(4, 3, figure=fig, hspace=0.35, wspace=0.3,
                      height_ratios=[1, 1.5, 1.5, 1])

# Header KPIs (spanning full width)
ax_kpi1 = fig.add_subplot(gs[0, 0])
total_sales = report_data['Sales'].sum()
ax_kpi1.text(0.5, 0.5, f'₹{total_sales:.0f}K', 
            ha='center', va='center', fontsize=28, fontweight='bold', color='#3498DB')
ax_kpi1.text(0.5, 0.2, 'TOTAL SALES', 
            ha='center', va='center', fontsize=12, color='gray')
ax_kpi1.axis('off')
ax_kpi1.set_facecolor('#E8F4F8')

ax_kpi2 = fig.add_subplot(gs[0, 1])
total_profit = report_data['Profit'].sum()
ax_kpi2.text(0.5, 0.5, f'₹{total_profit:.0f}K', 
            ha='center', va='center', fontsize=28, fontweight='bold', color='#2ECC71')
ax_kpi2.text(0.5, 0.2, 'TOTAL PROFIT', 
            ha='center', va='center', fontsize=12, color='gray')
ax_kpi2.axis('off')
ax_kpi2.set_facecolor('#E8F8E8')

ax_kpi3 = fig.add_subplot(gs[0, 2])
avg_customers = report_data['Customers'].mean()
ax_kpi3.text(0.5, 0.5, f'{avg_customers:.0f}', 
            ha='center', va='center', fontsize=28, fontweight='bold', color='#E74C3C')
ax_kpi3.text(0.5, 0.2, 'AVG CUSTOMERS', 
            ha='center', va='center', fontsize=12, color='gray')
ax_kpi3.axis('off')
ax_kpi3.set_facecolor('#F8E8E8')

# Main trend (spanning 2 columns)
ax_trend = fig.add_subplot(gs[1, :2])
monthly_perf = report_data.groupby('Month')[['Sales', 'Profit']].sum()
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
monthly_perf = monthly_perf.reindex(months_order)
ax_trend.plot(months_order, monthly_perf['Sales'].values, 
             marker='o', linewidth=3, label='Sales', color='#3498DB', markersize=10)
ax_trend.plot(months_order, monthly_perf['Profit'].values, 
             marker='s', linewidth=3, label='Profit', color='#2ECC71', markersize=10)
ax_trend.fill_between(range(len(months_order)), monthly_perf['Sales'].values, 
                      alpha=0.2, color='#3498DB')
ax_trend.set_title('Monthly Performance Trend', fontsize=14, fontweight='bold', pad=15)
ax_trend.set_ylabel('Amount (₹K)', fontsize=12)
ax_trend.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
ax_trend.grid(True, alpha=0.3, linestyle='--')
ax_trend.set_facecolor('#FAFAFA')

# Regional breakdown
ax_region = fig.add_subplot(gs[1, 2])
regional_sales = report_data.groupby('Region')['Sales'].sum().sort_values(ascending=True)
colors_gradient = plt.cm.viridis(np.linspace(0.3, 0.9, len(regional_sales)))
ax_region.barh(regional_sales.index, regional_sales.values, color=colors_gradient)
for i, (region, value) in enumerate(regional_sales.items()):
    ax_region.text(value + 5, i, f'₹{value:.0f}K', 
                  va='center', fontweight='bold', fontsize=10)
ax_region.set_title('Sales by Region', fontsize=14, fontweight='bold', pad=15)
ax_region.set_xlabel('Sales (₹K)', fontsize=11)
ax_region.set_facecolor('#FAFAFA')

# Product analysis
ax_product = fig.add_subplot(gs[2, 0])
product_perf = report_data.groupby('Product')[['Sales', 'Profit']].mean()
x = np.arange(len(product_perf.index))
width = 0.35
bars1 = ax_product.bar(x - width/2, product_perf['Sales'], width, 
                       label='Sales', color='#3498DB', alpha=0.8)
bars2 = ax_product.bar(x + width/2, product_perf['Profit'], width, 
                       label='Profit', color='#2ECC71', alpha=0.8)
ax_product.set_xticks(x)
ax_product.set_xticklabels(product_perf.index, fontsize=11)
ax_product.set_title('Product Performance', fontsize=14, fontweight='bold', pad=15)
ax_product.set_ylabel('Amount (₹K)', fontsize=11)
ax_product.legend()
ax_product.grid(axis='y', alpha=0.3, linestyle='--')
ax_product.set_facecolor('#FAFAFA')

# Customer distribution
ax_customers = fig.add_subplot(gs[2, 1])
sns.boxplot(data=report_data, x='Region', y='Customers', 
           palette='Set2', ax=ax_customers)
ax_customers.set_title('Customer Distribution by Region', fontsize=14, fontweight='bold', pad=15)
ax_customers.set_ylabel('Number of Customers', fontsize=11)
ax_customers.set_facecolor('#FAFAFA')

# Marketing efficiency
ax_marketing = fig.add_subplot(gs[2, 2])
ax_marketing.scatter(report_data['Marketing_Spend'], report_data['Sales'], 
                    s=100, alpha=0.6, c=report_data['Profit'], cmap='RdYlGn')
ax_marketing.set_title('Marketing ROI Analysis', fontsize=14, fontweight='bold', pad=15)
ax_marketing.set_xlabel('Marketing Spend (₹K)', fontsize=11)
ax_marketing.set_ylabel('Sales (₹K)', fontsize=11)
ax_marketing.grid(True, alpha=0.3, linestyle='--')
ax_marketing.set_facecolor('#FAFAFA')

# Bottom: Correlation heatmap (spanning all columns)
ax_corr = fig.add_subplot(gs[3, :])
correlation = report_data[['Sales', 'Profit', 'Customers', 'Marketing_Spend']].corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
           center=0, linewidths=2, cbar_kws={'label': 'Correlation'}, ax=ax_corr)
ax_corr.set_title('Performance Metrics Correlation', fontsize=14, fontweight='bold', pad=15)

# Overall title
fig.suptitle('Q2 2026 Executive Performance Report', 
            fontsize=18, fontweight='bold', y=0.98)

# Add footer
fig.text(0.5, 0.01, 'Generated by Data Analytics Team | Confidential', 
        ha='center', fontsize=10, style='italic', color='gray')

plt.savefig('07_executive_report.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Executive report layout saved")

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 55 COMPLETE ✅")
print("="*70)
print("\n📊 Professional Layouts Created:")
print("  1. ✅ 01_basic_grid_2x2.png - Simple grid layout")
print("  2. ✅ 02_grid_3x2.png - Mixed chart types")
print("  3. ✅ 03_gridspec_asymmetric.png - Custom sized panels")
print("  4. ✅ 04_complex_dashboard.png - Advanced GridSpec")
print("  5. ✅ 05_shared_axes.png - Synchronized comparisons")
print("  6. ✅ 06_matplotlib_seaborn_combo.png - Library integration")
print("  7. ✅ 07_executive_report.png - Professional report layout")
print("\n🎯 Layout Techniques Mastered:")
print("  • plt.subplots() for simple grids")
print("  • GridSpec for custom arrangements")
print("  • Asymmetric layouts (different sized panels)")
print("  • Shared axes for aligned comparisons")
print("  • Combining Matplotlib + Seaborn seamlessly")
print("  • KPI cards + charts integration")
print("  • Professional report design")
print("\n💡 Key Principles:")
print("  • Large main chart + supporting details")
print("  • KPIs at top for immediate insight")
print("  • Logical flow: Overview → Details → Insights")
print("  • Consistent styling across all panels")
print("  • White space for readability")
print("\n🔥 Real Impact:")
print("  Before: Multiple separate charts")
print("  After: Comprehensive dashboard telling complete story")
print("  → All insights in ONE view")
print("  → Executive-ready reports")
print("  → Professional presentation quality")
print("="*70)