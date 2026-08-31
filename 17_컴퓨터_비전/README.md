# 컴퓨터 비전 학습 저장소

[← 저장소 목차](<../README.md>)

OpenCV, TensorFlow와 이미지 모델 실습을 DAY별로 모아 두었다. `.ipynb`는 실행용이고, 같은 이름의 `.md`는 개념과 결과를 빠르게 다시 볼 때 사용한다.

## 로컬 가상환경

이 저장소의 TensorFlow 2.15 환경은 **Python 3.10**을 사용한다. Windows PowerShell에서 다음 명령을 실행하면 프로젝트 루트의 `.venv`를 만들고, 패키지를 설치하고, Jupyter 커널을 등록한다.

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\setup_venv.ps1
```

이후 환경을 활성화하고 JupyterLab을 실행한다.

```powershell
.\.venv\Scripts\Activate.ps1
jupyter lab
```

노트북에서는 커널 **Python (컴퓨터 비전)** 을 선택한다. 환경을 새로 만들려면 `.\setup_venv.ps1 -Recreate`를 사용한다. `dlib`, PyTorch, SAM 등 선택 실습용 대형 패키지까지 모두 설치하려면 `.\setup_venv.ps1 -Full`을 사용한다.

## 과정 목차

| DAY | 주요 주제 | 학습노트 |
|---|---|---|
| DAY1 | OpenCV 기본 변환, TensorFlow 영상 표현과 노이즈 처리 | [DAY1 열기](<DAY1_260826/README.md>) |
| DAY2 | 주파수 변환과 에지 검출, 신경망, GAN, CIFAR-10 분류 | [DAY2 열기](<DAY2_260827/README.md>) |
| DAY3 | CNN 비교, VAE, GoogLeNet, 사전학습 모델, Vision Transformer | [DAY3 열기](<DAY3_260828/README.md>) |

## 문서 활용법

- `.ipynb`: 실행 가능한 원본 실습
- 동명 `.md`: 설명 중심 학습노트
- DAY별 `README.md`: 해당 날짜의 목차와 학습 순서
