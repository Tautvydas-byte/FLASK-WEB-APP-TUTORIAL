from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    return app  # returnina app'sas
