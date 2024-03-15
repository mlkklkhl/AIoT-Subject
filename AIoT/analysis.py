import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("human detection.csv", encoding="utf8")

# 2. Handling Categorical Data
# 2.1 Label encoding
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df["Label"] = label_encoder.fit_transform(df["Label"])

# Mean
mean = df.mean()
# Median
median = df.median()

print(mean, '\n')
print(median)

# Plot data distribution
df["Light"].plot(kind="density", figsize=(6, 6))

plt.vlines(df["Light"].mean(), ymin=0, ymax=0.001, linewidth=3.0, color="green", linestyles='dashed', label='Mean')
plt.vlines(df["Light"].median(), ymin=0, ymax=0.001, linewidth=2.0, color="red", linestyles='dotted', label='Median')

plt.title("Light Distribution")
plt.legend()
plt.show()

#  # Measures of Variability
# Range is the distance between the maximum and minimum observations
range = max(df["Mic"]) - min(df["Mic"])
# Interquartile range (IQR) are used to describe data,
# they are known as the "five number summary".
# They are the same percentile values returned by df.describe():
description = df["Light"].describe()

# Interquartile (IQR) range is another common measure of spread.
# IQR is the distance between the 3rd quartile and the 1st quartile:
IQR = df["Light"].quantile(0.75) - df["Light"].quantile(0.25)
# Variance and standard deviation are two other common measures of spread.
SD = df["Light"].std()
variance = df["Light"].var()

print("Range of Light: ", range, '\n')
print("Description of Light: ", description, '\n')
print("IQR of Light: ", IQR, '\n')
print("SD of Light: ", SD, '\n')
print("Variance of Light: ", variance, '\n')

# Correlation
cor = df.corr()
# we could use a heatmap; a data visualization technique where each
# value is represented by a color, according to its intensity in each scale.
sns.heatmap(cor, vmin=-1, vmax=1, annot=True)
plt.show()
