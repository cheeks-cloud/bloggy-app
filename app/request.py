import urllib.request,json
from .models import Quote
api_key = None
base_url = None

def configure_request(app):
  global base_url
  base_url = app.config['QUOTE_BASE_URL']

def get_quotes():
  get_quotes_url = base_url

  with urllib.request.urlopen(get_quotes_url)as url:
    get_quotes_data = url.read()
    get_quotes_reponse = json.loads(get_quotes_data) 
    quote_object = None

    if get_quotes_reponse:
      quotes_results = get_quotes_reponse
      quote_object = process_results(quotes_results)
    return quote_object


def process_results(quotes):
  quoteFound= []
  if quotes:
    id =  quotes.get('id')
    quote = quotes.get('quote')
    author = quotes.get('author')
   

    quote_object = Quote(id,quote,author)
    quoteFound.append(quote_object)

  return quoteFound