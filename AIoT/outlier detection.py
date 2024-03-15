import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("human detection.csv", encoding="utf8")

# 2. Show outlier using boxplow
sns.boxplot(data=df)
plt.title("Data before outlier elimination")
plt.show()

# # 3.1 Calculating the 1st Quartile and the 3rd Quartile of the ‘Light' column
Q1 = df['Light'].quantile(0.25)
Q3 = df['Light'].quantile(0.75)
print("The 1st and 2nd quartile value is {0:1f} and {1:1f} respectively".format(Q1,Q3))

# # 3.2 Calculating the Inter-quartile range
IQR = Q3 - Q1
print("The value of Inter Quartile Range is: ", IQR)

# # 3.3 Finding the Lower Fence and the Upper Fence
Lower_fence = Q1 - (1.5 * IQR)
Upper_fence = Q3 + (1.5 * IQR)
print("Lower Fence value: ", Lower_fence)
print("The upper Fence value: ", Upper_fence)

# # 3.4 Checking the data which have the ‘Light' less than the Lower Fence
# # or greater than the Upper Fence. Basically we are retrieving the outliers here
Clean = df[~(((df['Light'] < Lower_fence) | (df['Light'] > Upper_fence)))]
print(Clean.describe())

sns.boxplot(data=Clean)
plt.title("Light data after outlier elimination")
plt.show()