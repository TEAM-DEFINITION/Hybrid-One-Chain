from fastapi import FastAPI, Request, Form
# from fastapi.responses import RedirectResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
import uvicorn
# import json

from module_access_user import USER
from module_endecrypt import RSA_Cipher

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
# app.mount("/static", StaticFiles(directory='static'), name='static')
# templates = Jinja2Templates(directory='templates')

# Access API Management
# Signup API
@app.post("/app/signup")
async def appSignup(request: Request, user_id: str = Form(...), user_pwd: str = Form(...), clientrandom: str = Form(...), publickey: str = Form(...)):
    print(publickey)
    result = USER().genesis_block_create(user_id, user_pwd, clientrandom)
    return result

# Login API
@app.post("/app/login")
async def appLogin(request: Request, user_id: str = Form(...), user_pwd: str = Form(...)):
    result = USER().login(user_id, user_pwd)
    return result

# Post Access API
@app.post("/app/post")
async def appPost(request: Request, user_id: str = Form(...), user_pwd: str = Form(...), postcode: str = Form(...)):
    result = USER().next_block_create(user_id, user_pwd, postcode)
    return result

@app.get('/test')
async def test(request: Request):
    RSA_Cipher().encrypt()
    return 0

########################################################################################


# 글로벌 자동 시작
# if __name__== "__main__":
#    uvicorn.run("module_start:app", host="0.0.0.0", port=55555, reload=True)

# 로컬 자동 시작 // 127.0.0.1:8000 or 10.0.2.2:8000
if __name__ == "__main__":
    uvicorn.run("module_start:app", reload=True)