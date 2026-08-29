# DAY3

[← 전체 목차](<../README.md>)

CIFAR 이미지 분류를 기준으로 CNN 구조를 비교하고, VAE와 사전학습 모델, Vision Transformer까지 살펴본 날.

| 번호 | 내용 정리 | 실습 노트북 |
|---:|---|---|
| 06 | [CIFAR-10 MLP와 CNN 비교](<06_CIFAR-10 MLP와 CNN 비교.md>) | [Notebook](<06_CIFAR-10 MLP와 CNN 비교.ipynb>) |
| 07 | [얼굴 검출과 MNIST VAE](<07_얼굴 검출과 MNIST VAE.md>) | [Notebook](<07_얼굴 검출과 MNIST VAE.ipynb>) |
| 08 | [CIFAR-10 GoogLeNet 구현](<08_CIFAR-10 GoogLeNet 구현.md>) | [Notebook](<08_CIFAR-10 GoogLeNet 구현.ipynb>) |
| 09 | [ResNet50 사전학습 이미지 분류](<09_ResNet50 사전학습 이미지 분류.md>) | [Notebook](<09_ResNet50 사전학습 이미지 분류.ipynb>) |
| 10 | [EfficientNetB0 사전학습 이미지 분류](<10_EfficientNetB0 사전학습 이미지 분류.md>) | [Notebook](<10_EfficientNetB0 사전학습 이미지 분류.ipynb>) |
| 11 | [CIFAR-100 Vision Transformer](<11_CIFAR-100 Vision Transformer.md>) | [Notebook](<11_CIFAR-100 Vision Transformer.ipynb>) |

`07`에서 사용하는 `three_young_man.jpg`와 `09`, `10`에서 사용하는 `dog.png`는 실습 파일과 함께 들어 있다.

사전학습 모델은 첫 실행 때 ImageNet 가중치를 내려받는다. `06`의 체크포인트와 `07`의 학습 중 생성 이미지는 Git에 포함되지 않도록 설정했다.
