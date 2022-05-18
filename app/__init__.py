from flask import Flask
from app.config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES


db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)


def create_app(config_environment):
    app = Flask(__name__)
    app.config.from_object(config_options[config_environment])
    db.init_app(app)
    configure_uploads(app, photos)
    # login_manager.init_app(app)

    # Register blueprint
    from app.main.urls import home, auth, user, profile, subscription
    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(profile)
    app.register_blueprint(subscription)

    return app
