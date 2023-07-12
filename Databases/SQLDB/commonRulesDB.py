from Databases.SQLDB.DBOperations import dbOperationHandler

CONF_DB_NAME = "Databases/SQLDB/DBFiles/ConfDatas.db"
CONF_DB_TABLE = "CommonConfs"

class Conf:
    last_count = ['0', '0', '0', '0', '0']
    def __init__(self) -> None:
        pass
    
    async def getLast(self,role):
        # to create conf table
        # await self.createConfDB()
        # await self.insertConfDB(self.last_count)

        raw_conf = await self.readConfDB()
        raw_conf_list = list(raw_conf[0][0].split("="))
        data = int(raw_conf_list[role])
        raw_conf_list[role] = str(data + 1)
        lstC = "=".join(raw_conf_list)

        updateColumns = [["value",lstC]]
        conditions = [["label","common_variables","=" ],["key","last_account","=" ]]

        await self.updateConfDB(updateColumns, conditions)
        return data


    async def readConfDB(self):
        data = dict()
        data["dbName"] = CONF_DB_NAME
        data["tableName"] = CONF_DB_TABLE
        data["columns"]  = ["value"]
        data["conditions"] = [["label","common_variables","=" ],["key","last_account","=" ]]
        res =  await dbOperationHandler(None,None,data,"read_data")
        return res

    async def insertConfDB(self,str_arr):
        data = dict()
        data["dbName"] = CONF_DB_NAME
        data["tableName"] = CONF_DB_TABLE
        keys = ["label","key","value"]
        lstC = "=".join(str_arr)
        vals = ["common_variables", "last_account", lstC]

        data["keys"] = keys
        data["values"] = vals

        await dbOperationHandler(None,None,data,"insert_row")


    # common_variable last_count "1-23-45-10" (as a string, will split it into parts then get the last)
    async def createConfDB(self):
        columnsDesc = ["label TEXT", "key TEXT UNIQUE","value TEXT"]
        data = dict()
        data["dbName"] = CONF_DB_NAME
        data["tableName"] = CONF_DB_TABLE
        data["columnDesc"] = columnsDesc
        return await dbOperationHandler(None,None,data,"create_new_db")


    async def updateConfDB(self,columns, conditions ):
        data = dict()
        data["dbName"] = CONF_DB_NAME
        data["tableName"] = CONF_DB_TABLE
        data["columns"]  = columns       
        data["conditions"] = conditions      
        res = await dbOperationHandler(None,None,data,"update")