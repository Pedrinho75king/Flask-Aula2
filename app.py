from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/home")
def home():
    return redirect("/")