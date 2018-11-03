from App.views.blog_blue import blog
from App.views.order_blue import order
from App.views.person_blue import blue
from App.views.user_blue import user


def init_blue(app):
    app.register_blueprint(blue)
    app.register_blueprint(user)
    app.register_blueprint(blog)
    app.register_blueprint(order)




