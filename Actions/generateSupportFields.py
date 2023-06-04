from datetime import datetime
from Actions.constants import CLASS,COLLEGE_PREFIX,ROLE,DEPT,ID,USER_ID
import time,random
from FireabaseDB.firebase_get import getLast
from SQLDB.create import createDB


async def signUpSupports(dicu):
    try:
        role = dicu.get(ROLE)
        dept = dicu.get(DEPT)

        role = str(role)

        current_date = datetime.now().date()
        yearExtension = str(current_date)[2:4]

        classOFStudent = dept + yearExtension
        subjectCode = CLASS.get(dept)
        # 16 EE23 23 2023-06-01

        dicu = await getLast()
        last = dicu[role]

        id = COLLEGE_PREFIX + role + str(yearExtension) + subjectCode + str(last)
        # 3490323161
        current_time_millis = int(time.perf_counter() * 1000)
        random_int = random.randint(11, 99)
        userId = ROLE.get(role) + "_" + str(random_int) + "_" + str(current_time_millis)

        dicu[CLASS] = classOFStudent
        dicu[ID] = id
        dicu[USER_ID] = userId

        return 
    
    except Exception as e :
        print(" Hoga mara gese in create Ids",e )
    return 