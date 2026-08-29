# 22. SVD와 NMF 행렬 분해

SVD로 행렬을 분해·복원하고 Truncated SVD와 NMF의 저차원 표현을 비교한다.

[← DAY7 목차](<README.md>) · [원본 노트북](<22_SVD와 NMF 행렬 분해.ipynb>)

## 실습 내용

- U·Sigma·Vt의 역할과 행렬 복원을 이해한다.
- 작은 특이값을 버린 저랭크 근사를 확인한다.
- Truncated SVD와 PCA의 관계를 비교한다.
- NMF의 비음수 제약을 이해한다.

**데이터**  
합성 행렬과 Iris 수치 데이터

## 핵심 메모

### 특이값

행렬의 주요 변동 방향이 가진 중요도를 나타낸다.

### 저랭크 근사

큰 특이값만 남겨 원 행렬의 핵심 구조를 압축한다.

### NMF

음수가 없는 입력을 양수 성분의 조합으로 표현해 부분 기반 해석에 유리하다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 10 보기</summary>

```python
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

iris = load_iris()
iris_ftrs = iris.data
# 2개의 주요 component로 TruncatedSVD 변환
tsvd = TruncatedSVD(n_components=2)
tsvd.fit(iris_ftrs)
iris_tsvd = tsvd.transform(iris_ftrs)

# Scatter plot 2차원으로 TruncatedSVD 변환 된 데이터 표현. 품종은 색깔로 구분
plt.scatter(x=iris_tsvd[:,0], y= iris_tsvd[:,1], c= iris.target)
plt.xlabel('TruncatedSVD Component 1')
plt.ylabel('TruncatedSVD Component 2')
```

</details>

<details>
<summary>코드 셀 11 보기</summary>

```python
from sklearn.preprocessing import StandardScaler

# 붓꽃 데이터를 StandardScaler로 변환
scaler = StandardScaler()
iris_scaled = scaler.fit_transform(iris_ftrs)

# 스케일링된 데이터를 기반으로 TruncatedSVD 변환 수행 
tsvd = TruncatedSVD(n_components=2)
tsvd.fit(iris_scaled)
iris_tsvd = tsvd.transform(iris_scaled)

# 스케일링된 데이터를 기반으로 PCA 변환 수행 
pca = PCA(n_components=2)
pca.fit(iris_scaled)
iris_pca = pca.transform(iris_scaled)

# TruncatedSVD 변환 데이터를 왼쪽에, PCA변환 데이터를 오른쪽에 표현 
fig, (ax1, ax2) = plt.subplots(figsize=(9,4), ncols=2)
ax1.scatter(x=iris_tsvd[:,0], y= iris_tsvd[:,1], c= iris.target)
ax2.scatter(x=iris_pca[:,0], y= iris_pca[:,1], c= iris.target)
ax1.set_title('Truncated SVD Transformed')
ax2.set_title('PCA Transformed')
```

</details>

<details>
<summary>코드 셀 12 보기</summary>

```python
print((iris_pca - iris_tsvd).mean())
print((pca.components_ - tsvd.components_).mean())
```

</details>

<details>
<summary>코드 셀 15 보기</summary>

```python
from sklearn.decomposition import NMF
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
%matplotlib inline

iris = load_iris()
iris_ftrs = iris.data
nmf = NMF(n_components=2)
nmf.fit(iris_ftrs)
iris_nmf = nmf.transform(iris_ftrs)
plt.scatter(x=iris_nmf[:,0], y= iris_nmf[:,1], c= iris.target)
plt.xlabel('NMF Component 1')
plt.ylabel('NMF Component 2')

plt.show()
```

</details>

## 결과 메모

복원 오차와 축소 차원을 함께 기록해야 압축 효과를 평가할 수 있다. NMF는 입력에 음수가 있으면 직접 적용할 수 없다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `StandardScaler` | 평균 0, 표준편차 1로 표준화 |
| `PCA` | 분산을 보존하는 비지도 차원축소 |
| `TruncatedSVD` | 저랭크 행렬 분해 기반 차원축소 |
| `NMF` | 비음수 행렬 분해 |

## 정리

- Sigma를 대각행렬로 구성해 차원을 맞춘다.
- 축소 차원과 복원 손실의 균형을 본다.
- 알고리즘의 입력 제약을 먼저 확인한다.
