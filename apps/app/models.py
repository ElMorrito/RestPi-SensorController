from database.database import db
from database.models import BaseModel


class Sensor(BaseModel):
    name = db.Column(db.String(255), default="", unique=True)
    sensor_id = db.Column(db.String(255), default="",
                          nullable=False, unique=True)
    sensor_category = db.Column(db.String(255), default="Not specified")

    def __repr__(self):
        return "{}".format(self.sensor_id)
