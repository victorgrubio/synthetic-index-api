from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer, Float, DateTime, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import Null
from models import db


class Security(db.Model):

    __tablename__ = 'Security'
    id_security = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)

    @staticmethod
    def get_by_id(id):
        return Security.query.get(id)
    
    @staticmethod
    def get_all():
        return Security.query.all()



@db.event.listens_for(Security, "after_insert")
def recalculate_index(mapper, connection, target):
    app.logger.info('NEW SECURITY INDEX')

# class SecuritySchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Security
#         load_instance = True