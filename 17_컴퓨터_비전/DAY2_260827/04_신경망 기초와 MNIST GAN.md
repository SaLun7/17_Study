# 04. 신경망 기초와 MNIST GAN

논리게이트와 회귀 신경망으로 비선형 학습을 이해하고 MNIST 이미지를 생성하는 간단한 GAN을 구현한다.

[← DAY2 목차](<README.md>) · [원본 노트북](<04_신경망 기초와 MNIST GAN.ipynb>)

## 실습 내용

- 단일 퍼셉트론과 다층 신경망의 표현력 차이를 이해한다.
- Dense 회귀 모델의 가중치와 편향을 확인한다.
- Generator와 Discriminator의 역할을 구분한다.
- GAN 학습 루프와 손실을 구현한다.

**데이터**  
AND/OR/XOR 논리 데이터, 합성 회귀 데이터, MNIST 손글씨 이미지

## 핵심 메모

### 비선형 활성화

여러 선형 경계를 조합해 XOR 같은 비선형 문제를 표현한다.

### Generator

잠재벡터에서 가짜 이미지를 생성한다.

### Discriminator

입력 이미지가 진짜인지 가짜인지 판별한다.

### Adversarial training

두 모델이 서로 경쟁하며 동시에 개선되는 학습 구조다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 3 보기</summary>

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_dim = 2, activation= "sigmoid")
]);

model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 1),
              loss = "binary_crossentropy",
              metrics = ["accuracy"])

model.fit(x, and_y, epochs = 100, batch_size = 4)

loss, accuracy = model.evaluate(x, and_y)
print(loss)
print(accuracy)

predictions = model.predict(x)

print(predictions)
```

</details>

<details>
<summary>코드 셀 4 보기</summary>

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_dim = 2, activation= "sigmoid")
]);

model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 1),
              loss = "binary_crossentropy",
              metrics = ["accuracy"])

model.fit(x, or_y, epochs = 100, batch_size = 4)

loss, accuracy = model.evaluate(x, or_y)
print(loss)
print(accuracy)

predictions = model.predict(x)

print(predictions)
```

</details>

<details>
<summary>코드 셀 5 보기</summary>

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_dim = 2, activation= "sigmoid")
]);

model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 1),
              loss = "binary_crossentropy",
              metrics = ["accuracy"])

model.fit(x, xor_y, epochs = 100, batch_size = 4)

loss, accuracy = model.evaluate(x, xor_y)
print(loss)
print(accuracy)

predictions = model.predict(x)

print(predictions)
```

</details>

<details>
<summary>코드 셀 6 보기</summary>

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, input_dim = 2, activation= "relu"),
    tf.keras.layers.Dense(1, activation= "sigmoid")
])

model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 1),
              loss = "binary_crossentropy",
              metrics = ["accuracy"])

model.fit(x, xor_y, epochs = 100, batch_size = 4)

loss, accuracy = model.evaluate(x, xor_y)
print(loss)
print(accuracy)

predictions = model.predict(x)

print(predictions)
```

</details>

## 실습 흐름

AND, OR, XOR 데이터를 단일 퍼셉트론으로 학습해 선형 경계의 한계를 확인하고 XOR에는 은닉층과 비선형 활성화를 추가했다. 합성 회귀 데이터에서는 Dense 층의 가중치와 편향이 학습되는 과정을 살펴봤다. 이후 MNIST를 정규화하고 Generator와 Discriminator를 번갈아 학습시키며 epoch별 생성 영상을 저장했다.

## 결과 메모

GAN 손실 하나만으로 이미지 품질을 판단하기 어렵다. 고정된 noise의 생성 샘플을 epoch별로 비교하고 다양성과 mode collapse를 함께 확인한다.

### 실행 결과

```text
1/1 [==============================] - 0s 302ms/step - loss: 0.7284 - accuracy: 0.7500
1/1 [==============================] - 0s 4ms/step - loss: 0.6953 - accuracy: 0.7500
1/1 [==============================] - 0s 4ms/step - loss: 0.6657 - accuracy: 0.7500
1/1 [==============================] - 0s 3ms/step - loss: 0.6388 - accuracy: 0.7500
1/1 [==============================] - 0s 6ms/step - loss: 0.6140 - accuracy: 0.7500
1/1 [==============================] - 0s 8ms/step - loss: 0.5910 - accuracy: 0.7500
1/1 [==============================] - 0s 6ms/step - loss: 0.5697 - accuracy: 0.7500
1/1 [==============================] - 0s 7ms/step - loss: 0.5499 - accuracy: 0.7500
1/1 [==============================] - 0s 6ms/step - loss: 0.5315 - accuracy: 0.7500
1/1 [==============================] - 0s 8ms/step - loss: 0.5142 - accuracy: 0.7500
```

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `mean_squared_error` | 평균제곱오차 계산 |
| `Sequential` | 순차적으로 층을 쌓는 Keras 모델 |
| `Dense` | 완전연결 신경망 층 |

## 다시 볼 것

- XOR 결과로 은닉층과 비선형 활성화가 필요한 이유를 설명해 본다.
- GAN의 두 모델은 서로 다른 목적의 손실과 optimizer를 사용한다.
- 손실값만 보지 말고 고정된 잠재벡터의 생성 결과를 계속 비교한다.

## 정리

- GAN 입력 이미지를 모델 출력 범위와 맞춰 정규화한다.
- Generator와 Discriminator optimizer를 분리한다.
- 학습 샘플의 다양성을 주기적으로 시각화한다.
