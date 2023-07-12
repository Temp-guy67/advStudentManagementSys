from Commons.constants import SessionConstants,CommonConstants
import logging

#File name : SessionControllers


async def sessionLogin(data) :
    keys = []
    vals = []
    dicu = {}

    if data.get(SessionConstants.PHONE_LOGIN) and data[SessionConstants.PHONE_LOGIN] :
        phone = data[CommonConstants.PHONE]
        keys = [CommonConstants.PHONE]
        vals = [phone]
        dicu["isNumberLogin"] = True

    else :
        email = data[CommonConstants.EMAIL]
        password = data[CommonConstants.PASSWORD]
        keys = [CommonConstants.EMAIL, CommonConstants.PASSWORD]
        vals = [email, password]


    dicu["keys"] = keys
    dicu["values"] = vals


    logging.info("[SessionControllers][sessionLogin][Session Process started]")






