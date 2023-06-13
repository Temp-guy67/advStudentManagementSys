import logging


# Level We have  -> debug,info,warning,error,critical

def configure_logging():
    logging.basicConfig(
        filename='app.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Logger Inititated")
    print("Logger Inititated")

