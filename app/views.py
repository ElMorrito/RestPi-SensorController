from flask import Blueprint

app_blueprint = Blueprint(name="app", import_name=__name__)


@app_blueprint.route('/', methods=['GET', ])
def index():
    return "This will be the mainpage"
