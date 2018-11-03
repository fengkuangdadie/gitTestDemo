from App.ext import db
from App.models import BaseModel
from App.models.user_model import User


class Blog(BaseModel):

    b_content = db.Column(db.String(1000))
    b_title = db.Column(db.String(128))
    b_user = db.Column(db.Integer, db.ForeignKey(User.id))