from flask import Flask, render_template, jsonify
import json

app2 = Flask(__name__)

# Load product data from JSON file
def load_products():
    with open('data/products.json') as f:
        return json.load(f)

@app2.route('/')
def index():
    products = load_products()
    return render_template('index.html', products=products)

@app2.route('/product/<int:product_id>')
def product_detail(product_id):
    products = load_products()
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

if __name__ == '__main__':
    app2.run(debug=True)
