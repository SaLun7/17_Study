# DAY4 학습노트

[← 상위 목차](<../README.md>)

Transformer 번역, BERT·KoELECTRA 분류와 BART·T5 요약을 다룬 실습이다.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 09 | Transformer 독일어 영어 번역 | [학습노트](<09_Transformer 독일어 영어 번역.md>) | [Notebook](<09_Transformer 독일어 영어 번역.ipynb>) |
| 10 | GPT-2 생성과 BERT BART 활용 | [학습노트](<10_GPT-2 생성과 BERT BART 활용.md>) | [Notebook](<10_GPT-2 생성과 BERT BART 활용.ipynb>) |
| 11 | KoELECTRA 영화 리뷰 감정 분류 | [학습노트](<11_KoELECTRA 영화 리뷰 감정 분류.md>) | [Notebook](<11_KoELECTRA 영화 리뷰 감정 분류.ipynb>) |
| 12 | T5 뉴스 요약 | [학습노트](<12_T5 뉴스 요약.md>) | [Notebook](<12_T5 뉴스 요약.ipynb>) |

## 실행 메모

BERT·BART·KoELECTRA 평가 셀에서 읽는 `.pt`는 저장소에 없다. 학습 루프가 주석 처리된 부분을 확인하고 필요한 가중치를 준비한다. T5 앞부분의 함수 소스 확인 셀은 새 커널에서 정의 순서에 주의한다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
