
# Sales Data Clustering using K-Means and Hierarchical Clustering

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# 2. Load Dataset
df = pd.read_csv("sales_data_sample.csv", encoding="unicode_escape")

print("Dataset:")
print(df.head())

# 3. Select Numerical Features
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]]

# Handle missing values
X = X.dropna()

# 4. Scale Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Elbow Method to Find Optimal Clusters
inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# 6. K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

print("\nK-Means Cluster Counts:")
print(pd.Series(kmeans_labels).value_counts().sort_index())

# 7. Visualize K-Means Clusters
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 2],
    c=kmeans_labels, cmap="viridis"
)
plt.xlabel("Quantity Ordered (Scaled)")
plt.ylabel("Sales (Scaled)")
plt.title("K-Means Clustering")
plt.show()

# 8. Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(X_scaled)

print("\nHierarchical Cluster Counts:")
print(pd.Series(hierarchical_labels).value_counts().sort_index())

# 9. Dendrogram
linked = linkage(X_scaled, method="ward")

plt.figure(figsize=(10, 5))
dendrogram(linked, truncate_mode="lastp", p=30)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points / Clusters")
plt.ylabel("Distance")
plt.show()
