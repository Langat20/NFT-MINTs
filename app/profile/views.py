from flask import render_template
from app.create.models import Nft
from app.main.urls import user


@user.route('profile/<string:user_id>/')
def profile(user_id):
    nfts = Nft.query.filter_by(user_id=user_id).first()
    return render_template('profile.html', nfts=nfts)
