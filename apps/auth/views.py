from flask import Blueprint


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login_user():

    return 'youre now logged in'
