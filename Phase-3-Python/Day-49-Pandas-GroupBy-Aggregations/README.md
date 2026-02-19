\# Day 49 - Pandas GroupBy \& Aggregations



\## 🎯 What I Built

Complete business analytics pipeline using GroupBy - the most powerful Pandas operation.



\## 🔥 Core Skills Mastered

\- \*\*Split-Apply-Combine:\*\* Group → Aggregate → Analyze

\- \*\*Multiple Aggregations:\*\* Sum, mean, count, custom functions in one line

\- \*\*Pivot Tables:\*\* 2D views (Region × Product revenue matrix)

\- \*\*Transform \& Filter:\*\* Add group stats, filter groups by conditions

\- \*\*Time-Series Grouping:\*\* Monthly/weekly trends with growth rates



\## 📁 What's Inside

```bash

groupby\_basics.py              # Fundamentals

advanced\_aggregations.py       # Transform, filter, apply

pivot\_crosstab.py              # Pivot tables \& crosstabs

business\_reporting\_project.py  # Full executive report (500 transactions)

```



\## 💼 Real Project Delivered

\*\*Executive Sales Report (500 transactions analyzed)\*\*



Generated insights:

\- Regional performance + market share

\- Product rankings (80/20 analysis)

\- Customer segmentation (VIP vs Returning vs New)

\- Salesperson rankings

\- Monthly trends with growth rates

\- Strategic recommendations



\*\*Output:\*\* 3 CSV reports ready for executives



\## 🔑 Key Patterns

```python

\# Basic grouping

df.groupby('Region')\['Revenue'].sum()



\# Multiple aggregations

df.groupby('Product').agg(\['sum', 'mean', 'count'])



\# Multi-level grouping

df.groupby(\['Region', 'Product'])\['Revenue'].sum()



\# Pivot table

pd.pivot\_table(df, values='Revenue', index='Region', columns='Product')



\# Transform (add to original)

df\['Region\_Total'] = df.groupby('Region')\['Revenue'].transform('sum')

```



\## 💡 When to Use What

| Operation | Use Case |

|-----------|----------|

| `groupby()` | Flexible aggregations, further processing |

| `pivot\_table()` | 2D views, human-readable reports |

| `transform()` | Add group stats to original rows |

| `filter()` | Keep only certain groups |



\## 📊 Business Impact

One line answers business questions that took hours in Excel:

\- "Revenue by region?" → `groupby('Region')\['Revenue'].sum()`

\- "Top product per region?" → `groupby(\['Region','Product']).sum().nlargest()`

\- "Monthly growth?" → `groupby('Month').sum().pct\_change()`



\*\*This is 80% of what Data Analysts do daily.\*\*



---



\*\*Run:\*\* `python business\_reporting\_project.py` for complete analysis



\*\*Next:\*\* Day 50 - Week recap + Mini project combining all Python skills

