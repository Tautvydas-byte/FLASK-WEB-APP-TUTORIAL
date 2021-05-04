from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()  # create database
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)  # represent the name of the file
    app.config['SECRET_KEY'] = 'gtghtth'  # encrypt session data or cookies
    # where is database located {valuated as string everything}
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # use this app with database

    from .views import views  # importina blueprint is views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note  # importing Classes

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # dirrect if user not login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # knows that searching by id, do not need id=id
        return User.query.get(int(id))

    return app  # returnina app'sas


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

# import .models as models - 'as' because cannot referance User class like .models.User
