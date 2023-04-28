# importing libraries
import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter
import seaborn as sns
from scipy import stats
from numpy import median
sns.set(color_codes=True)
#Visualizing CSV Data
df = pd.read_csv(r'C:\Users\M\Downloads\NYC_Parks_Structures.csv')
sns.color_palette("tab10")
rows, columns = df.shape
print('rows: {:,},\ncolumns: {}'.format(rows, columns))
df['CNSTRCT_YR'] = df['CNSTRCT_YR'].replace({0:np.nan})
# printing the column names, non-null counts, and data types of our columns
df.info()
#Distribution Plots with Seaborn (Histograms)

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(df['CNSTRCT_YR'],
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(y=df['CNSTRCT_YR'], 
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(df['CNSTRCT_YR'],
             kde=True,
             ax=ax)
plt.show()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(data=df, 
             x='CNSTRCT_YR',
             hue='borough',
             ax=ax)
plt.show()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(data=df, 
             x='CNSTRCT_YR',
             hue='borough',
             multiple="stack",
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(data=df, 
             x='CNSTRCT_YR',
             hue='borough',
             element="step",
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(data=df, 
             x='CNSTRCT_YR',
             fill=False,
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(df['CNSTRCT_YR'],
             cumulative=True,
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(data=df,
             x='CNSTRCT_YR',
             hue='borough',
             cumulative=True,
             element="step",
             fill=False,
             ax=ax)
plt.tight_layout()

#Kernel Density Estimation Plots

fig, ax = plt.subplots(figsize=(8,6))
sns.kdeplot(df['CNSTRCT_YR'],
            ax=ax)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
sns.kdeplot(data=df, 
            x='CNSTRCT_YR',
            hue='borough', 
            ax=ax)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
sns.kdeplot(data=df, 
            x='CNSTRCT_YR',
            hue='borough', 
            multiple='stack', 
            ax=ax)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
sns.kdeplot(data=df, 
            x='CNSTRCT_YR',
            hue='borough', 
            multiple='fill', 
            ax=ax)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
sns.kdeplot(data=df, 
            x='CNSTRCT_YR',
            hue='borough', 
            cumulative=True, 
            common_norm=False, 
            common_grid=True, 
            ax=ax)
plt.tight_layout()

#Empirical Cummulative Distribution Functions
fig, ax = plt.subplots(figsize=(8,6))
sns.ecdfplot(data=df, 
             y="CNSTRCT_YR", 
             ax=ax)
plt.tight_layout()
#Distribuiton Plots on a faced grid

sns.displot(data=df, 
            x="CNSTRCT_YR", 
            bins=25,
            hue="borough", 
            kind="hist",
            height=7,
            facet_kws={"legend_out": True})
plt.tight_layout()

sns.displot(data=df, 
            x="CNSTRCT_YR", 
            bins=25,
            hue="borough", 
            multiple="stack",
            height=7,
            facet_kws={"legend_out": True})
plt.tight_layout()

#line Plots
by_year = df.groupby('CNSTRCT_YR')[['DOITT_ID']].count()
by_year = by_year.rename(columns={'DOITT_ID': 'count'})
by_year = by_year.reset_index()
by_year['CNSTRCT_YR'] = by_year['CNSTRCT_YR'].astype(int)
fig, ax = plt.subplots(figsize=(8,6))

sns.lineplot(data=by_year, 
             x="CNSTRCT_YR", 
             y="count", 
             ax=ax)
plt.tight_layout()

by_year.head()
line_pivot = pd.pivot_table(df, 
                            values='DOITT_ID', 
                            index=['CNSTRCT_YR'], 
                            columns=['borough'], 
                            aggfunc='count')

fig, ax = plt.subplots(figsize=(8,6))
sns.lineplot(data=line_pivot, 
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.lineplot(data=line_pivot['MN'], 
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
manhattan_df = df.loc[df['borough'] == 'MN']
sns.lineplot(data=manhattan_df, 
             x="CNSTRCT_YR", 
             y="GROUNDELEV", 
             ax=ax)
plt.tight_layout()

#Scatter Plots
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x=df['GROUNDELEV'],
                y=df['HEIGHTROOF'], 
                ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x=df['GROUNDELEV'],
                y=df['HEIGHTROOF'], 
                data=df, 
                hue="borough", 
                ax=ax)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x=df['GROUNDELEV'],
                y=df['HEIGHTROOF'], 
                data=df, 
                hue="CNSTRCT_YR", 
                ax=ax)
plt.tight_layout()


plt.figure(figsize=(8,6))
sns.scatterplot(x=df['GROUNDELEV'],
                y=df['HEIGHTROOF'], 
                data=df, 
                size="CNSTRCT_YR", 
                sizes=(15, 300))
plt.tight_layout()


#Count Plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(x="borough", 
              data=df, 
              ax=ax)
plt.tight_layout()

#scatter plot swarm
sns.catplot(x='borough', 
            y='HEIGHTROOF', 
            data=df, 
            height=7)
plt.tight_layout()
#box Plot
fig, ax = plt.subplots(figsize=(8,6))
df['GROUNDELEV'].plot.box(ax=ax)
plt.tight_layout()



df_box = df[['borough', 'GROUNDELEV']]
fig, ax = plt.subplots(figsize=(8,6))
df_box.boxplot(by='borough', ax=ax)
plt.xlabel('borough')
plt.tight_layout()

#Area Plot
area = df[df['CNSTRCT_YR'].between(2000, 2020)]


area = pd.pivot_table(area, 
                       values='DOITT_ID', 
                       index=['CNSTRCT_YR'], 
                       columns=['borough'], 
                       aggfunc=pd.Series.nunique)

area = area.rename(columns={'DOITT_ID': 'count'})
area.index = area.index.astype('int64')

print(area.index.dtype)
area.head()
fig, ax = plt.subplots(figsize=(8,6))
area.plot.area(ax=ax, stacked=False)
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xticks(rotation=0)
plt.xlabel('Construction Year', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
area_cumsum = area.cumsum()
area_cumsum.head()

area_cumsum.plot.area(ax=ax, stacked=False)
# formatting Y axis with comma
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xticks(rotation=0)
plt.xlabel('Construction Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))

area_cumsum.plot.area(ax=ax)

# formatting Y axis with comma
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xticks(rotation=0)
plt.xlabel('Construction Year', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))

area_cumsum.plot.area(ax=ax, stacked=False)

# formatting Y axis with comma
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xticks(rotation=0)
plt.xlabel('Construction Year', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.tight_layout()
#Pie Plot


pie = df.groupby('borough')['DOITT_ID'].count()
pie.rename("count", inplace=True)
pie = pie.sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8,6), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.2f}%\n({:,})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(pie, 
                                  autopct=lambda pct: func(pct, pie),
                                  textprops=dict(color="w"))

ax.legend(wedges, 
          pie.index,
          title="Borough",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1)) 

plt.setp(autotexts, size=12, weight="bold")
plt.tight_layout()

#boxen plot
data = df
order = ["MN", "BX", "BK", "QN", "SI"]
sns.catplot(x="borough", 
            y="GROUNDELEV", 
            kind="boxen", 
            data=data, 
            order=order, 
            height=7)
plt.tight_layout()

data = df
sns.catplot(x="borough", 
            y="GROUNDELEV",  
            kind="violin", 
            split=True, 
            data=data, 
            height=7)
plt.tight_layout()



#part 2 area Plot
fig, ax = plt.subplots(figsize=(8,6))
area.plot(kind='bar', 
           ax=ax)

# formatting Y axis with comma
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xticks(rotation=30)
plt.xlabel('Construction Year', fontsize=12)
plt.ylabel('Number of Newly Constructed Parks', fontsize=12)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
area.plot.bar(stacked=True, 
               ax=ax)

# formatting Y axis with comma
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.xticks(rotation=45)
plt.xlabel('Construction Year', fontsize=12)
plt.ylabel('Number of Newly Constructed Parks', fontsize=12)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(8,6))
area.sort_index(ascending=False).plot.barh(stacked=True, 
                                            ax=ax)

# formatting Y axis with comma
ax.get_xaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xticks(rotation=0)
plt.xlabel('Number of Newly Constructed Parks', fontsize=12)
plt.ylabel('Construction Year', fontsize=12)
plt.tight_layout()


g = df.groupby('CNSTRCT_YR')['DOITT_ID'].count().reset_index()
g = g.rename(columns={'DOITT_ID': 'count'})
g.set_index('CNSTRCT_YR', drop=False, inplace=True)
g.index = g.index.astype('int64')

# transforming our 'Year' index to datetime
g.index = pd.to_datetime(g.index, format='%Y')
print(g.index.dtype)
g.head()

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(g['count'], 
        linewidth=3)

# formatting Y axis with comma
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.xlabel('Construction Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()