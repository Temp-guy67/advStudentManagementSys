import logging
from Databases.SQLDB.accountDB import AccountObject
from Databases.SQLDB.passwordDB import PasswordObject
from Databases.SQLDB.rolesDB import RolesObject
from Commons.constants import SessionConstants,CommonConstants

# SessionController

async def createAccountForNewUser(dicu):
        accountObj = AccountObject()
        res = await accountObj.createAccountForUser(dicu)
        logging.info("[SessionController][createAccountForNewUser][Account Object done]")

        if res > 0 :
            passwordObj = PasswordObject()
            res = await passwordObj.savePassword(dicu)
            logging.info("[SessionController][createAccountForNewUser][Password Object done]")

            
        if res > 0 :
            rolesObj = RolesObject()
            await rolesObj.createRoleForUser(dicu)
            logging.info("[SessionController][createAccountForNewUser][Roles Object done]")
            return 1
              

async def getUserLogin(dicu):
    accountObj = AccountObject()
    res = await accountObj._readDataInAccountTable(dicu)



#File name : SessionControllers

async def sessionsController(dicu) :
    logging.info("[SessionController][sessionLogin][Session Process started] {} ".format(dicu))

    verifyingConstant = None                 # if it is email login, then verifyingConstant will be password, if phone login, it will be otp
    if dicu.get(CommonConstants.PHONE):
        userId = await __phoneLogin(dicu)
    else :
        userId = await __emailLogin(dicu)

    if not userId :
        return -1
    
    dicu[CommonConstants.USER_ID] = userId 

    #logger success full login

    return 
    # status = await __updateSessionDB(dicu, "post")

    res = None
    if status :
        res = await __getUserData(userId)
    return res



# get userdId from Account Table
async def __emailLogin(dicu):
    email = dicu.get(CommonConstants.EMAIL)
    password = dicu.get(CommonConstants.PASSWORD)

    conditions =[["email",email,"="]]
    
    data = {}
    data["columns"] = []
    data["conditions"] = conditions

    accountObj = AccountObject()
    res = await accountObj.readDataInAccountTable(data)

    
    # res = res[0]
    print("res is ", res , type(res))
    userId = res.get("user_id")
        
    if not await __verifyPassword(userId, password):
        pass


    logging.info("[SessionController] __emailLogin {}".format(res))
    pass 

# get userdId from Account Table
async def __phoneLogin(dicu):
    pass 


# to check if he is logged in somewhere else or not : and trusted device notification [will add later]# also delete and post two way
async def __updateSessionDB(data, opr):

    if opr == "post":
        pass
    elif opr == "delete":
        pass


# get user data from roles db and send as response
async def __getUserData(userId):
    role_conditions =[["USER_ID",userId,"="]]
    
    data = {}
    data["columns"] = []
    data["conditions"] = role_conditions

    rolesObj = RolesObject()
    rolesData = rolesObj.__readDataInRoleTable(data)



async def __verifyPassword(userId, password):
    passObj = PasswordObject()
    if passObj.validatePassword(userId,password) :
        return 1
    else :
        return 0