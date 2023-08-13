import random,string,hashlib,logging
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import PasswordConstants,CommonConstants

#FileName : PasswordDB

DB_NAME="Databases/SQLDB/DBFiles/Passwords.db"
TABLE_NAME = "Passwords"

class PasswordObject:
    keys = []
    vals = []

    def __init__(self):
        self.keys = []
        self.vals = []

    def __createPasswordObject(self,data) -> None:
        try :
            self.keys = []
            self.vals = []

            userId = data[CommonConstants.USER_ID]
            password = data[CommonConstants.PASSWORD]
            salt = self.__generate_salt()
            hashedPassword = self.__generate_hash(password, salt)

            self.keys.append(CommonConstants.USER_ID)
            self.vals.append(userId)

            self.keys.append(PasswordConstants.SALT)
            self.vals.append(salt)

            self.keys.append(PasswordConstants.HASHED_PASSWORD)
            self.vals.append(hashedPassword)

            self.__insertDataInPasswordTable()
        except Exception as ex :
            logging.error("[PasswordDB][__createPasswordObject][Exception caught] {} ".format(ex))


    async def __createPasswordTableInDB(self):
        try:
            columnsDesc = [
                'user_id TEXT PRIMARY KEY UNIQUE',
                'salt TEXT NOT NULL',
                'hashed_password TEXT',
                'last_updated_time TEXT',
                'updated_by TEXT'
            ]
            data = dict()
            data["dbName"] = DB_NAME
            data["tableName"] = TABLE_NAME
            data["columnDesc"] = columnsDesc
            return await dbOperationHandler(None,None,data,"create_new_db")

        except Exception as ex:
            logging.error("[PasswordDB][__createPasswordTableInDB][Exception caught] {} ".format(ex))


    async def __insertDataInPasswordTable(self):
        try :

            data = dict()
            data["dbName"] = DB_NAME
            data["tableName"] = TABLE_NAME
            data["keys"] = self.keys
            data["values"] = self.vals

            return await dbOperationHandler(None,None,data,"insert_row")
        except Exception as ex :
            logging.error("[PasswordDB][_insertDataInPasswordTable][Exception caught] {} ".format(ex))


    async def __readDatafromPasswordTable(self,userId):
        try :
            data = dict()
            data["tableName"] = TABLE_NAME
            data["dbName"] = DB_NAME
            data["columns"] = []
            data["conditions"] = [["userId", userId, "="]]
            return await dbOperationHandler(None,None,data,"read_data")
        except Exception as ex :
            logging.error("[PasswordDB][__readDatafromPasswordTable][Exception caught] {} ".format(ex))

        

    def __generate_salt(self):
        saltLength = PasswordConstants.LENGTH
        characters = string.ascii_letters + string.digits + string.punctuation
        random_string = ''.join(random.choice(characters) for _ in range(saltLength))
        return random_string


    def __generate_hash(self,password, salt):
        concatenated_string = password + salt
        hash_object = hashlib.sha256()

        hash_object.update(concatenated_string.encode('utf-8'))
        hash_value = hash_object.hexdigest()

        return hash_value




async def validatePassword(self, userId, password):
    try :
        passObj = PasswordObject() 
        arr = passObj.__readDatafromPasswordTable(userId)
        print("arr : ", arr)

        #get hashed pass
        #get salt 
        hashedPass = "asdasd"
        salt = "asad"

        #recreate curPass using => 
        recreatedPass = self.__generate_hash(password,salt)
        return recreatedPass == hashedPass

    except Exception as ex :
        logging.error("[PasswordDB][validatePassword][Exception caught] {} ".format(ex))
            

async def savePassword(dicu):
    try:
        passObj = PasswordObject()
        await passObj.__createPasswordTableInDB()

        await passObj.__createPasswordObject(dicu)
            
    except Exception as ex:
        logging.error("[PasswordDB][savePassword][Exception caught] {} ".format(ex))