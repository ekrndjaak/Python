from sklearn.datasets import load_iris
import pandas as pd

# 아이리스 데이터 불러오기
iris = load_iris()

# 데이터와 레이블을 DataFrame으로 변환하여 출력
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]
print(iris_df)