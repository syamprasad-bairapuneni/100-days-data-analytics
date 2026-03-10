\# Day 59 - Data Reshaping Basics



\## 🎯 What I Learned

Melt and pivot operations - converting between wide and long data formats.



\## 📚 Core Concepts



\*\*Wide Format:\*\*

\- Columns represent categories

\- Excel-style layout

\- Easy to read



\*\*Long Format:\*\*

\- Rows represent observations

\- Database-style layout

\- Easy to analyze



\## 🔑 Key Operations



\### Melt (Wide → Long)

```python

long = wide.melt(

&nbsp;   id\_vars='Employee',

&nbsp;   var\_name='Quarter',

&nbsp;   value\_name='Sales'

)

```



\### Pivot (Long → Wide)

```python

wide = long.pivot(

&nbsp;   index='Employee',

&nbsp;   columns='Quarter',

&nbsp;   values='Sales'

)

```



\### Pivot Table (With Aggregation)

```python

summary = pd.pivot\_table(

&nbsp;   data,

&nbsp;   values='Sales',

&nbsp;   index='Product',

&nbsp;   columns='Region',

&nbsp;   aggfunc='sum'

)

```



\## 💡 When to Use



\*\*Melt:\*\*

\- Excel data → Analysis format

\- Preparing for visualization

\- Groupby operations



\*\*Pivot:\*\*

\- Analysis → Report format

\- Creating summary tables

\- Excel-friendly output



\*\*Pivot Table:\*\*

\- Need aggregation (sum, mean)

\- Duplicate handling

\- Business reports



\## 📊 Examples Covered

\- Employee quarterly sales

\- Product monthly sales

\- Student grades

\- Temperature by time

\- Sales by product × region



\## 📁 Files

```

data\_reshaping\_basics.py    # 150+ lines

README.md                   # This file

```



\## 🎊 Status

\*\*Back after adaptation week!\*\*



Days completed: 59/100  

Days remaining: 41



\## 🎓 What's Next

\*\*Day 60:\*\* Merging and joining datasets



---



\*\*Time:\*\* 45 mins | \*\*Comeback:\*\* Strong ✅

