# DAY4 학습노트

[← 상위 목차](<../README.md>)

StoryBot의 선호도 학습과 생성 결과를 확인하고 WebBot 분산 학습 예제를 살펴봤다.

| 번호 | 주제 | 설명 문서 | 원본 노트북 |
|---:|---|---|---|
| 08 | StoryBot DPO와 생성 평가 | [학습노트](<08_StoryBot DPO와 생성 평가.md>) | [Notebook](<08_StoryBot DPO와 생성 평가.ipynb>) |
| 09 | WebBot BPE와 분산 사전학습 | [학습노트](<09_WebBot BPE와 분산 사전학습.md>) | [Notebook](<09_WebBot BPE와 분산 사전학습.ipynb>) |

## 실행 메모

StoryBot 원본 데이터는 `storybot/tiny_stories_train.txt`, `storybot/tiny_stories_valid.txt`, WebBot 원본 데이터는 `webbot/owt_train.txt`, `webbot/owt_valid.txt`에 준비한다. StoryBot 모듈과 DPO JSON은 DAY3 자료를 참조한다. WebBot 모듈은 이 DAY의 `webbot/`에 있다. API 평가와 W&B 기록은 로컬 학습과 별도로 설정을 확인한다.

노트가 필요하면 `.md`를 보고, 직접 실행할 때는 `.ipynb`를 연다.
