from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse
from Filter.verification import signupHandler,loginHandler
from Commons.services import onStartService,onShutdown
from Commons.constants import CommonConstants
import logging


app = FastAPI()

@app.on_event("startup")
async def startService():
    await onStartService()

# @app.on_event("shutdown")
# async def shutdown_event():
#     await onShutdown()

@app.get("/")
def root():
    return "Hello from SMS-v0.0.1! 🚀"


@app.post("/public/login")
async def login(request : Request):
    try:
        user_data = await request.json()
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent")

        user_data[CommonConstants.USER_AGENT] = user_agent
        user_data[CommonConstants.CLIENT_IP] = client_ip
        
        logging.info("[main][login][User Data Received] {}".format(user_data))
        temp = await loginHandler(user_data)
        response = JSONResponse(content=temp)
        return response
    except Exception as e :
        logging.exception("[main][Exception in login] {} ".format(e))


@app.post("/public/signup")
async def signup(request : Request):
    try :
        user_data = await request.json()
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent")

        user_data[CommonConstants.USER_AGENT] = user_agent
        user_data[CommonConstants.CLIENT_IP] = client_ip
        logging.info("[main][signup][User Data Received] {} ".format(user_data))

        temp = await signupHandler(user_data)
        response = JSONResponse(content=temp)
        return response
    except Exception as e :
        logging.exception("[main][Exception in signup] {} ".format(e))



# private now

@app.get("/user")
def user():
    return "Hello from Space! 🚀"


@app.get("/superadmin/{user_accesslevel}/readlogs")
def readlogs():
    try:
        pass


    except Exception as ex :
        logging.exception("[main][Exception in signup] {} ".format(ex))



@app.get("/")
def root():
    return "Hello from Space! 🚀"


