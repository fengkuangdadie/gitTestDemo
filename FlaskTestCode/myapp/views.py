import os

import random
from flask import Blueprint, request, jsonify, session, abort

from myapp.ext import cache, db
from myapp.models import User, Blog, Collection
from myapp.settings import BASE_DIR
from myapp.status_code import *

from myapp.utils import enc_pwd, send_mail, create_rand_str

blue = Blueprint("haha", __name__)

def init_blue(app):
    #注册蓝图
    app.register_blueprint(blue)

"""
用户Api
- 用户手机号注册
- 用户登录（删除用户不可得登录）
- 验证码和密码登录（密码实现数据安全）
- 用户信息修改
- 用户逻辑删除

"""
@blue.route("/register/", methods=["GET", "POST"])
def register_api():
    if request.method == "GET":
        #此处可以重定向到登录页面
        return "注册成功"
    else:
        #解析参数
        params = request.form
        u_phone = params.get("u_phone")
        u_name = params.get("u_name")
        u_password = params.get("u_password")
        email = params.get("email")
        u_icon = request.form.get("u_icon", None)
        #校验参数
        if u_name and u_password and u_phone and len(u_name) > 3 and len(str(u_phone)) == 11:
            #校验手机号
            enc_phone = User.query.filter(User.u_phone == u_phone).all()
            #若为True 则手机号注册过
            if len(enc_phone) == 0:
                # 给密码加密
                enc_pwd_str = enc_pwd(u_password)
                #实例化
                u = User()
                u.u_name = u_name
                u.u_password = enc_pwd_str
                #校验用户头像，若为None，则没上传
                if u_icon == None:
                    return "没上传头像，请上传头像"
                else:
                    #生成唯一头像名字
                    file_name = create_rand_str() + ".jpg"
                    #拼接文保存路径
                    file_path = os.path.join(BASE_DIR, 'static/icon' + file_name)
                    #保存文件
                    file = open(file_path, "wb")
                    for i in u_icon.chunks():
                        u.u_icon = file_path
                        #保存文件路径
                #将用户对象保存到数据库
                db.session.add(u)
                db.session.commit()

                res = send_mail(email, request.host)
                # 设置缓存
                cache.set(res, u.id, 60 * 60)
                data = {
                    "code": SUCCESS,
                    "msg": '注册成功',
                    "data": []
                }
                return jsonify(data)
            else:
                #手机号已被注册
                return jsonify({"code": FAIL, "msg": "手机号已被注册，请换个手机号重新注册", "data":[]})
        else:
            #参数不合适
            return jsonify({"code":NOT_LOGIN, "msg":"参数不对，请核对", "data":[]})

# - 用户登录（删除用户不可得登录）
@blue.route("/login/", methods=["GET", "POST"])
def login_api():
    if request.method == "GET":
        data = {
                    "code": SUCCESS
                }
        return jsonify(data)
    elif request.method == "POST":
        #解析参数
        params = request.form
        u_phone = params.get("u_phone")
        u_password = params.get("u_password")
        # print(u_name)
        # print(u_password)
        #校验数据
        #去数据库拿到用户名
        u = User.query.filter(User.u_phone == u_phone).all()
        if len(u) == 0 or u[0].is_delete == True:
            data = {
                "code":NOT_LOGIN,
                "msg":"用户名不存在",
                "data":[]
            }
            return jsonify(data)
        else:
            #校验用户密码
            if u[0].u_password == enc_pwd(u_password):
                #写入session
                session[u_phone] = u_phone
                data = {
                    "code":SUCCESS,
                    "msg":"登录成功",
                    "data":{
                        "user":u[0].u_phone,
                        "u_icon_url":u[0].u_icon
                    }
                }
                return jsonify(data)
            else:
                data = {
                    "code":NOT_LOGIN,
                    "msg":"登录失败",
                    "data":[]
                }
                return jsonify(data)


