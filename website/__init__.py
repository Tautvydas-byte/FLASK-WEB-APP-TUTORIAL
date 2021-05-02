from flask import Flask


def create_app():
    app = Flask(__name__)  # represent the name of the file
    app.config['SECRET_KEY'] = 'gtghtth'  # encrypt session data or cookies

    from .views import views  # importina blueprint is views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app  # returnina app'sas
