from flask_wft import FlaskForm
from wtforms import StringField, TextField, FileField, IntegerField,  SubmitField, ValidationError
from wtforms.validators import DataRequired


class NftForm(FlaskForm):
    nft_image = FileField("Upload File", validators=[DataRequired])
    title = StringField("eg:- Crypto Funk", validators=[DataRequired])
    category = StringField("Enter category", validators=[DataRequired])
    description = TextField(
        "eg:- This is a very limited item description", validators=[DataRequired])
    price = IntegerField("Enter price for the item", validators=[DataRequired])
    royalties = IntegerField("Enter amount in %", validators=[DataRequired])
    submit = SubmitField("CREATE NFT", validators=[DataRequired])
