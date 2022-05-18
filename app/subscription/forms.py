from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import Email


class SubscribeForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    submit = SubmitField("Subscribe")
