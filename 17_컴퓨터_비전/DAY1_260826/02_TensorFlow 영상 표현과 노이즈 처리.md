# 02. TensorFlow 영상 표현과 노이즈 처리

OpenCV 기본 변환을 확장해 TensorFlow 텐서, 색공간, 정규화, Salt-and-pepper와 Gaussian 노이즈를 다룬다.

[← DAY1 목차](<README.md>) · [원본 노트북](<02_TensorFlow 영상 표현과 노이즈 처리.ipynb>)

## 실습 내용

- PNG를 TensorFlow Tensor로 디코딩한다.
- RGB·Gray·HSV 색공간을 비교한다.
- 정규화와 표준화의 차이를 이해한다.
- 여러 노이즈와 필터 강도의 효과를 시각화한다.

**데이터**  
like_lenna.png 및 생성한 RGB 텐서

## 핵심 메모

### Tensor

shape, dtype, 값 범위를 가진 다차원 배열이다.

### 정규화

일반적으로 uint8 0~255 값을 float 0~1로 바꾼다.

### Salt-and-pepper

일부 픽셀이 극단값으로 바뀌는 충격성 노이즈다.

### Gaussian noise

연속적인 확률 분포의 잡음을 픽셀에 더한다.

## 코드

코드는 길어서 중요한 셀만 접어 두었다. 전체 실행 과정은 원본 노트북에서 확인한다.

<details>
<summary>코드 셀 1 보기</summary>

```python
import cv2 
image = cv2.imread("like_lenna.png", cv2.IMREAD_GRAYSCALE)

if image is not None:
    print("read!")

else:
    print("not!")

print(type(image))
```

</details>

<details>
<summary>코드 셀 28 보기</summary>

```python
lenna_image = cv2.imread("like_lenna.png", cv2.IMREAD_GRAYSCALE)

salted_lenna = generate_salt_noise(lenna_image)
pepered_lenna = generate_peper_noise(salted_lenna)
filtered_lenna = cv2.medianBlur(pepered_lenna, 5)

fig, axes = plt.subplots(1, 4, figsize= (20, 6))

axes[0].imshow(lenna_image, cmap = "gray")
axes[0].axis("off")

axes[1].imshow(salted_lenna, cmap = "gray")
axes[1].axis("off")

axes[2].imshow(pepered_lenna, cmap = "gray")
axes[2].axis("off")

axes[3].imshow(filtered_lenna, cmap = "gray")
axes[3].axis("off")

plt.tight_layout()
plt.show()
```

</details>

<details>
<summary>코드 셀 29 보기</summary>

```python
# 가우시안 필터

image = cv2.imread('like_lenna.png', cv2.IMREAD_GRAYSCALE)
mean = 0
sigma = 1
gaussian_noise = np.random.normal(mean, sigma, image.shape).astype('uint8')
noise_image = cv2.add(image, gaussian_noise)

plt.imshow(noise_image, cmap = 'gray')
plt.axis('off')
plt.show()
```

</details>

<details>
<summary>코드 셀 30 보기</summary>

```python
sigma_values = [1, 5, 10]
denoise_image = []

for sigma in sigma_values:
    denoise = cv2.GaussianBlur(noise_image, (0, 0), sigma)
    denoise_image.append(denoise)

fig, axes = plt.subplots(1, 4, figsize = (20, 10))

axes[0].imshow(noise_image, cmap = 'gray')
axes[0].axis('off')

for ax, img, sigma in zip(axes[1:], denoise_image, sigma_values):
    ax.imshow(img, cmap = 'gray')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

</details>

## 실습 흐름

PNG 파일을 TensorFlow 텐서로 디코딩하고 shape, dtype과 픽셀 범위를 확인했다. RGB 영상을 회색조와 HSV로 바꿔 채널이 표현하는 정보의 차이를 살펴본 뒤 0~1 정규화와 평균·표준편차 기반 표준화를 비교했다. Salt-and-pepper와 Gaussian 노이즈를 직접 더하고 필터 강도에 따라 영상의 세부 정보가 얼마나 남는지 확인했다.

## 결과 메모

노이즈 제거 결과는 깨끗해 보이는지뿐 아니라 경계와 질감이 얼마나 보존됐는지 함께 평가한다. 필터 sigma가 커지면 노이즈와 세부정보가 동시에 줄 수 있다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `cv2.imread` | 파일에서 영상 배열 읽기 |
| `cv2.resize` | 영상 크기 변경 |
| `cv2.flip` | 영상 축 방향 반전 |
| `cv2.getRotationMatrix2D` | 2차원 회전 변환행렬 생성 |
| `cv2.warpAffine` | Affine 변환 적용 |
| `tf.image` | TensorFlow 영상 변환 함수 모음 |

## 다시 볼 것

- 색공간 변환 전후의 채널 수와 값 범위를 확인한다.
- 노이즈 종류에 따라 평균·가우시안·중간값 필터의 효과가 다르다.
- 필터를 강하게 적용하면 노이즈와 함께 경계도 흐려질 수 있다.

## 정리

- OpenCV BGR과 matplotlib RGB를 변환한다.
- 시각화 전에 값 범위를 확인한다.
- 노이즈 종류에 맞는 필터를 선택한다.
