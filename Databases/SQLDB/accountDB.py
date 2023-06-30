import logging
from ResponseObject.response import ResponseObject
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import EMAIL,PHONE,ROLE,USER_ID,ID,VERIFIED,CLASS,LAST_UPDATED_TIME

#FilenName : accountDB
# .mode box to show data in bOX

DB_NAME="Databases/SQLDB/DBFiles/Accounts.db"
TABLE_NAME="AccountsData"

class AccountObject :
    keys = []
    vals = []
    def __init__(self,data):
        logging.info("[AccountObject][Constructer][Data] {} ".format(data))
        try :
            role = data[ROLE]
            if role:
                self.keys.append(ROLE)
                self.vals.append(role)
            
            email = data[EMAIL]
            if email:
                self.keys.append(EMAIL)
                self.vals.append(email)

            phone = data[PHONE]
            if phone:
                self.keys.append(PHONE)
                self.vals.append(phone)

            userId = data[USER_ID]
            if userId:
                self.keys.append(USER_ID)
                self.vals.append(userId)

            id = data[ID]
            if id:
                self.keys.append(ID)
                self.vals.append(id)

            verified = data[VERIFIED]
            if verified:
                self.keys.append(VERIFIED)
                self.vals.append(verified)

            lastUpdatedTime = data[LAST_UPDATED_TIME]
            if lastUpdatedTime:
                self.keys.append(LAST_UPDATED_TIME)
                self.vals.append(lastUpdatedTime)

        except Exception as ex :
            logging.error("[SQLDB][AccountObject][Exception in the Constructor] {} ".format(ex))


    def getDataAsDictionary(self):
        dicu = dict()
        dicu["keys"] = self.keys
        dicu["values"] = self.vals
        return dicu


async def createAccountTable():
    res = await __createAccountTableInDB()
    if res == 1 :
        logging.info("[accountDB][createAccount][Table Created]")
    else :
        logging.info("[accountDB][createAccount][Table NOT Created]")


async def createAccountForUser(accountObj):

    try :
        # await createAccountTable()
        dataInKeyValuePair = accountObj.getDataAsDictionary()
        return await __insertDataInAccountTable(dataInKeyValuePair)
        
    except Exception as ex :
        logging.error("[AccountDB][createAccountForUser][Got Exception] {} ".format(ex))


async def __createAccountTableInDB():
    columnsDesc = ["user_id TEXT UNIQUE", "email TEXT UNIQUE","phone TEXT UNIQUE" , "id TEXT UNIQUE","verified INTEGER", "role INTEGER","dob TEXT","access_level INTEGER", "inbox_id TEXT" , "last_updated_time TEXT"]

    data = dict()
    data["dbName"] = DB_NAME
    data["tableName"] = TABLE_NAME
    data["columnDesc"] = columnsDesc
    return await dbOperationHandler(None,None,data,"create_new_db")
    

async def __insertDataInAccountTable(data):
    data["dbName"] = DB_NAME
    data["tableName"] = TABLE_NAME

    await dbOperationHandler(None,None,data,"insert_row")


async def readDataInAccountTable(dicu):
    data = dict()
    data["dbName"] = DB_NAME
    data["tableName"] = TABLE_NAME
    data["columns"] = data["columns"]
    data["conditions"] = data["conditions"]

    return await dbOperationHandler(None,None,data,"read_data")


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



async def deleteFailedSingUpData(userId):
    pass



    
    
    
