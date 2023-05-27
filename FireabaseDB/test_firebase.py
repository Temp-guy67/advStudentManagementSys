from .firebase_config import db


async def firebase_test():
    print(" lNADED IN FIREABSE TEST ")
    user_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30,
        "city": "New York"
        }
    doc_ref = db.collection("users").document()
    doc_ref.set(user_data)

    # Return a response
    return {"message": "User created successfully"}