# 14. Darknet YOLOv3 실행

[← DAY4 목차](<README.md>) · [원본 노트북](<14_Darknet YOLOv3 실행.ipynb>)

Windows에서 Darknet을 직접 빌드하고 공개된 YOLOv3 가중치로 예제 이미지의 객체를 검출하는 과정을 담았다.

## Darknet과 YOLOv3

Darknet은 C와 CUDA로 작성된 신경망 프레임워크이고 YOLOv3의 원본 구현에 사용됐다. YOLO는 한 번의 순전파에서 여러 크기의 특징맵을 이용해 박스와 클래스 확률을 함께 예측한다. 후보 영역을 따로 분류하는 2단계 모델보다 빠른 검출을 목표로 한다.

원본 `pjreddie/darknet`은 Windows에서 바로 빌드하기 불편하므로 이 노트북에서는 CMake와 Visual Studio 빌드를 지원하는 `AlexeyAB/darknet` 포크를 사용한다.

## 실행 순서

1. DAY4 아래에 `darknet-windows` 폴더가 없으면 저장소를 내려받는다.
2. CMake가 Visual Studio용 빌드 파일을 만들고 Release 설정으로 `darknet.exe`를 컴파일한다.
3. 약 236MB인 YOLOv3 사전학습 가중치를 이어받기 옵션과 함께 내려받는다.
4. Darknet에 포함된 `dog.jpg`와 COCO 설정 파일을 이용해 검출을 실행한다.
5. 생성된 `predictions.jpg`를 노트북에서 표시한다.

`cfg/yolov3.cfg`에는 네트워크 구조가, `yolov3.weights`에는 학습된 가중치가 들어 있다. `data/dog.jpg`는 소스 저장소에 포함된 예제이므로 별도의 강아지 사진을 준비하지 않아도 된다.

## 파일 위치

기존의 고정 경로 `C:\dev`는 사용하지 않는다. 노트북이 저장소 최상위, 컴퓨터 비전 폴더 또는 DAY4 폴더에서 실행돼도 DAY4 위치를 찾아 `darknet-windows`를 사용하도록 수정했다. 소스, 빌드 결과, 가중치와 검출 이미지는 모두 이 폴더에 모이며 Git에서는 제외한다.

## 현재 실행 상태

노트북에 남아 있는 이전 출력에서는 CMake와 `darknet.exe`를 찾지 못해 검출이 끝까지 완료되지 않았다. 실제 성공 결과로 보지 않고 환경 준비가 덜 된 기록으로 남겨 둔다. Git for Windows, CMake와 Visual Studio의 ‘C++를 사용한 데스크톱 개발’ 워크로드를 설치한 뒤 빌드 셀부터 다시 실행해야 한다.

## 다시 볼 것

- `cmake`와 C++ 컴파일러가 터미널에서 인식되는지 먼저 확인한다.
- GPU 빌드는 CUDA와 cuDNN 버전 호환성도 확인한다.
- 빌드가 성공한 뒤 `darknet.exe`와 `predictions.jpg`가 실제로 생성됐는지 확인한다.
