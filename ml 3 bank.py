
# 1. Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.neural_network import MLPClassifier

# 2. Load Dataset
df = pd.read_csv("Churn_Modelling.csv")

print("Dataset:")
print(df.head())
print("\nDataset Shape:", df.shape)

# 3. Pre-process Dataset
df = df.dropna(subset=["Exited"])

# Remove unnecessary columns
X = df.drop(
    ["Exited", "RowNumber", "CustomerId", "Surname"],
    axis=1,
    errors="ignore"
)
y = df["Exited"].astype(int)

# Identify numerical and categorical columns
numeric_cols = X.select_dtypes(include=np.number).columns
categorical_cols = X.select_dtypes(exclude=np.number).columns

# Encode categorical data and scale numerical data
preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]), numeric_cols),

    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical_cols)
])

# 4. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Build Neural Network Classifier
model = Pipeline([
    ("preprocessing", preprocessor),
    ("neural_network", MLPClassifier(
        hidden_layer_sizes=(16, 8),
        activation="relu",
        solver="adam",
        max_iter=300,
        random_state=42,
        early_stopping=True
    ))
])

# 6. Train Model
model.fit(X_train, y_train)

# 7. Predict Customer Churn
y_pred = model.predict(X_test)

# 8. Evaluate Model
print("\n--- Neural Network Results ---")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred,
    target_names=["Not Churn", "Churn"],
    zero_division=0
))

# 9. Predict One Customer
sample = X_test.iloc[[0]]
prediction = model.predict(sample)[0]

print("\n--- Customer Churn Prediction ---")
if prediction == 1:
    print("Customer will leave the bank (Churn).")
else:
    print("Customer will stay with the bank (Not Churn).")
