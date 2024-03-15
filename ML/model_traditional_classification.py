import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import r2_score, accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split, KFold
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("BS/upsampled-pm-final-all-linear.csv", encoding="utf8").dropna()
# df = df[(df['Year'] == 2022) | (df['Year'] == 2023)]
# df = df[(df['Year'] == 2016) | (df['Year'] == 2019) | (df['Year'] == 2020) | (df['Year'] == 2021) | (df['Year'] == 2022) ]

print(df.describe().to_string())
print()

X = df[['Wind_s', 'SD_Wind_s', 'Max_Wind_s', 'Min_Wind_s', 'PM0.1G', 'PM1G', 'PM2.5G', 'PM2.5A', 'PM10A']]
y = df[['Month']]

#create a new KNN model
lr = LogisticRegression()
dt = DecisionTreeClassifier()
knn = KNeighborsClassifier(n_neighbors=3)
svr = SVC(kernel='rbf')
rf = RandomForestClassifier()

models = [{"model": lr, "name": "Linear Regression"}, {"model": dt, "name": "Decision Tree Regression"},
          {"model": knn, "name": "KNN Regression"}, {"model": svr, "name": "Support Vector Regression"},
          {"model": rf, "name": "Random Forest Regression"}]

########### Train-Test Start ############
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

for m in models:
    print("Model:", m["name"])
    model = m["model"].fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_pred = m["model"].predict(X_test)
    test_score = accuracy_score(y_test, y_pred)

    print('Accuracy:', round(test_score, 6))

    confusion_matrix = metrics.confusion_matrix(y_test, y_pred, labels=model.classes_)
    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=model.classes_)
    cm_display.plot(xticks_rotation='vertical')

    plt.title("Model:" + m["name"] + " = " + str(round(test_score, 6)))
    plt.show()
    print()
########### Train-Test End ############

# ########## Cross Validation Start ############
# k_folds = 5
# kf = KFold(n_splits=k_folds, random_state=1, shuffle=True)
#
# for m in models:
#     scores = []
#     print("Model:", m["name"])
#     for i, (train_index, test_index) in enumerate(kf.split(X)):
#         X_train = X.iloc[train_index, :]
#         y_train = y.iloc[train_index]
#         X_test = X.iloc[test_index, :]
#         y_test = y.iloc[test_index]
#         m["model"].fit(X_train, y_train)
#         y_pred = m["model"].predict(X_test)
#         test_score = accuracy_score(y_test, y_pred)
#         scores.append(round(test_score, 6))
#
#     print('cv_scores (Accuracy):', scores)
#
#     print()
# ########## Cross Validation End ############
