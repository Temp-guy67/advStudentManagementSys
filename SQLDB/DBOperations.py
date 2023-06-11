import sqlite3,logging
from DataObjects.entryObjects import accountObjectCreater

#FileName : DBOperations



async def dbOperationHandler(sessionId,userId,data,opr):
    try:
        logging.info("[DBOperations][Data received in dbOperationHandler][sessionId]",sessionId,"[userId]",userId,"[opr]",opr,"[data]",data)

        if opr == "create_new_db":
            await __createNewTable()
            accountObject = accountObjectCreater(dicu)
            print(" ACCOUNT OBJECT " , accountObject)
            
        
        elif opr == "insert" :
            
            await __insertIntoTable("AccountsData",accountObject)
            pass

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
        print("TABLE CREATED ",create_table_query)
        conn.close()
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __createTableTemplate] %s", str(ex))



#To Insert a Row into a table
async def __insertIntoTable(db_name,table_name,dicu):
    try:
        logging.info("[DBOperations][Data received in __insertIntoTableTemplate][db_name]",db_name,"[table_name]",table_name,"[Data]",dicu)
        columns = []
        values = []
        for k,v in dicu.items():
            columns.append(k)
            values.append(v)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        if len(columns) == len(values):
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ("
            query += ', '.join('?' for _ in values)
            query += ");"

            cursor.execute(query, values)
            conn.commit()
        conn.close()
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __insertIntoTableTemplate] %s", str(ex))



#To Read Data From a table
async def __readDataFromTable(db_name,table_name,columns, conditions,sign):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE "
        query += ' AND '.join(f"{key} {sign} '{value}'" for key, value in conditions.items())

        cursor.execute(query, conditions)
        conn.commit()
        conn.close()

    except Exception as ex :
        logging.exception("[DBOperations][Exception in __readDataFromTableTemplate] %s", str(ex))

async def __updateDataIntoTable(db_name,table_name,dicu):
    pass



async def __deleteDataFromTable(db_name,table_name,dicu):
    pass
