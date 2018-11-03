from App.ext import db


class BaseModelNoPrimaryKey(db.Model):
    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True


class BaseModel(BaseModelNoPrimaryKey):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)