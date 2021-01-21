from flask import Blueprint, render_template
from flask_login import login_required, current_user
import sqlite3 as sql


main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.name)


@main.route("/inventory")
@login_required
def inventory():
    inv = []
    try:
        conn = sql.connect("./inv_db.sqlite3")
        cur = conn.cursor()
        results = cur.execute(
            "SELECT product_id, description FROM inventory").fetchall()
        for result in results:
            inv.append(f"{result[0]} - {result[1]}")
    except:
        print("ERROR")
    return render_template("inventory.html", products=inv)


@main.route("/inventory", methods=["POST"])
@login_required
def inventory_post():
    pass
