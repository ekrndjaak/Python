from sklearn.datasets import load_iris
import numpy as np

# 아이리스 데이터 불러오기
iris = load_iris()
X = iris.data
y = iris.target

# 클래스별로 데이터 분할
X_class_0 = X[y == 0]
X_class_1 = X[y == 1]
X_class_2 = X[y == 2]

# 클래스별 평균과 분산 계산
mean_class_0 = np.mean(X_class_0, axis=0)
mean_class_1 = np.mean(X_class_1, axis=0)
mean_class_2 = np.mean(X_class_2, axis=0)

variance_class_0 = np.var(X_class_0, axis=0)
variance_class_1 = np.var(X_class_1, axis=0)
variance_class_2 = np.var(X_class_2, axis=0)

# 출력
print("Class 0 평균:", mean_class_0)
print("Class 0 분산:", variance_class_0)
print("Class 1 평균:", mean_class_1)
print("Class 1 분산:", variance_class_1)
print("Class 2 평균:", mean_class_2)
print("Class 2 분산:", variance_class_2)

# 데이터 정규화 (0~1로)
X_normalized = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

# 출력
print("\n정규화된 데이터:")
print(X_normalized)