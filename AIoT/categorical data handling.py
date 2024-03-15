import pandas as pd

# 1. Load the dataset
df = pd.read_csv("human detection.csv", encoding="utf8")

# 2. Handling Categorical Data
# 2.1 Label encoding
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df["Label"] = label_encoder.fit_transform(df["Label"])

# Check label mapping (normally with alphabetical order)
mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
print(mapping)
print(df.head().to_string())