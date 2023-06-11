import sqlite3
from Commons.constants import USER_ID,ID,CLASS_OF_STUDENT,FNAME,LNAME,MNAME


async def createStduentAccount(dicu):
    try:             
        classOfStudent = dicu.get(CLASS_OF_STUDENT)
        fname = dicu.get(FNAME)
        mname = dicu.get(MNAME)
        lname = dicu.get(LNAME)
        userId = dicu.get(USER_ID)
        id  = dicu.get(ID)
        lastUpdatedTime = "test"

        print(" all datda  ", )

        # conn = sqlite3.connect("Accounts.db")
        conn = sqlite3.connect("Accounts.db")
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS Students ( USER_ID TEXT , EMAIL TEXT, PHONE TEXT, PASSWORD TEXT, ID TEXT ,  INBOX_ID TEXT , FNAME TEXT ,  MNAME TEXT ,  LNAME TEXT , ACCESS_LEVEL TEXT,CURRENT_RANK INTEGER, CLASS TEXT, LAST_UPDATED_TIME TEXT)')
        print("TABLE initialised")

        cur.execute("INSERT INTO AccountData (USER_ID , ID, CLASS, FNAME, MNAME, LNAME, LAST_UPDATED_TIME) VALUES (?,?,?,?,?,?,?)",
        (userId, id,classOfStudent, fname, mname, lname,lastUpdatedTime ))

        conn.commit()
        conn.close()
        
    except Exception as ex :
            print("[CREATE][createStduentAccount][Got Exception] : ",ex)

