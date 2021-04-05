from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from chain_module_user import user
from endecrypt import FerCipher

# http://112.156.0.196:55555
# Fastapi function start
app = FastAPI()

# CORS Setting
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# static management
app.mount("/static", StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

# API Management
# Signup API
@app.post("/app/signup")
async def app_post(request:Request, user_id:str=Form(...), user_pwd:str=Form(...)):
    user().genesis_block_create(user_id)
    return "OK"

# Login API
@app.post("/app/login")
async def app_login(request:Request, user_id:str=Form(...), user_pwd:str=Form(...)):
    user().genesis_block_create(user_id)
    return "OK"

# Post Access API
@app.post("/app/post")
async def app_post(request:Request, user_id:str=Form(...), user_pwd:str=Form(...), postcode:str=Form(...)):
    result = user().next_block_create(user_id, user_pwd, postcode)
    return result


########################################################################################



# Test API Management

@app.get("/test")
async def test(request:Request):
    return FerCipher().encrypt()







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
    chain_module_auth.genesis_block_create(user_id)
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
    result = chain_module_auth.check(user_id)
    if result == 0:
        return templates.TemplateResponse("login.html", {"request":request, "id":" ", "pwd":" ", "error":"404"})
    return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})

# 체인 생성
@app.post("/chain/{step}")
async def chain(request:Request, step:str, user_id:str=Form(...), user_pwd:str=Form(...), data:str=Form(...)):
    if step == "0" :
        chain_module_auth.genesis_block_create(user_id)
        print(user_id)
        return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd})
    elif step == "1" :
        result = chain_module_auth.next_block_create(user_id, user_pwd, data)
        return templates.TemplateResponse("chaintest.html", {"request":request, "user_id":user_id, "user_pwd":user_pwd, "server_data":result})
    return 0

# 체인 검증 모듈
@app.get("/validate")
async def validate(request:Request):
    return 0


########################################################################################
# 자동 시작
if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=55555, reload=True)
    