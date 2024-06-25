from testapp import app, db
from flask import render_template,  request, redirect, url_for, flash
from testapp.models.models import Reserve, Menu
# from testapp.forms import LoginForm
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required


@app.route('/')
def index():
    title = "購買予約アプリ試作版"

    return render_template('testapp/index.html', webtitle = title)

@app.route("/login")
# @app.route("/login", methods=['GET', 'POST'])
def login():
    title = "ログイン"
    # form = LoginForm()
    # if form.validate_on_submit():
    #     #フォーム入力したアドレスがDB内にあるか検索
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user is not None:
    #             #check_passwordはUserモデル内の関数
    #             if user.check_password(form.password.data):
    #                 #ログイン処理。ログイン状態として扱われる。
    #                 login_user(user)
    #                 next = request.args.get('next')
    #                 if next == None or not next[0] == '/':
    #                     next = url_for('user_maintenance')
    #                 return redirect(next)
                    
    #             else:
    #                 flash('パスワードが一致しません')
    #     else:
    #         flash('入力されたユーザーは存在しません')

    # return render_template('testapp/login.html', form=form, webtitle=title)
    return render_template('testapp/login.html', webtitle=title)


@app.route('/logout')
def logout():
    #現在のユーザーをログアウト状態にする
    logout_user()
    return redirect(url_for('login'))



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

