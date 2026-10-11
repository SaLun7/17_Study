# DAY3 학습노트

[← 상위 목차](<../README.md>)

CodeBot 학습을 GRPO까지 확장하고 StoryBot의 사전학습과 웹서비스 구성을 살펴봤다.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 05 | CodeBot BPE 토크나이저 학습 | [학습노트](<05_CodeBot BPE 토크나이저 학습.md>) | [Notebook](<05_CodeBot BPE 토크나이저 학습.ipynb>) |
| 06 | CodeBot SFT와 GRPO | [학습노트](<06_CodeBot SFT와 GRPO.md>) | [Notebook](<06_CodeBot SFT와 GRPO.ipynb>) |
| 07 | StoryBot 사전학습 | [학습노트](<07_StoryBot 사전학습.md>) | [Notebook](<07_StoryBot 사전학습.ipynb>) |

## 실행 메모

CodeBot 가중치는 앞 학습 단계에서 만든다. StoryBot에는 `storybot/tiny_stories_train.txt`와 `tiny_stories_valid.txt`를 별도로 준비한다. [StoryBot 웹서비스](<storybot/web/README.md>)와 [CodeBot 웹 요구사항](<CodeBot/WEB_SERVICE_REQUIREMENTS.md>)도 이 폴더에 있다. GRPO 저장 기록은 초반 진행까지만 남아 있다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
