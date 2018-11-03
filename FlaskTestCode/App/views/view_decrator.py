from flask import request, abort, g

from App.ext import cache
from App.models import User


def login_required(fun):

    def wrapper(*args, **kwargs):

        token = request.args.get("token")
        # data = {}

        if not token:

            abort(400)

        user_id = cache.get(token)

        if not user_id:
            abort(401)

        user = User.query.get(user_id)

        if not user:
           abort(401)

        g.user = user
        g.auth = token

        return fun(*args, **kwargs)

    return wrapper


def permission_required(permission):

    def check_permission(fun):

        def wrapper(*args, **kwargs):

            token = request.args.get("token")
            # data = {}

            if not token:
                abort(400)

            user_id = cache.get(token)

            if not user_id:
                abort(401)

            user = User.query.get(user_id)

            if not user:
                abort(401)

            if not user.check_permission(permission):
                abort(403)

            g.user = user
            g.auth = token

            return fun(*args, **kwargs)

        return wrapper
    return check_permission

