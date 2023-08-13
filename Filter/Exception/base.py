# custom exception

class CustomError(Exception):
    def __init__(self, message, erroCode):
        super().__init__(message)
        self.error_code = erroCode

    def log_error(self):
        # You can add custom methods to your exception class
        # to perform specific actions when the exception is raised.
        print(f"Error code: {self.error_code}, Error message: {self.args[0]}")


def some_function(x):
    if x < 0:
        raise CustomError("x should be a positive number", 1055)


try:
    value = -10
    some_function(value)
except CustomError as e:
    e.log_error()
