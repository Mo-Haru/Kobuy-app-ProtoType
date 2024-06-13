from testapp import app
from testapp import db
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template('testapp/index.html')

@app.route("/menu")
def menu():
    return render_template("testapp/menu.html")

@app.route("/reserve", methods = ["GET", "POST"])
def reserve():
    if request.method == "GET":
        return render_template("testapp/reserve.html")
    if request.method == "POST":
        return "<h1>予約完了！！！</h1>"