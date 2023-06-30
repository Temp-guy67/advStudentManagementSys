class ResponseObject:
    SUCCESS="success"
    ERROR="error"

    
    def __init__(self,type, msg , code,anything) -> None:
        self.type = type
        self.message = msg
        self.code = code
        self.extra = anything