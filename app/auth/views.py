from flask import render_template, redirect, url_for, flash, request
from app.main.urls import auth
from .forms import RegisterForm, LoginForm
from .models import User
from flask_login import login_user, login_required, logout_user


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            user_email = User.query.filter_by(email=email).first()
            if user_email:
                flash("Email or username is already in use")
                return render_template('auth/signup.html', form=form)
            username = form.username.data
            password = form.password.data
            user = User(username=username, email=email, password=password)
            user.save()
            flash("Account created successfully")
            return redirect(url_for('auth.login'))
        flash("Wrong email or password. Please try again")
    return render_template('auth/signup.html', form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None and user.verify_password(password):
                login_user(user, form.remember_me)
                flash("Logged In Successfully!")
                return redirect(request.args.get('next') or url_for('user.profile', user_id=user.id))
        flash('Invalid email or password')
    return render_template('auth/login.html', form=form)


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    flash("Logged Out Successfully!")
    return redirect(url_for('home.index'))
