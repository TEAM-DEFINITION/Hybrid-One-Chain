from fastapi import FastAPI,Request

app = FastAPI()
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
