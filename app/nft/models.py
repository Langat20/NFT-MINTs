from app import db
from datetime import datetime
from app.auth.models import User


class Nft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nft_path = db.Column(db.String, nullable=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    royalties = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)
    on_sale = db.Column(db.Boolean, default=True)
    sold_at = db.Column(db.DateTime, nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        return True

    def __repr__(self):
        return self.title
