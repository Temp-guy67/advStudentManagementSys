import logging
from Databases.SQLDB.accountDB import AccountObject 
from Databases.SQLDB.passwordDB import PasswordObject
from Databases.SQLDB.rolesDB import RolesObject
from ResponseObject.response import ResponseObject

# commonDBhandler


async def createAccountForNewUser(dicu):
        accountObj = AccountObject()
        res = await accountObj.createAccountForUser(dicu)
        logging.info("[commonDBhandler][createAccountForNewUser][Account Object done]")

        if res > 0 :
            passwordObj = PasswordObject(dicu)
            res = await passwordObj.savePassword()
            logging.info("[commonDBhandler][createAccountForNewUser][Password Object done]")

            
        if res > 0 :
            rolesObj = RolesObject()
            await rolesObj.createRoleForUser(dicu)
            logging.info("[commonDBhandler][createAccountForNewUser][Roles Object done]")
            return 1
              

async def getUserLogin(dicu):
    accountObj = AccountObject()
    res = await accountObj._readDataInAccountTable(dicu)
