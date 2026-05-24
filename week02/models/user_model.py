_users = [
    {"id": 1, "name": "Alice", "email": "alice@test.com"},
    {"id": 2, "name": "Bob", "email": "bob@test.com"},
    {"id": 3, "name": "Carol", "email": "carol@test.com"},
]

#모든 사용자 조회
def get_users():
    return _users.copy()
#ID로 사용자 조회
def get_user_by_id(user_id: int):
    return next((u for u in _users if u["id"] == user_id),None)
#email로 사용자 조회
def get_user_by_email(email: str):
    return next((u for u in _users if u["email"] == email),None)