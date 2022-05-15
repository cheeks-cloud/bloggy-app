from flask import render_template,request,redirect,url_for,abort
from . import main
from  app.request import get_quotes
from ..models import Comment,User,Blog
from .forms import CommentForm,UpdateProfile,BlogForm
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():
    title = "Welcome to Blogging Application"

    quoteFound = get_quotes()
  
    return render_template('index.html',title=title,quotes = quoteFound)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.update_profile',uname=user.username))

    return render_template('profile/update.html',form =form)
  