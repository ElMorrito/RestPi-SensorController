from apps.api.api import ma

from models import Sensors


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensors
        exclude = ('date_created', 'date_modified', 'id')
