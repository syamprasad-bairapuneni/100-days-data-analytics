# Day 56 - Data Storytelling with Visualizations
# Turning Data into Compelling Narratives
# Author: Syamprasad
# Date: February 27, 2026

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
sns.set_theme(style="whitegrid")

print("="*70)
print("DAY 56 - DATA STORYTELLING WITH VISUALIZATIONS")
print("From Numbers to Narratives That Drive Action")
print("="*70)

# =========================================================================
# PART 1: THE PROBLEM - SETTING THE CONTEXT
# =========================================================================

print("\n📖 PART 1: Story Arc - Setting the Problem")

# Generate data showing a problem
np.random.seed(56)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2025 = [450, 430, 410, 390, 370, 350, 340, 330, 320, 310, 300, 290]
sales_target = [500] * 12

fig, ax = plt.subplots(figsize=(14, 8))

# Plot the declining trend
ax.plot(months, sales_2025, marker='o', linewidth=3, markersize=10, 
        color='#E74C3C', label='Actual Sales', zorder=3)

# Plot the target
ax.plot(months, sales_target, linestyle='--', linewidth=2, 
        color='#2ECC71', label='Target', zorder=2)

# Fill the gap
ax.fill_between(range(len(months)), sales_2025, sales_target, 
                alpha=0.3, color='#E74C3C', label='Gap to Target')

# Annotate the problem
ax.annotate('Sales declining steadily!', 
           xy=(6, sales_2025[6]), xytext=(8, 450),
           fontsize=14, fontweight='bold', color='#C0392B',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=2),
           arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', 
                          color='#E74C3C', lw=2))

# Highlight the worst month
worst_month_idx = sales_2025.index(min(sales_2025))
ax.scatter(worst_month_idx, sales_2025[worst_month_idx], 
          s=500, color='#C0392B', zorder=4, edgecolor='black', linewidth=2)
ax.text(worst_month_idx, sales_2025[worst_month_idx] - 30, 
       f'Lowest: ₹{sales_2025[worst_month_idx]}K',
       ha='center', fontsize=11, fontweight='bold', color='#C0392B')

# Styling
ax.set_title('THE PROBLEM: Sales Declining Throughout 2025', 
            fontsize=18, fontweight='bold', pad=20, color='#2C3E50')
