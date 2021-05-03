from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# url path XX/login


# metodai kuriuos gales pasiekti
# POST kai submit, is URL uzkrauna pagal GET
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form  # url, methods info prilyginami
    # print(data)
    return render_template("login.html", text="Testing", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])  # only POST request
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstname = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            # pass  # use it as a placeholder
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')

    return render_template("sign_up.html")

# pass - Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future.
#  They cannot have an empty body. The interpreter would give an error.
#  So, we use the pass statement to construct a body that does nothing.
