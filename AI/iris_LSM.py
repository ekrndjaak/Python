import pandas as pd
import numpy as np
from sklearn.datasets import load_iris


def avr(A, B):
    sum = 0
    for i in range(30):
        sum += A[i][B]
    output = sum/30
    return output

def var(A,B):
    avg = avr(A,B)
    diff = 0
    for i in range(len(A)):
        diff += (A[i][B] - avg) **2
    var_output = diff / len(A)
    return var_output

Iris = load_iris()
Iris_Data = pd.DataFrame(data=Iris['data'], columns=Iris['feature_names'])
iris_data = np.array([])
iris_data = np.array(Iris_Data.iloc[:])
print(iris_data.shape)
print(avr(iris_data,0))
print(var(iris_data, 0))