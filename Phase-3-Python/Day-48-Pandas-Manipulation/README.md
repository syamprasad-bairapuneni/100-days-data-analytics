\# Day 48 - Pandas Data Manipulation \& Transformation



\## 🎯 Objective

Master data manipulation techniques to transform raw, messy data into clean, analytics-ready datasets.



\## 📚 Topics Covered

\- Adding, modifying, and deleting columns

\- Applying functions (apply, map, applymap)

\- String operations (.str accessor)

\- Data type conversions

\- Datetime operations and feature extraction

\- Missing value detection and handling

\- End-to-end business transformation project



\## 📁 Files

1\. `column\_operations.py` - Add, modify, delete, rename columns

2\. `applying\_functions.py` - apply(), map(), string operations

3\. `data\_types\_datetime.py` - Type conversions and datetime features

4\. `missing\_data.py` - Detect, remove, fill missing values

5\. `business\_transformation\_project.py` - Full raw → clean pipeline

6\. `clean\_ecommerce\_data.csv` - Final cleaned dataset



\## 🚀 How to Run

```bash

python column\_operations.py

python applying\_functions.py

python data\_types\_datetime.py

python missing\_data.py

python business\_transformation\_project.py

```



\## 💡 Key Learnings



\### Column Operations

\- Direct assignment for simple columns

\- np.where() for conditional columns

\- assign() for chain operations

\- loc\[] for conditional updates



\### Function Application

\- apply() on Series: row-by-row transformation

\- apply(axis=1) on DataFrame: use multiple columns

\- map() for value replacement/mapping

\- Lambda functions for quick transformations



\### Missing Data Strategy

\- Mean fill → Normal distribution data

\- Median fill → Skewed data

\- Mode fill → Categorical data

\- Forward/Backward fill → Time series

\- Drop → When missing < 5%



\### Datetime Operations

\- Extract: year, month, day, day\_name, quarter

\- Arithmetic: days between dates

\- Rolling averages for trend analysis

\- Weekend vs weekday analysis



\## 🎯 Real Business Project

Complete ETL pipeline:

1\. Raw messy data (inconsistent case, wrong types, missing values)

2\. Data cleaning (standardize, convert, fill)

3\. Feature engineering (revenue, segments, datetime features)

4\. Data validation (business logic checks)

5\. Business insights generation



\## 📊 Skills Demonstrated

\- Data standardization (text case, types)

\- Business metric calculation (revenue, discount, segments)

\- Customer segmentation

\- Time-based feature engineering

\- End-to-end data pipeline



---

\*\*Progress:\*\* SQL ✅ | Power BI ✅ | Python ✅ | NumPy ✅ | Pandas ✅

