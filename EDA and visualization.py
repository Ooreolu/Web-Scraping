import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data from the CSV file into a DataFrame
df = pd.read_csv('British_Airways.csv')
# Replace infinity values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df2 = df
# Basic data analysis
# Summary statistics
summary = df.describe()
print(summary)

# Distribution of sentiment scores
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Sentiment', bins=30, kde=True)
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Recommended vs. Not Recommended
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Recommended', palette='Set2')
plt.title('Recommended vs. Not Recommended')
plt.xlabel('Recommended')
plt.ylabel('Count')
plt.show()

# Country-wise analysis
plt.figure(figsize=(12, 8))
sns.countplot(data=df, y='Country', order=df['Country'].value_counts().index, palette='viridis')
plt.title('Number of Reviews by Country')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()

# Sentiment vs. Recommended
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Recommended', y='Sentiment', palette='pastel')
plt.title('Sentiment vs. Recommended')
plt.xlabel('Recommended')
plt.ylabel('Sentiment Score')
plt.show()