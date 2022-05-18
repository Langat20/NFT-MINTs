from app import db
from datetime import datetime


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    joined_date = db.Column(db.DateTime, default=datetime.now())
    unsubscribed_date = db.Column(db.DateTime, default=datetime.now())
    is_active = db.Column(db.Boolean, default=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def unsubscribe(self):
        self.is_active = False
        db.session.commit()
        return True

    def __repr__(self):
        return self.email
