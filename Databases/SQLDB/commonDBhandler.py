import logging
from Databases.SQLDB.accountDB import AccountObject,createAccountForUser 
from Databases.SQLDB.passwordDB import 



async def createAccountForUser(dicu):
        accountObj = AccountObject(dicu)
        res = await createAccountForUser(accountObj)

        passwordObj = passwordObject(dicu)
