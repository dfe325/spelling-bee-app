from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    letter = StringField('Letter', validators=[DataRequired(), Length(max=10, message=('Too many letters.'))])
    submit = SubmitField('Submit')