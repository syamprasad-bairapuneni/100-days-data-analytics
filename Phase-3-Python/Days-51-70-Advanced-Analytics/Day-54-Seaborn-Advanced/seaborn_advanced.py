# Day 54 - Advanced Seaborn Techniques
# Multi-Dimensional Statistical Visualization
# Author: Syamprasad
# Date: February 25, 2026

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set theme
sns.set_theme(style="whitegrid")

print("="*70)
print("DAY 54 - ADVANCED SEABORN TECHNIQUES")
print("Multi-Dimensional Visualization & Pattern Discovery")
print("="*70)

# =========================================================================
# PART 1: CORRELATION HEATMAPS
# =========================================================================

print("\n🔥 PART 1: Correlation Heatmaps - Finding Relationships")

# Generate sample business data
np.random.seed(54)
n = 200

business_metrics = pd.DataFrame({
    'Marketing_Spend': np.random.uniform(50, 500, n),
    'Sales_Team_Size': np.random.randint(5, 50, n),
    'Customer_Satisfaction': np.random.uniform(3, 5, n),
    'Website_Traffic': np.random.uniform(1000, 10000, n),
    'Revenue': np.random.uniform(100, 1000, n)
})

# Add correlations (make it realistic)
business_metrics['Revenue'] = (
    business_metrics['Marketing_Spend'] * 1.5 + 
    business_metrics['Sales_Team_Size'] * 10 +
    business_metrics['Customer_Satisfaction'] * 50 +
    business_metrics['Website_Traffic'] * 0.05 +
    np.random.normal(0, 50, n)
)

# Calculate correlation matrix
correlation_matrix = business_metrics.corr()

# Create heatmap
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap 1: Basic correlation
sns.heatmap(correlation_matrix, 
            annot=True,  # Show values
            fmt='.2f',   # 2 decimal places
            cmap='coolwarm',  # Color scheme
            center=0,    # Center colormap at 0
            square=True, # Square cells
            linewidths=1,
            cbar_kws={'label': 'Correlation Coefficient'},
            ax=axes[0])
axes[0].set_title('Business Metrics Correlation Matrix', 
                  fontsize=13, fontweight='bold', pad=15)

# Heatmap 2: Triangle (avoid redundancy)
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix,
            mask=mask,
            annot=True,
            fmt='.2f',
            cmap='RdYlGn',
            center=0,
            square=True,
            linewidths=1,
            cbar_kws={'label': 'Correlation'},
            ax=axes[1])
axes[1].set_title('Correlation Matrix (Triangle View)', 
                  fontsize=13, fontweight='bold', pad=15)

