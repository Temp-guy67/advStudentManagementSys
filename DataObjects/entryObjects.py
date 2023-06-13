from Commons.constants import EMAIL,PHONE,ID,USER_ID,ROLE,VERIFIED,INBOX_ID


class AccountObejcts:
    def __init__(self):
        self.email = None
        self.phone = None
        self.id = None
        self.role = None
        self.userId = None
        self.verified = None 
        self.accessLevel = None
        self.inboxId = None 

def accountObjectCreater(dicu):
    print(" ACCOUNT CREATER ," , dicu)
    accountObject = {}
    if dicu.get(EMAIL):
        accountObject[EMAIL] = dicu[EMAIL]
    if dicu.get(PHONE):
        accountObject[PHONE] = dicu[PHONE]
    if dicu.get(ID):
        accountObject[ID] = dicu[ID]
    if dicu.get(ROLE):
        accountObject[ROLE] = dicu[ROLE]
    if dicu.get(USER_ID):
        accountObject[USER_ID] = dicu[USER_ID]
    if dicu.get(VERIFIED):
        accountObject[VERIFIED] = int(dicu[VERIFIED])
    return accountObject
        
# def passwordObjectCreater(dicu):
