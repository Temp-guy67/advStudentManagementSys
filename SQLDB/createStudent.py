import sqlite3
from Actions.constants import EMAIL,PHONE,PASSWORD,USER_ID,ID,CLASS_OF_STUDENT,VERIFIED,ROLE,FNAME,LNAME,MNAME


async def createStduent(dicu):
            
        classOfStudent = dicu.get(CLASS_OF_STUDENT)
        fname = dicu.get(FNAME)
        mname = dicu.get(MNAME)
        lname = dicu.get(LNAME)
        userId = dicu.get(USER_ID)
        id  = dicu.get(ID)

        print(" all datda  ", )

        # conn = sqlite3.connect("Accounts.db")
        conn = sqlite3.connect("Accounts.db")
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS Students ( USER_ID TEXT , EMAIL TEXT, PHONE TEXT, PASSWORD TEXT, ID TEXT, VERIFIED INTEGER , ROLE INTEGER)')
        print("TABLE initialised")

        cur.execute("INSERT INTO AccountData (USER_ID  , EMAIL , PHONE , PASSWORD , ID , VERIFIED  , ROLE ) VALUES (?,?,?,?,?,?,?)",
        (userId, email, phone, password, id, verified, role))