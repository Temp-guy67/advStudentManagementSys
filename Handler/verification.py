#verification login and signup

async def verificationHandler():
    pass



async def loginHandler():
    pass



async def signupHandler(user_data):
    try:
        dicu = {}
        dicu["email"] = user_data.get("email")
        dicu["password"] = user_data.get("password")
        dicu["phone"] = user_data.get("phone")
        dicu["role"] = user_data.get("role")
        dicu["verified"] = False
        print("dicu is : ",dicu)

        #get inbox id from firebase
        #create id and userid from account table
        
        return dicu

    except Exception as e :
        print(" Hoga mara gese ",e)

    return "Success"


