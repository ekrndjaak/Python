# 150개의 평균분산 4번 clear
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

mean_sepal_length = round(iris_data['sepal_length'].mean(),2)
mean_sepal_width = round(iris_data['sepal_width'].mean(),2)
mean_petal_length = round(iris_data['petal_length'].mean(), 2)
mean_petal_width = round(iris_data['petal_width'].mean(), 2)

var_sepal_length = df['sepal length (cm)'].var(ddof=1)
var_sepal_width = df['sepal width (cm)'].var(ddof=1)
var_petal_length = df['petal length (cm)'].var(ddof=1)
var_petal_width = df['petal width (cm)'].var(ddof=1)

setosa_data = df[df['class'] == 0].iloc[:, :-1]
mean_setosa = setosa_data.mean()
var_setosa = setosa_data.var(ddof=1)

versicolor_data = df[df['class']==1].iloc[:, :-1]
mean_versicolor = versicolor_data.mean()
var_versicolor = versicolor_data.var(ddof=1)

virginica_data = df[df['class']==2].iloc[:, :-1]
mean_virginica = virginica_data.mean()
var_virginica = virginica_data.var(ddof=1)

print("평균 :       ", mean_sepal_length,"       ", mean_sepal_width,"        ",
       mean_petal_length,"       ", mean_petal_width)
print("분산 :       ", var_sepal_length.round(2),"       ", var_sepal_width.round(2)
      ,"        ",var_petal_length.round(2),"       ", var_petal_width.round(2))
print("\n")
print("setosa의 평균:")
print(mean_setosa)
print("\n")
print("setosa의 분산:")
print(var_setosa)
print("\n")
print("versicolor의 평균:")
print(mean_versicolor)
print("\n")
print("versicolor의 분산:")
print(var_versicolor)
print("\n")
print("virginica의 평균:")
print(mean_virginica)
print("\n")
print("viginica의 분산:")
print(var_virginica)
