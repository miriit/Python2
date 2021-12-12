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

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

# 2. Data
data = pandas.read_csv("water-potability.csv")
data = data.dropna()

X = data.drop(columns=["Potability"])
y = data["Potability"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. + 4. Algoritmus + Trénování modelu
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

# 5. Vyhodnocení modelu
y_pred = clf.predict(X_test)
print(confusion_matrix(y_true=y_test, y_pred=y_pred))
print(precision_score(y_test, y_pred))
ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test,
                                      display_labels=clf.classes_,
                                      cmap=plt.cm.Blues)
plt.show()

# 6. Upravení parametrů modelu
ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
f1_scores = []
for k in ks:
      clf = KNeighborsClassifier(n_neighbors=k)
      clf.fit(X_train, y_train)
      y_pred = clf.predict(X_test)

      print(k, precision_score(y_test, y_pred))

#print(confusion_matrix(y_true=y_test, y_pred=y_pred))

# 7. Závěrečná predikce
clf = KNeighborsClassifier(n_neighbors=23)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(precision_score(y_test, y_pred))
print(confusion_matrix(y_true=y_test, y_pred=y_pred))
print((203 + 45) / len(y_test))
#Ne ??

ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test,
                                      display_labels=clf.classes_,
                                      cmap=plt.cm.Reds)
plt.show()
#Snad jsem to pochopila spravně :)