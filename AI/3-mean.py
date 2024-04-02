from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np

# iris 데이터 로드
iris = datasets.load_iris()
X = iris.data

# 데이터를 A, B, C로 나누기
A = X[:50]
B = X[50:100]
C = X[100:]

# KMeans 모델 생성 및 학습
kmeans_A = KMeans(n_clusters=3, random_state=42).fit(A)
kmeans_B = KMeans(n_clusters=3, random_state=42).fit(B)
kmeans_C = KMeans(n_clusters=3, random_state=42).fit(C)

# 각 군집의 중심점 확인
means_A = np.round(kmeans_A.cluster_centers_, 2)
means_B = np.round(kmeans_B.cluster_centers_, 2)
means_C = np.round(kmeans_C.cluster_centers_, 2)

# 중심점의 평균 계산
total_means = np.round(np.mean([means_A, means_B, means_C], axis=0), 2)

# 3-mean의 평균 출력
print("A의 3-mean:")
print(means_A)
print("\nB의 3-mean:")
print(means_B)
print("\nC의 3-mean:")
print(means_C)
print("\nA, B, C의 3-mean의 평균:")
print(total_means)

# 3-mean 값들을 비교하기 쉽게 정렬
sorted_means = np.sort(total_means, axis=0)
print("\n정렬된 3-mean 값들:")
print(sorted_means)