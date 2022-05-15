from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class Quote:
  def __init__(self,id,quote,author):
    self.id = id
    self.quote = quote
    self.author = author

class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique=True,index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  blog = db.relationship('Post',backref = 'users',lazy="dynamic")
  comment = db.relationship('Comment',backref = 'users',lazy="dynamic")
 

  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
      self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id)) 

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    blog = db.Column(db.Text,nullable=False)
    author = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='posts',lazy='dynamic')

    def get_blogs():
        blogs = Blog.query.all()
        return blogs

    def get_author(self,id):
        author = User.query.filter_by(id=id).first()
        return author.username

    def get_comments(self,blog):
        all_comments = Comment.query.filter_by(blog=blog).all()
        return all_comments

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.Text,nullable=False)
    blog = db.Column(db.Integer,db.ForeignKey('posts.id'))
    author = db.Column(db.Integer,db.ForeignKey('users.id'))
   
   
    def get_author(self,id):
        author = User.query.filter_by(id=id).first()
        return author.username

    def get_post(self):
        blog = Blog.query.filter_by(id=self.id).first()
        return blog