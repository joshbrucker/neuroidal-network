from flask import Flask
from flask import render_template
from flask import request

import neuroid

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/input", methods=["POST"])
def input():
    umbr = float(request.form["umbr"])
    beta = float(request.form["beta"])
    kr = float(request.form["kr"])
    maxcount = int(request.form["maxcount"])

    result = neuroid.run(umbr, beta, kr, maxcount)

    return render_template('index.html', results=result)
