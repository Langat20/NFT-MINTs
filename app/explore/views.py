from flask import render_template
from app.main.urls import explore

@explore.route('/explore-nfts')
def exploreNFTs():

    return render_template('explore/explore.html')