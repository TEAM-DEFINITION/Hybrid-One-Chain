from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import one_chain

app = FastAPI()

# static management
app.mount("/static", StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

# 메인
@app.get("/")
async def main(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})


# 회원가입 모듈
@app.get("/signup")
async def signup(request:Request):
    return 0

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
async def chain(request:Request, step:str, user_id:str=Form(...), user_pwd:str=Form(...)):
    if step == "0" :
        one_chain.genesis_block_create()
        print(user_id)
        return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})
    elif step == "1" :
        one_chain.next_block_create(user_id, user_pwd)
        return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})
    return 0

# 체인 검증 모듈
@app.get("/validate")
async def validate(request:Request):
    return 0

# 자동 시작
