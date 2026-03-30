import requests
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Service URLs (In Docker/K8s, these would be service names)
PRODUCT_SVC = "http://localhost:5001"
CART_SVC = "http://localhost:5002"
ORDER_SVC = "http://localhost:5003"

@app.route("/")
def home():
    # Fetch products from the Product Service
    products = requests.get(f"{PRODUCT_SVC}/products").json()
    # [Insert your original HTML template string here]
    return render_template_string(html, products=products)

@app.route("/cart", methods=["GET", "POST"])
def cart_proxy():
    if request.method == "GET":
        return jsonify(requests.get(f"{CART_SVC}/cart").json())
    
    # Logic to get product details and send to cart service
    data = request.json
    all_products = requests.get(f"{PRODUCT_SVC}/products").json()
    product = next((p for p in all_products if p['id'] == data['product_id']), None)
    
    res = requests.post(f"{CART_SVC}/cart", json=product)
    return jsonify(res.json()), res.status_code

@app.route("/checkout", methods=["POST"])
def checkout_proxy():
    # 1. Check if cart has items
    cart_items = requests.get(f"{CART_SVC}/cart").json()
    if not cart_items:
        return jsonify({"error": "Cart empty"}), 400

    # 2. Call Order Service
    order_res = requests.post(f"{ORDER_SVC}/checkout")
    
    # 3. If order success, clear cart
    if order_res.status_code == 200:
        requests.post(f"{CART_SVC}/cart/clear")
        
    return jsonify(order_res.json()), order_res.status_code

if __name__ == "__main__":
    app.run(port=5000)
