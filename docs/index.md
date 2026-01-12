# 문서 개요
Baro-Protect에 대한 통합 문서

# 이 프로젝트는 무엇인가?
Baro-Protect의 소프트웨어에 대한 통합 모노레포지토리

# 프로젝트 개요
## 사용 기술 스택
* Mobile Client : react-native android application
* Server For Mobile Client : Python FastAPI
* Database : Postgres
* 반납함 Controller : (미정) Python worker + Native C Applicatoin 

# 문서 구조 
index.md - 프로젝트 개요
documentation.md - 문서화 방법
(추가예정)/controller - 반납함 컨트롤러 관련 문서
(추가예정)/mobile - 모바일 클라이언트 관련 문서
(추가예정)/server - 서버 관련 문서

<br><br>
---
<br><br>


# Python Server 개발환경 설정
## 설치 필요한 패키지
* python 설치
[python 설치](https://www.python.org/downloads/)

3.13>= 권장

path 설정 필수

* poetry 설치

[poetry 설치](https://python-poetry.org/docs/)

pipx로 설치 권장

* docker 설치 
  
[Windows Docker Desktop 설치](https://docs.docker.com/desktop/setup/install/windows-install/)



## 환경변수 설정
server/.env.local 에 환경변수를 세팅한다.
```
API_DEBUG=True
```


<br><br>
---
<br><br>


# python 개발 서버
## 개발환경 Docker 실행

postgres 등 필요한 서비스를 docker로 로컬 환경에 띄운다.

위치 : root
```
docker-compose -f docker-compose.dev.yml up
```

```bash
docker-compose -f docker-compose.dev.yml down
```


## python 서버 수동 실행

위치 : /server

* 의존성 업데이트
```bash
poetry install 
```

* 서버 실행
```bash
poetry run uvicorn server.api.main:app --reload
```

