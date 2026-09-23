# CodeBot / StoryBot 학습 환경

프로젝트 루트의 `.venv` 하나를 모든 DAY 폴더에서 공유합니다.

## 설치 환경

- Python 3.12.14
- PyTorch 2.11.0 + CUDA 12.8 (`cu128`)
- NumPy 1.26.4 (`requirements.txt`의 `<2.0.0` 조건)
- 기존 requirements 전체 및 JupyterLab / ipykernel

## 노트북 사용

VS Code에서 **이 프로젝트 폴더 전체**를 열고 노트북 오른쪽 위의 커널 선택에서
**Python (CodeBot StoryBot CUDA)** 또는 **.venv (Python 3.12)** 를 선택하세요.
목록에 없다면 Python 환경 선택에서 `.venv\Scripts\python.exe`를 지정하세요.
VS Code에는 Python 및 Jupyter 확장이 필요합니다.

JupyterLab은 프로젝트 루트에서 다음 명령으로 시작할 수 있습니다.

```powershell
.\.venv\Scripts\jupyter-lab.exe
```

현재 DAY1 노트북은 `DAY1_260923/01.ipynb`입니다.
새 날짜의 폴더와 GPU 확인 셀이 있는 노트북은 다음과 같이 만드세요.

```powershell
.\.venv\Scripts\python.exe new_day.py 2
.\.venv\Scripts\python.exe new_day.py 3
```

각각 `DAY2/01.ipynb`, `DAY3/01.ipynb`를 생성합니다.
이미 내용이 있는 노트북은 덮어쓰지 않습니다.
폴더 이름을 직접 정해서 만들고 같은 커널을 선택해도 됩니다.

## 가상환경 활성화 (선택)

프로젝트 루트의 PowerShell에서:

```powershell
.\.venv\Scripts\Activate.ps1
```

활성화 없이 위처럼 `.venv` 안의 실행 파일을 직접 사용해도 됩니다.

## GPU 확인

```powershell
.\.venv\Scripts\python.exe verify_cuda.py
.\.venv\Scripts\python.exe -m pip check
```

GPU 행렬 곱셈과 역전파, NumPy 연동, 필수 패키지 import를 확인합니다.
학습 코드에서는 모델과 데이터를 모두 GPU로 이동해야 합니다.

```python
import torch
device = torch.device('cuda')
model = model.to(device)
inputs = inputs.to(device)
```

## 재설치

Python 3.12를 준비한 뒤 다음 스크립트를 실행하세요.
Python이 PATH에 없다면 `-Python`에 python.exe의 전체 경로를 전달하세요.

```powershell
.\setup_venv.ps1 -Python 'C:\path\to\python.exe'
```

`requirements.txt`는 원본 패키지 조건을 유지합니다.
`requirements-notebook.txt`는 노트북 도구를 추가하며,
`requirements-cuda.txt`는 이 GPU용 PyTorch 빌드를 지정합니다.
`requirements-lock.txt`는 검증된 전체 설치 버전을 기록합니다.
동일 버전으로 복원하려면 새 가상환경에서:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name codebot-storybot --display-name 'Python (CodeBot StoryBot CUDA)'
```

커널은 프로젝트 가상환경 내부에 등록되어 있습니다.
가상환경은 생성할 때 사용한 기본 Python을 참조하므로 해당 Python 경로가
삭제되거나 변경되면 Python 3.12를 지정해 가상환경을 다시 만드세요.

PyTorch 설치 안내: https://docs.pytorch.org/get-started/locally/
