from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from module_access_user import user

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
#app.mount("/static", StaticFiles(directory='static'), name='static')
#templates = Jinja2Templates(directory='templates')


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

# 자동 시작
if __name__== "__main__":
    uvicorn.run("module_start:app", host="0.0.0.0", port=55555, reload=True)
    