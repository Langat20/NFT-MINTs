from flask import render_template
from app.main.urls import explore
from app.nft.models import Nft


@explore.route('/explore-nfts/<string:category>/')
def explore_nfts(category):
    category = category.upper()
    print(category)
    if category == 'ALL':
        nfts = Nft.query.order_by(Nft.created_at).all()

    else:
        nfts = Nft.query.order_by(Nft.created_at).filter_by(
            category=category).all()
    return render_template('explore/explore.html', nfts=nfts)
