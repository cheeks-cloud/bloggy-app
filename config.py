import os
import re
class Config:
   
   QUOTE_BASE_URL="http://quotes.stormconsultancy.co.uk/random.json"
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