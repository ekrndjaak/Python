import numpy as np

# 활성화 함수: 단순한 단위 계단 함수
def activation_function(x):
    return 1 if x >= 0 else 0

# 델타 규칙을 이용한 가중치 조정
def delta_rule(x, y, weights, bias, learning_rate):
    weighted_sum = np.dot(x, weights) + bias
    prediction = activation_function(weighted_sum)
    error = y - prediction
    weights += learning_rate * error * x
    bias += learning_rate * error
    return weights, bias

# AND 게이트 학습
def train_AND_gate(epochs=10, learning_rate=0.1):
    # 입력과 정답 셋
    inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
    outputs = np.array([0, 0, 0, 1])
    
    # 가중치와 편향 초기화
    weights = np.random.rand(2)
    bias = np.random.rand()
    
    # 학습 과정
    for epoch in range(epochs):
        print(f"Epoch {epoch+1}/{epochs}")
        for x, y in zip(inputs, outputs):
            weights, bias = delta_rule(x, y, weights, bias, learning_rate)
            print(f"Updated weights: {weights}, Updated bias: {bias}")
        print("-----------")

    return weights, bias

# 학습 실행
weights, bias = train_AND_gate()

# 학습된 가중치로 AND 게이트 테스트
print("Testing trained AND gate")
for test in [[0,0],[0,1],[1,0],[1,1]]:
    weighted_sum = np.dot(test, weights) + bias
    print(f"Input: {test}, Output: {activation_function(weighted_sum)}")
