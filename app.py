from flask import Flask, redirect

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Olá, mundo"

@app.route("/")
def index():
    return redirect('/hello')