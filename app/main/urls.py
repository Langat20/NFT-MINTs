from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='/')
auth = Blueprint('auth', __name__, url_prefix='/auth')
profile = Blueprint('profile', __name__, url_prefix='/profile')
user = Blueprint('user', __name__, url_prefix='/user')

from app.home import views
from app.auth import views
from app.create import views
from app.profile import views
