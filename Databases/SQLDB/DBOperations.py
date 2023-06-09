import sqlite3,logging
from Commons.constants import CommonConstants

#FileName : DBOperations

#data is a dictionarry, nested dictionary . for proper strycture of data
async def dbOperationHandler(sessionId,userId,data,opr):
    try:
        if opr == "create_new_db":
            tableName = data["tableName"]
            dbName = data["dbName"]
            columnDesc = data["columnDesc"]
            return await __createNewTable(dbName, tableName,columnDesc)
        
        #accountData is a dictionnary
        elif opr == "insert_row" :
            tableName = data["tableName"]
            dbName = data["dbName"]
            keys = data["keys"]
            vals = data["values"]
            return await __insertIntoTable(dbName,tableName,keys,vals)
        
        elif opr == "read_data":
            tableName = data["tableName"]
            dbName = data["dbName"]
            columns = data["columns"]
            conditions = data["conditions"]
            dbData = await __readDataFromTable(dbName,tableName,columns, conditions)
            return dbData

        elif opr == "delete" :
            pass

        elif opr == "update" :
            tableName = data["tableName"]
            dbName = data["dbName"]
            columns = data["columns"]
            conditions = data["conditions"]
            dbData = await __updateDataIntoTable(dbName,tableName,columns, conditions)
        


    except Exception as ex :
        logging.exception("[DBoperations][createAccountForUser] %s", str(ex))


#to Create a new table
async def __createNewTable(db_name,table_name,columnsDesc):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columnsDesc)})"
        logging.info("[DBOperations][__createNewTable][query] {}".format(create_table_query))
        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        return 1
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __createTableTemplate] {} ".format(ex))
    return -1

#To Insert a Row into a table
# make columns and values and send it in data
async def __insertIntoTable(db_name,table_name,keys,values):
    try:
        logging.info("[DBOperations][__insertIntoTableTemplate] {} {}".format(keys,values))
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        if len(keys) == len(values):
            query = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ("
            query += ', '.join('?' for _ in values)
            query += ");"
            logging.info("[DBOperations][__insertIntoTable][query] {}".format(query))
            cursor.execute(query, values)
            conn.commit()
        conn.close()
        return 1
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __insertIntoTableTemplate] {}".format(ex))
    return -1


# To Read Data From a table
# columns will be the arrays of column name
# coditions will be the nested list feat [key,val,sign] ; individual coditions
async def __readDataFromTable(db_name,table_name,columns, conditions):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        if columns:
            select_columns = ', '.join(columns)
        else:
            select_columns = '*'

        query = f"SELECT {select_columns} FROM {table_name} "
        if conditions :
            query += " WHERE "
            query += ' AND '.join(f"{key} {sign} '{value}'" for key, value ,sign in conditions)
        query += ";"

        logging.info("[DBOperations][__readDataFromTable][query] {}".format(query))
        cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result

    except Exception as ex :
        logging.exception("[DBOperations][Exception in __readDataFromTableTemplate] {}".format(ex))


async def __updateDataIntoTable(db_name,table_name,columns, conditions):
    try :
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        query = f"UPDATE {table_name} SET "
        query += ' AND '.join(f"{key} = '{value}'" for key, value  in columns)
        if conditions :
            query += " WHERE "
            query += ' AND '.join(f"{key} {sign} '{value}'" for key, value ,sign in conditions)
        query += ";"

        logging.info("[DBOperations][__updateDataIntoTable][query] {}".format(query))
        cursor.execute(query)
        conn.commit()
        conn.close()
        return 1
    
    except Exception as ex :
        logging.exception("[DBOperations][Exception in __updateDataIntoTable] {}".format(ex))
    return 0



async def __deleteDataFromTable(db_name,table_name,data):
    pass
