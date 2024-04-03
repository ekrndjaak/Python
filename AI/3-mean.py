from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import numpy as np

# iris 데이터 불러오기
iris = load_iris()
X = iris.data

# 데이터를 A, B, C로 나누기
A = X[:50]
B = X[50:100]
C = X[100:]

# KMeans 모델 초기화
kmeans = KMeans(n_clusters=3, random_state=42)

# A에 대한 k-means 클러스터링
kmeans.fit(A)
A_cluster_centers = kmeans.cluster_centers_
A_cluster_mean = np.mean(A_cluster_centers, axis=0)

# B에 대한 k-means 클러스터링
kmeans.fit(B)
B_cluster_centers = kmeans.cluster_centers_
B_cluster_mean = np.mean(B_cluster_centers, axis=0)

# C에 대한 k-means 클러스터링
kmeans.fit(C)
C_cluster_centers = kmeans.cluster_centers_
C_cluster_mean = np.mean(C_cluster_centers, axis=0)

# 클러스터 중심 평균을 출력
print("A 클러스터 중심 평균:", A_cluster_mean)
print("B 클러스터 중심 평균:", B_cluster_mean)
print("C 클러스터 중심 평균:", C_cluster_mean)

# 클러스터 중심 평균을 비교하기 쉽게 정렬
cluster_means = np.vstack([A_cluster_mean, B_cluster_mean, C_cluster_mean])
sorted_indices = np.argsort(np.sum(cluster_means, axis=1))
sorted_cluster_means = cluster_means[sorted_indices]

# 정렬된 클러스터 중심 평균 출력
print("정렬된 클러스터 중심 평균:")
for i, mean in enumerate(sorted_cluster_means):
    print(f"Cluster {i+1}: {mean}")
