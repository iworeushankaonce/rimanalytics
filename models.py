from app import db
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120), index=True)
    def __repr__(self):
        return '<User %r>' % (self.name)