# seed.py
from db.database import SessionLocal
from models.board_model import Board

db = SessionLocal()

boards = [
    Board(title="첫 번째 게시글", content="안녕하세요 첫 글입니다", user_id=1),
    Board(title="두 번째 게시글", content="FastAPI 재밌다", user_id=2),
    Board(title="세 번째 게시글", content="SQLAlchemy 어렵다", user_id=1),
    Board(title="네 번째 게시글", content="Pydantic 이해했다", user_id=3),
]

db.add_all(boards)
db.commit()
db.close()

print("데이터 입력 완료")