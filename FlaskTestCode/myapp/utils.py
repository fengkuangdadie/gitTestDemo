import uuid

import hashlib
#from flask import render_template
from flask_mail import Message

from myapp.ext import mail


def enc_pwd(u_password):
    """
    加密密码
    :param pwd: 待加密的密码
    :return: 加密结果 32位16进制的字符串
    """
    md5 = hashlib.md5()
    md5.update(u_password.encode("utf-8"))
    return md5.hexdigest()

def create_rand_str():
    uid_val = uuid.uuid4()
    uid_str = str(uid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uid_str)
    return md5.hexdigest()

def send_mail(tos, host):
    title = "后台注册激活邮件"
    msg = Message(title, sender="493024318@qq.com", recipients=[tos])
    # 生成验证连接的页面
    rand_str = create_rand_str()
    url = "http://{host}/active/{random}".format(
        host=host,
        random=rand_str
    )
    # html = render_template("active.html", url=url)
    #     # msg.html = html
    mail.send(msg)
    return rand_str