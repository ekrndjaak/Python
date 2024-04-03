import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Iris 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

# K-means 모델 생성 및 학습
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# 군집 중심
centroids = kmeans.cluster_centers_

# 예측된 레이블
labels = kmeans.labels_

# 군집 중심과 예측된 레이블을 시각화
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# 실제 꽃 종류에 따른 분포
for i in range(3):
    ax[0].scatter(X[y == i, 0], X[y == i, 1], label=f'Iris {i}', c=f'C{i}')
ax[0].set_title('Actual Iris Species')
ax[0].set_xlabel('Sepal Length')
ax[0].set_ylabel('Sepal Width')
ax[0].legend()

# K-means에 의한 클러스터링 결과
for i in range(3):
    ax[1].scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i}', c=f'C{i}', marker='x')
ax[1].scatter(centroids[:, 0], centroids[:, 1], marker='o', s=200, c='red', label='Centroids')
ax[1].set_title('K-means Clustering')
ax[1].set_xlabel('Sepal Length')
ax[1].set_ylabel('Sepal Width')
ax[1].legend()

plt.show()
print("Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Cluster {i}: {centroid}")