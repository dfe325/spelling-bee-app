from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    letter = StringField('Letter', validators=[DataRequired(), Length(min=1, max=1)])
    submit = SubmitField('Get Answers')