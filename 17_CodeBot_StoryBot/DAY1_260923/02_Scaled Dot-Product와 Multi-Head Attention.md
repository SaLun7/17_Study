# 02. Scaled Dot-Product와 Multi-Head Attention

[← DAY1 목차](<README.md>) · [원본 노트북](<02_Scaled Dot-Product와 Multi-Head Attention.ipynb>)

비슷한 항목을 가중 평균하는 soft dictionary 예제에서 출발해 attention 계산을 직접 구현했다.

## 핵심 개념

일반 사전은 키 하나와 정확히 일치하는 값을 찾지만, soft dictionary는 query와 여러 key의 유사도를 가중치로 바꿔 value를 합친다. 이를 행렬로 쓰면 Q와 K의 내적, softmax, V와의 곱으로 이어진다.

내적값의 규모는 차원에 따라 커질 수 있어 key 차원의 제곱근으로 나눈다. Multi-Head Attention은 Q·K·V를 여러 head로 나누어 계산하고 결과를 합쳐 원래 임베딩 차원으로 돌린다.

입력 `(배치, 길이, 임베딩 차원)`을 여러 head로 나누면 각 head의 attention 점수는 길이×길이 행렬이 된다. 한 행은 현재 query가 모든 key를 참고하는 비중이며 softmax는 key 방향에 적용한다. 마지막에는 head 결과를 다시 합치므로 입력과 출력 shape이 같아도 내부에는 토큰 간 정보 교환이 일어난다.

## 실습 흐름

영화 특성과 평점으로 가중 평균을 계산한 뒤 PyTorch 행렬 연산으로 바꿨다. 스케일링 전후 내적 분산을 비교하고, 학습 가능한 투영층과 여러 head를 둔 모듈에서 입력·출력 shape을 확인했다.

## 실행 결과

저장된 스케일링 예제의 분산은 약 9.90에서 0.99로 줄었다. Multi-Head Attention의 입력과 출력은 모두 `(2, 10, 512)`다. 여기서는 임의 입력의 계산 구조를 확인했으며 언어 모델의 학습 성능을 평가한 것은 아니다.

## 필요한 파일

입력은 코드에서 생성한다. 별도 데이터나 체크포인트는 필요 없다.

## 다시 볼 것

softmax를 적용하는 축과 transpose 후의 shape을 확인한다. 언어 생성 모델에 넣을 때는 미래 토큰을 가리는 causal mask도 필요하다.
