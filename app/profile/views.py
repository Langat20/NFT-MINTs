from flask import render_template, request, redirect, url_for, flash
from app.create.models import Nft
from app.main.urls import user
from app.auth.models import User
from .forms import ProfileForm
from app import photos


@user.route('profile/<string:user_id>/')
def profile(user_id):
    nfts = Nft.query.filter_by(user_id=user_id).first()
    return render_template('profile/profile.html', nfts=nfts)


@user.route('profile/<string:user_id>/update/', methods=['POST'])
def update_profile(user_id):
    profile_form = ProfileForm()
    if request.method == 'POST':
        user = User.query.filter_by(id=user_id).first()
        if profile_form.validate_on_submit():
            filename = photos.save(request.files['photo'])
            user.profile_pic_path = f"photos/{filename}"
            user.update()
            return redirect(url_for('user.profile'))
        flash("Please enter correct form details and try again")
    return redirect(url_for('user.profile', user_id=user_id))
