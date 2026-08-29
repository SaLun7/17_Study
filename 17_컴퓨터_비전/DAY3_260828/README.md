# DAY3 학습노트

[← 상위 목차](<../README.md>)

CIFAR 이미지 분류를 기준으로 CNN 구조를 비교하고, VAE와 사전학습 모델, Vision Transformer까지 살펴본 날.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 06 | CIFAR-10 MLP와 CNN 비교 | [학습노트](<06_CIFAR-10 MLP와 CNN 비교.md>) | [Notebook](<06_CIFAR-10 MLP와 CNN 비교.ipynb>) |
| 07 | 얼굴 검출과 MNIST VAE | [학습노트](<07_얼굴 검출과 MNIST VAE.md>) | [Notebook](<07_얼굴 검출과 MNIST VAE.ipynb>) |
| 08 | CIFAR-10 GoogLeNet 구현 | [학습노트](<08_CIFAR-10 GoogLeNet 구현.md>) | [Notebook](<08_CIFAR-10 GoogLeNet 구현.ipynb>) |
| 09 | ResNet50 사전학습 이미지 분류 | [학습노트](<09_ResNet50 사전학습 이미지 분류.md>) | [Notebook](<09_ResNet50 사전학습 이미지 분류.ipynb>) |
| 10 | EfficientNetB0 사전학습 이미지 분류 | [학습노트](<10_EfficientNetB0 사전학습 이미지 분류.md>) | [Notebook](<10_EfficientNetB0 사전학습 이미지 분류.ipynb>) |
| 11 | CIFAR-100 Vision Transformer | [학습노트](<11_CIFAR-100 Vision Transformer.md>) | [Notebook](<11_CIFAR-100 Vision Transformer.ipynb>) |

`07`에서 사용하는 `three_young_man.jpg`와 `09`, `10`에서 사용하는 `dog.png`는 실습 파일과 함께 들어 있다.

사전학습 모델은 첫 실행 때 ImageNet 가중치를 내려받는다. `06`의 체크포인트와 `07`의 학습 중 생성 이미지는 Git에 포함되지 않도록 설정했다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
