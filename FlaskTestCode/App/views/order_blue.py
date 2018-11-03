from flask import Blueprint

from App.views.view_decrator import login_required

order = Blueprint("order", __name__, url_prefix='/orders')


@order.route('/')
@login_required
def orders():
    return "duo shou duo shou"