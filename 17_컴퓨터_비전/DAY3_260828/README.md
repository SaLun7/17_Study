# DAY3

[← 전체 목차](<../README.md>)

CIFAR 이미지 분류를 기준으로 CNN 구조를 비교하고, VAE와 사전학습 모델, Vision Transformer까지 살펴본 날.

| 번호 | 내용 정리 | 실습 노트북 |
|---:|---|---|
| 01 | [CIFAR-10 MLP와 CNN 비교](<01_CIFAR-10 MLP와 CNN 비교.md>) | [Notebook](<01_CIFAR-10 MLP와 CNN 비교.ipynb>) |
| 02 | [얼굴 검출과 MNIST VAE](<02_얼굴 검출과 MNIST VAE.md>) | [Notebook](<02_얼굴 검출과 MNIST VAE.ipynb>) |
| 03 | [CIFAR-10 GoogLeNet 구현](<03_CIFAR-10 GoogLeNet 구현.md>) | [Notebook](<03_CIFAR-10 GoogLeNet 구현.ipynb>) |
| 04 | [ResNet50 사전학습 이미지 분류](<04_ResNet50 사전학습 이미지 분류.md>) | [Notebook](<04_ResNet50 사전학습 이미지 분류.ipynb>) |
| 05 | [EfficientNetB0 사전학습 이미지 분류](<05_EfficientNetB0 사전학습 이미지 분류.md>) | [Notebook](<05_EfficientNetB0 사전학습 이미지 분류.ipynb>) |
| 06 | [CIFAR-100 Vision Transformer](<06_CIFAR-100 Vision Transformer.md>) | [Notebook](<06_CIFAR-100 Vision Transformer.ipynb>) |

`02`에서 사용하는 `three_young_man.jpg`와 `04`, `05`에서 사용하는 `dog.png`는 실습 파일과 함께 들어 있다.

사전학습 모델은 첫 실행 때 ImageNet 가중치를 내려받는다. `01`의 체크포인트와 `02`의 학습 중 생성 이미지는 Git에 포함되지 않도록 설정했다.
