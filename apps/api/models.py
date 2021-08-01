from apps.extensions import ma

from apps.app.models import Sensor


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensor
        exclude = ('date_created', 'date_modified', 'id')
