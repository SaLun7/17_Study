# WebBot 모듈과 데이터

[← DAY4 목차](<../README.md>)

`model.py`는 RoPE·GQA·RMSNorm·SwiGLU를 사용하는 GPT 구조이고 `utils.py`는 장치 선택과 토큰 생성을 담당한다. 모델 코드는 기존 DAY4 파일을 그대로 옮겼다.

`owt_train.txt`와 `owt_valid.txt`는 여기에 별도로 준비한다. `merge_rules.pkl`, 토큰 `.bin`, 모델 `.pt`는 노트북 실행 중 만들어지는 파일이다. 데이터는 저장소에 포함돼 있지 않다.

[학습노트](<../09_WebBot BPE와 분산 사전학습.md>)에서 저장된 실행 상태와 분산 학습 전 확인할 내용을 볼 수 있다.
