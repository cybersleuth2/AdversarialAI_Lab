import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

def install_missing_packages():
    required = [
        "flask"
    ]
    for package in required:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call(["pip", "install", package])

install_missing_packages()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
