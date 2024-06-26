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
    syohin = IntegerField("予約した商品")
    
