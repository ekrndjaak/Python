# 150개의 평균분산 4번 / 
# A만 가지고 평균분산 4개
# B만 가지고 평균분산 4개
# C만 가지고 평균분산 4개

import pandas as pd
from sklearn.datasets import load_iris

iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['class'] = iris.target

iris_data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "iris_class"]

print(iris_data.to_string())