from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/hello")
def index():
    page_name = "Home"
    name = request.args.get("name", "world")
    message = f"Olá, {name} !!"
    return render_template("index.html", page_name=page_name, message=message)

@app.route("/list")
def list():
    page_name = "Lista"
    return render_template("list.html", page_name=page_name)

@app.route("/")
def home():
    return redirect("/hello")