import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get MongoDB credentials from environment variables
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_db = os.getenv("MONGO_DB")

# Connect to MongoDB Atlas using environment variables
client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@shop-db.erft9.mongodb.net/?retryWrites=true&w=majority&appName={mongo_db}")
db = client[mongo_db]
products_collection = db['products']

# Homepage route
@app.route('/')
def home():
    return render_template('home.html')

# Products route
@app.route('/products')
def products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
