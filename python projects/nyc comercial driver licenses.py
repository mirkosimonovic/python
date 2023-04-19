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

df = pd.read_csv(r'C:\Users\M\Downloads\TLC_New_Driver_Application_Status.csv')
df.info()
fig, ax = plt.subplots(figsize=(8,6))

sns.histplot(df['Status'],
             
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))

sns.histplot(y=df['Status'], 
             
             bins=25,
             
             ax=ax)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(y=df['Medical Clearance Form'], 
           
             bins=25,
             ax=ax)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))

sns.histplot(data=df, 
             x="App Date", 
            
             ax=ax)

plt.tight_layout()



fig, ax = plt.subplots(figsize=(8,6))

sns.histplot(df['Drug Test'],
             bins=25,
             
             ax=ax)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(df['Driver Exam'],
             bins=25,
             
             ax=ax)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(8,6))
sns.histplot(df['Defensive Driving'],
             bins=25,
             
             ax=ax)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(8,6))
sns.lineplot(df['FRU Interview Scheduled'],

             
             ax=ax)
plt.tight_layout()


