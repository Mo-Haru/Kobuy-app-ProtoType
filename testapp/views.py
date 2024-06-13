from testapp import app
from flask import render_template 

@app.route('/')
def index():
    return '<h1>Kobuy-App-ProtoType<h1>'

@app.route("/menu")
def menu():
    return 