from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(250))
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    email = db.Column(db.String(250),unique = True,index = True)

    def __repr__(self):
         return f'User {self.username}'
    
class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(200))
    pitch = db.Column(db.String(200))
    time = db.Column(db.String(200))
    users = db.relationship('User',backref = 'pitches',lazy="dynamic")
     
    def __repr__(self):
        return f'User {self.name}'
     



