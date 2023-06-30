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
    try:
        user_data = await request.json()
        logging.info("[main][login][User Data Received] {}".format(user_data))
        temp = await loginHandler(user_data)
        response = JSONResponse(content=temp)
        return response
    except Exception as e :
        logging.exception("[main][Exception in login] {} ".format(e))


@app.get("/public/signup")
async def signup(request : Request):
    try :
        user_data = await request.json()
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent")

        user_data["user_agent"] = user_agent
        user_data["client_ip"] = client_ip
        logging.info("[main][signup][User Data Received] {}".format(user_data))

        temp = await signupHandler(user_data)
        response = JSONResponse(content=temp)

        return response
    except Exception as e :
        logging.exception("[main][Exception in signup] {} ".format(e))



# private now

@app.get("/user")
def user():
    return "Hello from Space! 🚀"

@app.get("/")
def root():
    return "Hello from Space! 🚀"