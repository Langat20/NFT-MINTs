from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
user = Blueprint('user', __name__, url_prefix='/user')
home = Blueprint('home', __name__, url_prefix='/')

from app.create import views
from app.auth import views
from app.home import views