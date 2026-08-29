# 01. OpenCV 영상 기본 변환

OpenCV로 영상을 읽고 크기변환, 반전, 회전, 자르기와 픽셀 수정을 수행한다.

[← DAY1 목차](<README.md>) · [원본 노트북](<01_OpenCV 영상 기본 변환.ipynb>)

## 실습 내용

- 영상 배열의 shape과 dtype을 확인한다.
- resize·flip·rotation의 좌표 변화를 이해한다.
- NumPy 슬라이싱으로 관심영역을 자른다.
- 슬라이스 수정이 원본에 미치는 영향을 확인한다.

**데이터**  
like_lenna.png 그레이스케일 영상

## 핵심 메모

### 영상 배열

그레이스케일 영상은 보통 높이×너비의 2차원 배열이다.

### Affine 변환

회전행렬과 warpAffine가 새 좌표로 픽셀을 재배치한다.

### NumPy view

슬라이스는 원본을 참조할 수 있어 값을 바꾸면 원본도 변할 수 있다.

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
<summary>코드 셀 11 보기</summary>

```python
height, width = image.shape
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)
res = cv2.warpAffine(image, matrix, (width, height), borderValue=255)

plt.imshow(res, cmap= "gray")
plt.title("30 Rotation Like Lenna")
plt.axis("off")
plt.show()
```

</details>

<details>
<summary>코드 셀 12 보기</summary>

```python
plt.imshow(image[50:150, 50:100], cmap= "gray")
plt.title("Like Lenna")
plt.axis("off")
plt.show()
```

</details>

<details>
<summary>코드 셀 13 보기</summary>

```python
croped_image = image[50:150, 50:150]
croped_image[:] = 200

plt.imshow(image, cmap= "gray")
plt.title("Like Lenna")
plt.axis("off")
plt.show()
```

</details>

## 결과 메모

각 결과를 단순 그림이 아니라 shape, 좌표, 경계 채움 방식의 변화로 해석한다. 영상이 None이면 경로와 작업 디렉터리를 먼저 점검한다.

## 사용한 함수

| 함수·클래스 | 역할 |
|---|---|
| `cv2.imread` | 파일에서 영상 배열 읽기 |
| `cv2.resize` | 영상 크기 변경 |
| `cv2.flip` | 영상 축 방향 반전 |
| `cv2.getRotationMatrix2D` | 2차원 회전 변환행렬 생성 |
| `cv2.warpAffine` | Affine 변환 적용 |

## 정리

- OpenCV 좌표와 NumPy [행, 열] 순서를 구분한다.
- 회전 후 잘림과 borderValue를 확인한다.
- 원본 보존이 필요하면 crop.copy()를 사용한다.
