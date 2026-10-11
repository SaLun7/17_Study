# RAG·생성형 AI 학습 저장소

[← 저장소 목차](<../README.md>)

문장 임베딩에서 시작해 감정 분류, 로컬 대화 모델, 문서 검색 기반 답변과 이미지 생성으로 이어지는 실습이다. 마지막 DAY는 마스코트 LoRA와 Flask 서버까지 포함한다.

## 과정 목차

| DAY | 주요 주제 | 학습노트 |
|---|---|---|
| DAY1 | 문장 임베딩과 사전학습 이미지 분류 | [DAY1 열기](<DAY1_261002/README.md>) |
| DAY2 | 미세조정·prompt tuning, Ollama·Chroma RAG와 이미지 생성 | [DAY2 열기](<DAY2_261006/README.md>) |
| DAY3 | 이미지 편집, 마스코트 LoRA와 모아 AI 서버 | [DAY3 열기](<DAY3_261004/README.md>) |

## 실행 환경

[requirements.txt](<requirements.txt>)는 기본 패키지, [requirements-gpu.txt](<requirements-gpu.txt>)는 Windows·NVIDIA용 환경 기록이다. 해당 환경을 노트북 커널로 선택한다. DAY2 이후의 대화 실습에는 별도로 설치한 Ollama와 `gemma3:4b`가 필요하다.

첫 셀이 과정 루트와 실행 DAY를 찾는다. 이미지와 지식 문서는 공용으로 읽고 모델·Chroma DB·생성 이미지는 DAY별 `work/`에 저장한다. 노트북이 설치나 모델 다운로드, 학습, 서버 실행을 포함하므로 처음부터 무조건 전체 실행하기보다 필요한 구간부터 확인한다.

## 공용 자료

| 위치 | 내용 | 준비 상태 |
|---|---|---|
| `assets/puppy.jpg` | 분류·이미지 변환용 강아지 사진 | 포함 |
| `assets/puppymask.png` | 부분 수정 영역 마스크 | 포함 |
| `assets/mascot/` | 마스코트 이미지와 캡션 JSONL | 포함 |
| `data/knowledge/` | 동아리 소개·과정·장비·행사·FAQ 텍스트 | 포함 |
| `DAY*/work/` | 실행 중 생성하는 모델·색인·그림 | Git 제외 |

기존 `assets/assets`와 `data/data`의 이중 폴더를 한 단계로 정리했다. DAY3의 날짜 표기는 원래 이름인 `261004`를 유지했으며 학습 순서는 DAY 번호 기준이다.

## 문서 활용법

- `.ipynb`: 실행용 노트북
- 동명 `.md`: 핵심 개념, 실습 흐름, 실행 결과, 필요한 파일과 다시 볼 내용을 정리한 학습노트
- DAY별 `README.md`: 실습 순서와 필요한 파일 안내

학습노트의 수치는 노트북에 저장된 이전 실행 기록을 기준으로 적었다. 정리 과정에서 장시간 학습이나 외부 API 평가는 다시 실행하지 않았다.
