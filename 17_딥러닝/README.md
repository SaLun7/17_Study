# 딥러닝 실습 환경

모든 날짜별 노트북은 프로젝트 루트의 공용 `.venv`를 사용합니다. 따라서 DAY 폴더마다 패키지를 다시 설치할 필요가 없습니다.

새 날짜 폴더 만들기:

```powershell
.\setup_day.ps1 -Day DAY2_260902
```

특정 날짜의 JupyterLab 실행:

```powershell
.\start_jupyter.ps1 -Day DAY2_260902
```

노트북 커널은 `Python (deep-learning)`을 선택하세요.
