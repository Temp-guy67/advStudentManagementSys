#verification login and signup
from Actions.constants import ROLE,EMAIL,PASSWORD,PHONE,VERIFIED,ROLE,DEPT
from FireabaseDB.firebase_get import getLast
from SQLDB.create import createDB
from Actions.generateSupportFields import signUpSupports

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
        signUpSupports(dicu)

        return 

    except Exception as e :
        print("[verification][signupHandler] ",e)

    return "Gar Mara"





