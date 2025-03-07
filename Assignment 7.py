import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("data_banknote_authentication.csv")
X = df.drop(columns=["class"])
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

svc_linear = SVC(kernel='linear')
svc_linear.fit(X_train, y_train)

y_pred_linear = svc_linear.predict(X_test)
print("Confusion Matrix (Linear Kernel):\n", confusion_matrix(y_test, y_pred_linear))
print("Classification Report (Linear Kernel):\n", classification_report(y_test, y_pred_linear))

svc_rbf = SVC(kernel='rbf')
svc_rbf.fit(X_train, y_train)

y_pred_rbf = svc_rbf.predict(X_test)
print("Confusion Matrix (RBF Kernel):\n", confusion_matrix(y_test, y_pred_rbf))
print("Classification Report (RBF Kernel):\n", classification_report(y_test, y_pred_rbf))

print("Comparison of SVM Models:")
print("- The linear kernel works well when data is linearly separable.")
print("- The RBF kernel is more flexible and can capture complex relationships between features.")
print("- If the RBF kernel performs better in classification metrics, it indicates the data has non-linear patterns.")
