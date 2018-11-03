import uuid

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from App.ext import cache
from App.models import User

user = Blueprint("user", __name__, url_prefix='/users')

LOGIN = "login"

REGISTER = "register"

HTTP_BAD_REQUEST = 400

HTTP_AUTH_FAIL = 920

HTTP_NOT_FOUND = 940

HTTP_OK = 200

HTTP_CREATE_OK = 201

HTTP_CREATE_FAIL = 900


@user.route('/', methods=["POST",])
def users():

    action = request.args.get("action")

    print(action)

    username = request.form.get("username")
    password = request.form.get("password")

    if action == LOGIN:

        user = User.query.filter(User.u_name.__eq__(username)).first()

        if user:
            if user.verify_password(password):
                token = uuid.uuid4().hex

                cache.set(token, user.id, timeout=60*60)

                data = {
                    "status": HTTP_OK,
                    "msg": "login success",
                    "token": token
                }

                return jsonify(data)
            else:

                data = {
                    "status": HTTP_AUTH_FAIL,
                    "msg": "password error"
                }

                return jsonify(data)
        else:

            data = {
                "status": HTTP_NOT_FOUND,
                "msg": "user doesn't exist"
            }

            return jsonify(data)

    elif action == REGISTER:

        user = User()
        user.u_name = username

        # password = generate_password_hash(password)

        user.u_password = password

        data = {}

        if user.save():
            data['status'] = HTTP_CREATE_OK
        else:
            data['status'] = HTTP_CREATE_FAIL

        return jsonify(data)

    else:
        data = {
            "status": HTTP_BAD_REQUEST,
            "msg": "must supply action"
        }

        return jsonify(data)
