import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')  # Default to '0.0.0.0' if HOST is not set
    port = int(os.getenv('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host=host, port=port)
