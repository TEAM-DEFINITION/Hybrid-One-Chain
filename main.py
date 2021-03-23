from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static management
app.mount("/static", StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get("/")
async def main(request:Request):
    return 0


# 회원 가입
@app.get("/signup")
async def signup(request:Request):
    return 0


# 인증 모듈
@app.get("/auth")
async def auth(request:Request):
    return 0


# 자동 시작
