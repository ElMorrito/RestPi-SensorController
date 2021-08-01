from app.extensions import ma
from app.database.models import Sensor


class SensorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sensor
