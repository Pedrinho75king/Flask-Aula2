from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    page_name = "Home"
    return render_template("index.html", page_name=page_name)

@app.route("/form")
def form():
    page_name = "Formulário"
    return render_template("form.html", page_name=page_name)

@app.route("/list")
def list():
    page_name = "Lista"
    return render_template("list.html", page_name=page_name)

@app.route("/home")
def home():
    return redirect("/")