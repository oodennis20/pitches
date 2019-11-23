from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250))
    pitches_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    password_secure = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True, index=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.author}'


class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250))
    pitch = db.Column(db.String(250))
    time = db.Column(db.String(250))
    users = db.relationship('User', backref='pitches', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
