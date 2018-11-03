from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.middleware import load_middleware
from App.settings import envs


def create_app(env):
    app = Flask(__name__)

    # init config
    app.config.from_object(envs.get(env))

    # init ext
    init_ext(app)

    # load middleware
    load_middleware(app)

    # init router
    init_api(app)

    return app
