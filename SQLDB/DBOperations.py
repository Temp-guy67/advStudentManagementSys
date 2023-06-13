import sqlite3,logging
from DataObjects.entryObjects import accountObjectCreater
from Commons.constants import USER_ID,SESSION_ID

#FileName : DBOperations

#data is a dictionarry, nested dictionary . for proper strycture of data
async def dbOperationHandler(sessionId,userId,data,opr):
    try:
        logging.info("[DBOperations][Data received in dbOperationHandler][sessionId]",sessionId,"[userId]",userId,"[opr]",opr,"[data]",data)

        if opr == "create_new_db":
            tableName = data["tableName"]
            dbName = data["dbName"]
            columnDesc = data["columnDesc"]
            await __createNewTable(dbName, tableName,columnDesc)
        
        #accountData is a dictionnary
        elif opr == "insert_row" :
            tableName = data["tableName"]
            dbName = data["dbName"]
            accountData = data["details"]
            await __insertIntoTable(dbName,tableName,accountData)

        elif opr == "delete" :
            pass

        elif opr == "update" :
            pass


    except Exception as ex :
        logging.exception("[DBoperations][createAccountForUser] %s", str(ex))


#to Create a new table
async def __createNewTable(db_name,table_name,columnsDesc):
    try:
        logging.info("[DBOperations][Data received in __createTableTemplate][db_name]",db_name,"[table_name]",table_name,"[columnsDesc]",columnsDesc)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columnsDesc)})"
        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        logging.info("[DBOperations][__createNewTable][Table has been Created]",db_name,"[table_name]",table_name,"[columnsDesc]",columnsDesc)
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __createTableTemplate] %s", str(ex))



#To Insert a Row into a table
# make columns and values and send it in data
async def __insertIntoTable(db_name,table_name,data):
    try:
        logging.info("[DBOperations][Data received in __insertIntoTableTemplate][db_name]",db_name,"[table_name]",table_name,"[Data]",data)
        keys = data["keys"]
        values = data["values"]

        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        if len(keys) == len(values):
            query = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ("
            query += ', '.join('?' for _ in values)
            query += ");"

            cursor.execute(query, values)
            conn.commit()
        conn.close()
        logging.info("[DBOperations]__insertIntoTableTemplate][Data Inserted]",db_name,"[table_name]",table_name,"[Data]",data)
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __insertIntoTableTemplate] %s", str(ex))



#To Read Data From a table
async def __readDataFromTable(db_name,table_name,columns, conditions,sign):
    try:
        logging.info("[DBOperations][Data received in __insertIntoTableTemplate][db_name]",db_name,"[table_name]",table_name,"[Data]")
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        query = f"SELECT {', '.join(columns)} FROM {table_name} "
        if conditions :
            query += " WHERE "
            query += ' AND '.join(f"{key} {sign} '{value}'" for key, value in conditions.items())
            query += ")"
        query += ";"

        cursor.execute(query, conditions)
        conn.commit()
        conn.close()

    except Exception as ex :
        logging.exception("[DBOperations][Exception in __readDataFromTableTemplate] %s", str(ex))

async def __updateDataIntoTable(db_name,table_name,data):
    pass



async def __deleteDataFromTable(db_name,table_name,data):
    pass
