# StoryBot 웹서비스

기존 `storybot/model_pretrain.pt`, `merge_rules.pkl`, `model.py`, `tokenizer.py`, `utils.py`를 사용하는 React + FastAPI 웹서비스입니다. 요구사항은 [스토리봇 PRD](../prd.md)에 있습니다.

## 실행

Python 3.12와 Node.js 20.19 이상이 필요합니다. 아래 명령은 `storybot/web` 폴더에서 실행합니다.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

개발 중에는 두 터미널을 사용합니다.

```powershell
$env:STORYBOT_ALLOWED_ORIGINS = 'http://127.0.0.1:5173,http://localhost:5173'
.venv\Scripts\python.exe -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

```powershell
cd frontend
npm install
npm run dev
```

브라우저에서 `http://127.0.0.1:5173`에 접속합니다. 모델 최초 로딩에는 시간이 걸릴 수 있습니다.

프론트엔드를 빌드하여 FastAPI에서 같은 주소로 제공하려면 `frontend` 폴더에서 `npm run build`를 실행한 뒤 FastAPI를 다시 시작합니다. 운영 환경에서는 HTTPS를 사용하고 `STORYBOT_COOKIE_SECURE=1`로 설정합니다.

## 데이터 및 인증

- SQLite 파일은 기본적으로 `web/data/storybot.sqlite3`에 만들어집니다. 다른 위치를 쓰려면 `STORYBOT_DB_PATH` 환경 변수를 지정합니다.
- 로그인 쿠키는 브라우저 세션 쿠키라 브라우저 종료 시 삭제됩니다. 서버의 세션 기록은 최대 30일 후 만료되며 로그아웃·비밀번호 변경·탈퇴 시 즉시 무효화됩니다.
- 비밀번호와 세션 토큰은 각각 해시로 저장합니다. 비공개 스토리와 수정·삭제 권한은 API에서 검사합니다.

## 검증

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.venv\Scripts\python.exe -m pytest -q tests
```
