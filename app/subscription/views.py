from flask import request, redirect, flash
from app.main.urls import subscription
from app.subscription.models import Subscription


@subscription.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    subscriber = Subscription(email=email)
    subscriber.save()
    flash("You've successfully subscribed to our subscription")
    return redirect('/')


@subscription.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')
    subscriber = Subscription.query.filter_by(email=email).first()
    if subscriber != None:
        subscriber.unsubscribe()
        flash("Unsubscribed from NFT-MINTs email subscription")
        return redirect('/')
    flash("No such subscriber")
