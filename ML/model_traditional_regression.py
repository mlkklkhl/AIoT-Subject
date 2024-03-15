import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score, train_test_split, KFold
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("BS/upsampled-pm-final-all-linear.csv", encoding="utf8").dropna()

# df = df[(df['Year'] == 2022) | (df['Year'] == 2023)]
# df = df[(df['Year'] == 2016) | (df['Year'] == 2019) | (df['Year'] == 2020) | (df['Year'] == 2021) | (df['Year'] == 2022) ]
print(df.describe().to_string())
print()

X = df[['Wind_s', 'SD_Wind_s', 'Max_Wind_s', 'Min_Wind_s', 'PM1G', 'PM2.5G', 'PM2.5A', 'PM10A']]
y = df[['PM0.1G']]

#create a new KNN model
lr = LinearRegression()
dt = DecisionTreeRegressor()
knn = KNeighborsRegressor(n_neighbors=3)
svr = SVR(kernel='rbf')
rf = RandomForestRegressor()

models = [{"model": lr, "name": "Linear Regression"}, {"model": dt, "name": "Decision Tree Regression"},
          {"model": knn, "name": "KNN Regression"}, {"model": svr, "name": "Support Vector Regression"},
          {"model": rf, "name": "Random Forest Regression"}]

############ Train-Test Start ############
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# for m in models:
#     print("Model:", m["name"])
#     model = m["model"].fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     r2 = r2_score(y_test, y_pred)
#     print('R2:', r2)
#     print()
############ Train-Test End ############

########## Cross Validation Start ############
k_folds = 5
kf = KFold(n_splits=k_folds, random_state=1, shuffle=True)

for m in models:
    scores = []
    print("Model:", m["name"])
    for i, (train_index, test_index) in enumerate(kf.split(X)):
        X_train = X.iloc[train_index, :]
        y_train = y.iloc[train_index]
        X_test = X.iloc[test_index, :]
        y_test = y.iloc[test_index]
        m["model"].fit(X_train, y_train)
        test_score = m["model"].score(X_test, y_test)
        scores.append(round(test_score, 6))
    print('cv_scores (R2):', scores)
    print()
########## Cross Validation End ############
