# Day 59 - Data Reshaping Basics
# Melt and Pivot Operations
# Author: Syamprasad
# Date: March 9, 2026

import pandas as pd
import numpy as np

print("="*70)
print("DAY 59 - DATA RESHAPING BASICS")
print("Welcome Back! Let's Ease Into Learning")
print("="*70)

# =========================================================================
# PART 1: UNDERSTANDING WIDE VS LONG FORMAT
# =========================================================================

print("\n📊 PART 1: Wide vs Long Format")

# Wide format (common in Excel)
wide_data = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Q1_Sales': [100, 120, 90, 110],
    'Q2_Sales': [110, 115, 95, 120],
    'Q3_Sales': [105, 125, 100, 115],
    'Q4_Sales': [115, 130, 105, 125]
})

print("\n1️⃣ WIDE Format (Original):")
print(wide_data)
print(f"   Shape: {wide_data.shape}")

# =========================================================================
# PART 2: MELT - WIDE TO LONG
# =========================================================================

print("\n🔄 PART 2: Melt - Wide to Long Format")

# Basic melt
long_data = wide_data.melt(
    id_vars='Employee',
    var_name='Quarter',
    value_name='Sales'
)

print("\n2️⃣ LONG Format (After Melt):")
print(long_data)
print(f"   Shape: {long_data.shape}")

print("\n💡 What happened:")
print("   • Wide: 4 rows × 5 columns")
print("   • Long: 16 rows × 3 columns")
print("   • Same data, different structure!")

# Clean up quarter names
long_data['Quarter'] = long_data['Quarter'].str.replace('_Sales', '')
print("\n3️⃣ Cleaned Quarter Names:")
print(long_data.head(8))

# =========================================================================
# PART 3: PIVOT - LONG TO WIDE
# =========================================================================

print("\n🔄 PART 3: Pivot - Long to Wide Format")

# Pivot back
pivoted_data = long_data.pivot(
    index='Employee',
    columns='Quarter',
    values='Sales'
)

print("\n4️⃣ PIVOTED Back to Wide:")
print(pivoted_data)
print(f"   Shape: {pivoted_data.shape}")

# Reset index to make it look like original
pivoted_data_clean = pivoted_data.reset_index()
print("\n5️⃣ With Index Reset:")
print(pivoted_data_clean)

# =========================================================================
# PART 4: PRACTICAL EXAMPLE - SALES DATA
# =========================================================================

print("\n💼 PART 4: Practical Business Example")

# Real-world scenario
sales_wide = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet'],
    'Jan': [50, 80, 30],
    'Feb': [55, 85, 35],
    'Mar': [60, 90, 40],
    'Apr': [58, 88, 38]
})

print("\n📊 Monthly Sales by Product (Wide):")
print(sales_wide)

# Melt for analysis
sales_long = sales_wide.melt(
    id_vars='Product',
    var_name='Month',
    value_name='Units_Sold'
)

print("\n📊 Monthly Sales by Product (Long):")
print(sales_long)

# Now we can easily analyze
print("\n📈 Analysis Made Easy:")
print(f"   Total units sold: {sales_long['Units_Sold'].sum()}")
print(f"   Average per product-month: {sales_long['Units_Sold'].mean():.1f}")

# Best month per product
best_months = sales_long.loc[sales_long.groupby('Product')['Units_Sold'].idxmax()]
print("\n🏆 Best Month for Each Product:")
print(best_months[['Product', 'Month', 'Units_Sold']])

# =========================================================================
# PART 5: PIVOT_TABLE (MORE POWERFUL)
# =========================================================================

print("\n📊 PART 5: Pivot Table with Aggregation")

# Generate sample data
np.random.seed(59)
transactions = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Sales': np.random.randint(100, 1000, 100)
})

print("\n1️⃣ Transaction Data Sample:")
print(transactions.head())

# Create pivot table
pivot_summary = pd.pivot_table(
    transactions,
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc='sum',
    fill_value=0
)

print("\n2️⃣ Pivot Table - Total Sales by Product × Region:")
print(pivot_summary)

# Add totals
pivot_summary['Total'] = pivot_summary.sum(axis=1)
print("\n3️⃣ With Row Totals:")
print(pivot_summary)

# =========================================================================
# PART 6: WHEN TO USE WHAT
# =========================================================================

print("\n🎯 PART 6: When to Use Each Operation")

print("\n📋 Use MELT when:")
print("   • Converting Excel-style data to analysis format")
print("   • Need to perform operations by category")
print("   • Preparing data for visualization")
print("   • Database-style operations needed")

print("\n📋 Use PIVOT when:")
print("   • Creating summary tables")
print("   • Converting analysis results to report format")
print("   • Making data Excel-friendly")
print("   • Creating comparison tables")

print("\n📋 Use PIVOT_TABLE when:")
print("   • Need aggregation (sum, mean, count)")
print("   • Handling duplicate entries")
print("   • Creating business reports")
print("   • Multi-level analysis")

# =========================================================================
# PART 7: QUICK EXAMPLES
# =========================================================================

print("\n⚡ PART 7: Quick Real-World Examples")

# Example 1: Student grades
grades = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'Science': [88, 85, 92],
    'English': [90, 88, 85]
})

print("\n1️⃣ Student Grades (Wide):")
print(grades)

grades_long = grades.melt(id_vars='Student', var_name='Subject', value_name='Score')
print("\n   Same Data (Long):")
print(grades_long)

# Example 2: Temperature data
temp_data = pd.DataFrame({
    'City': ['NYC', 'LA', 'Chicago'],
    'Morning': [20, 25, 15],
    'Afternoon': [30, 35, 25],
    'Evening': [25, 30, 20]
})

print("\n2️⃣ Temperature by Time (Wide):")
print(temp_data)

temp_long = temp_data.melt(id_vars='City', var_name='Time', value_name='Temperature')
print("\n   Same Data (Long):")
print(temp_long)

# =========================================================================
# SUMMARY
# =========================================================================

print("\n" + "="*70)
print("DAY 59 COMPLETE ✅")
print("="*70)

print("\n🎯 What You Learned:")
print("  1. ✅ Wide vs Long format concepts")
print("  2. ✅ melt() - Wide to Long conversion")
print("  3. ✅ pivot() - Long to Wide conversion")
print("  4. ✅ pivot_table() - With aggregation")
print("  5. ✅ Real-world use cases")

print("\n💡 Key Takeaways:")
print("  • Wide format = Easy to read (Excel-style)")
print("  • Long format = Easy to analyze (Database-style)")
print("  • melt() and pivot() are opposites")
print("  • pivot_table() adds aggregation power")

print("\n🎊 Welcome Back!")
print("   Day 59 done. 41 more to go!")
print("   Taking breaks is part of sustainable learning.")

print("\n🎯 Next: Day 60 - Merging & Joining Datasets")
print("="*70)