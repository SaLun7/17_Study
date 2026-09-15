# 자연어 처리 · 컴퓨터 비전 실습 환경

## 폴더 규칙

수업일별로 `DAY1_YYMMDD`, `DAY2_YYMMDD`, `DAY3_YYMMDD` 형식의 폴더를 추가하고,
각 폴더 안에 `01.ipynb`, `02.ipynb`처럼 노트북을 둡니다.

## 환경 설치

Python 3.12를 설치한 다음 PowerShell에서 프로젝트 폴더로 이동해 아래 명령을 한 번 실행합니다.

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\setup_env.ps1
```

설치 후 VS Code/Jupyter에서 커널 **Python (NLP-CV GPU ASCII)** 를 선택합니다.
KoNLPy의 Windows 한글 경로 문제를 피하기 위해 가상환경은 기본적으로
`$env:USERPROFILE\.venvs\nlp-cv`에 생성됩니다. 다른 위치를 쓰려면 실행 전에
`NLP_CV_VENV` 환경변수로 영문 경로를 지정합니다.
Hugging Face와 PyTorch가 내려받는 모델은 프로젝트의 `.cache` 아래에 저장됩니다.

## 다시 확인하기

```powershell
& "$env:USERPROFILE\.venvs\nlp-cv\Scripts\python.exe" .\verify_gpu.py
```

`CUDA available: True`와 GPU 이름이 출력되면 준비가 끝난 것입니다.

> PyTorch 공식 CUDA 패키지는 실행에 필요한 CUDA 런타임을 포함하므로 일반적인
> 노트북 학습에는 별도의 CUDA Toolkit(`nvcc`) 설치가 필요하지 않습니다.

## KoNLPy / Java

KoNLPy 형태소 분석기에는 JDK 17이 필요합니다. 한글 경로로 인한 JVM 로딩 문제를
피하려면 JDK를 `C:\Java\jdk-17`처럼 영문으로만 된 경로에 설치하고, 환경 설치 전에
`JAVA_HOME`과 `PATH`를 설정합니다.

```powershell
$env:JAVA_HOME = "C:\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
.\setup_env.ps1
```

현재 PC의 실제 JDK 설치 경로에 맞게 `JAVA_HOME` 값만 변경하면 됩니다.
