from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
    blog = TextAreaField('Blog', validators=[InputRequired()])
    author = TextAreaField('Blog author ', validators=[InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    about = TextAreaField('Comment content', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class UpdateBlog(FlaskForm):
    update = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
