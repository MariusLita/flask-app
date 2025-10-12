from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v0.0")
MESSAGE = os.getenv("APP_MESSAGE", "Hello from Flask App!")
NAMESPACE = os.getenv("POD_NAMESPACE", default = 'ns-read')

@app.route("/")
def home():
    return f"{MESSAGE} - Version: {VERSION} - Namespace: {NAMESPACE}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
