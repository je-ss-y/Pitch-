from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

# class ReviewForm(FlaskForm):

#     title = StringField('Review title',validators=[Required()])
#     review = TextAreaField('Movie review', validators=[Required()])
#     submit = SubmitField('Submit')
# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')


class PitchForm(FlaskForm):

    # description = StringField('pitch title',validators=[Required()])
    # title = StringField('pitch title',validators=[Required()])
    content = TextAreaField('Pitch here', validators=[Required()])
    category = RadioField('Label', choices=[ ('Religion','Religion'), ('Politics','Politics'),('Business','Business'),('Innovation','Innovation')],validators=[Required()])
    submit = SubmitField('Submit')
