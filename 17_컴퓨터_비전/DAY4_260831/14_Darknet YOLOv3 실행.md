# 14. Darknet YOLOv3 실행

[← DAY4 목차](<README.md>) · [원본 노트북](<14_Darknet YOLOv3 실행.ipynb>)

Windows에서 Darknet을 빌드하고 YOLOv3 가중치로 예제 이미지를 검출하는 과정을 정리한 노트북이다.

## 실습 내용

- Windows 빌드를 지원하는 AlexeyAB Darknet 저장소를 내려받는다.
- CMake와 Visual Studio 빌드 도구로 `darknet.exe`를 만든다.
- YOLOv3 가중치를 내려받아 기본 `dog.jpg` 예제에 적용한다.
- 생성된 `predictions.jpg`를 노트북에서 확인한다.

## 실행 결과

Darknet 소스와 가중치, `predictions.jpg`는 DAY4의 `darknet-windows` 폴더에 저장하며 이 폴더는 Git에서 제외한다.

노트북에 남아 있는 이전 출력에서는 CMake와 `darknet.exe`를 찾지 못해 검출이 끝까지 실행되지 않았다. 경로는 더 이상 `C:\\dev`를 사용하지 않도록 수정했으며, 필요한 개발 도구를 설치한 뒤 빌드 셀부터 다시 실행하면 된다.
