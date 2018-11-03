from flask import request


def load_middleware(app):

    @app.before_request
    def before():

        print(request.url)
