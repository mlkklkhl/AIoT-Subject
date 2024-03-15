import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("human detection-missing values.csv", encoding="utf8")

# 2. Check the datatype for each column
print(df.dtypes)

# 3. Data Summary
print(df.describe().to_string())
print(df.describe(include='object').to_string())

# pairplot with hue Label
figure = sns.pairplot(df, hue='Label')
figure.fig.subplots_adjust(top=0.9)
figure.fig.suptitle('Raw Data Distribution')
plt.show()

# 4. Finding the missing values

# # 4.1 Check for missing data in any of the variables.
print(df.info())

# # 4.2 Finding the missing values in each column
print(df.isnull().sum(), '\n')

# # # Eliminating missing values
# # Removing the data with missing values
datadrop = df.dropna()
print(datadrop.describe().to_string(), '\n')
print(datadrop.describe(include='object').to_string(), '\n')

# pairplot with hue Label
figure = sns.pairplot(datadrop, hue='Label')
figure.fig.subplots_adjust(top=0.9)
figure.fig.suptitle('Datadrop Distribution')
plt.show()

# # Replacing the missing values with Mean/Median/Mode
# for numerical data (mean/median)
Light_mean = df.Light.mean()
df.Light.fillna(Light_mean, inplace=True)

Mic_mean = df.Mic.mean()
df.Mic.fillna(Mic_mean, inplace=True)

PIR_mean = df.PIR.mean()
df.PIR.fillna(PIR_mean, inplace=True)

# for categorical data (mode)
# Label_mode = df['Label'].mode()[0]
# df['Label'].fillna(Label_mode, inplace=True)

print(df.isnull().sum(), '\n')

# pairplot with hue Label
figure = sns.pairplot(df, hue='Label')
figure.fig.subplots_adjust(top=0.9)
figure.fig.suptitle('Replacing the missing values with Mean/Median/Mode Distribution')
plt.show()

