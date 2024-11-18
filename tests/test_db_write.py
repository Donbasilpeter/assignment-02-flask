from pymongo import MongoClient

def test_mongodb_insert():
    client = MongoClient("mongodb+srv://donbasilpeter:jpNsN9iYPXAPu7fJ@shop-db.erft9.mongodb.net/?retryWrites=true&w=majority&appName=shop-db")
    db = client['shop_db']
    collection = db['products']
    
    # Define a test product
    test_product = {
        "name": "Test Product",
        "tag": "test-tag",
        "price": 100,
        "image_path": "test-image.jpg"
    }
    
    # Insert the product
    insert_result = collection.insert_one(test_product)
    assert insert_result.acknowledged, "Insert operation not acknowledged"
    
    # Verify the product exists in the database
    retrieved_product = collection.find_one({"_id": insert_result.inserted_id})
    assert retrieved_product is not None, "Inserted document not found"
    
    # Cleanup: Remove the test document
    collection.delete_one({"_id": insert_result.inserted_id})
