from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v2")
MESSAGE = os.getenv("APP_MESSAGE", "Hello from Flask App!")

@app.route("/")
def home():
    return f"{MESSAGE} - Version: {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

