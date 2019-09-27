
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
    Religion = Pitch.query.filter_by(category="Religion")
    Politics = Pitch.query.filter_by(category="Politics")
    Business = Pitch.query.filter_by(category="Business")
    Innovation = Pitch.query.filter_by(category="Innovation")

    return render_template('index.html', title = title , Religion = Religion ,Politics = Politics ,Business = Business , Innovation = Innovation )


# @main.route('/movie/<int:id>')
# def movie(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     movie = get_movie(id)
#     title = f'{movie.title}'
#     reviews = Review.get_reviews(movie.id)

#     return render_template('movie.html',title = title,movie = movie,reviews = reviews)



# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)


# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):

#     form = ReviewForm()

#     movie = get_movie(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data

#         new_review = Review(movie.id,title,movie.poster,review)
#         new_review.save_review()

#         return redirect(url_for('.movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
   form = PitchForm()
   # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
   if form.validate_on_submit():
    #    description = form.description.data
       content = form.content.data
       user_id = current_user
       category = form.category.data
       print(current_user._get_current_object().id)
       new_pitch = Pitch(user_id =current_user._get_current_object().id, content = content , category = category)
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
