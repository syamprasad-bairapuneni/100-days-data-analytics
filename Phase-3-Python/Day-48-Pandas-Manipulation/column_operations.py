# Day 48 - Column Operations in Pandas
# Author: Syamprasad
# Date: February 18, 2026

import pandas as pd
import numpy as np

print("="*70)
print("COLUMN OPERATIONS IN PANDAS")
print("="*70)

# Create sample dataset
data = {
    'Employee': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Raj'],
    'Department': ['Sales', 'Marketing', 'Sales', 'IT', 'Marketing'],
    'Base_Salary': [45000, 55000, 48000, 65000, 52000],
    'Experience_Years': [3, 5, 2, 7, 4],
    'Performance_Score': [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\n" + "="*70)
print("PART 1: ADDING NEW COLUMNS")
print("="*70)

# Method 1: Direct assignment
df['Company'] = 'TechCorp India'
print("\nAdded constant column:")
print(df[['Employee', 'Company']])

# Method 2: Calculated column
df['Annual_Salary'] = df['Base_Salary'] * 12
print("\nCalculated Annual Salary:")
print(df[['Employee', 'Base_Salary', 'Annual_Salary']])

# Method 3: Based on multiple columns
df['Salary_Per_Year_Exp'] = df['Base_Salary'] / df['Experience_Years']
print("\nSalary per year of experience:")
print(df[['Employee', 'Base_Salary', 'Experience_Years', 'Salary_Per_Year_Exp']].round(2))

# Method 4: Using np.where (conditional column)
df['Performance_Grade'] = np.where(
    df['Performance_Score'] >= 90, 'A',
    np.where(df['Performance_Score'] >= 80, 'B', 'C')
)
print("\nPerformance Grade (based on score):")
print(df[['Employee', 'Performance_Score', 'Performance_Grade']])

# Method 5: Using assign (chain-friendly)
df = df.assign(
    Bonus=df['Base_Salary'] * 0.10,
    Total_Compensation=df['Base_Salary'] + df['Base_Salary'] * 0.10
)
print("\nBonus and Total Compensation:")
print(df[['Employee', 'Base_Salary', 'Bonus', 'Total_Compensation']])

print("\n" + "="*70)
print("PART 2: MODIFYING EXISTING COLUMNS")
print("="*70)

# Update specific values
print("Before update:")
print(df[['Employee', 'Department']])

# Change department for specific employee
df.loc[df['Employee'] == 'Raj', 'Department'] = 'Sales'
print("\nAfter updating Raj's department:")
print(df[['Employee', 'Department']])

# Apply increment to all salaries
df['Base_Salary'] = df['Base_Salary'] * 1.10  # 10% raise
print("\nAfter 10% salary raise:")
print(df[['Employee', 'Base_Salary']])

# Conditional update using loc
df.loc[df['Performance_Grade'] == 'A', 'Bonus'] = df['Base_Salary'] * 0.15
print("\nAfter updating bonus for Grade A performers:")
print(df[['Employee', 'Performance_Grade', 'Bonus']])

print("\n" + "="*70)
print("PART 3: DELETING COLUMNS & ROWS")
print("="*70)

df_copy = df.copy()

# Drop single column
df_copy = df_copy.drop('Company', axis=1)
print("After dropping 'Company' column:")
print(df_copy.columns.tolist())

# Drop multiple columns
df_copy = df_copy.drop(['Salary_Per_Year_Exp', 'Annual_Salary'], axis=1)
print("\nAfter dropping multiple columns:")
print(df_copy.columns.tolist())

# Drop row by index
df_copy = df_copy.drop(index=0)  # Drop first row
print("\nAfter dropping row 0:")
print(df_copy)

# Drop rows based on condition
df_copy = df_copy[df_copy['Performance_Score'] >= 80]
print("\nAfter dropping low performers:")
print(df_copy)

print("\n" + "="*70)
print("PART 4: COLUMN RENAMING")
print("="*70)

df_rename = df.copy()

# Rename specific columns
df_rename = df_rename.rename(columns={
    'Employee': 'Employee_Name',
    'Base_Salary': 'Monthly_Salary',
    'Performance_Score': 'Score'
})
print("After renaming columns:")
print(df_rename.columns.tolist())

# Make all column names lowercase
df_rename.columns = df_rename.columns.str.lower()
print("\nAll lowercase:")
print(df_rename.columns.tolist())

# Replace spaces with underscores
df_rename.columns = df_rename.columns.str.replace(' ', '_')
print("\nSpaces replaced with underscores:")
print(df_rename.columns.tolist())

print("\n" + "="*70)
print("COLUMN OPERATIONS COMPLETE ✅")
print("="*70)