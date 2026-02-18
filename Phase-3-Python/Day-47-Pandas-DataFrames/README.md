# Day 47 - Pandas DataFrames Deep Dive

## 🎯 Objective
Master Pandas DataFrame operations for real-world data analytics - creating, selecting, filtering, sorting, and analyzing data.

## 📚 Topics Covered
- Creating DataFrames from multiple sources
- Column and row selection ([], loc, iloc)
- Boolean indexing and filtering
- String operations in selection
- Query method for SQL-like syntax
- Sorting by single and multiple columns
- Ranking data (overall and within groups)
- Finding top N and bottom N values
- Real sales analysis project

## 📁 Files
1. `creating_dataframes.py` - Multiple ways to create DataFrames
2. `selecting_data.py` - All selection methods (loc, iloc, boolean, query)
3. `sorting_ranking.py` - Sorting and ranking operations
4. `sales_analysis_project.py` - Complete analytics project
5. `sales_data.csv` - Sample dataset (generated)

## 🚀 How to Run
```bash
# Run in order:
python creating_dataframes.py   # Creates sales_data.csv
python selecting_data.py
python sorting_ranking.py
python sales_analysis_project.py
```

## 💡 Key Learnings

### DataFrame Creation
- **From dict**: Most common for small datasets
- **From CSV**: Real-world data loading
- **From NumPy**: Numerical computation results
- **With date ranges**: Time-series data

### Selection Methods
- **df['column']** → Series
- **df[['col1', 'col2']]** → DataFrame
- **df.loc[]** → Label-based selection
- **df.iloc[]** → Position-based selection
- **df.query()** → SQL-like syntax

### Boolean Indexing
- Single condition: `df[df['Revenue'] > 1000]`
- Multiple AND: `df[(cond1) & (cond2)]`
- Multiple OR: `df[(cond1) | (cond2)]`
- isin(): `df[df['Region'].isin(['North', 'South'])]`

### Sorting & Ranking
- Single column: `df.sort_values('Revenue')`
- Multiple columns: `df.sort_values(['Region', 'Revenue'])`
- Ranking: `df['Revenue'].rank()`
- Top N: `df.nlargest(10, 'Revenue')`

## 🎯 Real-World Applications

### Sales Analysis Project Covered
- Revenue distribution analysis
- Product performance metrics
- Regional market share
- Product-region combination insights
- Time-based trends (weekly, daily)
- Strategic recommendations

### Skills Demonstrated
- Data loading and preparation
- Multi-dimensional analysis (product × region × time)
- Identifying top/bottom performers
- Calculating market share
- Trend analysis
- Business insight generation

## 📊 Sample Insights Generated
- Top 10% transactions = X% of revenue
- Best product: Laptop (₹XX lakhs)
- Best region: North (XX% market share)
- Best week: Week X
- Strategic recommendations for growth

## 🎯 Next Steps
Tomorrow (Day 48): Data manipulation and transformation
- Adding/modifying columns
- Applying functions
- String operations
- Handling missing data
- Data type conversions

---
**Progress:** SQL ✅ | Power BI ✅ | Python ✅ | NumPy ✅ | Pandas Fundamentals ✅