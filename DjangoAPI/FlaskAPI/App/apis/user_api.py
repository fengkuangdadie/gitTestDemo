import uuid

from flask import request
from flask_restful import Resource, abort, marshal, fields

from App.ext import cache
from App.models.user_model import User
from App.settings import ADMINS

user_fields = {
    "u_name": fields.String,
    "u_password": fields.String(attribute="_u_password"),
    "u_age": fields.Integer(default=5)
}

result_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "token": fields.String,
    "url": fields.Url("usersresource", absolute=True, scheme="https"),
    "data": fields.Nested(user_fields)
}


class UsersResource(Resource):

    def post(self):

        action = request.args.get("action")

        username = request.form.get("username")
        password = request.form.get("password")

        if action == "register":

            user = User()
            user.u_name = username
            user.u_password = password

            if username in ADMINS:
                user.is_super = True

            if not user.save():
                abort(401)

            data = {
                "msg": "create ok",
                "status": 201
            }

            return data
        elif action == "login":

            user = User.query.filter(User.u_name.__eq__(username)).first()

            if not user:
                abort(404, msg="user doesn't exist")

            if not user.verify_password(password):
                abort(401, msg="password error")

            token = uuid.uuid4().hex

            cache.set(token, user.id, timeout=60*60)

            data = {
                "msg": "login success",
                "status": 200,
                "token": token,
                "data":user
            }

            return marshal(data, result_fields)
        abort(400, msg="must supply action")
