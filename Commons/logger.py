import logging


# Level We have  -> debug,info,warning,error,critical

def configure_logging():
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        format='%(name)s - %(levelname)s - %(message)s'
    )

