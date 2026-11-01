
# Email Spam Detection using KNN and SVM

# 1. Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# 2. Load Dataset
df = pd.read_csv("emails.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# 3. Pre-process Dataset
df.dropna(inplace=True)

# First column is email name, last column is spam label
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

print("\nClass Distribution:")
print(y.value_counts())

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

print("\n--- KNN Results ---")
print("Accuracy:", accuracy_score(y_test, knn_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, knn_pred))
print("Classification Report:\n",
      classification_report(y_test, knn_pred, zero_division=0))

# 5. Support Vector Machine (SVM)
svm = SVC(kernel="linear")
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

print("\n--- SVM Results ---")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, svm_pred))
print("Classification Report:\n",
      classification_report(y_test, svm_pred, zero_division=0))

# 6. Compare Model Performance
results = pd.DataFrame({
    "Model": ["KNN", "SVM"],
    "Accuracy": [
        accuracy_score(y_test, knn_pred),
        accuracy_score(y_test, svm_pred)
    ]
})

print("\n--- Model Comparison ---")
print(results.to_string(index=False))
