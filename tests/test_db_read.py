from pymongo import MongoClient

def test_mongodb_connection():
    client = MongoClient("mongodb+srv://donbasilpeter:jpNsN9iYPXAPu7fJ@shop-db.erft9.mongodb.net/?retryWrites=true&w=majority&appName=shop-db")
    
    try:
        # Use MongoDB's admin command to verify the connection
        client.admin.command('ping')
        assert True  # Connection successful
    except Exception as e:
        assert False, f"MongoDB connection failed: {e}"
