import os
import re
class Config:
   SQLCHEMY_TRACK_MODIFICATIONS = True 
   QUOTE_BASE_URL="http://quotes.stormconsultancy.co.uk/random.json"
   SECRET_KEY = os.environ.get("SECRET_KEY") 
   UPLOADED_PHOTOS_DEST = 'app/static/photos'
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
   MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
      SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")
      if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://')

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:cheeks@localhost/blogs' 
    DEBUG = True



config_options = {
    "development":DevConfig,
    "production":ProdConfig
}