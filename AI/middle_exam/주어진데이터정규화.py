#만약 데이터를 아이리스 데이터를 안쓰고 주어졌을때 
from sklearn.cluster import KMeans
import numpy as np

def normalize_data(data):
    # 데이터 정규화 (0~1로)
    normalized_data = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
    return normalized_data

def kmeans_clustering(data, num_clusters):
    # K-means 클러스터링 수행
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(data)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    return centroids, labels

# 주어진 학습 데이터(여기에 데이터 삽입하면 구해짐)
learnData = np.array([[55,131,31],  # 학습 데이터
                      [67,143,41],
                      [72,157,5],
                      [74,171,9],
                      [92,128,15],
                      [75,151,22],
                      [107,173,27],
                      [52,127,17]
                      ])

# K-means 클러스터링 수행
centroids, labels = kmeans_clustering(learnData, num_clusters=3)

# 클러스터링 결과 출력
print("Centroids:")
print(centroids)
print("Labels:")
print(labels)

# 클러스터링 결과를 0.0에서 1.0으로 정규화
normalized_centroids = normalize_data(centroids)
print("Normalized Centroids:")
print(normalized_centroids)