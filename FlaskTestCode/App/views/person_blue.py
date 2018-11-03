from flask import Blueprint

blue = Blueprint("blue", __name__, url_prefix='/persons')


@blue.route("/")
def index():
    return "Index"

