from sklearn.linear_model import LinearRegression

# 주어진 데이터
distances = [[14], [21], [26], [32], [36]]
prices = [127, 140, 151, 175, 180]

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(distances, prices)

# 거리가 90인 경우의 집 가격 예측
predicted_price = model.predict([[17]])

print("거리가 90일 때 예상 집 가격:", predicted_price[0])