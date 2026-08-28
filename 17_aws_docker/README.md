# AWS·Docker 실습

FastAPI 백엔드와 Nginx를 Docker Compose로 실행하는 배포 실습.

## 구성

| 경로 | 내용 |
|---|---|
| `backend/` | FastAPI 애플리케이션과 Dockerfile |
| `nginx/` | Nginx 프록시 설정 |
| `docker-compose.yml` | 백엔드와 Nginx 실행 구성 |

실행 전에 프로젝트 루트에 필요한 환경변수를 담은 `.env` 파일이 있어야 한다.

```bash
docker compose up --build
```
