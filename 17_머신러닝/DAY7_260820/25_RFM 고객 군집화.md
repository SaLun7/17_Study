# 25. RFM 고객 군집화

온라인 소매 거래를 정제하고 고객별 RFM 특성을 만든 뒤 K-Means로 고객을 세분화한다.

[← DAY7 목차](<README.md>) · [원본 노트북](<25_RFM 고객 군집화.ipynb>)

## 실습 내용

- 취소·결측·중복·비정상 거래를 정제한다.
- Recency·Frequency·Monetary를 고객별로 집계한다.
- log1p와 표준화로 긴 꼬리를 완화한다.
- 실루엣과 PCA로 군집을 평가하고 원 단위로 해석한다.

**데이터**  
Online Retail 거래 데이터: CustomerID, InvoiceDate, Quantity, UnitPrice

## 핵심 메모

### Recency

기준일로부터 마지막 구매까지의 일수다.

### Frequency

고객의 서로 다른 구매 주문 횟수다.

### Monetary

고객이 구매에 사용한 총 금액이다.

### 원 단위 해석

표준화 좌표가 아니라 실제 RFM 평균으로 고객군에 이름을 붙인다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 31 보기</summary>

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

for k in [2, 3, 4, 5]:
    kmeans = KMeans(n_clusters=k, random_state=42)

    cluster_labels = kmeans.fit_predict(rfm_scaled)

    score = silhouette_score(rfm_scaled, cluster_labels)

    print(k, score)
```

</details>

<details>
<summary>코드 셀 32 보기</summary>

```python
def visualize_silhouette(cluster_lists, X_features): 
    
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_samples, silhouette_score

    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import math
    
    # 입력값으로 클러스터링 갯수들을 리스트로 받아서, 각 갯수별로 클러스터링을 적용하고 실루엣 개수를 구함
    n_cols = len(cluster_lists)
    
    # plt.subplots()으로 리스트에 기재된 클러스터링 수만큼의 sub figures를 가지는 axs 생성 
    fig, axs = plt.subplots(figsize=(4*n_cols, 4), nrows=1, ncols=n_cols)
    
    # 리스트에 기재된 클러스터링 갯수들을 차례로 iteration 수행하면서 실루엣 개수 시각화
    for ind, n_cluster in enumerate(cluster_lists):
        
        # KMeans 클러스터링 수행하고, 실루엣 스코어와 개별 데이터의 실루엣 값 계산. 
        clusterer = KMeans(n_clusters = n_cluster, max_iter=500, random_state=42)
        cluster_labels = clusterer.fit_predict(X_features)
        
        sil_avg = silhouette_score(X_features, cluster_labels)
        sil_values = silhouette_samples(X_features, cluster_labels)
        
        y_lower = 10
        axs[ind].set_title('Number of Cluster : '+ str(n_cluster)+'\n' \
                          'Silhouette Score :' + str(round(sil_avg,3)) )
        axs[ind].set_xlabel("The silhouette coefficient values")
        axs[ind].set_ylabel("Cluster label")
        axs[ind].set_xlim([-0.1, 1])
# ... 이하 코드는 원본 노트북 참조
```

</details>

<details>
<summary>코드 셀 33 보기</summary>

```python
visualize_silhouette([2, 3, 4, 5], rfm_scaled)
```

</details>

<details>
<summary>코드 셀 34 보기</summary>

```python
kmeans = KMeans(n_clusters=2, random_state=42)

cluster_labels = kmeans.fit_predict(rfm_scaled)
```

</details>

## 결과 메모

군집 번호 자체보다 각 집단의 최근성·빈도·금액 차이가 핵심 결과다. 군집 수는 실루엣 점수와 마케팅 활용 가능성을 함께 보고 선택한다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `read_excel` | Excel 파일을 DataFrame으로 읽기 |
| `StandardScaler` | 평균 0, 표준편차 1로 표준화 |
| `PCA` | 분산을 보존하는 비지도 차원축소 |
| `KMeans` | 중심 거리 기반 군집화 |
| `silhouette_score` | 군집 응집도와 분리도 평가 |

## 정리

- 취소 주문과 음수 금액 처리 기준을 기록한다.
- 긴 꼬리를 변환한 뒤 스케일링한다.
- 고객군의 크기와 실제 행동 특성을 함께 보고 이름을 붙인다.
