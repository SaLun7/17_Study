# 18. 주택 가격 예측 - XGBoost와 LightGBM

House Prices 데이터의 결측치와 범주형 변수를 처리하고 XGBoost와 LightGBM으로 SalePrice를 예측한다.

[← DAY6 목차](<README.md>) · [원본 노트북](<18_주택 가격 예측 - XGBoost와 LightGBM.ipynb>)

## 실습 내용

- 가격 분포와 로그 변환 효과를 확인한다.
- 결측치와 불필요한 열을 처리한다.
- train/test 원-핫 열을 정렬한다.
- XGBoost와 LightGBM을 MAE/RMSE/R2로 비교한다.

**데이터**  
house_train/house_test: 주택 구조·면적·품질·입지 피처와 SalePrice

## 핵심 메모

### 열 정렬

train과 test를 따로 원-핫 인코딩하면 열 구성이 달라질 수 있으므로 동일한 스키마로 맞춘다.

### 가격 왜도

SalePrice의 긴 꼬리는 로그 변환으로 완화할 수 있다.

### 부스팅 회귀

비선형 관계와 피처 상호작용을 트리의 순차 결합으로 학습한다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 10 보기</summary>

```python
from sklearn.model_selection import train_test_split

y = df["SalePrice"]
X = df.drop(["SalePrice"], axis = 1)

print(y.shape)
print(X.shape)

X_dum = pd.get_dummies(X)

X_train, X_val, y_train, y_val = train_test_split(X_dum, y, test_size = 0.2, random_state = 42)
```

</details>

<details>
<summary>코드 셀 17 보기</summary>

```python
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

xgb = XGBRegressor()
xgb.fit(X_train, y_train)
print(xgb.score(X_train, y_train))
print(xgb.score(X_val, y_val))

pred = xgb.predict(X_val)
print(f"MAE: {mean_absolute_error(y_val, pred)}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_val, pred))}")
print(f"R2_SCORE: {r2_score(y_val, pred)}")
```

</details>

<details>
<summary>코드 셀 18 보기</summary>

```python
from lightgbm import LGBMRegressor

lgb = LGBMRegressor()
lgb.fit(X_train, y_train)
print(lgb.score(X_train, y_train))
print(lgb.score(X_val, y_val))

pred1 = lgb.predict(X_val)
print(f"MAE: {mean_absolute_error(y_val, pred1)}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_val, pred1))}")
print(f"R2_SCORE: {r2_score(y_val, pred1)}")
```

</details>

<details>
<summary>코드 셀 19 보기</summary>

```python
test_dum = pd.get_dummies(test)

test_dum = test_dum.reindex(columns=X_dum.columns,fill_value=0)

xgb_pred = xgb.predict(test_dum)
xgb_pred = xgb_pred.round(0)

print(xgb_pred)
```

</details>

## 결과 메모

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

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `read_csv` | CSV 파일을 DataFrame으로 읽기 |
| `train_test_split` | 학습용과 평가용 데이터 분리 |
| `XGBRegressor` | XGBoost 회귀 모델 |
| `LGBMRegressor` | LightGBM 회귀 모델 |
| `mean_squared_error` | 평균제곱오차 계산 |
| `mean_absolute_error` | 평균절대오차 계산 |
| `r2_score` | 평균 기준선 대비 설명력 계산 |

## 정리

- train/test에 동일한 대체·인코딩 규칙을 사용한다.
- 예측 파일의 Id와 행 순서를 보존한다.
- 원 가격과 로그 가격의 평가 지표를 혼동하지 않는다.
