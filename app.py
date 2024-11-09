from flask import Flask, jsonify

app = Flask(__name__)

# A simple route to simulate some work
@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/products')
def products():
    # Simulating a product list response
    return jsonify([
        {"id": 1, "name": "Product 1", "price": 100},
        {"id": 2, "name": "Product 2", "price": 150},
        {"id": 3, "name": "Product 3", "price": 200},
    ])

if __name__ == '__main__':
    app.run()
