# 02. K-Fold 교차검증

하나의 학습·검증 분할에 의존하지 않고 데이터를 여러 fold로 나누어 결정트리의 성능을 반복 평가한다.

[← 과정 목차](<../README.md>) · [원본 노트북](<02_K-Fold 교차검증.ipynb>)

## 실습 내용

- K-Fold의 학습/검증 인덱스 구조를 이해한다.
- 폴드별 점수와 평균 점수를 계산한다.
- 단일 분할보다 안정적인 성능 추정이 필요한 이유를 설명한다.

**데이터**  
Iris 데이터셋을 K개의 학습/검증 폴드로 순환 분할

## 핵심 메모

### K-Fold

전체 데이터를 K개 묶음으로 나누고 한 묶음씩 검증용으로 바꾸어 사용한다.

### 평균과 변동

평균은 대표 성능, 폴드 간 차이는 데이터 분할에 대한 민감도를 나타낸다.

### Stratified K-Fold

분류 문제에서는 각 fold의 클래스 비율을 유지하는 방식이 더 안전하다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 1 보기</summary>

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state = 42)

# KFold 교차검증을 위해 데이터를 5개의 폴드로 나눈다
kfold = KFold(n_splits=5)

# 각 교차검증에서 나온 정확도를 저장할 빈 리스트를 만든다
cv_accuracy = []

# features 데이터의 행 개수(전체 샘플 수)를 출력한다
print(features.shape[0])
```

</details>

<details>
<summary>코드 셀 2 보기</summary>

```python
n_iter = 0

for train_index, test_index in kfold.split(features):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]

    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1

    accuracy = np.round(accuracy_score(y_test, pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]

    print(n_iter, accuracy, train_size, test_size)
    cv_accuracy.append(accuracy)

print(np.mean(cv_accuracy))
```

</details>

## 결과 메모

평균 정확도만 보지 말고 각 fold 점수의 범위도 확인한다. 점수 차이가 크다면 데이터가 작거나 클래스 분포가 불안정할 수 있다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `KFold` | K개의 교차검증 분할 생성 |
| `DecisionTreeClassifier` | 결정트리 분류 모델 |
| `accuracy_score` | 분류 정확도 계산 |

## 정리

- 교차검증은 모델 선택에 사용하고 최종 테스트 세트는 따로 남긴다.
- 분류에서는 클래스 비율을 유지하는 층화 분할을 우선 고려한다.
- 전처리는 각 fold의 학습 부분에서만 fit해야 한다.
