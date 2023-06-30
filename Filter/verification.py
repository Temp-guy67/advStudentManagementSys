#verification login and signup
from Commons.constants import ROLE,EMAIL,PASSWORD,PHONE,ROLE,DEPT,FNAME,LNAME,MNAME,DOB,USER_AGENT,CLIENT_IP
from Commons.generateSupportFields import signUpSupports,loginSupports
from Databases.SQLDB.commonDBhandler import createAccountForNewUser
from Databases.SQLDB.accountDB import ifAccountDataExists
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
            dicu["is_phone_signin"] = True
            
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
        email = user_data.get("email") 
        password = user_data.get("password")
        phone = user_data.get("phone")
        role = user_data.get("role")
        dept = user_data.get("dept")
        fname = user_data.get("fname")
        mname = user_data.get("mname")
        lname = user_data.get("lname")
        dob = user_data.get("dob")
        userAgent = user_data.get("user_agent")
        clientIp = user_data.get("client_ip")
        

        if not email or not phone or not password or not role or not dept or not fname:
            return -1
        
        dicu = {}
        dicu[EMAIL] = email
        dicu[PHONE] = phone
        dicu[PASSWORD] = password
        dicu[ROLE] = role 
        dicu[DEPT] = dept
        dicu[FNAME] = fname 
        dicu[MNAME] = mname 
        dicu[LNAME] = lname 
        dicu[DOB] = dob
        dicu[USER_AGENT] = userAgent
        dicu[CLIENT_IP] = clientIp

        #check if exist or not
        check = await ifAccountDataExists(email,phone)
        responseObj = None
        if check and check["result"] == -1:
            res = await signUpSupports(dicu)
            if res:
                responseObj = await createAccountForNewUser(res)
        elif check and check["result"] == 1 :
            logging.exception("[verification][User {} Cannot be added ][reason {} already existed]".format(fname,check["reason"]))
            responseObj = -1
        return responseObj

    except Exception as e :
        logging.exception("[verification][Exception in signupHandler][UserData]{} [Exception] {}".format(user_data,e))
    return None





