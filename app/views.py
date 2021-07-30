from flask import Blueprint, render_template
import os

from app.api.controller.network_service import hostname, get_local_ip_address

app_template_folder = os.path.join(os.path.dirname(__file__) + '/templates')

app_blueprint = Blueprint(
    name="app", import_name=__name__, template_folder=app_template_folder)


@app_blueprint.route('/', methods=['GET', ])
def index():
    return render_template('index.html', name=hostname, ip=get_local_ip_address())
