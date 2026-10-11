# 18. 주택 가격 예측 - XGBoost와 LightGBM

[← DAY6 목차](<README.md>) · [원본 노트북](<18_주택 가격 예측 - XGBoost와 LightGBM.ipynb>)

House Prices 데이터의 결측치와 범주형 변수를 처리하고 XGBoost와 LightGBM으로 SalePrice를 예측한다.

## 핵심 개념

### 열 정렬

train과 test를 따로 원-핫 인코딩하면 열 구성이 달라질 수 있으므로 동일한 스키마로 맞춘다.

### 가격 왜도

SalePrice의 긴 꼬리는 로그 변환으로 완화할 수 있다.

### 부스팅 회귀

비선형 관계와 피처 상호작용을 트리의 순차 결합으로 학습한다.

주택 가격처럼 큰 값이 소수 섞인 자료에서는 로그 변환 전후의 오차가 다른 의미를 가진다. 대회 지표가 로그 RMSE라면 원 단위 RMSE와 혼동하지 않는다. train·test의 범주가 다를 때는 동일한 인코딩 열을 만들어야 모델이 같은 입력 구조를 받는다.

## 실습 흐름

훈련·테스트 파일의 열과 결측치를 먼저 비교하고 SalePrice 분포에 로그 변환을 적용했다. 식별자와 불필요한 열을 정리한 뒤 범주형 변수는 원-핫 인코딩하고 두 데이터의 열 순서를 맞췄다. XGBoost와 LightGBM을 학습해 로그 가격을 예측하고 원래 가격으로 복원한 뒤 여러 회귀 지표를 비교했다.

### 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `read_csv` | CSV 파일을 DataFrame으로 읽기 |
| `train_test_split` | 학습용과 평가용 데이터 분리 |
| `XGBRegressor` | XGBoost 회귀 모델 |
| `LGBMRegressor` | LightGBM 회귀 모델 |
| `mean_squared_error` | 평균제곱오차 계산 |
| `mean_absolute_error` | 평균절대오차 계산 |
| `r2_score` | 평균 기준선 대비 설명력 계산 |

## 실행 결과

저장된 결과에서는 모델별 MAE·RMSE·R2가 조금씩 다르다. 목적 지표를 먼저 정하고 같은 분할에서 비교해야 한다.

### 실행 결과

```text
24  Exterior2nd    1460 non-null   str
34  BsmtFinSF1     1460 non-null   int64
1         Lvl    AllPub  ...           0        0    NaN    NaN        Gar2
24  Exterior2nd    1458 non-null   str
34  BsmtFinSF1     1458 non-null   float64
Exterior2nd        1
BsmtFinSF1         1
Exterior2nd      1
MAE: 17530.755859375
RMSE: 27803.95827935296
```

## 필요한 파일

house_train/house_test: 주택 구조·면적·품질·입지 피처와 SalePrice

같은 DAY의 `data/house_train.csv`, `data/house_test.csv`가 필요하며 현재 저장소에는 없다.

## 다시 볼 것

- 훈련과 테스트를 따로 인코딩했을 때 빠지거나 새로 생긴 열이 없는지 확인한다.
- 결측값 처리 기준은 피처의 의미와 모델 특성을 함께 고려한다.
- 로그 공간의 RMSE와 원래 가격 단위의 오차가 의미하는 바를 구분한다.
