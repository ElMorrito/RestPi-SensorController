from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_user, logout_user
from models import User
from apps.auth.forms import LoginForm

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(email=username).first()
        # Check is user exists or password is not correct.
        if user is None or not user.check_password(password):
            flash("invalid credentials", category="error")

        if login_user(user):
            return redirect(url_for("admin.index"))
        return render_template("login.html", form=form)

    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("admin.index"))
