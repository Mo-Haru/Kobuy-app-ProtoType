from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('testapp.config')

# #インスタンス化
# login_manager = LoginManager()
# #アプリをログイン機能を紐付ける
# login_manager.init_app(app)
# #未ログインユーザーを転送する(ここでは'login'ビュー関数を指定)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

db = SQLAlchemy(app)
from testapp.models import models

import testapp.views
