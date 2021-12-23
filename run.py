from flask import Flask
from flask import render_template, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')