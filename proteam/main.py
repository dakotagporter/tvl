from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import DB

main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.name)


@main.route("/inventory")
@login_required
def inventory():
    return render_template("inventory.html")
