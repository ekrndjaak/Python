import numpy as np

weights = np.array([0.5, 0.5])
input_data = np.array([1,1])
target = 0

learning_rate = 0.1

prediction = np.dot(input_data, weights)

error = target - prediction

weights += learning_rate * error * input_data

print("updataed weights", weights)