from flask import Flask, jsonify, request
import time, random

app = Flask(__name__)

@app.route("/checkout", methods=["POST"])
def process_order():
    # Simulate payment logic
    time.sleep(random.randint(1, 2))
    if random.random() < 0.2:
        return jsonify({"error": "Payment failed"}), 500
    return jsonify({"status": "SUCCESS"}), 200

if __name__ == "__main__":
    app.run(port=5003)
