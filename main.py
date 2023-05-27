from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse
from Handler.verification import signupHandler,loginHandler

app = FastAPI()

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
        print(" Hoga mara gese in main ",e)
    return "working"



# private now

@app.get("/user")
def user():
    return "Hello from Space! 🚀"

@app.get("/")
def root():
    return "Hello from Space! 🚀"