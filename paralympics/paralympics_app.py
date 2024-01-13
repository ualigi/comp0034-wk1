from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello random and welcome to my paralympics app"


@app.route("/<name>")
def hello(name):
    return "Hello " + name + " and welcome to my paralympics app"
