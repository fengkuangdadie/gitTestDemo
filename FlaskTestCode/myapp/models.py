from myapp.ext import db


class User(db.Model):
    """用户模型"""
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    u_name = db.Column(
        db.String(255),
        nullable=True
    )
    u_phone = db.Column(
        db.String(13),
        nullable=True
    )
    u_password = db.Column(
        db.String(255),
        nullable=False
    )
    u_icon = db.Column(
        db.String(255),
    )
    is_delete = db.Column(
        db.Boolean,
        default=False
    )
    cols = db.relationship(
        "Collection",
        backref="user",
        lazy=True
    )


class Blog(db.Model):
    """博客模型"""
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    b_title = db.Column(
        db.String(255)
    )
    b_content = db.Column(
        db.String(255)
    )
    col = db.relationship(
        "Collection",
        backref="blog",
        lazy=True
    )
    def to_dict(self):
        return {"id": self.id, "b_title":self.b_title, "b_content":self.b_content}


class Collection(db.Model):
    """收藏模型"""
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    #设置与用户  一对多的关联关系
    u_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )
    #设置与博客 一对多的关联关系
    b_id = db.Column(
        db.Integer,
        db.ForeignKey("blog.id")
    )
    __table_args__ = (db.UniqueConstraint("u_id", "b_id", name="u_id_b_id_uin_unique"),)


