from testapp import app, db
from flask import render_template, request
from testapp.models import reserve

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
        reserve = reserve(
            reserver="a",
            e_mail="a",
            reserve_dic={"唐揚げ": buycnt}
        )
        db.session.add(reserve)
        db.session.commit()
        title = "予約完了"
        return render_template("testapp/reserve-done.html", webtitle = title, buycnt=buycnt)