from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('ログイン')


class RegisterForm(FlaskForm):
    username = StringField('本名', validators=[DataRequired()])
    grade = IntegerField("クラス", validators=[DataRequired()])
    cls = IntegerField("組", validators=[DataRequired()])
    num = IntegerField("番号", validators=[DataRequired()])
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('真新しいパスワード', validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('パスワードの確認', validators=[DataRequired(), Length(min=8), EqualTo('password')])
    submit = SubmitField('アカウントの作成')

    
class ReserveForm(FlaskForm):
    id = IntegerField("ID")
    productname1 = TextAreaField("予約した商品１つ目")
    productname2 = TextAreaField("予約した商品２つ目")
    productname3 = TextAreaField("予約した商品３つ目")
    productname4 = TextAreaField("予約した商品４つ目")
    productname5 = TextAreaField("予約した商品５つ目")