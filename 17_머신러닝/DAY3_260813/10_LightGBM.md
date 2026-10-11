# 10. LightGBM

[← DAY3 목차](<README.md>) · [원본 노트북](<10_LightGBM.ipynb>)

LightGBM으로 유방암 데이터를 분류하고 조기 종료와 특성 중요도를 확인한다.

## 핵심 개념

### Leaf-wise

손실을 가장 많이 줄이는 잎을 우선 확장해 빠르게 복잡한 구조를 만든다.

### num_leaves

모델 표현력을 크게 좌우하며 작은 데이터에서는 과적합을 유발할 수 있다.

### No further splits

현재 조건에서 추가 분할의 양의 이득을 찾지 못했다는 뜻이며 항상 실행 오류는 아니다.

잎을 우선 확장하는 방식은 손실을 빠르게 줄이지만 작은 자료에서는 일부 구간에 지나치게 맞출 수 있다. `num_leaves`와 `max_depth`, 최소 리프 표본 수를 같이 보면 복잡도를 조절하기 쉽다. 경고가 반복된다면 오류로 단정하기보다 데이터 크기와 분할 조건을 확인한다.

## 실습 흐름

LightGBM 분류기를 학습하고 트리 수, 잎 개수와 최소 leaf 데이터 수에 따른 변화를 살펴봤다. 검증 세트를 지정해 조기 종료 시점을 찾고 예측 확률로 ROC-AUC를 계산했다. XGBoost 결과와 성능, 학습 속도와 과적합 경향을 함께 비교했다.

### 사용한 함수

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

## 실행 결과

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

## 필요한 파일

Breast Cancer Wisconsin 이진 분류 데이터

데이터를 불러오는 셀부터 실행한다. 별도의 로컬 입력 파일을 지정하지 않는다.

## 다시 볼 것

- leaf-wise 성장은 빠르지만 작은 데이터에서는 과적합이 쉬울 수 있다.
- `num_leaves`와 `min_child_samples`를 따로 보지 말고 함께 조정한다.
- 범주형 피처를 어떤 방식으로 전달했는지 실험 기록에 남긴다.
