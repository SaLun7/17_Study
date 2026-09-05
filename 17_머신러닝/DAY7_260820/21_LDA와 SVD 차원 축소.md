# 21. LDA와 SVD 차원 축소

라벨을 이용하는 LDA와 행렬 분해 기반 Truncated SVD를 PCA와 비교한다.

[← DAY7 목차](<README.md>) · [원본 노트북](<21_LDA와 SVD 차원 축소.ipynb>)

## 실습 내용

- LDA가 클래스 분리를 최대화하는 방식을 이해한다.
- Truncated SVD의 저랭크 표현을 확인한다.
- PCA와 지도 여부·중심화 차이를 비교한다.
- 2차원 결과를 시각적으로 해석한다.

**데이터**  
Iris 데이터와 표준화된 수치 피처

## 핵심 메모

### LDA

클래스 내부 분산은 줄이고 클래스 간 분산은 늘리는 지도 차원축소다.

### Truncated SVD

행렬을 낮은 rank로 근사하며 희소 행렬에서 중심화 없이 사용할 수 있다.

### PCA 비교

PCA는 라벨을 사용하지 않고 전체 분산 보존에 집중한다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 8 보기</summary>

```python
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.datasets import load_iris

import matplotlib.pyplot as plt

iris = load_iris()

iris_ftrs = iris.data

tsvd = TruncatedSVD(n_components = 2)
tsvd.fit(iris_ftrs)
iris_tsvd = tsvd.transform(iris_ftrs)

plt.scatter(x = iris_tsvd[:, 0], y = iris_tsvd[:, 1], c = iris.target)
plt.xlabel("TSVD Comp 1")
plt.ylabel("TSVD Comp 2")
```

</details>

<details>
<summary>코드 셀 9 보기</summary>

```python
# from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()
# iris_scaled = scaler.fit_transform(iris_ftrs)

# tsvd = TruncatedSVD(n_components = 2)
# tsvd.fit(iris_scaled)
# iris

# pca = PCA(n_components= 2)
# pca.fit(iris_scaled)
# iris_pca = pca.transform(iris_scaled)

# fig, (ax1, ax2) = plt.subplots(figsize = (9,4), ncols = 2)
# ax1.scatter(x=iris_tsvd[: 0], y = iris_tsvd[:, 1], c = iris.target)
# ax2.scatter(x=iris_pca[: 0], y = iris_pca[:, 1], c = iris.pca)
# ax1.set_title('TSVD')
# ax2.set_title('PCA')
```

</details>

<details>
<summary>코드 셀 10 보기</summary>

```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD, PCA
import matplotlib.pyplot as plt

iris = load_iris()

scaler = StandardScaler()
iris_scaled = scaler.fit_transform(iris.data)

tsvd = TruncatedSVD(n_components=2)
iris_tsvd = tsvd.fit_transform(iris_scaled)

pca = PCA(n_components=2)
iris_pca = pca.fit_transform(iris_scaled)

fig, (ax1, ax2) = plt.subplots(figsize=(9, 4), ncols=2)

ax1.scatter(x=iris_tsvd[:, 0], y=iris_tsvd[:, 1], c=iris.target)
ax1.set_title('TSVD')

ax2.scatter(x=iris_pca[:, 0], y=iris_pca[:, 1], c=iris.target)
ax2.set_title('PCA')

plt.show()
```

</details>

<details>
<summary>코드 셀 11 보기</summary>

```python
from sklearn.decomposition import NMF

iris = load_iris()
iris_ftrs = iris.data
nmf = NMF(n_components = 2)
nmf.fit(iris_ftrs)
iris_nmf = nmf.transform(iris_ftrs)
plt.scatter(x = iris_nmf[:,0], y = iris_nmf[:, 1], c = iris.target)
plt.xlabel('MMF 1')
plt.xlabel('MMF 2')
plt.show()
```

</details>

## 실습 흐름

Iris 데이터를 표준화하고 LDA가 정답 라벨을 이용해 클래스 사이가 잘 벌어지는 축을 찾는 과정을 확인했다. 같은 입력을 Truncated SVD로 줄여 라벨을 보지 않는 표현과 비교했다. PCA까지 함께 놓고 지도 여부, 중심화와 사용할 수 있는 데이터 형태의 차이를 정리했다.

## 결과 메모

LDA의 분리도가 높아 보여도 라벨 정보를 사용한 결과다. 비지도 시각화와 분류 전처리 목적을 구분해 선택한다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `StandardScaler` | 평균 0, 표준편차 1로 표준화 |
| `PCA` | 분산을 보존하는 비지도 차원축소 |
| `LinearDiscriminantAnalysis` | 클래스 분리를 최대화하는 지도 차원축소 |
| `TruncatedSVD` | 저랭크 행렬 분해 기반 차원축소 |
| `NMF` | 비음수 행렬 분해 |

## 다시 볼 것

- LDA 변환 축 수는 클래스 수보다 하나 적은 값까지만 만들 수 있다.
- 희소 행렬에서는 평균을 빼지 않는 Truncated SVD가 실용적일 수 있다.
- 시각적으로 잘 나뉘는 것과 새 데이터 분류 성능을 구분한다.

## 정리

- 라벨 사용 여부를 명확히 기록한다.
- 희소 텍스트에는 Truncated SVD를 우선 고려한다.
- 축 수의 상한과 입력 조건을 확인한다.
