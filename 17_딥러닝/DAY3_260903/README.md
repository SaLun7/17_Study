# DAY3 학습노트

[← 상위 목차](<../README.md>)

CNN과 ResNet 구조를 살펴보고 안전모와 흉부 X-ray 이미지 분류를 실습한 날.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 05 | CIFAR-10 CNN과 ResNet 구조 | [학습노트](<05_CIFAR-10 CNN과 ResNet 구조.md>) | [Notebook](<05_CIFAR-10 CNN과 ResNet 구조.ipynb>) |
| 06 | 안전모 착용 분류와 전이학습 | [학습노트](<06_안전모 착용 분류와 전이학습.md>) | [Notebook](<06_안전모 착용 분류와 전이학습.ipynb>) |
| 07 | 흉부 X-ray 폐렴 분류 | [학습노트](<07_흉부 X-ray 폐렴 분류.md>) | [Notebook](<07_흉부 X-ray 폐렴 분류.ipynb>) |

## 실행 준비

데이터셋과 학습된 모델은 Git에 포함하지 않는다. 데이터는 별도로 준비해 다음 위치에 둔다.

```text
DAY3_260903/
├── helmet/
│   ├── images/
│   └── annotations/
└── chest_xray/
    ├── train/
    │   ├── NORMAL/
    │   └── PNEUMONIA/
    └── test/
        ├── NORMAL/
        └── PNEUMONIA/
```

`05`의 CIFAR-10과 전이학습용 사전학습 가중치는 처음 실행할 때 내려받는다. 체크포인트를 읽는 평가 셀은 학습 셀을 먼저 실행해 `.pt` 파일을 만든 뒤 실행한다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
