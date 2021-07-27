from app.extensions import ma
from app.models import SensorCategory


class SensorCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SensorCategory
