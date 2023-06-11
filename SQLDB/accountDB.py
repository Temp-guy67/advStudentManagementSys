
from SQLDB.passwordDB import savePassword
from SQLDB.studentDB import createStduentAccount 
from SQLDB.DBOperations import createAccountForUser


# .mode box to show data in bOX


async def createAccount(dicu):

    try :
        print("LANDED IN ACCOUNTdb createAccount")
        await createAccountForUser(dicu)

        # savePassword(dicu)
        # createStduentAccount(dicu)

        return "Suces full account created"
    except Exception as ex :
        print("[CREATE][createAccount][Got Exception] : ",ex)


async def createAccountTableInDB(table_name,columnDesc):
    table_name = "AccountsData"
    columnsDesc = ["user_id TEXT", "email TEXT","phone TEXT" , "id TEXT","verified INTEGER", "role INTEGER","dob TEXT","access_level INTEGER", "inbox_id TEXT" ]
    await __createTableTemplate(table_name,columnsDesc)
    print("TABLE initialised")


