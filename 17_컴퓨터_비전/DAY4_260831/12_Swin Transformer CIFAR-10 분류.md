# 12. Swin Transformer CIFAR-10 분류

[← DAY4 목차](<README.md>) · [원본 노트북](<12_Swin Transformer CIFAR-10 분류.ipynb>)

Swin Transformer Tiny 사전학습 모델을 이용해 CIFAR-10 이미지를 분류했다.

## 실습 내용

- CIFAR-10 데이터를 불러오고 Swin 전용 전처리를 적용했다.
- 사전학습 Swin Transformer의 특징 추출부에 분류층을 연결했다.
- Top-1과 Top-5 정확도를 함께 기록하고 학습 곡선을 확인했다.

## 실행 결과

10회 학습 후 테스트 정확도는 약 80.00%, Top-5 정확도는 약 98.84%였다. 노트북의 `num_classes`는 100으로 작성돼 있으므로 CIFAR-10의 10개 클래스와 맞추려면 재실행 전에 이 값을 확인해야 한다.
