# 딥러닝 학습 저장소

[← 저장소 목차](<../README.md>)

PyTorch의 신경망 기초에서 이미지 분류·세그멘테이션, 순환 신경망, 자연어 처리와 강화학습까지 실습한 자료다.

## 실행 환경

모든 DAY 폴더는 프로젝트 루트의 공용 `.venv`를 사용한다. 새 날짜 폴더를 만들거나 특정 날짜의 JupyterLab을 열 때는 아래 스크립트를 사용한다.

```powershell
.\setup_day.ps1 -Day DAY2_260902
```

```powershell
.\start_jupyter.ps1 -Day DAY2_260902
```

노트북에서는 `Python (deep-learning)` 커널을 선택한다.

## 과정 목차

| DAY | 주요 주제 | 학습노트 |
|---|---|---|
| DAY1 | PyTorch 환경, 신경망 기초와 MNIST MLP | [DAY1 열기](<DAY1_260901/README.md>) |
| DAY2 | 역전파, 활성화 함수, CNN과 CIFAR-10 | [DAY2 열기](<DAY2_260902/README.md>) |
| DAY3 | ResNet, 안전모 분류, 흉부 X-ray 폐렴 분류 | [DAY3 열기](<DAY3_260903/README.md>) |
| DAY4 | Cityscapes U-Net 세그멘테이션 | [DAY4 열기](<DAY4_260904/README.md>) |
| DAY5 | RNN·LSTM, 시계열, attention과 전이학습 | [DAY5 열기](<DAY5_260909/README.md>) |
| DAY6 | 객체 검출, U-Net·멀티태스크, 규칙 기반 감정 분석 | [DAY6 열기](<DAY6_260911/README.md>) |
| DAY7 | LSTM 감정 분류, Seq2Seq와 CartPole 강화학습 | [DAY7 열기](<DAY7_260914/README.md>) |

## 데이터 파일

DAY3의 `helmet`, `chest_xray`와 DAY4의 `cityscapes` 데이터는 용량이 커서 Git에서 제외했다. 각 DAY README에 적힌 위치에 별도로 준비해야 한다. CIFAR-10과 MNIST는 처음 실행할 때 자동으로 내려받는다.

DAY5의 ResNet 전이학습에는 `example.jpg`를 별도로 준비한다. DAY6·7은 임의 데이터와 구조 예제가 많으며, 자세한 실행 상태는 각 학습노트에 적었다.

## 문서 활용법

- `.ipynb`: 실행 가능한 원본 실습
- 동명 `.md`: 핵심 개념, 실습 흐름, 실행 결과와 복습 포인트를 정리한 학습노트
- DAY별 `README.md`: 해당 날짜의 목차와 학습 순서
