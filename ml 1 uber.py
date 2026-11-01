
# Uber Fare Prediction

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 2. Load Dataset
df = pd.read_csv("uber.csv")

# 3. Pre-process the Dataset
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce", utc=True
)
df.dropna(inplace=True)

df["hour"] = df["pickup_datetime"].dt.hour

df.drop(["key", "pickup_datetime"], axis=1, inplace=True, errors="ignore")

# 4. Identify Outliers using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

df = df[
    (df["fare_amount"] >= Q1 - 1.5 * IQR) &
    (df["fare_amount"] <= Q3 + 1.5 * IQR)
]

print("Dataset after preprocessing and outlier removal:")
print(df.head())


# 5. Check Correlation
print("\n--- Correlation Matrix ---")
print(df.corr(numeric_only=True))

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 6. Split Data
X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]

# Keep only numeric input columns
X = X.select_dtypes(include=["number"])

# Remove missing and infinite values
X = X.replace([float("inf"), float("-inf")], float("nan"))
data = pd.concat([X, y], axis=1).dropna()

X = data.drop("fare_amount", axis=1)
y = data["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# 7. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# 8. Random Forest Regression
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# 9. Evaluate and Compare Models
results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R2 Score": [
        r2_score(y_test, lr_pred),
        r2_score(y_test, rf_pred)
    ],
    "RMSE": [
        mean_squared_error(y_test, lr_pred) ** 0.5,
        mean_squared_error(y_test, rf_pred) ** 0.5
    ],
    "MAE": [
        mean_absolute_error(y_test, lr_pred),
        mean_absolute_error(y_test, rf_pred)
    ]
})

print("\n--- Model Comparison Results ---")
print(results.to_string(index=False))
