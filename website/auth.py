from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# url path XX/login


# metodai kuriuos gales pasiekti
# POST kai submit, is URL uzkrauna pagal GET
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form  # url, methods info prilyginami
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  # if by id then id=id
        if user:
            if check_password_hash(user.password, password):
                flash('Login in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('email does not exist', category='error')

    return render_template("login.html", text="Testing", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])  # only POST request
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()  # if by id then id=id
        if user:
            flash('Email already exists', category='error')
        if len(email) < 4:
            # pass  # use it as a placeholder
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name='firs_name',
                            password=generate_password_hash(password1, method='sha256'))  # creting new user, password koduoja sha256 formatu
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            # could be just '/', but then if change home url function, then need to change there also
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

# pass - Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future.
#  They cannot have an empty body. The interpreter would give an error.
#  So, we use the pass statement to construct a body that does nothing.
