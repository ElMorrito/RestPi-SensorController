
from flask import jsonify, Blueprint, request

from app.extensions import db
from app.schemas import SensorCategorySchema
from app.models import Sensor, SensorCategory
from service.sensor_service import get_temp_sensors


api_sensor_bp = Blueprint(
    'api_sensor_bp', import_name=__name__, url_prefix='/sensors')


@api_sensor_bp.get('/')
def sensor_list():
    sensors = get_temp_sensors()
    return jsonify(*sensors)


@api_sensor_bp.route('/categories', methods=['GET', 'POST'])
def category_list():

    if request.method == 'POST':

        name = request.get_json()['name']
        if name is None:
            return jsonify(message="name is required"), 400

        category = SensorCategory(name=name)
        db.session.add(category)
        db.session.commit()

        resp = {
            "name": category.name,
            "id": category.id,
            "created_at": category.date_created
        }
        return jsonify(resp), 201
    else:
        categories = SensorCategory.query.all()
        category_schema = SensorCategorySchema()
        return jsonify(category_schema.dump(categories, many=True)), 200
