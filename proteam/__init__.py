"""Initialize TVL - Proteam web application"""

from os import getenv
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


# Basic structure of application
def create_app():
    """
    Create and configure Flask app instantiation.
    """
    app = Flask(__name__)

    app.config["SECRET_KEY"] = 'secret-key-goes-here'
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    # app.config[""] - track modifications

    DB.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth
    app.register_blueprint(auth)

    from .main import main
    app.register_blueprint(main)

    return app
