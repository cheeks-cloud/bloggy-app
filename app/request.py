import urllib.request,json
# from .models import 
api_key = None
base_url = None

def configure_request(app):
  global api_key,base_url
  api_key = app.config['']
  base_url = app.config['']