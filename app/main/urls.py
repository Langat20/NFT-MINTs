from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
user = Blueprint('user', __name__, url_prefix='/user')
home = Blueprint('home', __name__, url_prefix='/')
profile = Blueprint('profile', __name__, url_prefix='/profile')

from app.profile import views
from app.auth import views
from app.home import views