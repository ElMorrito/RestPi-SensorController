from app.extensions import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    date_modified = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class Sensor(BaseModel):

    model_name = db.Column(db.String(255), default="")
    manufacturer_id = db.Column(db.String(255), default="")
    description = db.Column(db.String(255), default="")

    category_id = db.Column(db.Integer, db.ForeignKey('sensor_category.id'),
                            nullable=False)
    sensor_category = db.relationship('SensorCategory',
                                      backref=db.backref('Sensors', lazy=True))

    def __repr__(self):

        if self.model_name != "":
            return "{}".format(self.model_name)
        else:
            return " Sensor {}".format(self.id)


class SensorCategory(BaseModel):
    name = db.Column(db.String(255), default="None", nullable=False)

    def __repr__(self):
        return "{}".format(self.name)
