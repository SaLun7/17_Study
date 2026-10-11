# DAY4 StoryBot 데이터와 결과

[← DAY4 목차](<../README.md>)

`tiny_stories_train.txt`와 `tiny_stories_valid.txt`를 여기에 준비한다. DAY4에서 생성하는 토큰 바이너리, BPE 규칙, 사전학습·DPO 모델도 이 폴더에 저장한다. DAY3의 결과를 덮어쓰지 않도록 저장 위치를 구분했다.

모델·토크나이저·생성 함수는 [DAY3 storybot](<../../DAY3_260929/storybot/>) 모듈을 공유한다. DPO 데이터는 그 폴더의 `tiny_stories_dpo.json`을 읽는다.

[학습노트](<../08_StoryBot DPO와 생성 평가.md>)에서 생성 평가와 필요한 설정을 확인한다.
