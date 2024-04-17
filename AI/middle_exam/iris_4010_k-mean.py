from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 아이리스 데이터 불러오기
iris = load_iris()
X = iris.data[:, [2, 3]]  # petal width와 length만 선택
y = iris.target

# 클래스별로 데이터를 분할하기 위한 인덱스 계산
indices_class_0 = [i for i, label in enumerate(y) if label == 0]
indices_class_1 = [i for i, label in enumerate(y) if label == 1]
indices_class_2 = [i for i, label in enumerate(y) if label == 2]

# 각 클래스별로 40:10 비율로 데이터 분할
train_indices_class_0, eval_indices_class_0 = train_test_split(indices_class_0, train_size=40, test_size=10, random_state=42)
train_indices_class_1, eval_indices_class_1 = train_test_split(indices_class_1, train_size=40, test_size=10, random_state=42)
train_indices_class_2, eval_indices_class_2 = train_test_split(indices_class_2, train_size=40, test_size=10, random_state=42)

# 분할된 인덱스를 사용하여 학습 데이터와 평가 데이터 생성
train_indices = train_indices_class_0 + train_indices_class_1 + train_indices_class_2
eval_indices = eval_indices_class_0 + eval_indices_class_1 + eval_indices_class_2

learnData = X[train_indices]
evalData = X[eval_indices]

# 출력
print("LearnData:")
print(learnData)
print("Shape:", learnData.shape)
print("\nEvalData:")
print(evalData)
print("Shape:", evalData.shape)
