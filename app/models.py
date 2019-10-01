from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref='roles',lazy="dynamic")


    # def __repr__(self):
    #     return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitch=db.relationship('Pitch',backref='users',lazy ="dynamic")
    comments=db.relationship('Comment',backref='users',lazy ="dynamic")

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    description = db.Column(db.String(255))
    # upvote = db.Column(db.String(255))
    # downvote = db.Column(db.String(255))
    category = db.Column(db.String(255))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch' , lazy = 'dynamic')

    



    @classmethod
    def get_pitches(cls,id):
        pitches = pitches.query.order_by(pitch_id).desc().all()
        return pitches


    def __repr__(self):
        return f'User {self.pitch}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(15))
    content = db.Column(db.String(100) )            
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
       return f"Comment : id: {self.id} comment: {self.content}"






