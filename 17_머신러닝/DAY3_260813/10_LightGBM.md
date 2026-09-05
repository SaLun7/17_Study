# 10. LightGBM

LightGBM으로 유방암 데이터를 분류하고 조기 종료와 특성 중요도를 확인한다.

[← DAY3 목차](<README.md>) · [원본 노트북](<10_LightGBM.ipynb>)

## 실습 내용

- LightGBM의 leaf-wise 성장 방식을 이해한다.
- 검증 세트와 callback으로 조기 종료를 적용한다.
- 분류 지표와 AUC를 함께 평가한다.
- 분할 이득 관련 경고를 해석한다.

**데이터**  
Breast Cancer Wisconsin 이진 분류 데이터

## 핵심 메모

### Leaf-wise

손실을 가장 많이 줄이는 잎을 우선 확장해 빠르게 복잡한 구조를 만든다.

### num_leaves

모델 표현력을 크게 좌우하며 작은 데이터에서는 과적합을 유발할 수 있다.

### No further splits

현재 조건에서 추가 분할의 양의 이득을 찾지 못했다는 뜻이며 항상 실행 오류는 아니다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 2 보기</summary>

```python
from lightgbm import LGBMClassifier

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

dataset = load_breast_cancer()

df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target']= dataset.target
X_features = df.iloc[:, :-1]
y_label = df.iloc[:, -1]


X_train, X_test, y_train, y_test=train_test_split(X_features, y_label, test_size=0.2, random_state=42 )

X_tr, X_val, y_tr, y_val= train_test_split(X_train, y_train, test_size=0.1, random_state=42 )

lgbm_wrapper = LGBMClassifier(n_estimators=400, learning_rate=0.05, early_stopping_rounds=50, eval_metric="logloss",verbose=1)

evals = [(X_tr, y_tr), (X_val, y_val)]
lgbm_wrapper.fit(X_tr, y_tr, eval_set = evals)
pred = lgbm_wrapper.predict(X_test)
pred_proba = lgbm_wrapper.predict_proba(X_test)[:, 1]
```

</details>

<details>
<summary>코드 셀 3 보기</summary>

```python
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score, roc_auc_score

def get_clf_eval(y_test, pred=None, pred_proba=None):
    confusion = confusion_matrix( y_test, pred)
    accuracy = accuracy_score(y_test , pred)
    precision = precision_score(y_test , pred)
    recall = recall_score(y_test , pred)
    f1 = f1_score(y_test,pred)

    roc_auc = roc_auc_score(y_test, pred_proba)
    print('오차 행렬')
    print(confusion)
  
    print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},\
    F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))
```

</details>

<details>
<summary>코드 셀 4 보기</summary>

```python
get_clf_eval(y_test, pred, pred_proba)
```

</details>

<details>
<summary>코드 셀 5 보기</summary>

```python
from lightgbm import plot_importance
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 12))
plot_importance(lgbm_wrapper, ax=ax)
```

</details>

## 실습 흐름

LightGBM 분류기를 학습하고 트리 수, 잎 개수와 최소 leaf 데이터 수에 따른 변화를 살펴봤다. 검증 세트를 지정해 조기 종료 시점을 찾고 예측 확률로 ROC-AUC를 계산했다. XGBoost 결과와 성능, 학습 속도와 과적합 경향을 함께 비교했다.

## 결과 메모

빠른 학습만으로 모델을 선택하지 말고 검증 손실과 클래스별 지표를 확인한다. 경고가 반복되면 데이터 크기와 규제 파라미터를 함께 점검한다.

### 실행 결과

```text
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.625917 -> initscore=0.514740
[LightGBM] [Info] Start training from score 0.514740
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
Training until validation scores don't improve for 50 rounds
Early stopping, best iteration is:
오차 행렬
정확도: 0.9649, 정밀도: 0.9589, 재현율: 0.9859,    F1: 0.9722, AUC:0.9895
```

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_breast_cancer` | 유방암 분류 데이터셋 불러오기 |
| `train_test_split` | 학습용과 평가용 데이터 분리 |
| `LGBMClassifier` | LightGBM 분류 모델 |
| `accuracy_score` | 분류 정확도 계산 |
| `confusion_matrix` | TN·FP·FN·TP 혼동행렬 계산 |
| `precision_score` | 정밀도 계산 |
| `recall_score` | 재현율 계산 |
| `f1_score` | 정밀도와 재현율의 조화평균 계산 |
| `roc_auc_score` | 확률 순위 기반 ROC-AUC 계산 |

## 다시 볼 것

- leaf-wise 성장은 빠르지만 작은 데이터에서는 과적합이 쉬울 수 있다.
- `num_leaves`와 `min_child_samples`를 따로 보지 말고 함께 조정한다.
- 범주형 피처를 어떤 방식으로 전달했는지 실험 기록에 남긴다.

## 정리

- num_leaves와 max_depth의 관계를 확인한다.
- 조기 종료에 별도 검증 세트를 사용한다.
- 작은 데이터에서는 복잡도를 보수적으로 제한한다.
