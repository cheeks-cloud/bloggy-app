
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import UserMixin
# from . import login_manager

class Quote:
  def __init__(self,id,quote,author)