plt.suptitle('Correlation Analysis - Finding Key Relationships', 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('01_correlation_heatmaps.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Correlation heatmaps saved")
print(f"   Strongest correlation: Revenue ↔ Marketing Spend = {correlation_matrix.loc['Revenue', 'Marketing_Spend']:.2f}")

# =========================================================================
# PART 2: PAIR PLOTS - ALL VARIABLES AT ONCE
# =========================================================================

print("\n🔍 PART 2: Pair Plots - Multi-Variable Analysis")

# Create smaller dataset for pair plot
pair_data = business_metrics[['Marketing_Spend', 'Sales_Team_Size', 
                               'Customer_Satisfaction', 'Revenue']].sample(100)

# Add a categorical variable
pair_data['Performance'] = pd.cut(pair_data['Revenue'], 
                                   bins=3, 
                                   labels=['Low', 'Medium', 'High'])

# Create pair plot
pairplot = sns.pairplot(pair_data, 
                        hue='Performance',  # Color by performance
                        palette='viridis',
                        diag_kind='kde',    # Diagonal: KDE instead of histogram
                        corner=True,        # Only lower triangle
                        plot_kws={'alpha': 0.6, 's': 50})

pairplot.fig.suptitle('Pair Plot: All Variables vs All Variables', 
                      fontsize=15, fontweight='bold', y=1.02)
plt.savefig('02_pair_plot.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Pair plot saved")
print("   Shows all possible relationships in one view!")

# =========================================================================
# PART 3: JOINT PLOTS - BIVARIATE + DISTRIBUTIONS
# =========================================================================

print("\n📊 PART 3: Joint Plots - Bivariate Analysis with Marginals")

# Joint plot 1: Scatter with histograms
joint1 = sns.jointplot(data=business_metrics,
                       x='Marketing_Spend',
                       y='Revenue',
                       kind='scatter',
                       color='#3498DB',
                       marginal_kws={'bins': 30, 'fill': True},
                       height=8)
joint1.fig.suptitle('Marketing Spend vs Revenue (with distributions)', 
                    fontsize=13, fontweight='bold', y=1.02)
plt.savefig('03_joint_plot_scatter.png', dpi=300, bbox_inches='tight')
plt.close()

# Joint plot 2: Hexbin (for dense data)
joint2 = sns.jointplot(data=business_metrics,
                       x='Website_Traffic',
                       y='Revenue',
                       kind='hex',
                       color='#E74C3C',
                       height=8)
joint2.fig.suptitle('Website Traffic vs Revenue (density view)', 
                    fontsize=13, fontweight='bold', y=1.02)
plt.savefig('04_joint_plot_hex.png', dpi=300, bbox_inches='tight')
plt.close()

# Joint plot 3: Regression
joint3 = sns.jointplot(data=business_metrics,
                       x='Customer_Satisfaction',
                       y='Revenue',
                       kind='reg',
                       color='#2ECC71',
                       height=8)
joint3.fig.suptitle('Customer Satisfaction vs Revenue (with regression)', 
                    fontsize=13, fontweight='bold', y=1.02)
plt.savefig('05_joint_plot_regression.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Joint plots saved (3 types)")
print("   Scatter, Hexbin, and Regression views!")

# =========================================================================
# PART 4: FACET GRIDS - MULTI-DIMENSIONAL COMPARISONS
# =========================================================================

print("\n📈 PART 4: FacetGrid - Multi-Dimensional Analysis")

# Generate multi-dimensional data
facet_data = pd.DataFrame({
    'Region': np.repeat(['North', 'South', 'East', 'West'], 150),
    'Product': np.tile(np.repeat(['A', 'B', 'C'], 50), 4),
    'Quarter': np.tile(['Q1', 'Q2', 'Q3', 'Q4'] * 37 + ['Q1', 'Q2'], 4),
    'Sales': np.random.gamma(2, 50, 600)
})

# Create FacetGrid
g = sns.FacetGrid(facet_data, 
                  col='Region',      # Columns: Regions
                  row='Quarter',     # Rows: Quarters
                  hue='Product',     # Colors: Products
                  height=3,
                  aspect=1.2,
                  palette='Set2')

# Map the plot type
g.map(sns.scatterplot, 'Sales', alpha=0.6, s=50)
g.add_legend(title='Product')
g.fig.suptitle('Sales by Region × Quarter × Product', 
              fontsize=15, fontweight='bold', y=1.02)

# Adjust layout
g.set_axis_labels('', 'Sales (₹ Thousands)')
plt.savefig('06_facet_grid.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ FacetGrid saved")
print("   3 dimensions visualized: Region × Quarter × Product!")

# =========================================================================
# PART 5: CLUSTER MAP - HIERARCHICAL CLUSTERING
# =========================================================================

print("\n🔬 PART 5: Cluster Map - Pattern Discovery")

# Create sample data matrix
products = ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales_matrix = pd.DataFrame(
    np.random.randint(50, 200, size=(len(products), len(months))),
    index=products,
    columns=months
)

# Add some patterns
sales_matrix.iloc[0, :] *= 1.5  # Product A sells more
sales_matrix.iloc[:, 6:] *= 1.3  # Higher sales in second half

# Create cluster map
clustermap = sns.clustermap(sales_matrix,
                            cmap='YlOrRd',
                            annot=True,
                            fmt='d',
                            linewidths=0.5,
                            figsize=(12, 6),
                            cbar_kws={'label': 'Sales (₹K)'})
clustermap.fig.suptitle('Sales Cluster Map - Products × Months', 
                        fontsize=13, fontweight='bold', x=0.5, y=0.98)
plt.savefig('07_cluster_map.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Cluster map saved")
print("   Automatically groups similar patterns!")

# =========================================================================
# PART 6: COMPREHENSIVE DASHBOARD
# =========================================================================

print("\n💼 PART 6: Advanced Multi-Dimensional Dashboard")

# Generate comprehensive dataset
np.random.seed(54)
dashboard_data = pd.DataFrame({
    'Customer_Age': np.random.randint(18, 70, 300),
    'Annual_Income': np.random.uniform(30, 150, 300),
    'Purchase_Frequency': np.random.randint(1, 50, 300),
    'Avg_Purchase_Value': np.random.uniform(50, 500, 300),
    'Loyalty_Score': np.random.uniform(1, 10, 300),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 300),
    'Segment': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], 300)
})

# Add calculated field
dashboard_data['Total_Spend'] = (dashboard_data['Purchase_Frequency'] * 
                                 dashboard_data['Avg_Purchase_Value'])

# Create comprehensive dashboard
fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Plot 1: Correlation heatmap
ax1 = fig.add_subplot(gs[0, :2])
numeric_cols = ['Customer_Age', 'Annual_Income', 'Purchase_Frequency', 
                'Avg_Purchase_Value', 'Loyalty_Score', 'Total_Spend']
corr = dashboard_data[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
            square=True, linewidths=1, ax=ax1)
ax1.set_title('Customer Metrics Correlation', fontsize=12, fontweight='bold')

# Plot 2: Distribution by segment
ax2 = fig.add_subplot(gs[0, 2])
sns.violinplot(data=dashboard_data, y='Total_Spend', x='Segment', 
               palette='muted', ax=ax2)
ax2.set_title('Spend by Segment', fontsize=12, fontweight='bold')
ax2.set_ylabel('Total Spend (₹K)')
ax2.tick_params(axis='x', rotation=45)

# Plot 3: Scatter - Age vs Income
ax3 = fig.add_subplot(gs[1, 0])
sns.scatterplot(data=dashboard_data, x='Customer_Age', y='Annual_Income', 
                hue='Segment', style='Segment', s=60, alpha=0.6, ax=ax3)
ax3.set_title('Age vs Income by Segment', fontsize=12, fontweight='bold')
ax3.set_xlabel('Customer Age')
ax3.set_ylabel('Annual Income (₹L)')

# Plot 4: Box plot - Frequency by Region
ax4 = fig.add_subplot(gs[1, 1])
sns.boxplot(data=dashboard_data, x='Region', y='Purchase_Frequency', 
            palette='Set2', ax=ax4)
ax4.set_title('Purchase Frequency by Region', fontsize=12, fontweight='bold')
ax4.set_ylabel('Purchase Frequency')

# Plot 5: Density - Total Spend
ax5 = fig.add_subplot(gs[1, 2])
sns.kdeplot(data=dashboard_data, x='Total_Spend', hue='Segment', 
            fill=True, alpha=0.5, ax=ax5)
ax5.set_title('Spend Distribution by Segment', fontsize=12, fontweight='bold')
ax5.set_xlabel('Total Spend (₹K)')

# Plot 6: Strip plot - Loyalty by Segment
ax6 = fig.add_subplot(gs[2, 0])
sns.stripplot(data=dashboard_data, x='Segment', y='Loyalty_Score', 
              palette='viridis', alpha=0.6, ax=ax6)
ax6.set_title('Loyalty Score by Segment', fontsize=12, fontweight='bold')
ax6.tick_params(axis='x', rotation=45)

# Plot 7: Regression - Income vs Spend
ax7 = fig.add_subplot(gs[2, 1])
sns.regplot(data=dashboard_data, x='Annual_Income', y='Total_Spend', 
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax7)
ax7.set_title('Income vs Total Spend (Trend)', fontsize=12, fontweight='bold')
ax7.set_xlabel('Annual Income (₹L)')
ax7.set_ylabel('Total Spend (₹K)')

# Plot 8: Count by Region and Segment
ax8 = fig.add_subplot(gs[2, 2])
segment_region = dashboard_data.groupby(['Region', 'Segment']).size().reset_index(name='Count')
pivot_count = segment_region.pivot(index='Region', columns='Segment', values='Count')
sns.heatmap(pivot_count, annot=True, fmt='d', cmap='Blues', ax=ax8)
ax8.set_title('Customer Count: Region × Segment', fontsize=12, fontweight='bold')

plt.suptitle('Advanced Customer Analytics Dashboard', 
            fontsize=16, fontweight='bold', y=0.995)
plt.savefig('08_advanced_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Advanced dashboard saved")
print("   8 different visualizations revealing deep patterns!")

# =========================================================================
# PART 7: STATISTICAL ANNOTATIONS
# =========================================================================

print("\n📊 PART 7: Statistical Annotations Example")

# Create data with clear groups
stat_data = pd.DataFrame({
    'Group': np.repeat(['Control', 'Test_A', 'Test_B'], 100),
    'Conversion_Rate': np.concatenate([
        np.random.normal(5, 1, 100),   # Control
        np.random.normal(6.5, 1, 100), # Test A
        np.random.normal(7.5, 1, 100)  # Test B
    ])
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Box plot with annotations
sns.boxplot(data=stat_data, x='Group', y='Conversion_Rate', 
            palette='Set3', ax=ax1)
ax1.set_title('A/B Test Results - Conversion Rate', 
              fontsize=13, fontweight='bold')
ax1.set_ylabel('Conversion Rate (%)')

# Add mean values as annotations
means = stat_data.groupby('Group')['Conversion_Rate'].mean()
for i, (group, mean) in enumerate(means.items()):
    ax1.text(i, mean, f'μ={mean:.1f}%', 
            ha='center', va='bottom', fontweight='bold', fontsize=10)

# Plot 2: Violin plot
sns.violinplot(data=stat_data, x='Group', y='Conversion_Rate', 
               palette='pastel', ax=ax2)
ax2.set_title('Distribution Shape Comparison', 
              fontsize=13, fontweight='bold')
ax2.set_ylabel('Conversion Rate (%)')

plt.suptitle('Statistical Comparison - A/B Testing', 
            fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('09_statistical_annotations.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Statistical annotations saved")

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 54 COMPLETE ✅")
print("="*70)
print("\n📊 Advanced Visualizations Created:")
print("  1. ✅ 01_correlation_heatmaps.png - Find relationships")
print("  2. ✅ 02_pair_plot.png - All variables at once")
print("  3. ✅ 03_joint_plot_scatter.png - Bivariate + marginals")
print("  4. ✅ 04_joint_plot_hex.png - Density visualization")
print("  5. ✅ 05_joint_plot_regression.png - With trend line")
print("  6. ✅ 06_facet_grid.png - 3D: Region × Quarter × Product")
print("  7. ✅ 07_cluster_map.png - Hierarchical clustering")
print("  8. ✅ 08_advanced_dashboard.png - 8-panel comprehensive view")
print("  9. ✅ 09_statistical_annotations.png - A/B testing")
print("\n🎯 Advanced Techniques Mastered:")
print("  • Correlation heatmaps (find hidden relationships)")
print("  • Pair plots (all vs all comparison)")
print("  • Joint plots (bivariate + distributions)")
print("  • FacetGrid (multi-dimensional analysis)")
print("  • Cluster maps (automatic pattern grouping)")
print("  • Statistical annotations")
print("  • Multi-panel advanced dashboards")
print("\n💡 Key Power:")
print("  Advanced Seaborn reveals patterns invisible to basic charts!")
print("  → Correlation matrix: Find what drives what")
print("  → Pair plots: Compare everything simultaneously")
print("  → FacetGrid: Analyze multiple dimensions at once")
print("  → Cluster maps: Discover hidden groups automatically")
print("\n🔥 Real Business Impact:")
print("  Before: Analyze variables one-by-one (hours)")
print("  After: See all relationships instantly (minutes)")
print("="*70)