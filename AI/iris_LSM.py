import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

iris_data.columns =["sepal_lenghth", "sepal_width", "petal_length", "petal_width", "iris_class"]

print(iris_data.to_string())

plt.xlabel('length')
plt.xlabel('width')
plt.scatter(iris_data['sepal_length', 'sepal_width'])
plt.show()

