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

df = pd.read_csv(r'C:\Users\M\Downloads\Water_Consumption_in_the_City_of_New_York (1).csv')
df.info()
df.head()




fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(df['Per Capita(Gallons per person per day)'],
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))

sns.lineplot(data=df, 
             x="Year", 
             y="Per Capita(Gallons per person per day)",
             ax=ax)

fig, ax = plt.subplots(figsize=(8,6))
sns.lineplot(data=df, 
             x="Year", 
             y="NYC Consumption(Million gallons per day)", 
             ax=ax)

fig, ax = plt.subplots(figsize=(8,6))
sns.lineplot(data=df, 
             x="Year", 
             y="New York City Population", 
             ax=ax)

fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(data=df, 
             x="New York City Population", 
             y="NYC Consumption(Million gallons per day)",
            
            
            ax=ax)

fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x=df['Per Capita(Gallons per person per day)'],
                y=df['NYC Consumption(Million gallons per day)'],
                ax=ax)



