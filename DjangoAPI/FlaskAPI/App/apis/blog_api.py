from flask import request, g
from flask_restful import Resource, fields, abort, marshal, marshal_with

from App.apis.decrator import permission_required
from App.models.blog_model import Blog

blog_fields = {
    "b_title": fields.String,
    "b_content": fields.String,
    "id": fields.Integer
}


result_fields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(blog_fields))
    # "data": fields.List(fields.String)
}


class BlogsResource(Resource):

    @marshal_with(result_fields)
    def get(self):

        blogs = Blog.query.all()

        print(blogs)

        # str_list = ["123", "456", "789", "900"]

        data = {
            "msg":"ok",
            "status": 200,
            "data": blogs
        }

        return data

    @permission_required("WRITE")
    def post(self):

        content = request.form.get("content")
        title = request.form.get("title")

        blog = Blog()
        blog.b_content = content
        blog.b_title = title
        blog.b_user = g.user.id

        if not blog.save():
            abort(400, msg="can't save")

        data = {
            "msg": "ok",
            "status": 201,
            "data": marshal(blog, blog_fields)
        }

        return data


class BlogResource(Resource):

    def get(self, blog_id):

        blog = Blog.query.get(blog_id)

        data = {
            "msg": "ok",
            "status": 201,
            "data": marshal(blog, blog_fields)
        }

        return data

    @permission_required("WRITE")
    def patch(self, blog_id):

        blog = Blog.query.get(blog_id)

        content = request.form.get("content")
        title = request.form.get("title")

        blog.b_content = content or blog.b_content
        blog.b_title = title or blog.b_title

        if not blog.save():
            abort(400, msg="update fail")

        data = {
            "msg": "ok",
            "status": 201,
            "data": marshal(blog, blog_fields)
        }

        return data
