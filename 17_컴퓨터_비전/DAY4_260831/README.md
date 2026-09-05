# DAY4 학습노트

[← 상위 목차](<../README.md>)

Transformer 기반 이미지 분류와 Faster R-CNN, YOLO 객체 검출을 실습한 날.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 12 | Swin Transformer CIFAR-10 분류 | [학습노트](<12_Swin Transformer CIFAR-10 분류.md>) | [Notebook](<12_Swin Transformer CIFAR-10 분류.ipynb>) |
| 13 | Faster R-CNN과 YOLO 객체 검출 | [학습노트](<13_Faster R-CNN과 YOLO 객체 검출.md>) | [Notebook](<13_Faster R-CNN과 YOLO 객체 검출.ipynb>) |
| 14 | Darknet YOLOv3 실행 | [학습노트](<14_Darknet YOLOv3 실행.md>) | [Notebook](<14_Darknet YOLOv3 실행.ipynb>) |

`12`의 CIFAR-10과 사전학습 가중치, `13`의 예제 이미지와 PASCAL VOC 데이터는 실행 중 내려받을 수 있다. 대용량 데이터와 가중치는 Git에서 제외한다.

`13`은 컴퓨터 비전 폴더의 `models` 서브모듈을 사용한다. VOC 데이터와 학습 결과는 DAY4의 `data` 폴더에 저장하고, 마지막 검출 셀은 DAY1의 `like_lenna.png`를 바로 불러온다.

`14`는 Git, CMake, Visual Studio C++ 개발 도구가 설치된 Windows 환경을 기준으로 한다. AlexeyAB Darknet 소스와 가중치, 검출 결과는 DAY4의 `darknet-windows` 폴더에 모이며 Git에서는 제외한다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
