from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import one_chain

import uvicorn

# http://112.156.0.196:55555

# Fastapi 객체 선언
app = FastAPI()

# 리엑트 연동부분(손대지마시오)
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# static management
app.mount("/static", StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

# 메인
@app.get("/", tags=["root"])
async def main(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})


# 회원가입 모듈
@app.get("/signup")
async def signup(request:Request):
    return templates.TemplateResponse("signup.html", {"request":request, "id":" ", "pwd":" "})

@app.post("/signup")
async def signup(request:Request, user_id:str=Form(...), user_pwd:str=Form(...)):
    one_chain.genesis_block_create(user_id)
    return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})

# 인증 모듈
@app.get("/auth")
async def auth(request:Request):
    return 0

# 로그인 모듈
@app.get("/login")
async def login(request:Request):
    return templates.TemplateResponse("login.html", {"request":request, "id":" ", "pwd":" "})

@app.post("/login")
async def login(request:Request, user_id:str=Form(...), user_pwd:str=Form(...)):
    return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})

# 체인 생성
@app.post("/chain/{step}")
async def chain(request:Request, step:str, user_id:str=Form(...), user_pwd:str=Form(...), data:str=Form(...)):
    if step == "0" :
        one_chain.genesis_block_create(user_id)
        print(user_id)
        return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})
    elif step == "1" :
        result = one_chain.next_block_create(user_id, user_pwd, data)
        return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd, "server_data":result})
    return 0

# 체인 검증 모듈
@app.get("/validate")
async def validate(request:Request):
    return 0

# 자동 시작
if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=55555, reload=True)