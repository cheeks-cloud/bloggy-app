from flask import render_template,request,redirect,url_for
from . import main
from  app.request import get_quotes
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    title = "Welcome to Blogging Application"

    quoteFound = get_quotes()
  
    return render_template('index.html',title=title,quotes = quoteFound)