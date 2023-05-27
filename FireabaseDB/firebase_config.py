import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
firebase_admin.initialize_app(credentials.Certificate("newTest.json"))
db = firestore.client()
