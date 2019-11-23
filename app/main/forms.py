from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    category = SelectField(u'Pitch category', choices=[('coding', 'coding'), ('life', 'life'), ('funny', 'funny')])
        
    pitch = TextAreaField('Pitch')

    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('content')
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


