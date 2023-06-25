class ResponseObject:
    SUCCESS="success"
    ERROR="error"

    
    
    def __init__(self,type, msg , code) -> None:
        self.type = type
        self.message = msg
        self.code = code