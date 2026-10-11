# CodeBot·StoryBot 학습 저장소

[← 저장소 목차](<../README.md>)

BPE와 attention을 직접 구현하고 작은 언어 모델의 사전학습, SFT, GRPO·DPO를 실습했다. DAY3에는 StoryBot 웹서비스가 있고 DAY4에는 WebBot 확장 예제도 포함돼 있다.

## 과정 목차

| DAY | 주요 주제 | 학습노트 |
|---|---|---|
| DAY1 | 문자·바이트·BPE와 Multi-Head Attention | [DAY1 열기](<DAY1_260923/README.md>) |
| DAY2 | CodeBot 토크나이저, 사전학습과 SFT | [DAY2 열기](<DAY2_260928/README.md>) |
| DAY3 | CodeBot GRPO, StoryBot 사전학습과 웹서비스 | [DAY3 열기](<DAY3_260929/README.md>) |
| DAY4 | StoryBot DPO·생성 평가와 WebBot 분산 학습 | [DAY4 열기](<DAY4_260930/README.md>) |

## 실행 환경

과정 폴더에서 [setup_venv.ps1](<setup_venv.ps1>)로 환경을 준비하고 `Python (CodeBot StoryBot CUDA)` 커널을 선택한다. 스크립트는 Python 3.12를 기준으로 작성돼 있다.

```powershell
.\setup_venv.ps1 -Python 'C:\path\to\python.exe'
.\.venv\Scripts\python.exe verify_cuda.py
```

Python 경로는 실제 설치 위치에 맞춘다. `requirements.txt`는 기본 패키지 조건, `requirements-cuda.txt`는 GPU 패키지, `requirements-notebook.txt`는 노트북 도구, `requirements-lock.txt`는 이전 환경의 버전 기록이다.

노트북은 각 DAY 폴더에서 실행하도록 첫 셀에서 위치를 맞춘다. DAY2·3의 CodeBot 코드와 자료는 각각의 `CodeBot/`에 유지했다. DAY4는 DAY3 StoryBot 모듈을 공유하고 학습 결과는 DAY4에 따로 저장한다. `new_day.py`는 새 날짜의 빈 노트북을 만드는 보조 스크립트다.

## 데이터와 모델

CodeBot의 원본 텍스트·SFT JSON과 토크나이저 규칙은 포함돼 있다. TinyStories·OpenWebText의 큰 텍스트 파일은 별도 준비가 필요하다. 필요한 위치는 각 DAY 목차에서 확인한다. DAY4의 외부 모델 평가 셀은 API 키와 사용 비용이 필요하다.

DAY2의 `model_pretrain.pt`, `model_sft.pt`, `tiny_codes.bin`은 이미 Git에 등록된 파일이라 ignore 설정만으로 제외되지 않는다. 현재 파일과 기록은 유지했다. 앞으로 생성하는 체크포인트와 바이너리는 ignore 대상이다.

## 웹서비스

[StoryBot 웹서비스](<DAY3_260929/storybot/web/README.md>)에서 실행 방법을 확인한다. 웹 코드가 포함돼 있어도 모델 가중치는 따로 준비해야 한다.

## 문서 활용법

- `.ipynb`: 실행용 노트북
- 동명 `.md`: 개념, 실습 흐름, 저장된 결과와 다시 볼 내용을 정리한 학습노트
- DAY별 `README.md`: 실습 순서와 필요한 파일 안내

학습노트의 수치는 노트북에 저장된 이전 실행 기록을 기준으로 적었다. 정리 과정에서 장시간 학습이나 외부 API 평가는 다시 실행하지 않았다.
