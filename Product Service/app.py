from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 80000, "img": "https://cdn-icons-png.flaticon.com/512/2920/2920277.png"},
    {"id": 2, "name": "Phone", "price": 30000, "img": "https://cdn-icons-png.flaticon.com/512/15/15874.png"},
    {"id": 3, "name": "Headphones", "price": 2000, "img": "https://cdn-icons-png.flaticon.com/512/727/727245.png"}
]

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(port=5001)
