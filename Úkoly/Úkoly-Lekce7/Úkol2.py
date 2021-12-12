import pandas
import requests
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)
data = pandas.read_csv("kosatce.csv")
X = data.drop(columns=["target"])
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
f1_scores = []
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)  # model, classifier, klasifikátor
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(k, f1_score(y_test, y_pred))