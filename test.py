from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 아이리스 데이터 불러오기
iris = load_iris()
X = iris.data[:, [2, 3]]  # petal width와 length만 선택

# k-means 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 정규화를 위한 MinMaxScaler 객체 생성 및 학습 데이터에 적용
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# 클러스터링 결과 출력
print("클러스터 중심:", kmeans.cluster_centers_)
print("클러스터 레이블:", kmeans.labels_)

# 정규화된 데이터 출력
print("정규화된 데이터:\n", X_normalized)
