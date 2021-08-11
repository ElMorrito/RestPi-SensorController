from apps.api.api import ma

from models import Sensor


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensor
        exclude = ('date_created', 'date_modified', 'id')
