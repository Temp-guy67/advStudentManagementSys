#verification login and signup
from Commons.constants import CommonConstants,SessionConstants
from Commons.generateSupportFields import signUpSupports
from Databases.SQLDB.commonDBhandler import createAccountForNewUser
from Databases.SQLDB.accountDB import ifAccountDataExists
from Filter.sessionControllers import sessionLogin
import logging


async def verificationHandler():
    pass



async def loginHandler(user_data):
    try :
        dicu = {}
        email = user_data.get("email") 
        password = user_data.get("password")
        phone = user_data.get("phone")

        if email and password :
            dicu[CommonConstants.EMAIL] = email
            dicu[CommonConstants.PASSWORD] = password

        elif phone and (not email and not password) :
            dicu[CommonConstants.PHONE] = user_data.get("phone")
            dicu[SessionConstants.PHONE_LOGIN] = True
        else :
            return -1
            
        res = await sessionLogin(dicu)
        return res

    except Exception as e :
        logging.exception("[verification][Exception in loginHandler]  %s", str(e),"[UserData]",user_data)


async def forgotPassword(user_data):
    try:
        dicu = {}
        dicu[CommonConstants.EMAIL] = user_data.get("email")
        dicu[CommonConstants.PHONE] = user_data.get("phone")
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
        
        check = await ifAccountDataExists(email,phone)
        responseObj = None

        # check if exist or not
        if check and check["result"] == 1 :
            logging.exception("[verification][User {} Cannot be added ][reason {} already existed]".format(fname,check["reason"]))
            return -1

        dicu = {}
        dicu[CommonConstants.EMAIL] = email
        dicu[CommonConstants.PHONE] = phone
        dicu[CommonConstants.PASSWORD] = password
        dicu[CommonConstants.ROLE] = role 
        dicu[CommonConstants.DEPT] = dept
        dicu[CommonConstants.FNAME] = fname 
        dicu[CommonConstants.MNAME] = mname 
        dicu[CommonConstants.LNAME] = lname 
        dicu[CommonConstants.DOB] = dob
        dicu[CommonConstants.USER_AGENT] = userAgent
        dicu[CommonConstants.CLIENT_IP] = clientIp

        if check and check["result"] == -1:
            res = await signUpSupports(dicu)
            if res:
                responseObj = await createAccountForNewUser(res)
                if responseObj == 1 :
                    responseObj = "Data Inserted Sucessfully"
                else:
                    responseObj = "Pod Mara gelo r ki"
        return responseObj

    except Exception as e :
        logging.exception("[verification][Exception in signupHandler][UserData]{} [Exception] {}".format(user_data,e))
    return None





