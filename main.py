from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse
from Filter.verification import signupHandler,loginHandler
from Commons.services import onStartService


app = FastAPI()

@app.on_event("startup")
async def startService():
    await onStartService()

@app.get("/")
def root():
    return "Hello from Space! 🚀"


@app.get("/public/login")
async def login():
    return "Hello from Space! 🚀"

@app.get("/public/signup")
async def signup(request : Request):
    user_data = await request.json()

    try :
        temp = await signupHandler(user_data)
        response = JSONResponse(content=temp)
        return {"message" : response}

    except Exception as e :
        print("[main][signup]Failed ",e)
    return "working"



# private now

@app.get("/user")
def user():
    return "Hello from Space! 🚀"

@app.get("/")
def root():
    return "Hello from Space! 🚀"