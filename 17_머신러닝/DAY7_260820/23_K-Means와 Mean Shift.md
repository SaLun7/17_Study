# 23. K-Means와 Mean Shift

중심 기반 K-Means와 밀도 봉우리를 찾는 Mean Shift를 Iris와 합성 데이터에서 비교한다.

[← 과정 목차](<../README.md>) · [원본 노트북](<23_K-Means와 Mean Shift.ipynb>)

## 실습 내용

- K-Means의 중심 갱신 과정을 이해한다.
- PCA 2축에서 군집 결과를 시각화한다.
- Mean Shift의 bandwidth 역할을 확인한다.
- 정답 클래스와 군집 라벨의 차이를 이해한다.

**데이터**  
Iris 및 make_blobs 합성 군집 데이터

## 핵심 메모

### K-Means

각 점을 가장 가까운 중심에 배정하고 중심을 평균으로 갱신한다.

### Mean Shift

밀도가 높은 방향으로 중심 후보를 이동시켜 봉우리를 찾는다.

### 군집 라벨

숫자는 임의의 식별자이며 실제 클래스 번호와 직접 일치하지 않는다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 11 보기</summary>

```python
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=200, random_state=42)
cluster_labels = kmeans.fit_predict(X)
df_cls['kmeans_label']  = cluster_labels

centers = kmeans.cluster_centers_
unique_labels = np.unique(cluster_labels)

markers=['o', 's', '^', 'P','D','H','x']


for label in unique_labels:
    label_cluster = df_cls[df_cls['kmeans_label']==label]
    center = centers[label]
    plt.scatter(x=label_cluster['ftr1'], y=label_cluster['ftr2'], edgecolor='k', 
                marker=markers[label] )
    plt.scatter(x=center[0], y=center[1], s=200, color='white',
                alpha=0.9, edgecolor='k', marker=markers[label])
    plt.scatter(x=center[0], y=center[1], s=70, color='k', edgecolor='k', 
                marker='$%d$' % label)

plt.show()
```

</details>

<details>
<summary>코드 셀 13 보기</summary>

```python
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift

X, y = make_blobs(n_samples=200, n_features=2, centers=3, 
                  cluster_std=0.7, random_state=42)

meanshift= MeanShift(bandwidth=0.8)
cluster_labels = meanshift.fit_predict(X)
print(np.unique(cluster_labels))
```

</details>

<details>
<summary>코드 셀 14 보기</summary>

```python
meanshift= MeanShift(bandwidth=1.0)
cluster_labels = meanshift.fit_predict(X)
print(np.unique(cluster_labels))
```

</details>

<details>
<summary>코드 셀 16 보기</summary>

```python
import pandas as pd


df = pd.DataFrame(data=X, columns=['ftr1', 'ftr2'])
df['target'] = y

best_bandwidth = estimate_bandwidth(X)

meanshift= MeanShift(bandwidth=best_bandwidth)
cluster_labels = meanshift.fit_predict(X)
print(np.unique(cluster_labels))
```

</details>

## 결과 메모

구형이고 크기가 비슷한 군집에서는 K-Means가 효과적이다. Mean Shift는 군집 수를 직접 지정하지 않지만 bandwidth에 민감하다.

### 실행 결과

```text
ftr1      ftr2  target
```

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `load_iris` | Iris 데이터셋 불러오기 |
| `PCA` | 분산을 보존하는 비지도 차원축소 |
| `KMeans` | 중심 거리 기반 군집화 |
| `MeanShift` | 밀도 봉우리 기반 군집화 |

## 정리

- 거리 기반 군집 전 스케일링한다.
- 군집 번호를 서열로 해석하지 않는다.
- 데이터 형태와 알고리즘 가정이 맞는지 시각화한다.
