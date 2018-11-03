import os
from redis import StrictRedis

#from manager import app


class Config():
    DEBUG = False
    #设置session密匙
    SECRET_KEY = "pofuchenzhoubaierqinguanzhongshuchu"
    # 设置连接的redis数据库 默认连接到本地6379
    SESSION_TYPE = "redis"
    # 设置远程
    #app.config['SESSION_REDIS'] = StrictRedis(host="127.0.0.1", db=1)
    # 设置修改追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #发送邮件的相关配置
    MAIL_SERVER="smtp.qq.com"
    MAIL_PORT=465
    MAIL_USERNAME="493024318@qq.com"
    MAIL_PASSWORD = "yaricwaaydxvbggb"
    MAIL_USE_SSL=True
    # MAIL_USE_TLS=True

#定义系统路径的变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(db_conf):
    #配置mysql数据库
    uri = "{db}+{engine}://{user}:{pwd}@{host}:{port}/{name}".format(
        db=db_conf.get("DB"),
        engine=db_conf.get("ENGINE"),
        user=db_conf.get("USER"),
        pwd=db_conf.get("PWD"),
        host=db_conf.get("HOST"),
        port=db_conf.get("PORT"),
        name=db_conf.get("NAME")
    )
    return uri


class DebugConfig(Config):
    DEBUG = True
    DATABASE = {
        "DB":"mysql",
        "ENGINE": "pymysql",
        "USER": "root",
        "PWD":"111",
        "HOST": "10.0.120.113",
        "PORT": 3306,
        "NAME":"TestDatabase"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


config = {
    "debug": DebugConfig
}