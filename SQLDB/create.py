import sqlite3
from Actions.constants import EMAIL,PHONE,PASSWORD,USER_ID,ID,CLASS_OF_STUDENT,VERIFIED,ROLE,FNAME,LNAME,MNAME


async def createAccount(dicu):

    try :
        # print(" data has been received in [CREATE][CREATEDB] ",dicu)
        email = dicu.get(EMAIL)
        phone = dicu.get(PHONE)
        password = dicu.get(PASSWORD)
        userId = dicu.get(USER_ID)
        id  = dicu.get(ID)
        verified = dicu.get(VERIFIED)
        if verified == False :
            verified = 0 
        else :
            verified = 1
        role = dicu.get(ROLE)

        #personal Data


        print(" all datda  ", userId,email,phone,password,id,verified,role)

        # conn = sqlite3.connect("Accounts.db")
        conn = sqlite3.connect("Accounts.db")
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS AccountData ( USER_ID TEXT , EMAIL TEXT, PHONE TEXT, PASSWORD TEXT, ID TEXT, VERIFIED INTEGER , ROLE INTEGER , DOB TEXT , ACCESS_LEVEL INTEGER, INBOX_ID TEXT)')
        print("TABLE initialised")

        cur.execute("INSERT INTO AccountData (USER_ID  , EMAIL , PHONE , PASSWORD , ID , VERIFIED  , ROLE ) VALUES (?,?,?,?,?,?,?)",
        (userId, email, phone, password, id, verified, role))

        # print(" DATA UPADTED SUCCESSFULLY")
        conn.commit()
        conn.close()

        return "Suces full account created"
    except Exception as ex :
        print("[CREATE][CREATEDB][Got Exception] : ",ex)