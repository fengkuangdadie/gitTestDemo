from flask import Flask

from App.ext import init_ext
from App.middleware import load_middleware
from App.settings import envs
from App.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # init config
    app.config.from_object(envs.get(env))

    # init ext
    init_ext(app)

    # load middleware
    load_middleware(app)

    # init router
    init_blue(app)

    return app
