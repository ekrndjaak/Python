import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

result = []

for i in range(0, len(iris_df), 30):
    subset = iris_df.iloc[i:i+30]
    subset_mean = subset.mean()
    subset_var = subset.var()
    result.append((subset_mean, subset_var))

for idx, (mean, var) in enumerate(result):
    print(f"Subset {idx+1}:")
    print("Mean:")
    print(mean)
    print("Variance:")
    print(var)
    
plt.xlabel('length')
plt.ylabel('width')
plt.scatter(mean, var)
plt.show()
