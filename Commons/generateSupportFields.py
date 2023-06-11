from datetime import datetime
from Commons.constants import DEPTCODE,COLLEGE_PREFIX,ROLE,DEPT,ID,USER_ID,CLASS,USERROLE
import time,random
from FireabaseDB.firebase_get import getLast
from SQLDB.accountDB import createAccount
import logging



async def signUpSupports(dicu):
    try:
        role = dicu.get(ROLE)
        dept = dicu.get(DEPT)

        role = str(role)

        current_date = datetime.now().date()
        yearExtension = str(current_date)[2:4]

        classOFStudent = dept + yearExtension
        subjectCode = DEPTCODE[dept]
        # 16 EE23 23 2023-06-01

        temp = await getLast()
        last = temp[role]

        id = COLLEGE_PREFIX + role + str(yearExtension) + subjectCode + str(last)
        # 3490323161

        current_time_millis = int(time.perf_counter() * 1000)
        random_int = random.randint(11, 99)
        userId = USERROLE.get(role) + "_" + str(random_int) + "_" + str(current_time_millis)

        dicu[CLASS] = classOFStudent
        dicu[ID] = id
        dicu[USER_ID] = userId
        await createAccount(dicu)
        return dicu
    
    except Exception as e :
        logging.exception("[generateSupportFields][Exception in signUpSupports] %s", str(e))
    return 