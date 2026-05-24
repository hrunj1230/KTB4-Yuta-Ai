# Week02 - FastAPI 게시판 프로젝트

FastAPI를 사용한 로그인 및 게시판 CRUD 프로젝트

## 기술 스택

- Python 3.14.5
- FastAPI - 웹 프레임워크
- Uvicorn - ASGI 서버
- SQLAlchemy - ORM (DB 연결)
- Jinja2 - HTML 템플릿 엔진
- SQLite - 데이터베이스

## 프로젝트 구조

```
week02/
├── main.py                 # FastAPI 앱 진입점
├── db/
│   └── database.py         # DB 연결 설정
├── routers/                # URL 라우팅
│   ├── user_router.py
│   ├── board_router.py
│   └── page_router.py
├── controllers/            # 비즈니스 로직
│   ├── user_controller.py
│   └── board_controller.py
├── models/                 # DB 테이블 정의
│   ├── user_model.py
│   └── board_model.py
├── schemas/                # Pydantic 요청/응답 모델
│   ├── user_schema.py
│   └── board_schema.py
├── templates/              # HTML 템플릿
├── static/                 # CSS 등 정적 파일
└── seed.py                 # 테스트 데이터 삽입
```

## 설치 및 실행

### 1. 프로젝트 초기화

```bash
uv init --python 3.14.5
```

### 2. 패키지 설치

```bash
uv add fastapi
uv add uvicorn
uv add sqlalchemy
uv add jinja2
```

### 3. 서버 실행

```bash
uv run python -m uvicorn main:app --reload
```

### 4. 테스트 데이터 삽입 (선택)

```bash
uv run python seed.py
```

## API 목록

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/` | 로그인 페이지로 리다이렉트 |
| GET | `/login` | 로그인 페이지 |
| GET | `/board` | 게시판 페이지 |
| GET | `/detail/{post_id}` | 게시글 상세 페이지 |
| GET | `/user/` | 전체 사용자 목록 조회 |
| POST | `/user/login` | 로그인 |
| GET | `/board/list` | 게시글 목록 조회 |

