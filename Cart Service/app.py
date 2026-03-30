from flask import Flask, jsonify, request

app = Flask(__name__)
cart = []

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    item = request.json
    cart.append(item)
    return jsonify({"message": "Added"}), 201

@app.route("/cart/clear", methods=["POST"])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Cleared"}), 200

if __name__ == "__main__":
    app.run(port=5002)
