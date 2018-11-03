from flask_restful import Api

from App.apis.blog_api import BlogsResource, BlogResource
from App.apis.goods_api import GoodsResource
from App.apis.permission_api import PermissionsResource
from App.apis.user_api import UsersResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(UsersResource, "/users/")
api.add_resource(PermissionsResource, "/permissions/")

api.add_resource(BlogsResource, "/blogs/")
api.add_resource(BlogResource, "/blogs/<int:blog_id>/")

api.add_resource(GoodsResource, "/goods/")