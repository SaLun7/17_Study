# 20. PCA 차원 축소

PCA로 고차원 데이터를 분산이 큰 직교 축으로 변환하고 Iris와 유방암 데이터를 저차원에서 시각화한다.

[← 과정 목차](<../README.md>) · [원본 노트북](<20_PCA 차원 축소.ipynb>)

## 실습 내용

- PCA의 주성분과 설명분산비를 이해한다.
- 표준화 전후 차이를 확인한다.
- 2차원 축소 결과를 클래스별로 시각화한다.
- 원 피처와 주성분의 관계를 해석한다.

**데이터**  
Iris 및 Breast Cancer 수치 피처

## 핵심 메모

### 주성분

원 피처의 선형결합으로 만든 서로 직교하는 새 축이다.

### 설명분산비

각 축이 전체 변동 중 얼마나 설명하는지 나타낸다.

### 표준화

단위가 큰 피처가 분산을 지배하지 않도록 스케일을 맞춘다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 4 보기</summary>

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(iris_scaled)
iris_pca = pca.transform(iris_scaled)
print(iris_pca.shape)
```

</details>

<details>
<summary>코드 셀 14 보기</summary>

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

cols_bill = ['BILL_AMT'+str(i) for i in range(1,7)]
cols_pay = ['PAY_' + str(i) for i in range(1, 7)]
cols_amt = ['PAY_AMT' + str(i) for i in range(1, 7)]
print(cols_bill)
cols_bill.extend(cols_pay)
cols_bill.extend(cols_amt)
print(cols_bill)
```

</details>

<details>
<summary>코드 셀 15 보기</summary>

```python
X[cols_bill] = X[cols_bill].astype(float)

scaler = StandardScaler()
df_scaled = scaler.fit_transform(X[cols_bill])
X.loc[:, cols_bill] = df_scaled
pca = PCA(n_components=2)
pca.fit(df_scaled)
print(pca.explained_variance_ratio_)
```

</details>

<details>
<summary>코드 셀 17 보기</summary>

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(X)

pca = PCA(n_components=6)
df_pca = pca.fit_transform(df_scaled)
scores_pca = cross_val_score(rcf, df_pca, y, scoring='accuracy', cv=3)

print(scores_pca)
print(np.mean(scores_pca))
```

</details>

## 결과 메모

2차원 그림에서 클래스가 잘 나뉘어 보여도 축소 과정에서 손실된 정보가 있다. 모델 전처리로 사용할 때는 파이프라인 안에서 교차검증한다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `read_excel` | Excel 파일을 DataFrame으로 읽기 |
| `cross_val_score` | 교차검증 점수 계산 |
| `StandardScaler` | 평균 0, 표준편차 1로 표준화 |
| `RandomForestClassifier` | 여러 무작위 트리를 결합한 분류 모델 |
| `PCA` | 분산을 보존하는 비지도 차원축소 |

## 정리

- PCA 전에 피처 단위를 확인한다.
- 설명분산비 누적값으로 축 수를 결정한다.
- 주성분을 원 피처 하나와 동일시하지 않는다.
