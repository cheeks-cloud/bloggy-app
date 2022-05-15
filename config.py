import os
import re
class Config:
   
  #  QUOTE_API_BASE_URL = "/{}?api_key={} "
  #  QUOTE_API_KEY = os.environ.get("MOVIE_API_KEY")
   SECRET_KEY = os.environ.get("SECRET_KEY") 
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:cheeks@localhost/watchlist'


class ProdConfig(Config):
    pass 

class DevConfig(Config):
    DEBUG = True



config_options = {
    "development":DevConfig,
    "production":ProdConfig
}