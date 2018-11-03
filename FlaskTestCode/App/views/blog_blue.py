from flask import Blueprint, request, jsonify, g

from App.ext import cache
from App.models import User, USER_PERMISSION_READ, USER_PERMISSION_WRITE
from App.views.view_decrator import login_required, permission_required

blog = Blueprint("blog", __name__ ,url_prefix="/blogs")


@blog.route("/", methods = ["GET", "POST", "DELETE"])
@permission_required(USER_PERMISSION_WRITE)
def blogs():

    # token = request.args.get("token")
    # data = {}
    #
    # if not token:
    #     data['status'] = 400
    #     return jsonify(data)
    #
    # user_id = cache.get(token)
    #
    # if not user_id:
    #
    #     data["status"] = 401
    #
    #     return jsonify(data)
    #
    # user = User.query.get(user_id)
    #
    # if not user:
    #
    #     data['status'] = 401
    #
    #     return jsonify(data)

    # user = User.query.get(cache.get(request.args.get("token")))

    # user = g.user
    # data = {}
    #
    # method = request.method
    #
    # if method == "GET":
    #     # if user.u_permission & USER_PERMISSION_READ == USER_PERMISSION_READ:
    #     if user.check_permission(USER_PERMISSION_READ):
    #         data['status'] = 200
    #         data['msg'] = 'ok'
    #         return jsonify(data)
    #     else:
    #         data['status'] = 403
    #         data['msg'] = "permission deny"
    #         return jsonify(data)
    # elif method == "POST":
    #     pass
    # elif method == "DELETE":
    #     pass

    data = {
        "msg": "ok",
        "status": 200
    }

    return jsonify(data)

