from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# from testapp.models.models import User

app = Flask(__name__)
app.config.from_object('testapp.config')
db = SQLAlchemy(app)


migrate = Migrate(app, db)
#インスタンス化
login_manager = LoginManager()
#アプリをログイン機能を紐付ける
login_manager.init_app(app)
#未ログインユーザーを転送する(ここでは'login'ビュー関数を指定)
login_manager.login_view = 'users.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def create_app():
    # Blueprintやその他の初期化処理はここで行います
    from testapp.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app




from testapp.models import models

# import testapp.views
