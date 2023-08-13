import datetime
from Commons.constants import CommonConstants,TypeClassifications
import time,random
# from SQLDB.accountDB import createAccount
from Databases.SQLDB.commonRulesDB import Conf
import logging

# File Name : generateSupportFields

async def signUpSupports(dicu):
    try:
        role = dicu.get(CommonConstants.ROLE)
        dept = dicu.get(CommonConstants.DEPT)

        role = str(role)

        currentDateTime = datetime.datetime.now()
        yearExtension = str(currentDateTime.year)

        classOFStudent = dept + yearExtension
        subjectCode = TypeClassifications.DEPTCODE[dept]
        # 16 EE23 23 2023-06-01

        confObj = Conf()
        last = await confObj.getLast(int(role))

        id = CommonConstants.COLLEGE_PREFIX + role + str(yearExtension) + subjectCode + str(last)
        # 3490323161

        current_time_millis = int(time.perf_counter() * 1000)
        random_int = random.randint(11, 99)
        userId = TypeClassifications.USERROLE.get(role) + "_" + str(random_int) + "_" + str(current_time_millis)

        dicu[CommonConstants.CLASS] = classOFStudent
        dicu[CommonConstants.ID] = id
        dicu[CommonConstants.USER_ID] = userId
        dicu[CommonConstants.LAST_UPDATED_TIME] = str(currentDateTime)
        dicu[CommonConstants.VERIFIED] = 0

        logging.info("[generateSupportFields][signUpSupports][Completed user support data][data]  {}".format(dicu))
        return dicu
    except Exception as e :
        logging.exception("[generateSupportFields][Exception in signUpSupports]  {}".format(e))
        return None

