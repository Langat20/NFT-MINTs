from flask import render_template
from app.main.urls import home
from app.nft.models import Nft

# Homepage View


@home.route('/')
def index():
    nfts = Nft.query.order_by(Nft.created_at).limit(3).all()
    return render_template('home/index.html', nfts=nfts)
