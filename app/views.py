from flask import Blueprint, render_template
import os

from service.sensor_service import get_temp_sensors

app_template_folder = os.path.join(os.path.dirname(__file__) + '/templates')

print(app_template_folder)
app_blueprint = Blueprint(
    name="app", import_name=__name__, template_folder=app_template_folder)

sensors = get_temp_sensors()


@app_blueprint.route('/', methods=['GET', ])
def index():
    return render_template('index.html', sensors=sensors)
