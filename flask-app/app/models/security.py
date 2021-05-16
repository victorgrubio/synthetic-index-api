from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer, Float, DateTime, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import Null
from sqlalchemy.sql.schema import ForeignKey
from models import db


class Security(db.Model):

    __tablename__ = 'Security'
    id_security = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)

    @staticmethod
    def get_all():
        return Security.query.all()


class SecurityPrice(db.Model):

    __tablename__ = 'Security_price'
    id_security_price = Column(Integer, primary_key=True, autoincrement=True)
    id_security = Column(Integer, ForeignKey("Security.id_security"))
    price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now(), nullable=False)

