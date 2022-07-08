from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError

class TimelinePostForm(FlaskForm):
  name = StringField('Name', validators=[Length(0, 64)])
  email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
  content = TextAreaField('content')
  submit = SubmitField('Submit')