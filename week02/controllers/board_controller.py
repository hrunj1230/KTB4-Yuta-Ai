from fastapi import HTTPException
from models import board_model
from sqlalchemy.orm import Session

#게시판 목록 조회
def get_board_list(db: Session):
    boards = db.query(board_model.Board).all()
    if not boards:
        raise HTTPException(status_code=404, detail="no_board_found")
    return [board.to_dict() for board in boards]

#게시판 게시글 쓰기
def add_new_board(db: Session,data: dict):
    if not data or "title" not in data or "content" not in data:
        raise HTTPException(status_code=400, detail="title_and_content_required")
    new_board = board_model.Board(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"]
    )
    db.add(new_board)
    db.commit()
    db.refresh(new_board)

    return new_board.to_dict()
#게시판 게시글 삭제
def del_board(db:Session, board_id: int):
    board = db.query(board_model.Board).filter(
        board_model.Board.id == board_id
    ).first()
    if not board:
        raise HTTPException(status_code=404, detail="board_not_found")
    db.delete(board)
    db.commit()
    return {"message":"delete","id": board_id}