# 자연어 처리·컴퓨터 비전 학습 저장소

[← 저장소 목차](<../README.md>)

현재 자료는 PyTorch 기초와 자연어 처리 실습이 중심이다. 토큰화·임베딩에서 문장 분류, Transformer 번역과 사전학습 모델 활용으로 이어진다.

## 과정 목차

| DAY | 주요 주제 | 학습노트 |
|---|---|---|
| DAY1 | PyTorch 회귀·이진 분류와 모델 저장 | [DAY1 열기](<DAY1_260914/README.md>) |
| DAY2 | 텍스트 증강, 한국어 토큰화와 Skip-gram | [DAY2 열기](<DAY2_260915/README.md>) |
| DAY3 | Word2Vec·FastText, LSTM·TextCNN과 번역 준비 | [DAY3 열기](<DAY3_260916/README.md>) |
| DAY4 | Transformer 번역, BERT·KoELECTRA 분류와 BART·T5 요약 | [DAY4 열기](<DAY4_260917/README.md>) |

## 실행 환경

과정 폴더에서 Python 3.12로 다음 스크립트를 실행한다.

```powershell
.\setup_env.ps1
```

VS Code에서는 `Python (NLP-CV GPU ASCII)` 커널을 선택한다. 기본 가상환경은 한글 경로 문제를 피하기 위해 `$env:USERPROFILE\.venvs\nlp-cv`에 만든다. 다른 영문 경로를 사용하려면 `NLP_CV_VENV`를 지정한다. KoNLPy용 JDK는 영문 경로에 준비하고 `JAVA_HOME`을 맞춘다. 상세 설치 동작은 [setup_env.ps1](<setup_env.ps1>)과 패키지 목록을 참고한다.

각 노트북의 첫 셀에서 과정 루트를 찾아 작업 위치와 모듈 경로를 맞춘다. 따라서 공용 `data/`와 `models/`를 DAY마다 복사할 필요가 없다. 번역 실습의 `torchtext` 폴더와 `torchtext_compat.py`는 수업 환경 호환용 코드다.

## 데이터와 모델

`data/non_linear.csv`, `data/binary.csv`는 별도로 준비한다. NSMC·KorNLI·청원 말뭉치·Multi30k·뉴스 데이터와 사전학습 모델은 실행 중 내려받는다. `models/`의 BPE·WordPiece·Word2Vec 파일은 포함돼 있지만 BERT·BART·KoELECTRA 분류·요약 체크포인트는 없다. DAY4 평가 셀을 실행하려면 학습 결과를 먼저 준비해야 한다.

## 문서 활용법

- `.ipynb`: 실행용 노트북
- 동명 `.md`: 핵심 개념, 실습 흐름, 실행 결과, 필요한 파일과 다시 볼 내용을 정리한 학습노트
- DAY별 `README.md`: 실습 순서와 필요한 파일 안내

학습노트의 수치는 노트북에 저장된 이전 실행 기록을 기준으로 적었다. 정리 과정에서 장시간 학습이나 외부 API 평가는 다시 실행하지 않았다.
