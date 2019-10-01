
from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
# from .forms import ReviewForm,UpdateProfile
from .forms import PitchForm
from ..models import User,Pitch
from flask_login import login_required,current_user
from .. import db,photos

# Review = reviews.Review






# Views
@main.route('/')
def index():

    
    title = 'Home - Welcome to The best Movie Review Website Online'
    pitch =  Pitch.query.filter_by().first()
    description =  Pitch.query.filter_by().first()
    Religion = Pitch.query.filter_by(category="Religion")
    Politics = Pitch.query.filter_by(category="Politics")
    Business = Pitch.query.filter_by(category="Business")
    Innovation = Pitch.query.filter_by(category="Innovation")

    return render_template('index.html', title = title , Religion = Religion ,Politics = Politics ,Business = Business , Innovation = Innovation , description =  description)



@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(id):

    form = CommentForm()

    # pitch = Pitch.query.get(pitch_id)

    if form.validate_on_submit():
        content = form.content.data

        new_comment = Comment(content= content, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment',pitch_id = pitch_id ))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comment.html',form = form, comment = all_comments, pitch = pitch)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
   form = PitchForm()
   # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
   if form.validate_on_submit():
       description = form.description.data
       content = form.content.data
       user_id = current_user
       category = form.category.data
       print(current_user._get_current_object().id)
       new_pitch = Pitch(user_id =current_user._get_current_object().id, content = content , category = category , description = description)
       db.session.add(new_pitch)
       db.session.commit()
       return redirect(url_for('main.index'))
   return render_template('pitches.html',form=form)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)


#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
     

    # return render_template('profile/update.html',form =form)
