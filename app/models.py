from app import db
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    pwdhash = db.Column(db.String(54))
    
    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def __repr__(self):
       return '<User %s, Email %s, Password %s>' %(self.nickname, self.email, self.pwdhash) 
