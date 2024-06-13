from testapp import app
from flask import render_template 

@app.route('/')
def index():
    return render_template('testapp/index.html')

@app.route("/menu")
def menu():
    return 