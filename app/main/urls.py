from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='/')
auth = Blueprint('auth', __name__, url_prefix='/auth')
profile = Blueprint('profile', __name__, url_prefix='/profile')
favorites = Blueprint('favorites', __name__, url_prefix='/favorites')
user = Blueprint('user', __name__, url_prefix='/user')
subscription = Blueprint('subscription', __name__, url_prefix='/subscription')

from app.home import views
from app.auth import views
from app.home import views
from app.favorites import views
from app.nft import views
from app.profile import views
from app.subscription import views
