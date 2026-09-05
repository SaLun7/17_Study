# 13. Faster R-CNN과 YOLO 객체 검출

[← DAY4 목차](<README.md>) · [원본 노트북](<13_Faster R-CNN과 YOLO 객체 검출.ipynb>)

사전학습 Faster R-CNN으로 객체를 검출하고 PASCAL VOC 데이터로 YOLO 형태의 모델을 구성했다.

## 실습 내용

- TensorFlow Hub의 Faster R-CNN ResNet50 모델과 COCO 라벨맵을 불러왔다.
- 예제 사진에서 객체의 위치와 클래스, 신뢰도를 표시했다.
- PASCAL VOC 이미지와 XML 어노테이션을 내려받아 학습용 배열로 만들었다.
- VGG16 특징 추출부를 이용한 YOLO 형태의 모델과 다중 손실 함수를 구성했다.
- 예측 박스를 원본 이미지 좌표로 바꿔 표시하는 과정을 작성했다.

## 실행 메모

PASCAL VOC 압축 파일과 학습 데이터, `yolo.h5`는 용량이 커서 저장소에 포함하지 않는다. 객체 검출 API를 불러오는 셀은 컴퓨터 비전 폴더의 `models` 서브모듈을 사용한다.

VOC 데이터는 DAY4의 `data` 폴더에 내려받고 이후 학습 셀도 같은 위치를 읽는다. 마지막 검출 셀은 DAY1에 있는 `like_lenna.png`를 사용하므로 이미지를 따로 복사할 필요는 없다.
