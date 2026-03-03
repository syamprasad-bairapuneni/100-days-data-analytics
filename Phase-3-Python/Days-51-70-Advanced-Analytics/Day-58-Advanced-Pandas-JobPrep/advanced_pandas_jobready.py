# Day 58 - Advanced Pandas Techniques
# Real-World Data Analysis Skills
# Author: Syamprasad
# Date: March 3, 2026

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("="*70)
print("DAY 58 - ADVANCED PANDAS TECHNIQUES")
print("Real-World Data Analysis Skills")
print("="*70)

# =========================================================================
# PART 1: ADVANCED FILTERING & SELECTION
# =========================================================================

print("\n🔍 PART 1: Advanced Filtering Techniques")

# Generate realistic dataset
np.random.seed(58)

df = pd.DataFrame({
    'Employee_ID': range(1, 201),
    'Name': [f'Employee_{i:03d}' for i in range(1, 201)],
    'Department': np.random.choice(['Engineering', 'Sales', 'Marketing', 'HR', 'Finance'], 200),
    'Salary': np.random.randint(40000, 150000, 200),
    'Experience_Years': np.random.randint(0, 25, 200),
    'Performance_Rating': np.random.uniform(2.0, 5.0, 200),
    'Bonus_Percent': np.random.randint(0, 30, 200),
    'Location': np.random.choice(['Bangalore', 'Mumbai', 'Hyderabad', 'Delhi', 'Pune'], 200)
})

print(f"\n✅ Dataset: {len(df)} employees across {df['Department'].nunique()} departments")

# Technique 1: Multiple conditions
print("\n1️⃣ Complex Boolean Filtering:")
high_performers = df[
    (df['Salary'] > 80000) & 
    (df['Performance_Rating'] > 4.0) & 
    (df['Experience_Years'] > 5)
]
print(f"   High performers (Salary>80K, Rating>4.0, Exp>5): {len(high_performers)}")

# Technique 2: Query method (SQL-like)
print("\n2️⃣ Query Method (SQL-like):")
query_result = df.query('Department == "Engineering" and Salary > 100000')
print(f"   Engineers earning >100K: {len(query_result)}")

# Technique 3: isin() for multiple values
print("\n3️⃣ Filter by Multiple Values:")
top_depts = df[df['Department'].isin(['Engineering', 'Sales'])]
print(f"   Employees in Engineering/Sales: {len(top_depts)}")

# Technique 4: between() for ranges
print("\n4️⃣ Range Filtering:")
mid_career = df[df['Experience_Years'].between(5, 15)]
print(f"   Mid-career (5-15 years): {len(mid_career)}")

# Technique 5: nlargest/nsmallest
print("\n5️⃣ Top/Bottom N:")
top_earners = df.nlargest(10, 'Salary')[['Name', 'Department', 'Salary']]
print(f"   Top 10 earners:\n{top_earners.head(3)}")

# =========================================================================
# PART 2: GROUPBY MASTERY
# =========================================================================

print("\n📊 PART 2: Advanced GroupBy Operations")

# Multiple aggregations
print("\n1️⃣ Department Statistics:")
dept_stats = df.groupby('Department').agg({
    'Salary': ['mean', 'median', 'std'],
    'Performance_Rating': 'mean',
    'Employee_ID': 'count'
}).round(2)

dept_stats.columns = ['Avg_Salary', 'Median_Salary', 'Std_Salary', 'Avg_Performance', 'Count']
print(dept_stats)

# Transform (add group statistics to original)
print("\n2️⃣ Adding Group Statistics:")
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
df['Salary_vs_Dept_Avg'] = df['Salary'] - df['Dept_Avg_Salary']
print(f"\n   Sample with dept comparison:\n{df[['Name', 'Department', 'Salary', 'Dept_Avg_Salary']].head()}")

# Custom aggregation function
print("\n3️⃣ Custom Aggregation:")
def salary_range(x):
    return x.max() - x.min()

