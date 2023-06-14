import random,string,sqlite3,hashlib
from SQLDB.DBOperations import dbOperationHandler
from Commons.constants import USER_ID,PASSWORD


DB_NAME="DBFiles/Passwords.db"

async def savePassword(data):
    try:
        await __createPasswordTableInDB()
        userId = data[USER_ID]
        password = data[PASSWORD]
        salt = await __generate_salt(10)
        hashedPassword = await __generate_hash(password, salt)

        dicu = dict()
        dicu["user_id"] = userId
        dicu["salt"] = salt
        dicu["hashed_password"] = hashedPassword
        await __insertDataInPasswordTable(dicu)
    except Exception as ex:
        print("[password][savePassword]",ex)


async def __createPasswordTableInDB():
    try:
        db_name = DB_NAME
        table_name = 'Passwords'
        columnsDesc = [
            'user_id TEXT PRIMARY KEY',
            'salt TEXT NOT NULL',
            'hashed_password TEXT'
        ]
        data = dict()
        data["dbName"] = db_name
        data["tableName"] = table_name
        data["columnDesc"] = columnsDesc
        await dbOperationHandler(None,None,data,"create_new_db")

    except Exception as ex:
        print("[password][create]",ex)


async def __insertDataInPasswordTable(dicu):
    try :
        db_name = DB_NAME
        table_name = 'Passwords'
        details = {}
        keys = []
        values = []

        for k,v in dicu.items():
            keys.append(k)
            values.append(v)
        details["keys"] = keys
        details["values"] = values

        data = dict()
        data["dbName"] = db_name
        data["tableName"] = table_name
        data["details"] = details

        await dbOperationHandler(None,None,data,"insert_row")


    except Exception as ex :
        print("[password][__insertDataInPasswordTable]",ex)



    


async def __generate_salt(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


async def __generate_hash(string1, string2):
    concatenated_string = string1 + string2
    hash_object = hashlib.sha256()

    hash_object.update(concatenated_string.encode('utf-8'))
    hash_value = hash_object.hexdigest()

    return hash_value



async def validatePassword(userId, password):
    pass
    arr = getPassword(userId)

    



async def getPassword(userId):
    #get hashed password and salt
    pass


