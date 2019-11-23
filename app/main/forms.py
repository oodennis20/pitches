from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):

 category = StringField('Choose category', choices=[('coding', 'coding'), ('life', 'life'), ('funny', 'funny')])

 pitch = TextAreaField('Pitch')

 submit = SubmitField('Submit')