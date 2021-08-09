from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_user
from models import Users
auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    error = None

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(
            email=username).first()
        if not user:
            error = "User does not exixts"
            return render_template('login.html', error=error)

        if user.check_password(password):
            login_user(user=user)

        return redirect(url_for('admin.index'))

    return render_template('login.html', error=error)
