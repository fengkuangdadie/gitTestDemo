from flask import request, g
from flask_restful import abort

from App.ext import cache
from App.models.user_model import User


def permission_required(permission):

    def check_permission(fun):

        def wrapper(*args, **kwargs):

            token = request.args.get("token")

            if not token:
                abort(400, msg="must login")

            user_id = cache.get(token)

            if not user_id:
                abort(401, msg="status not avaliable token")

            user = User.query.get(user_id)

            if not user:
                abort(401, msg="status not avaliable user")

            if not user.check_permission(permission):
                abort(403, msg="can't write")

            g.user = user
            g.auth = token

            return fun(*args, **kwargs)
        return wrapper
    return check_permission
