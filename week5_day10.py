# Import pandas
# Read the wine data into a DataFrame.
# Use the attributes and methods available on DataFrames to answer the following questions:
# How many rows and columns are in the DataFrame?
# What data type is in each column?
# Are all of the variables continuous, or are any categorical?
# How many non-null values are in each column?
# What are the min, mean, max, median for all numeric columns?

import numpy as np
import pandas as pd

df = pd.read_csv('winequality-red.csv',delimiter=';')
df.head()
df.count()

[[x,len(df[x].unique())] for x in df.columns]

# Check for any nulls
df.isnull().any()

#Way 1

[[x,len(df[x]),df[x].mean(),df[x].min(),df[x].max(),df[x].median()] for x in df.columns]

# min, max, median mean
w = pd.DataFrame([df.min()])
x = pd.DataFrame([df.mean()])
y = pd.DataFrame([df.median()])
z = pd.DataFrame([df.max()])
pd.concat([w,x,y,z],keys=['min','mean','median','max'])

#2 

df['chlorides'].head(10)
df['chlorides'][0:10]
df['chlorides'].loc[0:9]
df['chlorides'].iloc[0:10]

#From the back of the list
df['chlorides'].iloc[-10:]
df['chlorides'].iloc[df['chlorides'].count()-10:]

df[['chlorides', 'density']].iloc[264:283]

df[df['chlorides'] < .10]

df[df['chlorides'] > df['chlorides'].mean()]

df[(df['pH'] > 3.0) & (df['pH'] < 3.5)]

df[(df['pH'] > 3.0) & (df['pH'] < 3.5) & (df['residual sugar'] < 2.0)]

#3

df.groupby('quality')['chlorides'].mean()

df[(df['pH'] > 3.0) & (df['pH'] < 4.0)].groupby('pH')['alcohol'].mean()

# For observations with an alcohol value between 9.25 and 9.5, find the highest amount of residual sugar.
df[(df['alcohol'] > 9.25) & (df['alcohol'] < 9.5)].max()

# Create a new column, called total_acidity, that is the sum of fixed acidity and volatile acidity.
df['total_acidity'] = df['volatile acidity'] + df['fixed acidity']


# Find the average total_acidity for each of the quality values.
df.groupby('quality')['total_acidity'].mean()

#Find the top 5 density values.
df.sort_values(by='density')[-5:]

# Find the 10 lowest sulphates values.
df.sort_values(by='sulphates')[:5]

#4

# Plot the average amount of chlorides for each quality value (1 from Part 3).
import seaborn as sns
import matplotlib.pyplot as plt

#%matplotlib inline   only used for jupyter notebook

df.groupby('quality')['chlorides'].mean().plot()
df[(df['pH'] > 3.0) & (df['pH'] < 4.0)].groupby('pH')['alcohol'].mean().plot()
df[(df['alcohol'] > 9.25) & (df['alcohol'] < 9.5)].max().plot()

# Plot the alcohol values against pH values. Does there appear to be any relationship between the two?
df[['alcohol','pH']].plot(kind='hist')

# Plot a histogram of the quality values. Are they evenly distributed within the data set?
df[['quality']].plot(kind='hist')

# Plot a boxplot to look at the distribution of citric acid.
df[['citric acid']].plot(kind='density')










