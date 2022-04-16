from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    business_type = StringField('type', validators=[DataRequired()])
    submit = SubmitField("Submit")
