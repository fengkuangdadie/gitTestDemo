from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db


class Person(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    p_name = db.Column(db.String(32), unique=True)

    p_age = db.Column(db.Integer, default=1)


USER_PERMISSION_READ = 1
USER_PERMISSION_WRITE = 2
USER_PERMISSION_DELETE = 4


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    u_name = db.Column(db.String(32), unique=True)

    _u_password = db.Column(db.String(256))

    u_permission = db.Column(db.Integer, default=USER_PERMISSION_READ)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def check_permission(self, permission):
        return self.u_permission & permission == permission

    def verify_password(self, password):
        return check_password_hash(self._u_password, password)

    @property
    def u_password(self):
        raise Exception("can't access")

    @u_password.setter
    def u_password(self, password):
        self._u_password = generate_password_hash(password)

