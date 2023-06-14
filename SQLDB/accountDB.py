import logging
from SQLDB.passwordDB import savePassword
from SQLDB.DBOperations import dbOperationHandler
from DataObjects.entryObjects import accountObjectCreater

#FilenName : accountDB
# .mode box to show data in bOX

DB_NAME="DBFiles/Accounts.db"

async def createAccount(dicu):

    try :
        await __createAccountTableInDB()
        logging.info("[accountDB][createAccount][Table Created]")
        obj = accountObjectCreater(dicu)
        await __insertDataInAccountTable(obj.items())
        logging.info("[accountDB][createAccount][Data Inserted in Account Table]")
        print("[accountDB][createAccount][Data Inserted in Account Table]")
        await savePassword(dicu)
        print("[accountDB][createAccount][Password Saved in Password Table]")
        logging.info("[accountDB][createAccount][Password Saved in Password Table]")
        # createStduentAccount(dicu)

        return "Suces full account created"
    except Exception as ex :
        print("[AccountDB][createAccount][Got Exception] : ",ex)


async def __createAccountTableInDB():
    # db_name = "Accounts.db"
    db_name = DB_NAME
    table_name = "AccountsData"
    columnsDesc = ["user_id TEXT", "email TEXT","phone TEXT" , "id TEXT","verified INTEGER", "role INTEGER","dob TEXT","access_level INTEGER", "inbox_id TEXT" , "last_updated_time TEXT" ]

    data = dict()
    data["dbName"] = db_name
    data["tableName"] = table_name
    data["columnDesc"] = columnsDesc
    await dbOperationHandler(None,None,data,"create_new_db")
    

async def __insertDataInAccountTable(data):
    print(" data revceived in __insert ",data)
    db_name = DB_NAME
    table_name = "AccountsData"

    details = {}
    keys = []
    values = []
    print(" DATA in Account Creation : " , data)
    for k,v in data:
        keys.append(k)
        values.append(v)
    details["keys"] = keys
    details["values"] = values

    data = dict()
    data["dbName"] = db_name
    data["tableName"] = table_name
    data["details"] = details
    await dbOperationHandler(None,None,data,"insert_row")





