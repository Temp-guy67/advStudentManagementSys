#verification login and signup
from Commons.constants import ROLE,EMAIL,PASSWORD,PHONE,VERIFIED,ROLE,DEPT
from Commons.generateSupportFields import signUpSupports,loginSupports
import logging


async def verificationHandler():
    pass



async def loginHandler(user_data):
    try :
        dicu = {}
        phoneSignIn = False
        if user_data.get(EMAIL) and user_data.get(PASSWORD) :
            dicu[EMAIL] = user_data.get(EMAIL)
            dicu[PASSWORD] = user_data.get(PASSWORD)

        if user_data.get(PHONE) :
            dicu[PHONE] = user_data.get("phone")
            phoneSignIn = True
            
        res = await loginSupports(dicu)
        return res

    except Exception as e :
        logging.exception("[verification][Exception in loginHandler]  %s", str(e),"[UserData]",user_data)


async def forgotPassword(user_data):
    try:
        dicu = {}
        dicu[EMAIL] = user_data.get("email")
        dicu[PHONE] = user_data.get("phone")
        await signUpSupports(dicu)

    except Exception as e :
        logging.exception("[verification][Exception in signupHandler]  %s", str(e),"[UserData]",user_data)

async def signupHandler(user_data):
    try:
        dicu = {}
        dicu[EMAIL] = user_data.get("email")
        dicu[PASSWORD] = user_data.get("password")
        dicu[PHONE] = user_data.get("phone")
        dicu[VERIFIED] = "0"
        dicu[ROLE] = user_data.get("role")
        dicu[DEPT]  = user_data.get("dept")
        await signUpSupports(dicu)

    except Exception as e :
        logging.exception("[verification][Exception in signupHandler]  %s", str(e),"[UserData]",user_data)
    





