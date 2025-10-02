from flask import Flask
import os

app = Flask(__name__)

# Get version from environment variable (default v1)
VERSION = os.getenv("APP_VERSION", "v1")
MESSAGE = os.getenv("APP_MESSAGE", "Hello from Flask App!")

@app.route("/")
def home():
    return f"{MESSAGE} - Version: {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

