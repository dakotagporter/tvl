from flask import Blueprint, render_template
from . import DB

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/profile")
def inventory():
    return render_template("profile.html")
