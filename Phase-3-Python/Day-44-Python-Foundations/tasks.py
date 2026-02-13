# Day 44 - Python Foundations Revival
# Author: Syamprasad
# Date: February 13, 2026

# PART 1: Lists & List Comprehensions
print("="*50)
print("TASK 1: Lists & List Comprehensions")
print("="*50)

sales = [1200, 1500, 980, 2100, 1750, 1300]

# Task 1: Filter sales > 1000
high_sales = [s for s in sales if s > 1000]
print(f"Sales > 1000: {high_sales}")

# Task 2: Total and average
total_sales = sum(sales)
avg_sales = total_sales / len(sales)
print(f"Total Sales: Rs.{total_sales}")
print(f"Average Sales: Rs.{avg_sales:.2f}")

# Task 3: Max and Min
print(f"Max Sale: Rs.{max(sales)}")
print(f"Min Sale: Rs.{min(sales)}")

# Task 4: Categorize
categories = ["High" if s > 1500 else "Normal" for s in sales]
print(f"Categories: {categories}")

# PART 2: Dictionaries
print("\n" + "="*50)
print("TASK 2: Dictionaries & Real Data")
print("="*50)

employees = [
    {"name": "Rahul", "dept": "Sales", "sales": 45000},
    {"name": "Priya", "dept": "Marketing", "sales": 32000},
    {"name": "Amit", "dept": "Sales", "sales": 51000},
    {"name": "Sneha", "dept": "Marketing", "sales": 28000}
]

# Task 1: Total sales by department
dept_sales = {}
for emp in employees:
    dept = emp["dept"]
    if dept in dept_sales:
        dept_sales[dept] += emp["sales"]
    else:
        dept_sales[dept] = emp["sales"]

print(f"Sales by Department: {dept_sales}")

# Task 2: Top performer
top_performer = max(employees, key=lambda x: x["sales"])
print(f"Top Performer: {top_performer['name']} - Rs.{top_performer['sales']}")

# Task 3: Filter > 30000
high_performers = [emp for emp in employees if emp["sales"] > 30000]
print(f"High Performers (>30k): {[e['name'] for e in high_performers]}")

# PART 3: Functions
print("\n" + "="*50)
print("TASK 3: Functions for Analytics")
print("="*50)

def calculate_growth_rate(old_value, new_value):
    """Calculate percentage growth rate"""
    return ((new_value - old_value) / old_value) * 100

def categorize_performance(value, thresholds):
    """Categorize performance based on thresholds"""
    if value < thresholds[0]:
        return "Low"
    elif value < thresholds[1]:
        return "Medium"
    else:
        return "High"

def clean_data(data_list):
    """Remove None, 0, and negative values"""
    return [x for x in data_list if x and x > 0]

def summary_stats(numbers):
    """Return summary statistics"""
    clean_nums = clean_data(numbers)
    return {
        "mean": sum(clean_nums) / len(clean_nums),
        "median": sorted(clean_nums)[len(clean_nums)//2],
        "max": max(clean_nums),
        "min": min(clean_nums),
        "count": len(clean_nums)
    }

# Test functions
print(f"Growth Rate (1000 to 1500): {calculate_growth_rate(1000, 1500):.2f}%")
print(f"Performance (35000): {categorize_performance(35000, [20000, 50000])}")

test_data = [100, 200, None, 0, -50, 300, 150]
print(f"Cleaned Data: {clean_data(test_data)}")
print(f"Summary Stats: {summary_stats(test_data)}")

# PART 4: Sales Incentive Calculator
print("\n" + "="*50)
print("TASK 4: Sales Incentive Calculator")
print("="*50)

def calculate_bonus(sales):
    """Calculate bonus based on sales performance"""
    if sales < 20000:
        return 0
    elif sales < 40000:
        return sales * 0.05
    elif sales < 60000:
        return sales * 0.08
    else:
        return sales * 0.12

test_sales = [15000, 25000, 45000, 75000]
for sale in test_sales:
    bonus = calculate_bonus(sale)
    print(f"Sales: Rs.{sale} -> Bonus: Rs.{bonus:.2f} ({(bonus/sale*100) if bonus else 0:.1f}%)")