dept_range = df.groupby('Department')['Salary'].agg([
    ('Min', 'min'),
    ('Max', 'max'),
    ('Range', salary_range)
])
print(dept_range)

# =========================================================================
# PART 3: PIVOT TABLES & RESHAPING
# =========================================================================

print("\n🔄 PART 3: Pivot Tables & Data Reshaping")

# Pivot table
print("\n1️⃣ Pivot Table: Department × Location")
pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='Location',
    aggfunc='mean',
    fill_value=0
).round(0)
print(pivot)

# Cross-tabulation
print("\n2️⃣ Cross-Tabulation:")
crosstab = pd.crosstab(
    df['Department'],
    df['Location'],
    values=df['Salary'],
    aggfunc='count',
    margins=True
)
print(crosstab)

# =========================================================================
# PART 4: HANDLING MISSING DATA
# =========================================================================

print("\n🔧 PART 4: Missing Data Handling")

# Introduce some missing values
df_missing = df.copy()
df_missing.loc[np.random.choice(df_missing.index, 20), 'Salary'] = np.nan
df_missing.loc[np.random.choice(df_missing.index, 15), 'Performance_Rating'] = np.nan

print(f"\n1️⃣ Missing Value Detection:")
print(f"   Missing salaries: {df_missing['Salary'].isna().sum()}")
print(f"   Missing ratings: {df_missing['Performance_Rating'].isna().sum()}")

# Fill strategies
print("\n2️⃣ Filling Strategies:")
df_filled = df_missing.copy()
df_filled['Salary'].fillna(df_filled['Salary'].median(), inplace=True)
df_filled['Performance_Rating'].fillna(df_filled['Performance_Rating'].mean(), inplace=True)
print(f"   After filling - Missing: {df_filled.isna().sum().sum()}")

# =========================================================================
# PART 5: STRING OPERATIONS
# =========================================================================

print("\n🔤 PART 5: String Operations")

# Add email column
df['Email'] = df['Name'].str.lower().str.replace('_', '.') + '@company.com'

print("\n1️⃣ String Methods:")
print(f"   Sample emails:\n{df[['Name', 'Email']].head()}")

# Extract information
df['Employee_Number'] = df['Name'].str.extract(r'(\d+)').astype(int)
print(f"\n   Extracted numbers: {df['Employee_Number'].head()}")

# =========================================================================
# PART 6: DATETIME OPERATIONS
# =========================================================================

print("\n📅 PART 6: DateTime Operations")

# Create date columns
start_date = pd.Timestamp('2020-01-01')
df['Join_Date'] = [start_date + pd.Timedelta(days=np.random.randint(0, 1800)) for _ in range(len(df))]
df['Days_Employed'] = (pd.Timestamp('2026-03-01') - df['Join_Date']).dt.days

print(f"\n1️⃣ Date Statistics:")
print(f"   Earliest join: {df['Join_Date'].min().date()}")
print(f"   Latest join: {df['Join_Date'].max().date()}")
print(f"   Avg days employed: {df['Days_Employed'].mean():.0f}")

# Extract date parts
df['Join_Year'] = df['Join_Date'].dt.year
df['Join_Month'] = df['Join_Date'].dt.month

print(f"\n2️⃣ Employees by Join Year:")
print(df['Join_Year'].value_counts().sort_index())

# =========================================================================
# PART 7: MERGING & JOINING
# =========================================================================

print("\n🔗 PART 7: Merging & Joining")

# Create second dataset
projects = pd.DataFrame({
    'Employee_ID': np.random.choice(df['Employee_ID'], 100),
    'Project_Name': [f'Project_{chr(65+i%5)}' for i in range(100)],
    'Hours_Spent': np.random.randint(10, 200, 100)
})

print(f"\n1️⃣ Joining Employee & Project Data:")
merged = df.merge(projects, on='Employee_ID', how='left')
print(f"   Merged dataset: {len(merged)} rows")
print(f"   Employees with projects: {merged['Project_Name'].notna().sum()}")

