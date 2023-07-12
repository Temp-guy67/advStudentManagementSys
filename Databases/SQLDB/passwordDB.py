import random,string,hashlib
from Databases.SQLDB.DBOperations import dbOperationHandler
from Commons.constants import PasswordConstants,CommonConstants

DB_NAME="Databases/SQLDB/DBFiles/Passwords.db"
TABLE_NAME = "Passwords"

class PasswordObject:
    keys = []
    vals = []

    def __init__(self,data) -> None:
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
        
    async def savePassword(self):
        try:
            # await self.__createPasswordTableInDB()

            return await self.__insertDataInPasswordTable()
            
        except Exception as ex:
            print("[password][savePassword]",ex)


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
            print("[password][create]",ex)


    async def __insertDataInPasswordTable(self):
        try :

            data = dict()
            data["dbName"] = DB_NAME
            data["tableName"] = TABLE_NAME
            data["keys"] = self.keys
            data["values"] = self.vals

            return await dbOperationHandler(None,None,data,"insert_row")
        except Exception as ex :
            print("[password][__insertDataInPasswordTable]",ex)


    def __generate_salt(self):
        saltLength = PasswordConstants.LENGTH
        characters = string.ascii_letters + string.digits + string.punctuation
        random_string = ''.join(random.choice(characters) for _ in range(saltLength))
        return random_string


    def __generate_hash(self,string1, string2):
        concatenated_string = string1 + string2
        hash_object = hashlib.sha256()

        hash_object.update(concatenated_string.encode('utf-8'))
        hash_value = hash_object.hexdigest()

        return hash_value



    async def validatePassword(self, userId, password):
        arr = self.getPassword(userId)

        


    async def getPassword(self,userId):
        #get hashed password and salt
        pass


