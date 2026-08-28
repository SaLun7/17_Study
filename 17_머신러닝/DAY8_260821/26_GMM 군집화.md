# 26. GMM 군집화

Gaussian Mixture Model의 확률적 군집을 K-Means와 비교하고 타원형 분포에서의 차이를 확인한다.

[← 과정 목차](<../README.md>) · [원본 노트북](<26_GMM 군집화.ipynb>)

## 실습 내용

- 여러 가우시안 분포의 혼합 가정을 이해한다.
- 소속 확률과 최종 군집 라벨을 구분한다.
- 공분산이 타원형 군집을 표현하는 방식을 확인한다.
- K-Means와 결과를 비교한다.

**데이터**  
Iris와 선형 변환된 make_blobs 합성 데이터

## 핵심 메모

### 혼합분포

각 가우시안 구성요소가 데이터를 생성할 확률을 함께 추정한다.

### Soft assignment

한 점이 각 구성요소에 속할 확률을 제공한다.

### 공분산

군집의 크기·방향·타원 형태를 표현한다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 2 보기</summary>

```python
from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=3, random_state=42).fit(iris.data)
gmm_cluster_labels = gmm.predict(iris.data)

df['gmm_cluster'] = gmm_cluster_labels
df['target'] = iris.target

res = df.groupby(['target'])['gmm_cluster'].value_counts()
print(res)
```

</details>

<details>
<summary>코드 셀 3 보기</summary>

```python
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300,random_state=42).fit(iris.data)
kmeans_cluster_labels = kmeans.predict(iris.data)
df['kmeans_cluster'] = kmeans_cluster_labels
res1 = df.groupby(['target'])['kmeans_cluster'].value_counts()
print(res1)
```

</details>

<details>
<summary>코드 셀 6 보기</summary>

```python
kmeans = KMeans(3, random_state=42)
kmeans_label = kmeans.fit_predict(X_tras)
df['kmeans_label'] = kmeans_label

visualize_cluster_plot(kmeans, df, 'kmeans_label',iscenter=True)
```

</details>

<details>
<summary>코드 셀 7 보기</summary>

```python
gmm = GaussianMixture(n_components=3, random_state=42)
gmm_label = gmm.fit_predict(X_tras)
df['gmm_label'] = gmm_label

visualize_cluster_plot(gmm, df, 'gmm_label',iscenter=False)
```

</details>

## 결과 메모

타원형으로 늘어난 데이터에서는 중심 거리만 쓰는 K-Means보다 GMM이 형태를 유연하게 표현할 수 있다. 구성요소 수는 별도로 선택해야 한다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `KMeans` | 중심 거리 기반 군집화 |
| `GaussianMixture` | 가우시안 혼합 확률 군집화 |

## 정리

- 군집 번호를 클래스 번호와 직접 비교하지 않는다.
- predict_proba로 경계 불확실성을 확인한다.
- BIC/AIC와 안정성을 사용해 구성요소 수를 검토한다.