# =========================================================================
# PART 8: QUICK VISUALIZATION
# =========================================================================

print("\n📈 PART 8: Quick Visualizations")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Chart 1: Salary by Department
dept_salary = df.groupby('Department')['Salary'].mean().sort_values(ascending=True)
axes[0, 0].barh(dept_salary.index, dept_salary.values, color='steelblue', alpha=0.7)
axes[0, 0].set_title('Average Salary by Department', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Salary (₹)')

# Chart 2: Experience vs Salary
axes[0, 1].scatter(df['Experience_Years'], df['Salary'], alpha=0.5, s=50)
axes[0, 1].set_title('Experience vs Salary', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Experience (Years)')
axes[0, 1].set_ylabel('Salary (₹)')
axes[0, 1].grid(True, alpha=0.3)

# Chart 3: Performance Distribution
sns.boxplot(data=df, x='Department', y='Performance_Rating', 
           palette='Set2', ax=axes[1, 0])
axes[1, 0].set_title('Performance by Department', fontsize=12, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)

# Chart 4: Location Distribution
location_counts = df['Location'].value_counts()
axes[1, 1].pie(location_counts.values, labels=location_counts.index, 
              autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('Employee Distribution by Location', fontsize=12, fontweight='bold')

plt.suptitle('Day 58 - Employee Analytics Dashboard', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('employee_analytics_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Visualization saved: employee_analytics_dashboard.png")

# =========================================================================
# PART 9: PRACTICAL SCENARIOS
# =========================================================================

print("\n💼 PART 9: Real-World Scenarios")

print("\n📊 Scenario 1: Top Performers per Department")
top_per_dept = df.groupby('Department').apply(
    lambda x: x.nlargest(3, 'Performance_Rating')[['Name', 'Performance_Rating']]
).reset_index(drop=True)
print(top_per_dept.head(9))

print("\n📊 Scenario 2: Salary Outliers")
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Salary'] < Q1 - 1.5*IQR) | (df['Salary'] > Q3 + 1.5*IQR)]
print(f"   Outliers detected: {len(outliers)}")
print(f"   Range: ₹{outliers['Salary'].min():,.0f} - ₹{outliers['Salary'].max():,.0f}")

print("\n📊 Scenario 3: Retention Analysis")
recent_hires = df[df['Days_Employed'] < 365]
veteran_employees = df[df['Days_Employed'] > 1825]  # 5 years
print(f"   Recent hires (<1 year): {len(recent_hires)}")
print(f"   Veterans (>5 years): {len(veteran_employees)}")
print(f"   Avg veteran salary: ₹{veteran_employees['Salary'].mean():,.0f}")
print(f"   Avg new hire salary: ₹{recent_hires['Salary'].mean():,.0f}")

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 58 COMPLETE ✅")
print("="*70)

print("\n🎯 Skills Practiced:")
print("  1. ✅ Advanced filtering (query, isin, between)")
print("  2. ✅ GroupBy operations (agg, transform, apply)")
print("  3. ✅ Pivot tables and cross-tabulation")
print("  4. ✅ Missing data handling")
print("  5. ✅ String operations (.str methods)")
print("  6. ✅ DateTime operations")
print("  7. ✅ Merging and joining datasets")
print("  8. ✅ Quick visualizations")
print("  9. ✅ Real-world scenarios")

print("\n💡 Key Techniques Learned:")
print("  • Complex boolean filtering for precise data selection")
print("  • Transform() to add group statistics to original rows")
print("  • IQR method for robust outlier detection")
print("  • Pivot tables for multi-dimensional analysis")

print("\n📊 Day 58 Analysis:")
print(f"   Dataset: {len(df)} employees analyzed")
print(f"   Departments: {df['Department'].nunique()}")
print(f"   Locations: {df['Location'].nunique()}")
print(f"   Visualizations: 4 charts created")

print("\n🎯 Next: Day 59 - Data reshaping with melt and pivot")
print("="*70)