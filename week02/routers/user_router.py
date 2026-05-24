from fastapi import APIRouter
from controllers import user_controller

router = APIRouter(prefix="/user")

#전체 사용자 목록 조회
@router.get("/")
def get_users():
    return user_controller.get_users()
#로그인
@router.post("/login")    
def login(data : dict):
    return user_controller.login(data)