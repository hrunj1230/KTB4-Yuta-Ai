from fastapi import FastAPI
from routers.user_router import router as user_router
from routers.page_router import router as page_router
from routers.board_router import router as board_router
from fastapi.staticfiles import StaticFiles
from db.database import Base, engine

app = FastAPI()

app.include_router(user_router, tags=["users"])
app.include_router(board_router, tags=["board"])
app.include_router(page_router)

#css 접근
app.mount("/static", StaticFiles(directory="static"), name="static")

#database
Base.metadata.create_all(bind=engine)