# 05. EfficientNetB0 사전학습 이미지 분류

[← DAY3 목차](<README.md>) · [원본 노트북](<05_EfficientNetB0 사전학습 이미지 분류.ipynb>)

ResNet50과 같은 강아지 사진을 ImageNet 사전학습 EfficientNetB0으로 분류해 결과를 비교했다.

## 실습 내용

- ImageNet 출력층을 포함한 EfficientNetB0을 불러왔다.
- 입력 이미지를 224×224로 맞추고 모델 전용 전처리를 적용했다.
- 모델 구조를 확인한 뒤 상위 세 개 예측을 출력했다.

## 실행 결과

| 예측 | 확률 |
|---|---:|
| toy poodle | 54.50% |
| miniature poodle | 34.10% |
| standard poodle | 3.68% |

모델의 전체 파라미터는 약 533만 개다. EfficientNet은 네트워크의 깊이, 너비, 입력 해상도를 한쪽만 크게 하지 않고 함께 조절하는 방식으로 성능과 계산량을 맞춘다.

ResNet50과 1순위 품종은 달랐지만 두 모델 모두 푸들 계열을 상위 결과로 냈다. 현재 폴더에는 실행에 사용한 `dog.png`가 없다.
