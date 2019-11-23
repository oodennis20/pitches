from . import db

class User(db.model)
    __tablename__='users'
    
    id = id.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),index = True)
    email = db.Column(db.String(25),unique = True,index = True)

    
    
    
    
    
    