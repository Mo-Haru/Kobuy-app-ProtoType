from testapp import db
from testapp import create_app
create_db = 0         # 0(app.run) or 1(create database)

app = create_app()

if __name__ == '__main__':
    if create_db == 0:
        app.run()
    if create_db == 1:
        with app.app_context():
            db.create_all()
