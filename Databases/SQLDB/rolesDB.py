import logging
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import CommonConstants

#FilenName : RolesDB
# .mode box to show data in bOX

DB_NAME="Databases/SQLDB/DBFiles/Roles.db"
TABLE_NAME="RolesData"

class RolesObject :  
    def __init__(self):
        self.keys = []
        self.vals = []

    async def __createRolesObject(self,data):
        logging.info("[RolesDB][__createRolesObject][Data] {} ".format(data))
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

            fname = data[CommonConstants.FNAME]
            if fname :
                self.keys.append(CommonConstants.FNAME)
                self.vals.append(fname)

            mname = data[CommonConstants.MNAME]
            if mname :
                self.keys.append(CommonConstants.MNAME)
                self.vals.append(mname)

            lname = data[CommonConstants.LNAME]
            if fname :
                self.keys.append(CommonConstants.LNAME)
                self.vals.append(lname)
            
            cls = data[CommonConstants.CLASS]
            if cls :
                self.keys.append(CommonConstants.CLASS)
                self.vals.append(cls)


            lastUpdatedTime = data[CommonConstants.LAST_UPDATED_TIME]
            if lastUpdatedTime:
                self.keys.append(CommonConstants.LAST_UPDATED_TIME)
                self.vals.append(lastUpdatedTime)

        except Exception as ex :
            logging.error("[RolesDB][__createRolesObject][Exception in the Constructor] {} ".format(ex))


    async def createRoleTable(self):
        res = await self.__createRoleTableInDB()
        if res == 1 :
            logging.info("[RolesDB][createRoleTable][Table Created]")
        else :
            logging.info("[RolesDB][createRoleTable][Table NOT Created]")


    async def createRoleForUser(self, data):
        try :
            #To Create new table
            # await self.createRoleTable()

            await self.__createRolesObject(data)
            return await self.__insertDataInRoleTable()
            
        except Exception as ex :
            logging.error("[RolesDB][createAccountForUser][Got Exception] {} ".format(ex))


    async def __createRoleTableInDB(self):
        columnsDesc = ["USER_ID TEXT" ,"ROLE TEXT", "EMAIL TEXT", "PHONE TEXT", "PASSWORD TEXT", "ID TEXT" , "INBOX_ID TEXT" ,"FNAME TEXT",  "MNAME TEXT" ,  "LNAME TEXT", "ACCESS_LEVEL TEXT","CURRENT_RANK INTEGER", "CLASS TEXT", "LAST_UPDATED_TIME TEXT"]

        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columnDesc"] = columnsDesc
        return await dbOperationHandler(None,None,data,"create_new_db")
        

    async def __insertDataInRoleTable(self):
        data = {}
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["keys"] = self.keys
        data["values"] = self.vals

        return await dbOperationHandler(None,None,data,"insert_row")
    
    async def __readDataInRoleTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]

        return await dbOperationHandler(None,None,data,"read_data")
    
    async def __updateDataInRoleTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]

        return await dbOperationHandler(None,None,data,"update")
    
    async def __deleteDataInRoleTable(self,dicu):
        data = dict()
        data["dbName"] = DB_NAME
        data["tableName"] = TABLE_NAME
        data["columns"] = dicu["columns"]
        data["conditions"] = dicu["conditions"]

        return await dbOperationHandler(None,None,data,"delete")





    






    
    
    
