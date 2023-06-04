from .firebase_config import db


async def getLast():
    collection_ref = db.collection('last')

    # Get the data from the collection
    data = collection_ref.get()

    # Iterate through the data
    for doc in data:
        dicu = doc.to_dict()
    return dicu