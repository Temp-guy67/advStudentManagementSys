from Commons.logger import configure_logging
import tracemalloc

async def onStartService():
    configure_logging()
    tracemalloc.start()
    
async def onShutdown():
    pass


