from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://donbasilpeter:jpNsN9iYPXAPu7fJ@shop-db.erft9.mongodb.net/?retryWrites=true&w=majority&appName=shop-db")
db = client['shop_db']
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
