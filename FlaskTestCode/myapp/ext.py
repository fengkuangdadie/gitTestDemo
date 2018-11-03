from flask_migrate import Migrate

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
#from flask_login import LoginManager
from myapp import settings
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()


cache = Cache(config={
    'CACHE_TYPE': 'redis',
    "CACHE_REDIS_DB":2,
    "CACHE_REDIS_HOST":"127.0.0.1"
})
mail = Mail()

def init_ext(app):
    #初始化db
    db.init_app(app)

    migrate.init_app(app=app,db=db)

    cache.init_app(app=app)

    mail.init_app(app)


