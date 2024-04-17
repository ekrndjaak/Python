import numpy as np

def activation_function(x):
    return 1 if x >= 0 else 0

def delta_rule(x, y, weights, bias, learning_rate):
    weighted_sum = np.dot(x, weights) + bias
    prediction = activation_function(weighted_sum)
    error = y - prediction
    weights += learning_rate * error * x
    bias += learning_rate * error
    return weights, bias, weighted_sum, prediction

def train_OR_gate(inputs, outputs, epochs=100, learning_rate=0.01):
    num_inputs = len(inputs[0])
    weights = np.random.rand(num_inputs)
    bias = np.random.rand()
    
    for epoch in range(epochs):
        for x, y in zip(inputs, outputs):
            weights, bias, _, _ = delta_rule(x, y, weights, bias, learning_rate)
    return weights, bias

def test_OR_gate(inputs, weights, bias):
    print("Testing OR gate:")
    for test_input in inputs:
        weighted_sum = np.dot(test_input, weights) + bias
        output = activation_function(weighted_sum)
        print(f"Input: {test_input}, Weighted Sum: {weighted_sum}, Output: {output}")

# 훈련 데이터셋
training_inputs = np.array([[0,0],[0,0.3],[0,0.5],[0,0.8],
                            [0,1], [0.3, 0], [0.5, 0],
                            [0.8, 0], [1, 1]])
training_outputs = np.array([0, 1, 1, 1, 1, 1, 1, 1, 1])  # OR 게이트의 출력

# OR 게이트 학습
weights, bias = train_OR_gate(training_inputs, training_outputs)

# OR 게이트 테스트
def test_OR_gate_with_intermediate_values(inputs, weights, bias):
    print("Testing OR gate with intermediate values:")
    for test_input in inputs:
        weighted_sum = np.dot(test_input, weights) + bias
        intermediate_value = weighted_sum
        output = activation_function(weighted_sum)
        print(f"Input: {test_input}, Weighted Sum: {weighted_sum}, y: {intermediate_value}, Output: {output}")

test_inputs = [[0,0],[0,0.3],[0,0.5],[0,0.8],
               [0,1], [0.3, 0], [0.5, 0],
               [0.8, 0], [1, 1]]
test_OR_gate_with_intermediate_values(test_inputs, weights, bias)
