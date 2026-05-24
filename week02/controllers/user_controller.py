from fastapi import HTTPException
from models import user_model

#사용자 목록 조회
def get_users():
    users = user_model.get_users()
    if not users:
        raise HTTPException(status_code=404, detail="no_users_found")
    return users

def login(data: dict):
    if not data or "email" not in data:
        raise HTTPException(status_code=400, detail="email_required")
    user = user_model.get_user_by_email(data["email"])
    if not user:
        raise HTTPException(status_code=401 ,detail="user_not_found")
    return user