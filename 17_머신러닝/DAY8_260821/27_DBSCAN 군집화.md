# 27. DBSCAN 군집화

DBSCAN의 eps와 min_samples를 조정하며 밀도 기반 군집과 노이즈 탐지를 이해한다.

[← 과정 목차](<../README.md>) · [원본 노트북](<27_DBSCAN 군집화.ipynb>)

## 실습 내용

- 핵심점·경계점·노이즈의 차이를 이해한다.
- eps와 min_samples가 결과에 미치는 영향을 확인한다.
- K-Means·GMM과 비선형 군집 결과를 비교한다.
- 노이즈 비율과 군집 수를 함께 평가한다.

**데이터**  
Iris와 make_circles 비선형 합성 데이터

## 핵심 메모

### eps

한 점의 이웃으로 인정하는 반경이다.

### min_samples

핵심점이 되기 위해 필요한 최소 이웃 수다.

### Noise -1

어느 고밀도 영역에도 연결되지 않은 점을 뜻한다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 6 보기</summary>

```python
dbscan = DBSCAN(eps=0.6, min_samples=16, metric='euclidean')
dbscan_labels = dbscan.fit_predict(iris.data)

df['dbscan_cluster'] = dbscan_labels
df['target'] = iris.target

res = df.groupby(['target'])['dbscan_cluster'].value_counts()
print(res)

visualize_cluster_plot(dbscan, df, 'dbscan_cluster', iscenter=False)
```

</details>

<details>
<summary>코드 셀 8 보기</summary>

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, max_iter=1000, random_state=42)
kmeans_labels = kmeans.fit_predict(X)
df['kmeans_cluster'] = kmeans_labels

visualize_cluster_plot(kmeans, df, 'kmeans_cluster', iscenter=True)
```

</details>

<details>
<summary>코드 셀 9 보기</summary>

```python
from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=2, random_state=42)
gmm_label = gmm.fit(X).predict(X)
df['gmm_cluster'] = gmm_label

visualize_cluster_plot(gmm, df, 'gmm_cluster', iscenter=False)
```

</details>

<details>
<summary>코드 셀 10 보기</summary>

```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.2, min_samples=10, metric='euclidean')
dbscan_labels = dbscan.fit_predict(X)
df['dbscan_cluster'] = dbscan_labels

visualize_cluster_plot(dbscan, df, 'dbscan_cluster', iscenter=False)
```

</details>

## 결과 메모

동심원처럼 중심 기반 방법이 나누기 어려운 구조를 DBSCAN은 밀도 연결로 구분할 수 있다. 밀도가 크게 다른 군집에는 하나의 eps가 잘 맞지 않을 수 있다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `PCA` | 분산을 보존하는 비지도 차원축소 |
| `KMeans` | 중심 거리 기반 군집화 |
| `GaussianMixture` | 가우시안 혼합 확률 군집화 |
| `DBSCAN` | 밀도 연결 기반 군집화와 노이즈 탐지 |

## 정리

- 거리 기반이므로 먼저 스케일링한다.
- eps를 키우면 군집 병합과 노이즈 감소 가능성이 커진다.
- 노이즈가 적다는 이유만으로 좋은 결과라고 판단하지 않는다.
