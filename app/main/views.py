from flask import render_template
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Pitches, User
from . import main
from .. import db
from .forms import PitchForm

@main.route('/')
def index():
    '''
    my index page
    return
    '''
    message= "Hello"
    return render_template('index.html', message=message)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():
    
    form = PitchForm()
    
    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data


        # Updated pitchinstance
        new_pitch = Pitches(category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        # save review method
        new_pitch.save_pitch()

    return render_template('pitch.html',pitch_entry= form)

@main.route('/categories/<cate>')
def category(cate):
    '''
    function to return the pitches by category
    '''
    category = Pitches.get_pitches(cate)
    # print(category)
    title = f'{cate}'
    return render_template('categories.html',title = title, category = category)

@main.route('/categories/<int:pitches_id>', methods=['GET','POST'])
def comment(pitches_id):
    pitches = Pitches.query.get_or_404(pitches_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comments(comment=comment, post=post, user_id=current_user.id)
        db.session.add(new_pitches_comment)
        db.session.commit()
    comments = CommentsPitches.query.all()
    title = 'comments'
    return render_template('comments.html', title=title, pitches=pitches, pitches_form=form, comments=comments)













