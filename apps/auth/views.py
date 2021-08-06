from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')


@auth_bp.route('/login')
def login_user():

    return render_template('login.html')
