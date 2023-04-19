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

df = pd.read_csv(r'C:\Users\M\Downloads\Projected_Population_2010-2040_-_Summary.csv')
df.info()
sns.color_palette("tab10")
fig, ax = plt.subplots(figsize=(8,6))

sns.barplot(data=df, x="Borough", y="% of Total Borough Population - 2010",hue='Age Group', errorbar="sd", palette="Set1",)

plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, x="Borough", y="% of Total Borough Population - 2020",hue='Age Group', errorbar="sd", palette="Set1",)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, x="Borough", y="% of Total Borough Population - 2030",hue='Age Group', errorbar="sd", palette="Set1",)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(data=df, x="Borough", y="% of Total Borough Population - 2040",hue='Age Group', errorbar="sd", palette="Set1",)

plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))

sns.kdeplot(data=df, 
            x='2020',
            hue='Borough',
            palette="Set1", 
            ax=ax)

plt.tight_layout()




fig, ax = plt.subplots(figsize=(8, 6))
df = df.reset_index(drop=True)


sns.barplot(data=df,
            x='Borough',  
            y='Change in Number - 2010-2040 ', 
            palette="Set1", 
            ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(data=df,
            x='Borough',  
            y='Change in Number - 2010-2020', 
            palette="Set1", 
            ax=ax)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(data=df,
            x='Borough',  
            y='Change in Number - 2020-2030 ', 
            palette="Set1", 
           ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(data=df,
            x='Borough',  
            y='Change in Number - 2030-2040 ', 
            palette="Set1", 
            ax=ax)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(data=df,
            x='Borough',  
            y='Change in Percent - 2010-2040', 
            palette="Set1", 
            ax=ax)

fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(data=df,
            x='Borough',  
            y='Change in Percent - 2010-2020', 
            palette="Set1", 
            ax=ax)

fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(data=df,
            x='Borough',  
            y='Change in Percent - 2020-2030', 
            palette="Set1", 
            ax=ax)

fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(data=df,
            x='Borough',  
            y='Change in Percent - 2030-2040', 
            palette="Set1", 
            ax=ax)
plt.show()


sns.barplot(data=df, x="Borough", y="Change in Percent - 2010-2040",hue="Age Group", errorbar="sd", palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="Change in Percent - 2010-2020",hue="Age Group", errorbar="sd", palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="Change in Percent - 2020-2030",hue="Age Group", errorbar="sd", palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="Change in Percent - 2030-2040",hue="Age Group", errorbar="sd",palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="2010",hue="Age Group", errorbar="sd", palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="2020",hue="Age Group", errorbar="sd",palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="2030",hue="Age Group", errorbar="sd",palette="Set1",)
plt.show()
sns.barplot(data=df, x="Borough", y="2040",hue="Age Group",estimator=median,palette="Set1",)
plt.show()



sns.barplot(data=df, x="Borough", y="Change in Number - 2010-2040 ",hue="Age Group", errorbar="sd", errcolor="black",palette="Set1")
plt.show()
sns.barplot(data=df, x="Borough", y="Change in Number - 2010-2020",hue="Age Group", errorbar="sd", errcolor="black",palette="Set1")
plt.show()

sns.barplot(data=df, x="Borough", y="Change in Number - 2020-2030 ",hue="Age Group", errorbar="sd", errcolor="black",palette="Set1")
plt.show()
sns.barplot(data=df, x="Borough", y="Change in Number - 2030-2040 ",hue="Age Group", errorbar="sd", errcolor="black",palette="Set1")
plt.show()









