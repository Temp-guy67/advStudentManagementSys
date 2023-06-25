import logging
from ResponseObject.response import ResponseObject
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import EMAIL,PHONE,ROLE,USER_ID,ID,VERIFIED,CLASS,LAST_UPDATED_TIME

#FilenName : accountDB
# .mode box to show data in bOX

DB_NAME="DBFiles/Accounts.db"
TABLE_NAME="AccountsData"


class AccountObject :
    def __init__(self,data):
        logging.info("[AccountObject][Constructer][Data] %s",str(data))
        try :
            self.role = data[ROLE]
            self.email = data[EMAIL]
            self.phone = data[PHONE]
            self.userId = data[USER_ID]
            self.id = data[ID]
            self.cls = data[CLASS]
            self.verified = data[VERIFIED]
            self.lastUpdatedTime = data[LAST_UPDATED_TIME]
            logging.info("[AccountObject][Constructer][Object Created] ")

        except Exception as ex :
            logging.error("[SQLDB][AccountObject][Exception in the Constructor]",ex)

    def getDataAsDictionary(self):
        dicu = dict()
        keys = []
        vals = []

        role = self.role
        if role:
            keys.append(ROLE)
            vals.append(role)
        
        email = self.email
        if email:
            keys.append(EMAIL)
            vals.append(email)

        phone = self.phone
        if phone:
            keys.append(PHONE)
            vals.append(phone)

        userId = self.userId
        if userId:
            keys.append(USER_ID)
            vals.append(userId)

        id = self.id
        if id:
            keys.append(ID)
            vals.append(id)

        cls = self.cls
        if cls:
            keys.append(CLASS)
            vals.append(cls)

        verified = self.verified
        if verified:
            keys.append(VERIFIED)
            vals.append(verified)

        lastUpdatedTime = self.lastUpdatedTime
        if lastUpdatedTime:
            keys.append(LAST_UPDATED_TIME)
            vals.append(lastUpdatedTime)

        
        dicu["keys"] = keys
        dicu["values"] = vals

        return dicu


async def createAccountTable():
    await __createAccountTableInDB()
    logging.info("[accountDB][createAccount][Table Created]")



async def createAccountForUser(accountObj):

    try :
        data = accountObj.getDataAsDictionary()
    
        currentUserId = data.get("user_id")
        print(" data user Id ",currentUserId)
        
        # chck if the data already existed or not
        res = await __ifAccountDataExists(accountObj)

        response = None

        if not res: 
            await __insertDataInAccountTable(data)
            logging.info("[accountDB][createAccount][Data Inserted in Account Table]")
            response = ResponseObject(ResponseObject.SUCCESS, "Account Has been Created Successfully", "1")
        else:
            logging.info("[accountDB][createAccount][Data already existed in Account Table]")
            response = ResponseObject(ResponseObject.ERROR, "Data Already Existed", "-1")
        
        
        return response

        
    except Exception as ex :
        print("[AccountDB][createAccount][Got Exception] : ",ex)


async def __createAccountTableInDB():
    columnsDesc = ["user_id TEXT UNIQUE", "email TEXT UNIQUE","phone TEXT UNIQUE" , "id TEXT UNIQUE","verified INTEGER", "role INTEGER","dob TEXT","access_level INTEGER", "inbox_id TEXT" , "last_updated_time TEXT" ]

    data = dict()
    data["dbName"] = DB_NAME
    data["tableName"] = TABLE_NAME
    data["columnDesc"] = columnsDesc
    await dbOperationHandler(None,None,data,"create_new_db")
    

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

async def __ifAccountDataExists(datas):
    email = datas.get("email")
    phone = datas.get("phone")
    arr = [["email",email,"="] , ["phone",phone,"="]]
    table_name = "AccountsData"
    res = []
    for e in arr :
        data = dict()
        data["columns"] = None
        data["conditions"] = [e]
            
        data["dbName"] = DB_NAME
        data["tableName"] = table_name
        temp =  await dbOperationHandler(None,None,data,"read_data")
        if temp :
            res += e
            return res
    return res




async def deleteFailedSingUpData(userId):
    pass
