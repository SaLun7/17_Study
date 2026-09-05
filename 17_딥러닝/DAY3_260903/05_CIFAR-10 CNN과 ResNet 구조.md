# 05. CIFAR-10 CNN과 ResNet 구조

[← DAY3 목차](<README.md>) · [원본 노트북](<05_CIFAR-10 CNN과 ResNet 구조.ipynb>)

CIFAR-10용 CNN을 구성하고 잔차 연결을 이용한 ResNet 구조까지 확장했다.

## 실습 내용

- 합성곱, 패딩, 스트라이드와 특징맵 크기를 확인했다.
- 배치 정규화와 드롭아웃을 포함한 CIFAR-10 CNN을 만들었다.
- ResidualBlock에서 입력과 출력을 더하는 잔차 연결을 구현했다.
- BasicBlock을 쌓아 ResNet 형태의 모델을 구성했다.
- StepLR, ReduceLROnPlateau, CosineAnnealingLR과 가중치 초기화를 살펴봤다.

## 실행 결과

구성한 ResNet의 파라미터는 약 1,117만 개이고 임의 입력에 대해 10개 클래스 출력을 확인했다. 이 노트북은 구조 구현 중심이라 ResNet의 최종 분류 성능은 따로 평가하지 않았다.
