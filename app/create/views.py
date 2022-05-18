from flask import render_template, redirect, url_for, request, flash
from app.create.models import Nft
from app.create.forms import NftForm
from app.auth.models import User
from app.main.urls import user
from app import photos


@user.route('/<int:user_id>/nft/create', methods=['GET', 'POST'])
def create_nft(user_id):
    nft_form = NftForm()
    if request.method == 'POST':
        user = User.query.filter_by(id=user_id).first()
        if nft_form.validate_on_submit():
            filename = photos.save(request.files['photo'])
            image_path = f"photos/{filename}"
            title = nft_form.title.data
            category = nft_form.category.data
            description = nft_form.description.data
            price = nft_form.price.data
            royalties = nft_form.royalties.data
            nft = Nft(title=title, description=description, category=category,
                      price=price, royalties=royalties, nft_image_path=image_path)
            nft.save()
            return redirect(url_for('user.profile', user_id=user_id))

        flash("Please fill the form with the correct details")
    return render_template('profile.html')
