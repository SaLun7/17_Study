# 09. XGBoost

[← DAY3 목차](<README.md>) · [원본 노트북](<09_XGBoost.ipynb>)

XGBoost의 Native API와 scikit-learn Wrapper API를 사용해 유방암 데이터를 분류하고 조기 종료를 적용한다.

## 핵심 개념

### Boosting

얕은 트리를 순차적으로 추가해 남은 오류를 줄인다.

### Learning rate

한 트리의 기여를 줄이면 더 많은 트리가 필요하지만 일반화가 좋아질 수 있다.

### Early stopping

검증 점수가 일정 기간 개선되지 않으면 학습을 중단한다.

부스팅 모델은 트리를 많이 쌓을수록 학습 자료를 더 잘 맞힐 수 있지만 검증 점수는 먼저 나빠질 수 있다. Early stopping에 쓰는 자료와 최종 성능 보고에 쓰는 자료를 구분해야 한다. 피처 중요도는 어떤 변수가 분할에 쓰였는지의 단서이지 예측 방향이나 인과효과를 보여주지 않는다.

## 실습 흐름

XGBoost 전용 데이터 형식과 scikit-learn 방식의 분류기를 각각 사용해 같은 부스팅 흐름을 확인했다. 반복마다 손실이 줄어드는 과정을 기록하고 검증 성능이 좋아지지 않으면 일찍 멈추도록 설정했다. 예측 클래스와 확률을 이용해 혼동행렬, F1과 ROC-AUC를 비교했다.

### 사용한 함수

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

## 실행 결과

train logloss와 validation logloss의 차이가 커지기 시작하면 과적합 가능성이 있다. 최종 성능은 조기 종료에 쓰지 않은 테스트 세트에서 확인한다.

### 실행 결과

```text
오차 행렬
정확도: 0.9561, 정밀도: 0.9583, 재현율: 0.9718,    F1: 0.9650, AUC:0.9938
<Axes: title={'center': 'Feature importance'}, xlabel='Importance score', ylabel='Features'>
정확도: 0.9561, 정밀도: 0.9583, 재현율: 0.9718,    F1: 0.9650, AUC:0.9931
정확도: 0.9561, 정밀도: 0.9583, 재현율: 0.9718,    F1: 0.9650, AUC:0.9944
```

## 필요한 파일

Breast Cancer Wisconsin 이진 분류 데이터

데이터를 불러오는 셀부터 실행한다. 별도의 로컬 입력 파일을 지정하지 않는다.

## 다시 볼 것

- `n_estimators`가 커도 조기 종료가 있으면 필요한 반복에서 멈출 수 있다.
- 학습률을 낮출 때는 보통 더 많은 트리가 필요하다.
- 조기 종료에 사용하는 검증 세트를 최종 테스트 세트와 분리한다.
