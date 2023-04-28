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

df = pd.read_csv(r'C:\Users\M\Desktop\Buildings.csv')
df.info()
sns.color_palette("tab10")
df.info()
df.head()
df.tail()
df.sort_values('Height (meters)')
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, y="Building", x="Height (meters)", palette="Set1",order=df.sort_values('Height (meters)',ascending = False).Building)
df.sort_values('Floors')
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, y="Building", x="Floors", palette="Set1",order=df.sort_values('Floors',ascending=False).Building)

fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, y="Building", x='Height (meters)', palette="Set1",)



df['Costruction Costs adjusted for inflation (2012) (billion )'] = (df['Costruction Costs adjusted for inflation (2012) (billion )']).replace(',','', regex=True).astype(np.int64)
df['Construction Costs (/sqm)']= df['Construction Costs (/sqm)'].replace(',','', regex=True).astype(np.int64)
df.sort_values('Costruction Costs adjusted for inflation (2012) (billion )')
df.sort_values("Construction Costs (/sqm)")
df.sort_values("Total Construction Costs (billion ).text")
sns.barplot(data=df, y="Building", x="Construction Costs (/sqm)",order=df.sort_values('Construction Costs (/sqm)',ascending = False).Building, palette="Set1",)
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, y="Building", x='Costruction Costs adjusted for inflation (2012) (billion )', palette="Set1",order=df.sort_values('Costruction Costs adjusted for inflation (2012) (billion )',ascending = False).Building)
df["Total Construction Costs (billion ).text"] = (df["Total Construction Costs (billion ).text"]).replace(',','', regex=True).astype(np.int64)
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, y="Building", x="Total Construction Costs (billion ).text", palette="Set1",order=df.sort_values('Total Construction Costs (billion ).text',ascending = False).Building)

fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(data=df,  y="Building",x='Year Built', palette="Set1",)
