import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("suv.csv")

X = df[["Age", "EstimatedSalary"]]
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

dt_entropy = DecisionTreeClassifier(criterion='entropy', random_state=20)
dt_entropy.fit(X_train, y_train)
y_pred_entropy = dt_entropy.predict(X_test)

print("Confusion Matrix (Entropy Criterion):\n", confusion_matrix(y_test, y_pred_entropy))
print("Classification Report (Entropy Criterion):\n", classification_report(y_test, y_pred_entropy))

dt_gini = DecisionTreeClassifier(criterion='gini', random_state=20)
dt_gini.fit(X_train, y_train)
y_pred_gini = dt_gini.predict(X_test)

print("Confusion Matrix (Gini Criterion):\n", confusion_matrix(y_test, y_pred_gini))
print("Classification Report (Gini Criterion):\n", classification_report(y_test, y_pred_gini))
print("Comparison of Decision Tree Models:")
print("- Both entropy and gini are effective splitting criteria.")
print("- Entropy tends to be slightly more computationally expensive.")
print("- If both show similar accuracy, gini might be preferable for efficiency.")
print("- Examining precision, recall, and f1-score provides insights into performance on imbalanced data.")
