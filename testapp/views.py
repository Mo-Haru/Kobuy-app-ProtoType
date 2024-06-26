from testapp import app, db, LoginManager
from flask import render_template,  request, redirect, url_for, flash, Blueprint
from testapp.models.models import Reserve, Menu, User, Notification
from testapp.forms import LoginForm, RegisterForm
from flask_login import UserMixin, login_user, logout_user, login_required

main = Blueprint('main', __name__)

@app.route('/')
def index():
    title = "購買予約アプリ試作版"

    return render_template('testapp/index.html', webtitle = title)

@app.route("/login", methods=['GET', 'POST'])
def login():
    title = "ログイン"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('メールアドレスまたはパスワードが間違っています')
    return render_template('testapp/login.html', form=form, webtitle=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    title = "アカウントの作成"
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        if form.password.data != form.confirm.data:
            flash('パスワードが一致しません')
        else:
            user = User(
                username=form.username.data,
                grade=form.grade.data,
                cls=form.cls.data,
                num=form.num.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'{form.username.data}さん登録ありがとうございます。')
            return redirect(url_for('login'))
    return render_template('testapp/register.html', form=form, webtitle=title)




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
@login_required
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

