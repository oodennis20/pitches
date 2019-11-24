from flask import render_template
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Pitches, User
from . import main
from .. import db,photos
from .forms import PitchForm, CommentForm, UpdateProfile


@main.route('/')
def index():
    '''
    my index page
    return
    '''
    message = "Hello"
    return render_template('index.html', message=message)


@main.route('/pitch/', methods=['GET', 'POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data

        # Updated pitchinstance
        new_pitch = Pitches(category=category, pitch=pitch,user_id=current_user.id)

        title = 'New Pitch'

        # save review method
        new_pitch.save_pitch()

    return render_template('pitch.html', pitch_entry=form)


@main.route('/categories/<cate>')
def category(cate):
    '''
    function to return the pitches by category
    '''
    category = Pitches.get_pitches(cate)
    # print(category)
    title = f'{cate}'
    return render_template('categories.html', title=title, category=category)


@main.route('/categories/<pitches_id>', methods=['GET', 'POST'])
@login_required
def new_comment():

    pitches = Pitches.query.get_or_404(pitches_id)
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        # Updated pitchinstance
        new_comment = CommentVote(comment=comment, post=post, pitches_id=pitches_id, user_id=current_user.id)

        title = 'New comment'

        new_comment.save_comment()

    return render_template('categories.html', comment_form=form)


@main.route('/categories/<pitches_id>')
def comment(pitches_id):
    '''
    function to return the comments by pitch id
    '''
    comment = CommentVote.get_comments(pitches_id)
    # print(category)
    title = f'{pitches_id}'
    return render_template('categories.html', title=title, comment=comment)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.author))

    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

