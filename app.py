from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template("index.html")

@app.route("/")
def index():
    return redirect('/hello')