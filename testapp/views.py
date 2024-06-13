from testapp import app

@app.route('/')
def index():
    return '<h1>Kobuy-App-ProtoType<h1>'

@app.route("/")
def menu():
    return 