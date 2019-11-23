from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(250))
    email = db.Column(db.String(250),unique = True,index = True)

    def __repr__(self):
         return f'User {self.username}'
    
