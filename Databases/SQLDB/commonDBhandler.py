import logging
from Databases.SQLDB.accountDB import AccountObject,createAccountForUser 
# from Databases.SQLDB.passwordDB import passwordObject
from ResponseObject.response import ResponseObject



async def createAccountForNewUser(dicu):
        accountObj = AccountObject(dicu)
        res = await createAccountForUser(accountObj)
        return "res in work " ,res 

                
        # if res > 0 :
            # passwordObj = passwordObject(dicu)
            
        

