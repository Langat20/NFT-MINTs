from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/accounts')
blog = Blueprint('blog', __name__, url_prefix='article')
comment = Blueprint('comment', __name__, url_prefix='article/comment')