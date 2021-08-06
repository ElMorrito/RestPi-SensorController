import os
from flask import Blueprint, render_template

from apps.utils import hostname, get_local_ip_address

app_blueprint = Blueprint(
    name="frontend", import_name=__name__, template_folder='/templates/frontend')


@app_blueprint.route('/', methods=['GET', ])
def index():
    return render_template('index.html', name=hostname, ip=get_local_ip_address())
