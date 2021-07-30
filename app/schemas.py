from app.extensions import ma
from app.models import Sensor


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensor
