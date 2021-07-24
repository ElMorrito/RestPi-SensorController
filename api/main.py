from flask import Blueprint
from flask import json, request
import markdown
import os


from api.views.device import api_device_bp
from api.views.sensors import api_sensor_bp

api_blueprint = Blueprint(name='api', import_name=__name__, url_prefix='/api')
api_blueprint.register_blueprint(api_device_bp)
api_blueprint.register_blueprint(api_sensor_bp)


@api_blueprint.route("/")
def index():
    with open(os.path.dirname(api_blueprint.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)
