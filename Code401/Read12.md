# Pandas
[10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)

[Real Python Pandas Tutorial](https://realpython.com/learning-paths/pandas-data-science/)

[ Masterting Pandas](https://towardsdatascience.com/be-a-more-efficient-data-scientist-today-master-pandas-with-this-guide-ea362d27386)

### Panda

- based on numpy mathematics
- Used for tabular data analysis.
- series is a single vector
- datafame is comprised of multiple vectors


```python
import pandas as pd
s = pd.Series(list)


Panda Methods 
dates = pd.date_range('20180101', periods=6)

```

#### DataFrame Methods

```python
df.head()  # 5 top
df.tail()
df.index
df.columns

df.to_numpy()
df.describe()
df.info()
df.mean()
df.value_counts()

df.apply(function)   # applies to columns, axis=1 for rows
df.apply(lambda x: function to each row)
df.applymap() # all cells in DF

df.sort_index(axis=1, ascending=False)
df.sort_values(by='<col name>')


df['A']  # series
df[['A':'D']] # DF
```

#### DataFrame Slicing

```python
df[0:3]   # slice Rows

df.loc[:]
df.loc[:, 'A', 'B']  # all rows of col A + B

df.iloc[3]              # select by row index position
df.iloc[3:5, 0:2]       # row 3-5, columns 0-2  not inclusive 
df.iloc[[1,2,4], [0,2]] # rows 1,2,4 / col 0 and 1

df.iloc[1,1]            # single cell
df.iloc[:, 1:3]         # all rows, col 1 and 2


df = pd.read_csv('file.csv')

```

#### DataFrame Boolean Indexing

```python
df[df > 5]                    # all values greater than 5
df['E'] = value               # assign value to column E
df[df2['E'].isin(['x', 'y'])] # check for values where col E is in list. 

```


##### DF Null

```python
df.dropna(how='any')
df.fillna(value=100)

pd.isna(df1)

```

#### DF Merging

- pd.concat() adds to df
- pd.merge(left, right, on='col' how='inner')   SQL style

#### DF Grouping and Reshaping

- df.groupby('A').sum()
- df.stack()
- df.melt()
- df.reset_index()

- df.pivot_table(df, values='d', index=['A', 'B'], columns=['C'])

- Categorical allocation

#### Plotting

- matplotlib.pyplot as plt
- df.plot()
- df.plot.scatter(x='', y='', alpha='')
- df.plot.box()
- df.plot.area(figsize=(12,10), subplots=True)


[Python Programmer](https://www.youtube.com/watch?v=dcqPhpY7tWk&t=391s)