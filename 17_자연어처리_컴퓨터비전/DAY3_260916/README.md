# DAY3 학습노트

[← 상위 목차](<../README.md>)

단어 임베딩을 비교하고 LSTM·TextCNN으로 문장을 분류했다. 마지막에는 번역 모델에 넣을 데이터를 준비했다.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 05 | Word2Vec FastText와 순환 신경망 | [학습노트](<05_Word2Vec FastText와 순환 신경망.md>) | [Notebook](<05_Word2Vec FastText와 순환 신경망.ipynb>) |
| 06 | Word2Vec 임베딩 LSTM 감정 분류 | [학습노트](<06_Word2Vec 임베딩 LSTM 감정 분류.md>) | [Notebook](<06_Word2Vec 임베딩 LSTM 감정 분류.ipynb>) |
| 07 | TextCNN 감정 분류 | [학습노트](<07_TextCNN 감정 분류.md>) | [Notebook](<07_TextCNN 감정 분류.ipynb>) |
| 08 | 위치 인코딩과 번역 데이터 준비 | [학습노트](<08_위치 인코딩과 번역 데이터 준비.md>) | [Notebook](<08_위치 인코딩과 번역 데이터 준비.ipynb>) |

## 실행 메모

06·07번은 과정 공용 `models/word2vec.model`을 사용한다. 파일은 포함돼 있으며 05번에서 다시 만들 수 있다. 번역 데이터 준비에는 독일어·영어 spaCy 모델이 필요하다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
