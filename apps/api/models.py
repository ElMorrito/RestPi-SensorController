from apps.extensions import ma

from database.models import Sensor
from flask_marshmallow import Marshmallow
from flask_security import Security


#ma = Marshmallow()


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensor
        exclude = ('date_created', 'date_modified', 'id')
