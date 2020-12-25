"""User Authentication"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import DB

auth = Blueprint('auth', __name__)


@auth.route('/')
@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)
    return redirect(url_for("main.home"))


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/register', methods=["POST"])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.register'))

    new_user = User(email=email, name=name, password=generate_password_hash(
                                                    password, method='sha256'))

    DB.session.add(new_user)
    DB.session.commit()

    return redirect(url_for("auth.login"))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
