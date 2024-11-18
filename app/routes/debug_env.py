from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/debug_env", methods=["GET"])
def debug_env():
    return jsonify({
        "API_KEY_1": os.getenv("API_KEY_ADMIN", "Not Set"),
        "API_KEY_2": os.getenv("API_KEY_SUB", "Not Set"),
    })

if __name__ == "__main__":
    app.run(debug=True)