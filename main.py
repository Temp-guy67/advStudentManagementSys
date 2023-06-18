from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse
from Filter.verification import signupHandler,loginHandler
from Commons.services import onStartService
import logging


app = FastAPI()

@app.on_event("startup")
async def startService():
    await onStartService()

@app.get("/")
def root():
    return "Hello from Space! 🚀"


@app.get("/public/login")
async def login(request : Request):
    user_data = await request.json()
    logging.info("[main][login][Request Landed] %s ", str(user_data))
    try:
        temp = await loginHandler(user_data)
        response = JSONResponse(content=temp)
        return response
    except Exception as e :
        logging.exception("[main][Exception in login] %s", str(e))


@app.get("/public/signup")
async def signup(request : Request):
    user_data = await request.json()
    logging.info("[main][signup][Request Landed] %s", str(user_data))
    try :
        temp = await signupHandler(user_data)
        response = JSONResponse(content=temp)
        return response
    except Exception as e :
        logging.exception("[main][Exception in signup] %s", str(e))



# private now

@app.get("/user")
def user():
    return "Hello from Space! 🚀"

@app.get("/")
def root():
    return "Hello from Space! 🚀"