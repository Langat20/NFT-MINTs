from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class ProfileForm(FlaskForm):
    profile_image = FileField("Upload File", validators=[DataRequired()])
    submit = SubmitField("CREATE NFT", validators=[DataRequired()])
