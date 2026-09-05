# 09. XGBoost

XGBoost의 Native API와 scikit-learn Wrapper API를 사용해 유방암 데이터를 분류하고 조기 종료를 적용한다.

[← DAY3 목차](<README.md>) · [원본 노트북](<09_XGBoost.ipynb>)

## 실습 내용

- DMatrix와 Wrapper API의 차이를 이해한다.
- logloss와 검증 손실을 모니터링한다.
- early stopping으로 최적 반복 수를 찾는다.
- AUC와 특성 중요도를 확인한다.

**데이터**  
Breast Cancer Wisconsin 이진 분류 데이터

## 핵심 메모

### Boosting

얕은 트리를 순차적으로 추가해 남은 오류를 줄인다.

### Learning rate

한 트리의 기여를 줄이면 더 많은 트리가 필요하지만 일반화가 좋아질 수 있다.

### Early stopping

검증 점수가 일정 기간 개선되지 않으면 학습을 중단한다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 8 보기</summary>

```python
pred_prob = xgb_model.predict(dtest)
print(np.round(pred_prob[:10],3))

pred = [ 1 if x > 0.5 else 0 for x in pred_prob ]
print(pred[:10])
```

</details>

<details>
<summary>코드 셀 9 보기</summary>

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
<summary>코드 셀 12 보기</summary>

```python
from xgboost import XGBClassifier

xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)
xgb_wrapper.fit(X_train, y_train)
w_preds = xgb_wrapper.predict(X_test)
w_pred_proba = xgb_wrapper.predict_proba(X_test)[:, 1]
```

</details>

<details>
<summary>코드 셀 14 보기</summary>

```python
from xgboost import XGBClassifier

xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3,
                            early_stopping_rounds=100, eval_metric="logloss")
evals = [(X_test, y_test)]
xgb_wrapper.fit(X_train, y_train, eval_set=evals, verbose=True)

preds = xgb_wrapper.predict(X_test)
pred_probs = xgb_wrapper.predict_proba(X_test)[:, 1]
```

</details>

## 실습 흐름

XGBoost 전용 데이터 형식과 scikit-learn 방식의 분류기를 각각 사용해 같은 부스팅 흐름을 확인했다. 반복마다 손실이 줄어드는 과정을 기록하고 검증 성능이 좋아지지 않으면 일찍 멈추도록 설정했다. 예측 클래스와 확률을 이용해 혼동행렬, F1과 ROC-AUC를 비교했다.

## 결과 메모

train logloss와 validation logloss의 차이가 커지기 시작하면 과적합 가능성이 있다. 최종 성능은 조기 종료에 쓰지 않은 테스트 세트에서 확인한다.

### 실행 결과

```text
오차 행렬
정확도: 0.9561, 정밀도: 0.9583, 재현율: 0.9718,    F1: 0.9650, AUC:0.9938
<Axes: title={'center': 'Feature importance'}, xlabel='Importance score', ylabel='Features'>
정확도: 0.9561, 정밀도: 0.9583, 재현율: 0.9718,    F1: 0.9650, AUC:0.9931
정확도: 0.9561, 정밀도: 0.9583, 재현율: 0.9718,    F1: 0.9650, AUC:0.9944
```

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_breast_cancer` | 유방암 분류 데이터셋 불러오기 |
| `train_test_split` | 학습용과 평가용 데이터 분리 |
| `XGBClassifier` | XGBoost 분류 모델 |
| `accuracy_score` | 분류 정확도 계산 |
| `confusion_matrix` | TN·FP·FN·TP 혼동행렬 계산 |
| `precision_score` | 정밀도 계산 |
| `recall_score` | 재현율 계산 |
| `f1_score` | 정밀도와 재현율의 조화평균 계산 |
| `roc_auc_score` | 확률 순위 기반 ROC-AUC 계산 |

## 다시 볼 것

- `n_estimators`가 커도 조기 종료가 있으면 필요한 반복에서 멈출 수 있다.
- 학습률을 낮출 때는 보통 더 많은 트리가 필요하다.
- 조기 종료에 사용하는 검증 세트를 최종 테스트 세트와 분리한다.

## 정리

- 검증 데이터와 테스트 데이터를 구분한다.
- n_estimators는 learning_rate와 함께 선택한다.
- 특성 중요도를 인과관계로 해석하지 않는다.
