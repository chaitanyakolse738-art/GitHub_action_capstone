from flask import Flask, jsonify
from datetime import datetime, timezone
import time

app = Flask(__name__)

start_time = time.time()


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Health API",
        "application": "DevOps Capstone Project",
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "uptime": round(time.time() - start_time, 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": "DevOps Health API",
        "language": "Python",
        "framework": "Flask",
        "environment": "development"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)