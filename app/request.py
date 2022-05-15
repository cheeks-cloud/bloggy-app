import urllib.request,json
from .models import Quote
api_key = None
base_url = None

def configure_request(app):
  global api_key,base_url
  api_key = app.config['']
  base_url = app.config['']

def get_quotes():
  get_quotes_url = base_url .format(x,api_key)

  with urllib.request.urlopen(get_quotes_url)as url:
    get_quotes_data = url.read()
    get_quotes_reponse = json.loads(get_quotes_data) 
    quotes_results = None

    if get_quotes_reponse['results']:
      quotes_results_list = get_quotes_reponse['results']
      quotes_results  = process_results(quotes_results_list)

  return quotes_results


# def process_results(quote_list):
#   quotes_results = []
#   for quote_item in quote_list:
#     id =  quote_item.get('id')
#     quote = quote_item.get('quote')
#     author = quote_item.get('author')
   
#     if id:
#       quote_object = Quote(id,quote,author)
#       quotes_results.append(quote_object)

#   return quotes_results 