ax.set_xlabel('Month', fontsize=13, fontweight='bold')
ax.set_ylabel('Sales (₹ Thousands)', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_facecolor('#F8F9FA')

# Add context text
fig.text(0.5, 0.02, 
        'Context: Sales have dropped 36% from January to December, missing targets by increasing margins',
        ha='center', fontsize=11, style='italic', color='#7F8C8D',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('01_story_problem.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Problem visualization saved")

# =========================================================================
# PART 2: THE INVESTIGATION - DIGGING DEEPER
# =========================================================================

print("\n🔍 PART 2: Story Arc - Investigation & Root Cause")

# Generate data for root cause analysis
regions_data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West'] * 3,
    'Quarter': np.repeat(['Q1', 'Q2', 'Q3', 'Q4'], 3)[:12],
    'Sales': [120, 110, 95, 125,  # Q1
             115, 105, 90, 120,  # Q2
             110, 80, 85, 115,   # Q3
             ]
})

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: Regional breakdown
ax1 = axes[0, 0]
region_sales = regions_data.groupby('Region')['Sales'].sum().sort_values()
colors = ['#2ECC71' if x > 320 else '#E74C3C' for x in region_sales.values]
bars = ax1.barh(region_sales.index, region_sales.values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

# Highlight problem region
for i, (region, value) in enumerate(region_sales.items()):
    if value == region_sales.min():
        ax1.text(value + 10, i, f'⚠️ Issue here! Only ₹{value}K', 
                va='center', fontsize=11, fontweight='bold', color='#C0392B')
    else:
        ax1.text(value + 10, i, f'₹{value}K', va='center', fontsize=10)

ax1.set_title('Root Cause #1: South Region Underperforming', 
             fontsize=13, fontweight='bold', color='#2C3E50')
ax1.set_xlabel('Total Sales (₹K)', fontsize=11, fontweight='bold')
ax1.axvline(x=region_sales.mean(), color='orange', linestyle='--', linewidth=2, label='Average')
ax1.legend()

# Chart 2: Product category breakdown
ax2 = axes[0, 1]
products = ['Laptops', 'Phones', 'Tablets', 'Accessories']
product_sales = [280, 260, 150, 110]
product_growth = [-5, -3, -15, -8]  # % growth

x_pos = np.arange(len(products))
bars2 = ax2.bar(x_pos, product_sales, alpha=0.8, edgecolor='black', linewidth=1.5)

# Color by growth
for i, (bar, growth) in enumerate(zip(bars2, product_growth)):
    if growth < -10:
        bar.set_color('#E74C3C')
    elif growth < 0:
        bar.set_color('#F39C12')
    else:
        bar.set_color('#2ECC71')
    
    # Add growth labels
    ax2.text(i, product_sales[i] + 10, f'{growth}%', 
            ha='center', fontsize=10, fontweight='bold',
            color='#C0392B' if growth < -10 else '#7F8C8D')

ax2.set_xticks(x_pos)
ax2.set_xticklabels(products)
ax2.set_title('Root Cause #2: Tablet Sales Crashed (-15%)', 
             fontsize=13, fontweight='bold', color='#2C3E50')
ax2.set_ylabel('Sales (₹K)', fontsize=11, fontweight='bold')

# Highlight problem product
rect = patches.Rectangle((2-0.4, 0), 0.8, product_sales[2], 
                         linewidth=3, edgecolor='red', facecolor='none', linestyle='--')
ax2.add_patch(rect)

# Chart 3: Customer satisfaction trend
ax3 = axes[1, 0]
satisfaction_months = ['Jan', 'Apr', 'Jul', 'Oct', 'Dec']
satisfaction_scores = [4.5, 4.3, 3.9, 3.5, 3.2]

ax3.plot(satisfaction_months, satisfaction_scores, marker='o', linewidth=3, 
        markersize=12, color='#E74C3C')
ax3.fill_between(range(len(satisfaction_months)), satisfaction_scores, 
                alpha=0.3, color='#E74C3C')

# Add threshold line
ax3.axhline(y=4.0, color='#2ECC71', linestyle='--', linewidth=2, label='Acceptable (4.0)')

# Annotate crisis point
crisis_idx = satisfaction_scores.index(min(satisfaction_scores))
ax3.annotate('Critical Level!', 
           xy=(crisis_idx, satisfaction_scores[crisis_idx]), 
           xytext=(crisis_idx-0.5, 4.0),
           fontsize=12, fontweight='bold', color='#C0392B',
           bbox=dict(boxstyle='round', facecolor='#FADBD8', edgecolor='#E74C3C'),
           arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2))

ax3.set_title('Root Cause #3: Customer Satisfaction Declining', 
             fontsize=13, fontweight='bold', color='#2C3E50')
ax3.set_ylabel('Satisfaction Score', fontsize=11, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_ylim(2.5, 5)

# Chart 4: Competition analysis
ax4 = axes[1, 1]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
our_market_share = [35, 33, 30, 27]
competitor_share = [30, 32, 35, 38]

ax4.plot(quarters, our_market_share, marker='o', linewidth=3, markersize=10,
        label='Our Share', color='#E74C3C')
ax4.plot(quarters, competitor_share, marker='s', linewidth=3, markersize=10,
        label='Competitor', color='#3498DB')

# Highlight crossover point
ax4.annotate('Competitor overtook us!', 
           xy=(2.5, 32.5), xytext=(1.5, 25),
           fontsize=12, fontweight='bold', color='#C0392B',
           bbox=dict(boxstyle='round', facecolor='#FADBD8', edgecolor='#E74C3C'),
           arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2))

ax4.set_title('Root Cause #4: Losing Market Share to Competition', 
             fontsize=13, fontweight='bold', color='#2C3E50')
ax4.set_ylabel('Market Share (%)', fontsize=11, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.suptitle('INVESTIGATION: Four Key Factors Driving Decline', 
            fontsize=18, fontweight='bold', color='#2C3E50')
plt.tight_layout()
plt.savefig('02_story_investigation.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Investigation visualization saved")

# =========================================================================
# PART 3: THE INSIGHT - AHA MOMENT
# =========================================================================

print("\n💡 PART 3: Story Arc - The Key Insight")

fig, ax = plt.subplots(figsize=(14, 8))

# Show correlation between satisfaction and sales
np.random.seed(56)
satisfaction = np.linspace(3.2, 4.5, 12)
sales_corr = satisfaction * 100 + np.random.normal(0, 10, 12)

# Scatter plot
ax.scatter(satisfaction, sales_corr, s=200, alpha=0.6, c=range(12), 
          cmap='RdYlGn', edgecolor='black', linewidth=2)

# Add regression line
z = np.polyfit(satisfaction, sales_corr, 1)
p = np.poly1d(z)
ax.plot(satisfaction, p(satisfaction), "r--", linewidth=3, alpha=0.8, label='Trend Line')

# Annotate the insight
ax.annotate('THE INSIGHT:\nCustomer satisfaction\ndirectly drives sales!', 
           xy=(3.7, 380), xytext=(4.0, 450),
           fontsize=16, fontweight='bold', color='#27AE60',
           bbox=dict(boxstyle='round,pad=1', facecolor='#D5F4E6', 
                    edgecolor='#27AE60', linewidth=3),
           arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', 
                          color='#27AE60', lw=3))

# Add correlation coefficient
correlation = np.corrcoef(satisfaction, sales_corr)[0, 1]
ax.text(0.05, 0.95, f'Correlation: {correlation:.2f}\n(Strong positive)', 
       transform=ax.transAxes, fontsize=13, fontweight='bold',
       verticalalignment='top',
       bbox=dict(boxstyle='round', facecolor='#FFF9C4', alpha=0.9, edgecolor='#F39C12', linewidth=2))

# Styling
ax.set_title('THE INSIGHT: Strong Correlation Between Satisfaction & Sales', 
            fontsize=18, fontweight='bold', pad=20, color='#2C3E50')
ax.set_xlabel('Customer Satisfaction Score', fontsize=13, fontweight='bold')
ax.set_ylabel('Sales (₹ Thousands)', fontsize=13, fontweight='bold')
ax.legend(loc='lower right', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_facecolor('#F8F9FA')

# Add colorbar
sm = plt.cm.ScalarMappable(cmap='RdYlGn', norm=plt.Normalize(vmin=0, vmax=12))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Month (Jan → Dec)', fontsize=11, fontweight='bold')

# Add key insight box
fig.text(0.5, 0.02, 
        '💡 Key Finding: Every 0.1 point increase in satisfaction = ₹10K more in sales',
        ha='center', fontsize=12, fontweight='bold', color='#27AE60',
        bbox=dict(boxstyle='round', facecolor='#D5F4E6', alpha=0.9, edgecolor='#27AE60', linewidth=2))

plt.tight_layout()
plt.savefig('03_story_insight.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Insight visualization saved")

# =========================================================================
# PART 4: THE SOLUTION - ACTION PLAN
# =========================================================================

print("\n🎯 PART 4: Story Arc - The Solution")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: Proposed improvements
ax1 = axes[0, 0]
initiatives = ['Improve\nSupport', 'Faster\nShipping', 'Product\nQuality', 'Loyalty\nProgram']
impact_on_satisfaction = [0.4, 0.3, 0.5, 0.2]
implementation_cost = [50, 80, 120, 40]

# Bubble chart
sizes = [cost * 5 for cost in implementation_cost]
colors_initiatives = ['#2ECC71', '#3498DB', '#F39C12', '#9B59B6']
bubbles = ax1.scatter(range(len(initiatives)), impact_on_satisfaction, 
                     s=sizes, c=colors_initiatives, alpha=0.6, edgecolor='black', linewidth=2)

# Annotate each bubble
for i, (init, impact, cost) in enumerate(zip(initiatives, impact_on_satisfaction, implementation_cost)):
    ax1.text(i, impact, f'₹{cost}K', ha='center', va='center', 
            fontsize=10, fontweight='bold')

ax1.set_xticks(range(len(initiatives)))
ax1.set_xticklabels(initiatives, fontsize=11)
ax1.set_title('Proposed Initiatives (Size = Cost)', 
             fontsize=13, fontweight='bold', color='#2C3E50')
ax1.set_ylabel('Expected Impact on Satisfaction', fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')

# Highlight best ROI
best_idx = impact_on_satisfaction.index(max(impact_on_satisfaction))
rect = patches.Rectangle((best_idx-0.3, 0), 0.6, impact_on_satisfaction[best_idx], 
                         linewidth=3, edgecolor='#27AE60', facecolor='none', linestyle='--')
ax1.add_patch(rect)
ax1.text(best_idx, 0.55, '⭐ Best ROI', ha='center', fontsize=11, 
        fontweight='bold', color='#27AE60')

# Chart 2: Projected recovery timeline
ax2 = axes[0, 1]
timeline_months = ['Current', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 6']
satisfaction_projected = [3.2, 3.5, 3.8, 4.1, 4.3, 4.5]
sales_projected = [290, 320, 355, 390, 420, 450]

ax2_twin = ax2.twinx()

# Plot satisfaction
line1 = ax2.plot(timeline_months, satisfaction_projected, marker='o', linewidth=3, 
                markersize=10, color='#3498DB', label='Satisfaction')
ax2.fill_between(range(len(timeline_months)), satisfaction_projected, 
                alpha=0.2, color='#3498DB')

# Plot sales
line2 = ax2_twin.plot(timeline_months, sales_projected, marker='s', linewidth=3, 
                     markersize=10, color='#2ECC71', label='Sales')
ax2_twin.fill_between(range(len(timeline_months)), sales_projected, 
                     alpha=0.2, color='#2ECC71')

# Styling
ax2.set_title('Projected Recovery Timeline', fontsize=13, fontweight='bold', color='#2C3E50')
ax2.set_ylabel('Satisfaction Score', fontsize=11, fontweight='bold', color='#3498DB')
ax2_twin.set_ylabel('Sales (₹K)', fontsize=11, fontweight='bold', color='#2ECC71')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)

# Combined legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax2.legend(lines, labels, loc='upper left')

# Chart 3: Before vs After comparison
ax3 = axes[1, 0]
categories = ['Sales', 'Customer\nSatisfaction', 'Market\nShare', 'Profit\nMargin']
before = [290, 3.2, 27, 15]
after = [450, 4.5, 35, 22]

x = np.arange(len(categories))
width = 0.35

bars1 = ax3.bar(x - width/2, before, width, label='Before (Current)', 
               color='#E74C3C', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax3.bar(x + width/2, after, width, label='After (6 Months)', 
               color='#2ECC71', alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f}' if height > 10 else f'{height:.1f}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

ax3.set_xticks(x)
ax3.set_xticklabels(categories, fontsize=10)
ax3.set_title('Before vs After: Expected Improvements', 
             fontsize=13, fontweight='bold', color='#2C3E50')
ax3.legend()
ax3.grid(axis='y', alpha=0.3)

# Chart 4: Investment vs Return
ax4 = axes[1, 1]
investment_phases = ['Phase 1\n(Month 1-2)', 'Phase 2\n(Month 3-4)', 'Phase 3\n(Month 5-6)']
investment = [130, 100, 60]
expected_return = [65, 190, 250]
cumulative_roi = [65, 255, 505]

x_inv = np.arange(len(investment_phases))
width = 0.25

bars_inv = ax4.bar(x_inv - width, investment, width, label='Investment', 
                  color='#E67E22', alpha=0.8, edgecolor='black', linewidth=1.5)
bars_ret = ax4.bar(x_inv, expected_return, width, label='Return (That Phase)', 
                  color='#3498DB', alpha=0.8, edgecolor='black', linewidth=1.5)
bars_cum = ax4.bar(x_inv + width, cumulative_roi, width, label='Cumulative Return', 
                  color='#2ECC71', alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars_inv, bars_ret, bars_cum]:
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'₹{height}K', ha='center', fontsize=9, fontweight='bold')

ax4.set_xticks(x_inv)
ax4.set_xticklabels(investment_phases, fontsize=10)
ax4.set_title('Investment vs ROI Analysis', fontsize=13, fontweight='bold', color='#2C3E50')
ax4.set_ylabel('Amount (₹K)', fontsize=11, fontweight='bold')
ax4.legend(fontsize=9)
ax4.grid(axis='y', alpha=0.3)

# Add break-even line
ax4.axhline(y=290, color='red', linestyle='--', linewidth=2, label='Break-even')

plt.suptitle('THE SOLUTION: Comprehensive Action Plan with Projections', 
            fontsize=18, fontweight='bold', color='#2C3E50')
plt.tight_layout()
plt.savefig('04_story_solution.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Solution visualization saved")

# =========================================================================
# PART 5: THE COMPLETE STORY - ONE PAGE
# =========================================================================

print("\n📖 PART 5: Complete Story on One Page")

fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(4, 3, hspace=0.4, wspace=0.3, 
                      height_ratios=[0.5, 1.5, 1.5, 1])

# Title section
ax_title = fig.add_subplot(gs[0, :])
ax_title.text(0.5, 0.5, 'Sales Recovery Strategy: From Crisis to Growth', 
             ha='center', va='center', fontsize=24, fontweight='bold', color='#2C3E50')
ax_title.text(0.5, 0.1, 'A Data-Driven Story', 
             ha='center', va='center', fontsize=14, style='italic', color='#7F8C8D')
ax_title.axis('off')
ax_title.set_facecolor('#ECF0F1')

# Problem section (large)
ax_problem = fig.add_subplot(gs[1, :])
ax_problem.plot(months, sales_2025, marker='o', linewidth=3, markersize=8, 
               color='#E74C3C', label='Actual Sales')
ax_problem.plot(months, sales_target, linestyle='--', linewidth=2, 
               color='#2ECC71', label='Target')
ax_problem.fill_between(range(len(months)), sales_2025, sales_target, 
                        alpha=0.2, color='#E74C3C')
ax_problem.set_title('① THE PROBLEM: 36% Sales Decline', 
                    fontsize=16, fontweight='bold', color='#C0392B', pad=15)
ax_problem.set_ylabel('Sales (₹K)', fontsize=11, fontweight='bold')
ax_problem.legend(loc='upper right')
ax_problem.grid(True, alpha=0.3)
ax_problem.set_facecolor('#FFF5F5')

# Root causes (3 small charts)
# Root Cause 1
ax_rc1 = fig.add_subplot(gs[2, 0])
region_sales = regions_data.groupby('Region')['Sales'].sum().sort_values()
colors_rc = ['#E74C3C' if x < 320 else '#2ECC71' for x in region_sales.values]
ax_rc1.barh(region_sales.index, region_sales.values, color=colors_rc, alpha=0.7)
ax_rc1.set_title('② Root Cause: South Region', fontsize=12, fontweight='bold')
ax_rc1.set_xlabel('Sales (₹K)', fontsize=10)

# Root Cause 2
ax_rc2 = fig.add_subplot(gs[2, 1])
ax_rc2.plot(satisfaction_months, satisfaction_scores, marker='o', 
           linewidth=3, color='#E74C3C')
ax_rc2.axhline(y=4.0, color='orange', linestyle='--', linewidth=2)
ax_rc2.set_title('② Root Cause: Low Satisfaction', fontsize=12, fontweight='bold')
ax_rc2.set_ylabel('Score', fontsize=10)
ax_rc2.grid(True, alpha=0.3)

# Root Cause 3
ax_rc3 = fig.add_subplot(gs[2, 2])
ax_rc3.bar(range(len(products)), product_sales, alpha=0.7)
ax_rc3.set_xticks(range(len(products)))
ax_rc3.set_xticklabels(products, rotation=45, fontsize=9)
ax_rc3.set_title('② Root Cause: Tablet Crash', fontsize=12, fontweight='bold')
ax_rc3.set_ylabel('Sales (₹K)', fontsize=10)

# Solution section (bottom - spanning all)
ax_solution = fig.add_subplot(gs[3, :])
timeline_full = ['Now', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6']
sales_recovery = [290, 310, 335, 365, 395, 425, 450]
ax_solution.plot(timeline_full, sales_recovery, marker='o', linewidth=4, 
                markersize=12, color='#2ECC71', label='Projected Recovery')
ax_solution.fill_between(range(len(timeline_full)), sales_recovery, 
                         alpha=0.3, color='#2ECC71')
ax_solution.axhline(y=450, color='#3498DB', linestyle='--', linewidth=2, 
                   label='Target Achievement')
ax_solution.set_title('③ THE SOLUTION: 6-Month Recovery Plan', 
                     fontsize=16, fontweight='bold', color='#27AE60', pad=15)
ax_solution.set_ylabel('Projected Sales (₹K)', fontsize=11, fontweight='bold')
ax_solution.set_xlabel('Timeline', fontsize=11, fontweight='bold')
ax_solution.legend(loc='lower right', fontsize=11)
ax_solution.grid(True, alpha=0.3)
ax_solution.set_facecolor('#F0FFF0')

# Annotate solution
ax_solution.annotate('Target achieved!', 
                    xy=(6, 450), xytext=(5, 410),
                    fontsize=13, fontweight='bold', color='#27AE60',
                    bbox=dict(boxstyle='round', facecolor='#D5F4E6', edgecolor='#27AE60', linewidth=2),
                    arrowprops=dict(arrowstyle='->', color='#27AE60', lw=2))

# Key Actions box
fig.text(0.5, 0.01, 
        '🎯 KEY ACTIONS: Improve Support Quality (+0.4) | Enhance Product Quality (+0.5) | Launch Loyalty Program (+0.2) → Expected ROI: 174% in 6 months',
        ha='center', fontsize=11, fontweight='bold', color='white',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#27AE60', edgecolor='black', linewidth=2))

plt.savefig('05_complete_story_one_page.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Complete story (one page) saved")

# =========================================================================
# PART 6: BEFORE & AFTER TRANSFORMATION
# =========================================================================

print("\n🔄 PART 6: Before & After - The Transformation")

fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(18, 8))

# BEFORE: Boring data table
ax_before.axis('tight')
ax_before.axis('off')
table_data = [
    ['Month', 'Sales', 'Target', 'Gap'],
    ['Jan', '450', '500', '-50'],
    ['Feb', '430', '500', '-70'],
    ['Mar', '410', '500', '-90'],
    ['Apr', '390', '500', '-110'],
    ['...', '...', '...', '...'],
    ['Dec', '290', '500', '-210']
]
table = ax_before.table(cellText=table_data, cellLoc='center', loc='center',
                       colWidths=[0.2, 0.2, 0.2, 0.2])
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 3)

# Style header
for i in range(4):
    table[(0, i)].set_facecolor('#95A5A6')
    table[(0, i)].set_text_props(weight='bold', color='white')

ax_before.set_title('BEFORE: Raw Data Table', 
                   fontsize=16, fontweight='bold', pad=20, color='#7F8C8D')
ax_before.text(0.5, 0.1, '❌ Hard to see patterns\n❌ No insights\n❌ Requires analysis', 
              ha='center', transform=ax_before.transAxes, fontsize=12, color='#E74C3C')

# AFTER: Storytelling visualization
ax_after.plot(months, sales_2025, marker='o', linewidth=3, markersize=10, color='#E74C3C')
ax_after.plot(months, sales_target, linestyle='--', linewidth=2, color='#2ECC71')
ax_after.fill_between(range(len(months)), sales_2025, sales_target, alpha=0.2, color='#E74C3C')

# Add annotations
ax_after.annotate('Declining trend clear!', 
                 xy=(6, sales_2025[6]), xytext=(8, 450),
                 fontsize=12, fontweight='bold', color='#C0392B',
                 bbox=dict(boxstyle='round', facecolor='#FADBD8', edgecolor='#E74C3C'),
                 arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2))

ax_after.set_title('AFTER: Visual Story', 
                  fontsize=16, fontweight='bold', pad=20, color='#2C3E50')
ax_after.set_xlabel('Month', fontsize=12, fontweight='bold')
ax_after.set_ylabel('Sales (₹K)', fontsize=12, fontweight='bold')
ax_after.grid(True, alpha=0.3)
ax_after.text(0.5, 0.1, '✅ Pattern obvious\n✅ Insight immediate\n✅ Action clear', 
             ha='center', transform=ax_after.transAxes, fontsize=12, color='#27AE60',
             bbox=dict(boxstyle='round', facecolor='#D5F4E6', alpha=0.8))

plt.suptitle('The Power of Visual Storytelling', fontsize=20, fontweight='bold', color='#2C3E50')
plt.tight_layout()
plt.savefig('06_before_after_transformation.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Before/After transformation saved")

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 56 COMPLETE ✅")
print("="*70)
print("\n📖 Story Visualizations Created:")
print("  1. ✅ 01_story_problem.png - Setting the context (declining sales)")
print("  2. ✅ 02_story_investigation.png - Root cause analysis (4 factors)")
print("  3. ✅ 03_story_insight.png - The aha moment (satisfaction→sales)")
print("  4. ✅ 04_story_solution.png - Action plan with projections")
print("  5. ✅ 05_complete_story_one_page.png - Full narrative on one page")
print("  6. ✅ 06_before_after_transformation.png - Visual storytelling power")
print("\n🎯 Storytelling Techniques Mastered:")
print("  • Narrative arc: Problem → Investigation → Insight → Solution")
print("  • Guided annotations to direct attention")
print("  • Color coding for emotional response (red=bad, green=good)")
print("  • Before/After comparisons")
print("  • Progressive disclosure (build complexity)")
print("  • Action-oriented conclusions")
print("\n💡 Key Storytelling Principles:")
print("  ① Start with the problem (create tension)")
print("  ② Show your investigation (build credibility)")
print("  ③ Reveal the insight (aha moment)")
print("  ④ Present the solution (release tension)")
print("  ⑤ Make it actionable (call to action)")
print("\n🔥 Impact:")
print("  Data alone: Numbers on a page")
print("  Data story: Compelling narrative → Decisions → Action")
print("  → Good analysis finds insights")
print("  → Great storytelling creates change")
print("="*70)