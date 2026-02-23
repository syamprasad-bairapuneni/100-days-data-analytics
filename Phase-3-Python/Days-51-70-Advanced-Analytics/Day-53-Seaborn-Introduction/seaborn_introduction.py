# Day 53 - Seaborn Introduction
# Statistical Visualization Made Easy
# Author: Syamprasad
# Date: February 24, 2026

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style (makes everything beautiful automatically!)
sns.set_theme(style="whitegrid")

print("="*70)
print("DAY 53 - SEABORN INTRODUCTION")
print("Statistical Visualization Made Beautiful & Easy")
print("="*70)

# =========================================================================
# PART 1: WHY SEABORN? - COMPARISON WITH MATPLOTLIB
# =========================================================================

print("\n📊 PART 1: Matplotlib vs Seaborn Comparison")

# Generate sample data
np.random.seed(53)
data = pd.DataFrame({
    'values': np.random.normal(100, 15, 1000)
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Matplotlib way (more code)
ax1.hist(data['values'], bins=30, color='steelblue', alpha=0.7, edgecolor='black')
ax1.set_xlabel('Values', fontsize=11)
ax1.set_ylabel('Frequency', fontsize=11)
ax1.set_title('Matplotlib: Manual Styling', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Seaborn way (one line, automatic beauty!)
sns.histplot(data=data, x='values', bins=30, kde=True, ax=ax2)
ax2.set_title('Seaborn: Automatic Beauty', fontsize=13, fontweight='bold')

plt.suptitle('Why Seaborn? Less Code, More Beauty', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('01_matplotlib_vs_seaborn.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Comparison chart saved")
print("   Matplotlib: ~10 lines of code")
print("   Seaborn: 1 line of code! 🎯")

# =========================================================================
# PART 2: DISTRIBUTION PLOTS
# =========================================================================

print("\n📈 PART 2: Distribution Analysis")

# Generate sample sales data
sales_data = pd.DataFrame({
    'Daily_Sales': np.random.gamma(shape=2, scale=50, size=500)
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Histogram with KDE
sns.histplot(data=sales_data, x='Daily_Sales', bins=30, kde=True, 
             color='#3498DB', ax=axes[0, 0])
axes[0, 0].set_title('Histogram with KDE (Density Curve)', 
                     fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Daily Sales (₹ Thousands)')

# Plot 2: KDE Plot only
sns.kdeplot(data=sales_data, x='Daily_Sales', fill=True, 
            color='#E74C3C', alpha=0.6, ax=axes[0, 1])
axes[0, 1].set_title('KDE Plot (Smooth Distribution)', 
                     fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Daily Sales (₹ Thousands)')

# Plot 3: Box Plot (shows quartiles)
sns.boxplot(data=sales_data, y='Daily_Sales', 
            color='#2ECC71', ax=axes[1, 0])
axes[1, 0].set_title('Box Plot (Quartiles & Outliers)', 
                     fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Daily Sales (₹ Thousands)')

# Plot 4: Violin Plot (combines box + KDE)
sns.violinplot(data=sales_data, y='Daily_Sales', 
               color='#F39C12', ax=axes[1, 1])
axes[1, 1].set_title('Violin Plot (Distribution Shape)', 
                     fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Daily Sales (₹ Thousands)')

plt.suptitle('Distribution Analysis - 4 Different Views', 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('02_distribution_plots.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Distribution plots saved")
print("   4 different ways to visualize the same data!")

# =========================================================================
# PART 3: CATEGORICAL PLOTS
# =========================================================================

print("\n📊 PART 3: Categorical Data Analysis")

# Sample data: Sales by region and product
categorical_data = pd.DataFrame({
    'Region': np.repeat(['North', 'South', 'East', 'West'], 100),
    'Product': np.tile(['Laptop', 'Phone', 'Tablet', 'Watch'], 100),
    'Sales': np.random.normal(500, 100, 400)
})

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: Bar Plot (with confidence intervals!)
sns.barplot(data=categorical_data, x='Region', y='Sales', 
            palette='Set2', ax=axes[0, 0])
axes[0, 0].set_title('Average Sales by Region (with 95% CI)', 
                     fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Sales (₹ Thousands)')

# Plot 2: Count Plot
sns.countplot(data=categorical_data, x='Product', 
              palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Transaction Count by Product', 
                     fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Number of Transactions')

# Plot 3: Box Plot by Category
sns.boxplot(data=categorical_data, x='Region', y='Sales', 
            palette='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Sales Distribution by Region', 
                     fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Sales (₹ Thousands)')

# Plot 4: Violin Plot by Category
sns.violinplot(data=categorical_data, x='Product', y='Sales', 
               palette='muted', ax=axes[1, 1])
axes[1, 1].set_title('Sales Distribution by Product', 
                     fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Sales (₹ Thousands)')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.suptitle('Categorical Analysis - Regional & Product Performance', 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('03_categorical_plots.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Categorical plots saved")
print("   Notice the automatic confidence intervals? That's Seaborn magic! ✨")

# =========================================================================
# PART 4: RELATIONSHIP PLOTS
# =========================================================================

print("\n🔗 PART 4: Analyzing Relationships")

# Sample data: Marketing spend vs Revenue
np.random.seed(53)
relationship_data = pd.DataFrame({
    'Marketing_Spend': np.random.uniform(10, 100, 200),
    'Revenue': np.random.uniform(50, 500, 200),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 200)
})
# Add correlation
relationship_data['Revenue'] = (relationship_data['Marketing_Spend'] * 4 + 
                                np.random.normal(0, 50, 200))

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Scatter Plot with Regression Line
sns.regplot(data=relationship_data, x='Marketing_Spend', y='Revenue', 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red', 'linewidth':2},
            ax=axes[0])
axes[0].set_title('Marketing Spend vs Revenue (with Trend Line)', 
                  fontsize=13, fontweight='bold')
axes[0].set_xlabel('Marketing Spend (₹ Lakhs)')
axes[0].set_ylabel('Revenue (₹ Lakhs)')

# Plot 2: Scatter Plot by Category (color-coded)
sns.scatterplot(data=relationship_data, x='Marketing_Spend', y='Revenue', 
                hue='Region', style='Region', s=100, alpha=0.7, ax=axes[1])
axes[1].set_title('Marketing Spend vs Revenue by Region', 
                  fontsize=13, fontweight='bold')
axes[1].set_xlabel('Marketing Spend (₹ Lakhs)')
axes[1].set_ylabel('Revenue (₹ Lakhs)')

plt.suptitle('Relationship Analysis - Correlation Discovery', 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('04_relationship_plots.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Relationship plots saved")
print("   Automatic regression line! Seaborn does the math for you! 📈")

# =========================================================================
# PART 5: BUILT-IN THEMES SHOWCASE
# =========================================================================

print("\n🎨 PART 5: Seaborn's Built-in Themes")

# Sample data
theme_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [45, 67, 52, 78, 61]
})

# Different theme styles
themes = ['whitegrid', 'darkgrid', 'white', 'dark', 'ticks']

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

for idx, theme in enumerate(themes):
    sns.set_theme(style=theme)
    sns.barplot(data=theme_data, x='Category', y='Values', 
                palette='viridis', ax=axes[idx])
    axes[idx].set_title(f'Theme: {theme}', fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('Values')

# Remove extra subplot
axes[5].axis('off')

# Reset to default
sns.set_theme(style='whitegrid')

plt.suptitle("Seaborn's 5 Built-in Professional Themes", 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('05_seaborn_themes.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Theme showcase saved")
print("   5 professional themes, instant application! 🎨")

# =========================================================================
# PART 6: REAL BUSINESS CASE - SALES ANALYSIS
# =========================================================================

print("\n💼 PART 6: Real Business Analysis")

# Generate realistic sales data
np.random.seed(53)
n = 500

business_data = pd.DataFrame({
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], n),
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet'], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'Sales': np.random.gamma(2, 50, n),
    'Customers': np.random.randint(10, 100, n)
})

# Create comprehensive analysis
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Plot 1: Sales Distribution
ax1 = fig.add_subplot(gs[0, 0])
sns.histplot(data=business_data, x='Sales', bins=30, kde=True, 
             color='#3498DB', ax=ax1)
ax1.set_title('Overall Sales Distribution', fontsize=12, fontweight='bold')
ax1.set_xlabel('Sales Amount (₹ Thousands)')

# Plot 2: Sales by Product
ax2 = fig.add_subplot(gs[0, 1])
sns.boxplot(data=business_data, x='Product', y='Sales', 
            palette='Set2', ax=ax2)
ax2.set_title('Sales Distribution by Product', fontsize=12, fontweight='bold')
ax2.set_ylabel('Sales Amount (₹ Thousands)')

# Plot 3: Sales by Region
ax3 = fig.add_subplot(gs[1, 0])
sns.violinplot(data=business_data, x='Region', y='Sales', 
               palette='muted', ax=ax3)
ax3.set_title('Sales Distribution by Region', fontsize=12, fontweight='bold')
ax3.set_ylabel('Sales Amount (₹ Thousands)')

# Plot 4: Monthly Performance
ax4 = fig.add_subplot(gs[1, 1])
sns.barplot(data=business_data, x='Month', y='Sales', 
            palette='coolwarm', ax=ax4)
ax4.set_title('Average Sales by Month', fontsize=12, fontweight='bold')
ax4.set_ylabel('Sales Amount (₹ Thousands)')

# Plot 5: Sales vs Customers
ax5 = fig.add_subplot(gs[2, 0])
sns.scatterplot(data=business_data, x='Customers', y='Sales', 
                hue='Product', style='Product', s=80, alpha=0.6, ax=ax5)
ax5.set_title('Sales vs Customer Count by Product', fontsize=12, fontweight='bold')
ax5.set_xlabel('Number of Customers')
ax5.set_ylabel('Sales Amount (₹ Thousands)')

# Plot 6: Heatmap of average sales
ax6 = fig.add_subplot(gs[2, 1])
pivot_data = business_data.pivot_table(values='Sales', 
                                       index='Product', 
                                       columns='Region', 
                                       aggfunc='mean')
sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlOrRd', 
            cbar_kws={'label': 'Avg Sales (₹K)'}, ax=ax6)
ax6.set_title('Average Sales: Product × Region', fontsize=12, fontweight='bold')

plt.suptitle('Complete Business Sales Analysis Dashboard', 
            fontsize=16, fontweight='bold')
plt.savefig('06_business_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Business analysis dashboard saved")
print("   6 different insights in one comprehensive view! 📊")

# =========================================================================
# PART 7: THE POWER OF SEABORN - CODE COMPARISON
# =========================================================================

print("\n⚡ PART 7: The Power of Seaborn - Code Efficiency")

print("\nCode Comparison for the same visualization:")
print("\n" + "="*70)
print("MATPLOTLIB (Manual approach):")
print("="*70)
print("""
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data['values'], bins=30, color='steelblue', alpha=0.7)
ax.set_xlabel('Values', fontsize=11)
ax.set_ylabel('Frequency', fontsize=11)
ax.set_title('Distribution', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output.png', dpi=300)

Lines of code: ~10
Time to write: ~2 minutes
""")

print("="*70)
print("SEABORN (Automatic approach):")
print("="*70)
print("""
sns.histplot(data=data, x='values', bins=30, kde=True)
plt.savefig('output.png', dpi=300)

Lines of code: 2
Time to write: 10 seconds
Result: SAME quality, MORE features (KDE included!)
""")

print("="*70)
print("\n💡 Seaborn Benefits:")
print("  • 5x less code")
print("  • Automatic beautiful styling")
print("  • Built-in statistical calculations")
print("  • Professional themes included")
print("  • Pandas DataFrame integration")
print("  • Immediate insight generation")

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 53 COMPLETE ✅")
print("="*70)
print("\n📊 Visualizations Created:")
print("  1. ✅ 01_matplotlib_vs_seaborn.png - Direct comparison")
print("  2. ✅ 02_distribution_plots.png - 4 distribution views")
print("  3. ✅ 03_categorical_plots.png - Categorical analysis")
print("  4. ✅ 04_relationship_plots.png - Correlation analysis")
print("  5. ✅ 05_seaborn_themes.png - Theme showcase")
print("  6. ✅ 06_business_analysis.png - Complete dashboard")
print("\n🎯 Seaborn Skills Mastered:")
print("  • Distribution plots (hist, kde, box, violin)")
print("  • Categorical plots (bar, count)")
print("  • Relationship plots (scatter, regplot)")
print("  • Heatmaps")
print("  • Automatic statistical calculations")
print("  • Built-in professional themes")
print("  • Pandas DataFrame integration")
print("\n💡 Key Takeaway:")
print("  Seaborn: Where statistics meets beauty automatically!")
print("  Less code → More insights → Faster analysis")
print("\n🔥 Why Seaborn Wins:")
print("  Matplotlib: Great for full control")
print("  Seaborn: Great for quick, beautiful statistical viz")
print("  Use both: Matplotlib for custom, Seaborn for speed!")
print("="*70)