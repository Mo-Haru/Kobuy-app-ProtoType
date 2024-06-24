from testapp import app, db

create_db = 1 #    0(app.run) or 1(create database)

if __name__ == '__main__':
    if create_db == 0:
        app.run()
    if create_db == 1:
        with app.app_context():
            db.create_all()
