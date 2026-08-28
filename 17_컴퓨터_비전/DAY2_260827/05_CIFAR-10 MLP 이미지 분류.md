# 05. CIFAR-10 MLP 이미지 분류

CIFAR-10 컬러 이미지를 정규화하고 학습·검증·테스트로 나눈 뒤 MLP 기준선 모델을 학습한다.

[← 과정 목차](<README.md>) · [원본 노트북](<05_CIFAR-10 MLP 이미지 분류.ipynb>)

## 실습 내용

- 데이터 shape과 라벨 구조를 확인한다.
- 픽셀값을 0~1로 정규화한다.
- 학습 45,000개와 검증 5,000개를 분리한다.
- Flatten 기반 MLP를 학습·평가한다.

**데이터**  
CIFAR-10: 32×32 RGB 이미지, 10개 클래스

## 핵심 메모

### Flatten

32×32×3 공간 배열을 하나의 긴 벡터로 바꾼다.

### Softmax

10개 클래스의 확률 분포를 출력한다.

### Sparse categorical loss

정수 클래스 라벨에 사용하는 다중 분류 손실이다.

### CNN 비교

MLP는 공간 이웃 구조를 버리므로 이미지에서는 CNN보다 비효율적일 수 있다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 1 보기</summary>

```python
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
```

</details>

<details>
<summary>코드 셀 2 보기</summary>

```python
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data();
```

</details>

<details>
<summary>코드 셀 5 보기</summary>

```python
plt.figure(figsize = (1, 1))
plt.imshow(train_images[32])
```

</details>

<details>
<summary>코드 셀 12 보기</summary>

```python
mlp_model.fit(train_images, train_labels, epochs = 5, 
              validation_data = (val_images, val_labels))
```

</details>

## 결과 메모

MLP는 데이터 파이프라인을 검증하는 좋은 기준선이다. 최종 셀이 미실행 상태라면 정확도를 문서에 확정값으로 기록하지 않고 재실행 후 추가한다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `Sequential` | 순차적으로 층을 쌓는 Keras 모델 |
| `Dense` | 완전연결 신경망 층 |

## 정리

- 검증 데이터로 모델을 선택하고 테스트는 최종 평가에만 사용한다.
- 정규화 전후 dtype과 범위를 확인한다.
- 다음 단계에서는 CNN과 같은 조건으로 비교한다.
