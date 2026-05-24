from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from controllers import board_controller

router=APIRouter(prefix="/board")

#게시글 가져오기
@router.get("/list")
def get_list_board(db: Session = Depends(get_db)):
    return board_controller.get_board_list(db)

@router.post("/add")
def add_new_board(data: dict, db: Session =Depends(get_db)):
    return board_controller.add_new_board(db, data)

@router.delete("/del/{board_id}")
def del_board(board_id: int, db: Session =Depends(get_db)):
    return board_controller.del_board(db, board_id)