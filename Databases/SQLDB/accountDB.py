import logging
from ResponseObject.response import ResponseObject
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import CommonConstants

#FilenName : accountDB
# .mode box to show data in bOX

DB_NAME="Databases/SQLDB/DBFiles/Accounts.db"
TABLE_NAME="AccountsData"

class AccountObject :  
    def __init__(self):
        self.keys = []
        self.vals = []

    async def __createAccountObject(self,data):
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

        except Exception as ex :
            logging.error("[accountDB][createAccountObject][Exception in the Constructor] {} ".format(ex))


    async def createAccountTable(self):
        res = await self.__createAccountTableInDB()
        if res == 1 :
            logging.info("[accountDB][createAccount][Table Created]")
        else :
            logging.info("[accountDB][createAccount][Table NOT Created]")


    async def createAccountForUser(self, data):
        try :
            #To Create new table
            # await self.createAccountTable()

            await self.__createAccountObject(data)
            return await self.__insertDataInAccountTable()
            
        except Exception as ex :
            logging.error("[AccountDB][createAccountForUser][Got Exception] {} ".format(ex))


    async def __createAccountTableInDB(self):
        columnsDesc = ["user_id TEXT UNIQUE", "email TEXT UNIQUE","phone TEXT UNIQUE" , "id TEXT UNIQUE","verified INTEGER", "role INTEGER","dob TEXT","access_level INTEGER", "inbox_id TEXT" , "last_updated_time TEXT"]

        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columnDesc"] = columnsDesc
        return await dbOperationHandler(None,None,data,"create_new_db")
        

    async def __insertDataInAccountTable(self):
        data = {}
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["keys"] = self.keys
        data["values"] = self.vals

        return await dbOperationHandler(None,None,data,"insert_row")
    
    async def _readDataInAccountTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]

        return await dbOperationHandler(None,None,data,"read_data")
    
    async def __updateDataInAccountTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]

        return await dbOperationHandler(None,None,data,"update")
    
    async def __deleteDataInAccountTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]

        return await dbOperationHandler(None,None,data,"delete")



async def ifAccountDataExists(email,phone):
    res = {}

    try:
        arr = [["email",email,"="] , ["phone",phone,"="]]
        table_name = "AccountsData"
    
        for e in arr :
            data = dict()
            data["columns"] = None
            data["conditions"] = [e]
                
            data["dbName"] = DB_NAME
            data["tableName"] = table_name
            temp =  await dbOperationHandler(None,None,data,"read_data")
            if temp :
                res["result"] = 1
                res["reason"] = e[0]
                return res
        res["result"] = -1
        res["reason"] = None
    except Exception as ex :
        logging.error("[AccountDB][ifAccountDataExists][Got Exception] {} ".format(ex))

    return res

    






    
    
    
