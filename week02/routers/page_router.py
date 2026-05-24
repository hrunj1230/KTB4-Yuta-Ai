from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
#html
templates = Jinja2Templates(directory="templates")

@router.get("/")
def root():
    return RedirectResponse("/login")

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )
@router.get("/board")
def board_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="board.html",
        context={}
    )
@router.get("/detail/{post_id}")
def detail_page(request: Request,post_id : int):
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={}
    )