import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('bank.csv', delimiter=';')

df2 = df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]

df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'])

df3['y'] = df3['y'].apply(lambda x: 1 if x == 'yes' else 0)

correlation_matrix = df3.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of df3')
plt.show()


y = df3['y']
X = df3.drop(columns=['y'])

print(y.head())
print(X.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

logreg = LogisticRegression(max_iter=1000)

logreg.fit(X_train, y_train)

y_pred_logreg = logreg.predict(X_test)

cm_logreg = confusion_matrix(y_test, y_pred_logreg)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)

print('Confusion Matrix for Logistic Regression:\n', cm_logreg)
print('Accuracy Score for Logistic Regression:', accuracy_logreg)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)

cm_knn = confusion_matrix(y_test, y_pred_knn)
accuracy_knn = accuracy_score(y_test, y_pred_knn)

print('Confusion Matrix for K-Nearest Neighbors (k=3):\n', cm_knn)
print('Accuracy Score for K-Nearest Neighbors (k=3):', accuracy_knn)

print(f"Logistic Regression Accuracy: {accuracy_logreg}")
print(f"K-Nearest Neighbors (k=3) Accuracy: {accuracy_knn}")


"""
The logistic regression model achieved an accuracy of X%, while the KNN model achieved an accuracy of Y%. 
Both models are valuable, but depending on the data distribution and the problem at hand, one may outperform the other.
Logistic regression often works well for binary classification problems with a linear decision boundary, while KNN can perform better in cases with more complex decision boundaries.
"""