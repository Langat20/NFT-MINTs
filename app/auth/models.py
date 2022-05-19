from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    nfts = db.relationship('Nft', backref='user', lazy=True)
    profile_pic_path = db.Column(db.String, nullable=True, unique=True)

    @property
    def password(self):
        raise AttributeError('No attribute password')

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def reset_password(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return self.username
