from flask import request
from flask_restful import Resource, reqparse

parse = reqparse.RequestParser()
parse.add_argument("name", help="请提供需要的商品名称", required=True)
parse.add_argument("price", type=float, help="请提供商品价钱", required=True)
parse.add_argument("hobby", action="append", dest="hehe")


parse_get = reqparse.RequestParser()

parse_get.add_argument("sessionid", location="cookies")


class GoodsResource(Resource):

    def post(self):

        args = parse.parse_args()

        print(args.get("name"))

        print(args.get("hobby"))

        print(request.args.getlist("hobby"))

        print(request.args)

        print(args.get("hehe"))

        return {"msg": "ok"}

    def get(self):

        args = parse_get.parse_args()

        print(args.get("sessionid"))

        return {"msg": "get ok"}
