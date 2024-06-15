from testapp import app
from flask import render_template, request

@app.route('/')
def index():
    title = "購買予約アプリ試作版"

    return render_template('testapp/index.html', webtitle = title)

@app.route("/menu")
def menu():
    title = "購買メニュー"
    return render_template("testapp/menu.html", webtitle = title)



@app.route("/reserve", methods = ["GET", "POST"])
def reserve():
    title = "購買予約フォーム"
    if request.method == "GET":
        return render_template("testapp/reserve.html", webtitle = title)
    if request.method == "POST":
        buycnt = request.form["buycnt"]
        
        title = "予約完了"
        return render_template("testapp/reserve-done.html", webtitle = title, buycnt=buycnt)