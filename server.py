from testapp import app, db

<<<<<<< HEAD
create_db = 0         # 0(app.run) or 1(create database)
=======
create_db = 0 #    0(app.run) or 1(create database)
>>>>>>> 37601d0496e98080aead6e4b7ab9ba4b94baf2f9

if __name__ == '__main__':
    if create_db == 0:
        app.run()
    if create_db == 1:
        with app.app_context():
            db.create_all()
