# DAY3 실습

- `05.ipynb`: CNN·ResNet 기초 실습 (CIFAR-10)
- `pro1.ipynb`: 안전모 이미지 분류 및 전이학습
- `pro2.ipynb`: 흉부 X-ray 이미지 분류 실습

## 실행 준비

프로젝트 공용 `.venv` 커널을 선택하고, 작업 폴더를 `DAY3_260903`으로 두어 각 노트북을 위에서부터 실행합니다.

데이터셋과 학습된 모델은 Git에 포함하지 않습니다. 데이터는 별도로 준비해 다음 위치에 배치합니다.

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

`pro1.ipynb`는 `helmet`을 직접 읽으므로 별도의 `images` 폴더 연결은 필요하지 않습니다.
`05.ipynb`의 CIFAR-10과 전이학습용 사전학습 가중치는 최초 실행 시 다운로드될 수 있습니다.
체크포인트를 읽는 평가 셀은 해당 학습 셀을 실행해 `.pt` 파일을 생성한 뒤 실행합니다.
기존 확장자 없는 `best_transfer_model`을 사용하는 경우 새 학습 셀을 실행해 `best_transfer_model.pt`를 생성합니다.

노트북에 저장된 출력은 이전 실행 결과입니다. 경로·학습률 조절 수정 후 결과는 재실행해서 확인합니다.
