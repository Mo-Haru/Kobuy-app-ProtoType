from testapp import app, db
from flask import render_template, request
from testapp.models.models import Reserve, Menu

@app.route('/')
def index():
    title = "購買予約アプリ試作版"

    return render_template('testapp/index.html', webtitle = title)

@app.route("/menu")
def menu():
    title = "購買メニュー"
    return render_template("testapp/menu.html", webtitle = title)

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    if request.method == "GET":
        title = "お問い合わせフォーム"
        return render_template("testapp/contact.html", webtitle = title)
    if request.method == "POST":
        title = "お問い合わせ完了"
        return render_template("testapp/contact-done.html", webtitle = title)




@app.route("/reserve", methods = ["GET", "POST"])
def reserve():
    title = "購買予約フォーム"
    if request.method == "GET":
        return render_template("testapp/reserve.html", webtitle = title)
    if request.method == "POST":
        buycnt = request.form["buycnt"]
        reserver_name = request.form["name"]
        reserver_e_mail = request.form["e_mail"]
        reserve = Reserve(
            reserver=reserver_name,
            e_mail=reserver_e_mail,
            resreve_dic=f"唐揚げ{buycnt}個"
        )
        db.session.add(reserve)
        db.session.commit()
        title = "予約完了"
        print(f"名前：{reserver_name}, メールアドレス：{reserver_e_mail}, 唐揚げを{buycnt}個頼みました。")
        return render_template("testapp/reserve-done.html", webtitle = title, buycnt=buycnt)
    

@app.route("/reserve_list")
def reserve_list():
    reserve = Reserve.query.all()
    return render_template("/testapp/reserve_list.html", reserve=reserve)