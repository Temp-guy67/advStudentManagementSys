#verification login and signup
from Commons.constants import ROLE,EMAIL,PASSWORD,PHONE,VERIFIED,ROLE,DEPT
from Commons.generateSupportFields import signUpSupports
import logging


async def verificationHandler():
    pass



async def loginHandler():
    pass



async def signupHandler(user_data):
    try:
        dicu = {}
        dicu[EMAIL] = user_data.get("email")
        dicu[PASSWORD] = user_data.get("password")
        dicu[PHONE] = user_data.get("phone")
        dicu[VERIFIED] = 0
        dicu[ROLE] = user_data.get("role")
        dicu[DEPT]  = user_data.get("dept")
        # print(" DICU in signupHandler",dicu)
        await signUpSupports(dicu)

        return 

    except Exception as e :
        logging.exception("[verification][Exception in signupHandler]  %s", str(e))
        # print("",e)

    return "Gar Mara"





