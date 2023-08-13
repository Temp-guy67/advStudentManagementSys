import logging,time
from ResponseObject.response import ResponseObject
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import CommonConstants
from Databases.dbconstants import SessionsConstants

#FilenName : SessionDB
# .mode box to show data in bOX

DB_NAME="Databases/SQLDB/DBFiles/Sessions.db"
TABLE_NAME="SessionsData"

class SessionObject :  
    def __init__(self):
        self.keys = []
        self.vals = []

    async def __createNewSession(self,data):
        logging.info("[SessionDB][__createNewSession][Data] {} ".format(data))
        try :
            self.keys = []
            self.vals = []

            userId = data[CommonConstants.USER_ID]
            if userId:
                self.keys.append(CommonConstants.USER_ID)
                self.vals.append(userId)

            clientIp = data[CommonConstants.CLIENT_IP]
            if clientIp:
                self.keys.append(CommonConstants.CLIENT_IP)
                self.vals.append(clientIp)

            userAgent = data[CommonConstants.USER_AGENT]
            if userAgent:
                self.keys.append(CommonConstants.USER_AGENT)
                self.vals.append(userAgent)

            currentTime = time.time()
            currentTimeinMilis = int(currentTime * 1000)

            self.keys = SessionsConstants.SESSION_START_TIME
            self.vals = currentTimeinMilis

            self.keys = SessionsConstants.LAST_CHECKING_TIME
            self.vals = currentTimeinMilis

            self.__insertDataInSessionTable()

        except Exception as ex :
            logging.error("[SessionDB][__createNewSession][Exception caught] {} ".format(ex))



    async def __createSessionTableInDB(self):
        columnsDesc = ["USER_ID TEXT UNIQUE","SESSION_START_TIME TEXT","SESSION_END_TIME TEXT", "LAST_CHECKING_TIME TEXT", "CLIENT_IP TEXT","USER_AGENT TEXT", "TRUSTED_DEVICES TEXT" ]

        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columnDesc"] = columnsDesc
        return await dbOperationHandler(None,None,data,"create_new_db")
        

    async def __insertDataInSessionTable(self):
        data = {}
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["keys"] = self.keys
        data["values"] = self.vals
        return await dbOperationHandler(None,None,data,"insert_row")
    
    async def __readDataFromSessionTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]
        return await dbOperationHandler(None,None,data,"read_data")
    
    async def __updateDataInSessionTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]
        return await dbOperationHandler(None,None,data,"update")
    
    async def __deleteDataFromSessionTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]
        return await dbOperationHandler(None,None,data,"delete")



async def ifUserAlreadyInSession(userId):
    res = {}
    try:
        arr = [["USER_ID",userId,"="]]
        data= dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        emp = await dbOperationHandler(None,None,data,"read_data")
        
        if emp :
            return 1 
        else :
            return 0
    except Exception as ex :
        logging.error("[SessionDB][ifUserAlreadyInSession][Got Exception] {} ".format(ex))

    return 0

    






    
    
    
