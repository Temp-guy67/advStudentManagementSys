import logging
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import CommonConstants
from Databases.dbconstants import DBConstants,DBOperationOPR

#FilenName : accountDB
# .mode box to show data in bOX

DB_NAME="Databases/SQLDB/DBFiles/Accounts.db"
TABLE_NAME="AccountsData"

class AccountObject :  
    def __init__(self):
        self.keys = []
        self.vals = []

    async def _createAccountObject(self,data):
        logging.info("[accountDB][createAccountObject][Data] {} ".format(data))
        try :
            self.keys = []
            self.vals = []
            role = data[CommonConstants.ROLE]
            if role:
                self.keys.append(CommonConstants.ROLE)
                self.vals.append(role)
            
            email = data[CommonConstants.EMAIL]
            if email:
                self.keys.append(CommonConstants.EMAIL)
                self.vals.append(email)

            phone = data[CommonConstants.PHONE]
            if phone:
                self.keys.append(CommonConstants.PHONE)
                self.vals.append(phone)

            userId = data[CommonConstants.USER_ID]
            if userId:
                self.keys.append(CommonConstants.USER_ID)
                self.vals.append(userId)

            id = data[CommonConstants.ID]
            if id:
                self.keys.append(CommonConstants.ID)
                self.vals.append(id)

            verified = data[CommonConstants.VERIFIED]
            if verified is not None:
                self.keys.append(CommonConstants.VERIFIED)
                self.vals.append(verified)

            lastUpdatedTime = data[CommonConstants.LAST_UPDATED_TIME]
            if lastUpdatedTime:
                self.keys.append(CommonConstants.LAST_UPDATED_TIME)
                self.vals.append(lastUpdatedTime)

            return self.__insertDataInAccountTable()

        except Exception as ex :
            logging.error("[accountDB][createAccountObject][Exception in the Constructor] {} ".format(ex))


    async def _createAccountTableInDB(self):
        columnsDesc = ["user_id TEXT UNIQUE", "email TEXT UNIQUE","phone TEXT UNIQUE" , "id TEXT UNIQUE","verified INTEGER", "role INTEGER","dob TEXT","access_level INTEGER", "inbox_id TEXT" , "last_updated_time TEXT"]

        data = dict()
        data[DBConstants.DB_NAME] = DB_NAME
        data[DBConstants.TABLE_NAME] = TABLE_NAME
        data[DBConstants.COLUMN_DESC] = columnsDesc
        return await dbOperationHandler(None,None,data, DBOperationOPR.CREATE)
        

    async def __insertDataInAccountTable(self):
        data = {}
        data[DBConstants.DB_NAME] = DB_NAME
        data[DBConstants.TABLE_NAME] = TABLE_NAME
        data["keys"] = self.keys
        data["values"] = self.vals
        return await dbOperationHandler(None,None,data,DBOperationOPR.INSERT)
    
    async def _readDataInAccountTable(self,dicu):
        data = dict()
        data[DBConstants.DB_NAME] = DB_NAME
        data[DBConstants.TABLE_NAME] = TABLE_NAME
        data[DBConstants.COLUMNS] = dicu["columns"]
        data[DBConstants.CONDITIONS] = dicu["conditions"]
        return await dbOperationHandler(None,None,data,DBOperationOPR.READ)
    
    async def _updateDataInAccountTable(self,dicu):
        data = dict()
        data[DBConstants.DB_NAME] = DB_NAME
        data[DBConstants.TABLE_NAME] = TABLE_NAME
        data[DBConstants.COLUMNS] = dicu["columns"]
        data[DBConstants.CONDITIONS] = dicu["conditions"]
        return await dbOperationHandler(None,None,data,DBOperationOPR.UPDATE)
    
    async def _deleteDataInAccountTable(self,dicu):
        data = dict()
        data[DBConstants.DB_NAME] = DB_NAME
        data[DBConstants.TABLE_NAME] = TABLE_NAME
        data[DBConstants.COLUMNS] = dicu["columns"]
        data[DBConstants.CONDITIONS] = dicu["conditions"]
        return await dbOperationHandler(None,None,data,DBOperationOPR.DELETE)
    

###########################################################################

async def createAccountForUser(data):
    try :
        accObj = AccountObject()
        #To create new account Table
        # await accObj.__createAccountTableInDB()
        return await accObj._createAccountObject(data)
        
    except Exception as ex :
        logging.error("[AccountDB][createAccountForUser][Caught Exception] {} ".format(ex))


async def readAccountData(column, contidions):
    data = dict()
    data["columns"] = column
    data["conditions"] = contidions
    accObj = AccountObject()
    temp = await accObj._readDataInAccountTable(data)
    return temp


async def ifAccountDataExists(email,phone):
    try:
        arr = [["email",email,"="] , ["phone",phone,"="]]    
        for e in arr :
            res = await readAccountData([], [e])
            if res :
                return e[0]
    except Exception as ex :
        logging.error("[AccountDB][ifAccountDataExists][Got Exception] {} ".format(ex))

    return None

async def getLoginData(data):
    if data.get("email"):
        conditions = [["email",data["email"],"="]]
    
    if data.get("phone"):
        conditions = [["phone",data["phone"],"="]]

        







    
    
    
