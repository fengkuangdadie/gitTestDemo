from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel


class User(BaseModel):

    u_name = db.Column(db.String(32), unique=True)

    _u_password = db.Column(db.String(256))

    is_super = db.Column(db.Boolean, default=False)

    @property
    def u_password(self):
        raise Exception("cant't access")

    @u_password.setter
    def u_password(self, password):
        self._u_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._u_password, password)

    def check_permission(self, permission_name):
        if self.is_super:
            return True
        permissions = UserPermission.query.filter(UserPermission.u_user_id.__eq__(self.id))

        for permission in permissions:
            if Permission.query.get(permission.u_permission_id).p_name == permission_name:
                return True
        return False


class Permission(BaseModel):

    p_name = db.Column(db.String(32), unique=True)


class UserPermission(BaseModel):
    u_permission_id = db.Column(db.Integer, db.ForeignKey(Permission.id))
    u_user_id = db.Column(db.Integer, db.ForeignKey(User.id))