from flask import render_template,request,redirect,url_for,abort
from . import main
from  app.request import get_quotes
from ..models import Comment,User,Blog
from .forms import CommentForm,UpdateProfile,BlogForm,UpdateBlog
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():
    title = "Welcome to Blogging Application"

    quoteFound = get_quotes()
  
    return render_template('index.html',title=title,quotes = quoteFound)

@main.route('/blogs/display')
def display():
    title = "Welcome to Blogging Application"
 
    return render_template('display.html',title=title)

@main.route('/blog/<blog_id>/update')
@login_required
def updatedblog(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    form = UpdateBlog
    if form.validate_on_submit(form):
        blog.updated = form.updated.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.updatedblog',blog_id=blog.id))

    return render_template('update.html',form=form)


@main.route('/<blog_id>/',methods=['GET','DELETE'])
@login_required
def deleteBlog(blog_id):
    blogDeleted = Blog.query.filter_by(id=blog_id).first()

    if blogDeleted:
        db.session.delete(blogDeleted)
        db.session.commit()

        return redirect(url_for('main.index'))

    else:
        pass
    return redirect(url_for('main.display'))



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

@main.route('/post',methods=['GET','POST'])
@login_required
def write_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog= form.blog.data,author = current_user.id)
    
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('auth.profile',uname=current_user.username))


    return render_template('blogs.html',form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('auth.profile',uname=uname)) 

@main.route('/comment/<comment_id>/add/comment', methods = ['GET','POST'])
@login_required
def newComment(comment_id):
    form = CommentForm() 
    if form.validate_on_submit():
        about = form.about.data 
        new_comment = Comment(about=about,author=current_user.id,blog=comment_id)
        db.session.add(new_comment)
        db.session.commit()
       
        return redirect(url_for('main.index'))
  
    return render_template('auth/comments.html',comment_form=form)

@main.route('/<blog_id>/<comment_id>/',methods=['GET','DELETE'])
@login_required
def deleteComment(comment_id):
    commentToDelete = Comment.query.filter_by(comment_id=comment_id).first()

    if commentToDelete:
        db.session.delete(commentToDelete)
        db.session.commit()
        return redirect(url_for('main.index'))
