from flask import render_template
from app.main.urls import explore
from app.nft.models import Nft


@explore.route('/explore-nfts')
def exploreNFTs():
    nfts = Nft.query.all()
    return render_template('explore/explore.html', nfts=nfts)
