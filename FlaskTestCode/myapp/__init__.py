from flask import Flask

from myapp import settings
from myapp.ext import init_ext
from myapp.views import init_blue


def create_app(env_name="debug"):
    #初始化app
    app = Flask(__name__)
    app.config.from_object(settings.config.get(env_name))
    init_ext(app)
    init_blue(app)
    return app