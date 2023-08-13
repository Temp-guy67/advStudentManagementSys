import sqlite3,logging
from Commons.constants import CommonConstants
from Databases.dbconstants import DBOperationOPR,DBConstants

#FileName : DBOperations
# data is a dictionary, nested dictionary . for proper structure of data

async def dbOperationHandler(sessionId,userId,data,opr):
    try:
        if opr == DBOperationOPR.CREATE:
            tableName = data[DBConstants.TABLE_NAME]
            dbName = data[DBConstants.DB_NAME]
            columnDesc = data[DBConstants.COLUMN_DESC]
            return await __createNewTable(dbName, tableName,columnDesc)
        
        elif opr == DBOperationOPR.INSERT :
            tableName = data[DBConstants.TABLE_NAME]
            dbName = data[DBConstants.DB_NAME]
            keys = data[DBConstants.KEYS]
            vals = data[DBConstants.VALUES]
            return await __insertIntoTable(dbName,tableName,keys,vals)
        
        elif opr == DBOperationOPR.READ:
            tableName = data[DBConstants.TABLE_NAME]
            dbName = data[DBConstants.DB_NAME]
            columns = data[DBConstants.COLUMNS]
            conditions = data[DBConstants.CONDITIONS]
            dbData = await __readDataFromTable(dbName, tableName, columns, conditions)
            return dbData

        elif opr == DBOperationOPR.DELETE :
            pass

        elif opr == DBOperationOPR.UPDATE :
            tableName = data[DBConstants.TABLE_NAME]
            dbName = data[DBConstants.DB_NAME]
            columns = data[DBConstants.COLUMNS]
            conditions = data[DBConstants.CONDITIONS]
            dbData = await __updateDataIntoTable(dbName, tableName, columns, conditions)
        


    except Exception as ex :
        logging.exception("[DBoperations][createAccountForUser]Exception Caught {} ".format(ex))


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
# columns will be the arrays of column name ["name" , "age"]
# coditions will be the nested list feat [[key1,val1,sign1],[key2,val2,sign2]] ]; individual coditions
# IF WANT TO READ ALL DATA send empty [] as columns

# Now how we are going to return it.  it will be standard hash deta. List of hashtables
# [ {"name"="abc","age"="10"}, {} , {}......]


async def __readDataFromTable(db_name,table_name,columns, conditions):
    table_data = []
    logging.info("[DBOperations][__readDataFromTable][query] {}".format(columns))
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        if columns:
            select_columns = ', '.join(columns)
        else:
            cursor.execute(f"PRAGMA table_info({table_name})")
            column_info = cursor.fetchall()
            columns = [info[1] for info in column_info]
            select_columns = ', '.join(columns)
            
        query = f"SELECT {select_columns} FROM {table_name} "
        if conditions :
            query += " WHERE "
            query += ' AND '.join(f"{key} {sign} '{value}'" for key, value ,sign in conditions)
        query += ";"

        logging.info("[DBOperations][__readDataFromTable][query] {}".format(query))
        cursor.execute(query)
        result = cursor.fetchall()

        # Combine column names and table data into a list of dictionaries
        
        for row in result:
            select_columns_list = select_columns.split(",")
            oneRow = {}
            for i in range(len(row)):
                oneRow[select_columns_list[i]] = row[i]
            table_data.append(oneRow)

    except Exception as ex :
        logging.exception("[DBOperations][Exception in __readDataFromTableTemplate] {}".format(ex))

    return table_data


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
