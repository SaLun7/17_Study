# 아파트 실거래가 조회

[← 저장소 목차](<../README.md>)

국토교통부 아파트 매매 실거래가 API를 호출하고, 조회 결과를 Flask 화면에 보여 주는 작은 실습이다.

## 실행 준비

Python 3.14 이상과 공공데이터포털의 해당 API 활용 신청이 필요하다. 이 폴더에서 의존성을 설치한 뒤 `.env`에 `SERVICE_KEY`를 설정한다. `.env`와 실제 키는 Git에 올리지 않는다.

```powershell
uv sync
```

`uv`를 사용하지 않는다면 `pyproject.toml`의 Flask, requests, python-dotenv를 현재 가상환경에 설치하면 된다.

## 실행과 확인

```powershell
uv run python app.py
```

브라우저에서 `/`를 열고 법정동 코드(`LAWD_CD`)와 계약 연월(`DEAL_YMD`, 예: `202606`)을 입력한다. `/search`가 두 값을 받아 `scrapper.py`의 `fetch_apt_trade`를 호출하고, API의 XML 응답을 표에 전달한다. `main.py`는 현재 인사말만 출력하는 초기 파일이며 웹 앱의 시작점은 `app.py`다.

## 파일 위치

- `app.py`: Flask 화면과 조회 경로
- `scrapper.py`: 실거래가 API 요청과 XML 파싱
- `templates/`: 입력 화면과 결과 화면
- `pyproject.toml`, `uv.lock`: 실행 환경 기록

API 키가 없거나 공공 API가 응답하지 않으면 검색 결과를 확인할 수 없다. 실제 거래 자료를 저장소에 포함한 프로젝트는 아니다.
