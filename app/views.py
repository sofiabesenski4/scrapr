from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    text = StringField('name', validators=[DataRequired()])
    place_type = StringField('type', validators=[DataRequired()])