#- 密码登录（密码实现数据安全）
@blue.route("/enc_pwd_login", methods=["POST"])
def enc_pwd_login():
    #解析参数
    u_phone = request.form.get("u_phone")
    #校验参数
    if u_phone:
        u = User.query.filter(User.u_phone == u_phone).all()
        if len(u) == 0:
            #用户不存在
            data = {
                "code":PERMISSION_DENY,
                "msg":"用户名不存在",
                "data":[]
            }
            return jsonify(data)
        else:
            #随机生成一个六位数
            random_num = random.randrange(100000, 1000000)
            #发短信，此处不会写，跳过
            #设置缓存， 60*60秒过期
            cache.set(u_phone, random_num,60*60)
            data = {
                "code":SUCCESS,
                "msg":"用户登录验证码，请查收",
                "data":u_phone
            }
            return jsonify(data)
    else:
        #参数错误
        data = {
            "code":NOT_LOGIN,
            "msg":"参数有误，无法操作",
            "data":[]
        }
        return jsonify(data)

#- 用户信息修改
@blue.route("/user_info_modify/", methods=["GET", "POST"])
def user_info_modify():
    if request.method == "GET":
        data = {
            "code":FAIL,
            "msg":"lele",
            "data":[]
        }
        return jsonify(data)
    else:
        #解析参数
        params = request.form
        u_name = params.get("u_name")
        u_password = params.get("u_password")
        u_phone = params.get("u_phone")
        #加密密码
        enc_pwd_two = enc_pwd(u_password)
        #去数据库那对象
        user = User.query.filter(User.u_name == u_name).first()
        user.u_password = enc_pwd_two
        user.u_phone = u_phone
        # 把数据保存到数据库
        db.session.add(user)
        db.session.commit()
        data = {
            "code": SUCCESS,
            "msg": "ok",
            "data": {}
        }
        return jsonify(data)


#用户逻辑删除
@blue.route("/user_delete/", methods=["GET", "POST"])
def user_delete():
    if request.method == "GET":
        data = {
            "code": FAIL,
            "msg": "lele",
            "data": []
        }
        return jsonify(data)
    else:
        #解析参数
        param = request.form
        u_name = param.get("u_name")
        if User.query.filter(User.name == u_name).first():
            # 从数据里获取用户对象
            user = User.query.filter(User.u_name == u_name).first()
            if user.is_delete == 0:
                # 修改用户状态
                user.is_delete = 1
                # 保存到数据库
                db.session.add(user)
                db.session.commit()
                data = {
                    "code": SUCCESS,
                    "msg": "ok",
                    "data": {}
                }
                return jsonify(data)
            else:
                data = {
                    "code": FAIL,
                    "msg": "用户已经是删除状态",
                    "data": {}
                }
                return jsonify(data)
        else:
            data = {
                "code": FAIL,
                "msg": "用户不存在",
                "data": {}
            }
        return jsonify(data)


"""- 博客Api
  - 博客创建
  - 博客修改
  - 博客删除
- 用户，博客结合操作
  - 收藏博客
  - 获取某用户的所有收藏
  - 获取收藏某博客的所有用户
"""


#博客创建
@blue.route("/create_blog/")
def create_blog():
    b = Blog()
    b.b_title = "flask很难受"
    b.b_content = "django更难受"

    #添加博客到数据库
    db.session.add(b)
    #提交
    db.session.commit()
    return b.b_title, b.b_content

#博客修改
@blue.route("/modify/")
def modify():
    res = Blog.query.filter_by(id=1)
    res.b_title = "lala"
    res.b_content = "hehe"
    return "ok"

#博客删除
@blue.route("/delete/")
def blog_delete_one():
    #先做查询，在做删除
    blog = Blog.query.filter_by(id=1).first()
    db.session.delete(blog)
    #提交操作
    db.session.commit()
    return "fire吼"

#收藏博客
@blue.route("/collect_one/<int:uid>/<int:bid>")
def collect_one(uid, bid):
    data = Collection(
        user = uid,
        blog = bid
    )
    db.session.add(data)
    db.session.commit()
    return "收藏成功"

# 获取某用户   的所有收藏
@blue.route("/get_user_all_collect/<int:cid>")
def get_user_all_collect(cid):
    collection = Collection.query.get(cid)
    cols = collection.cols
    return "前端你给我把数据赶快送过来"

#获取收藏某博客   的所有用户
@blue.route("/get_collect_all_user/<int:uid>")
def get_collect_all_user(uid):
    res = Collection.query.filter(Collection.my_user == uid)
    print(res[0])
    return "buxiaodeduibudui"





