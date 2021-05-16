from flask.globals import request
from models import Security, SecurityPrice
import pandas as pd
import numpy as np
from flask import current_app as app
from models import db


class IndexService(object):
    
    @classmethod
    def get_syntetic_index(cls):
        # Add app context to work with db
        with app.app_context():
            # Get securities
            securities = Security.get_all()
            # Get index price
            index_price = [100]
            # Get returns per security
            return_security_array = [
                cls.get_return_per_security(security)
                for security in securities
            ]
            # Compute the index
            for index, item in enumerate(return_security_array[:]):
                index_price.append(index_price[index]*(1+sum(item)))
            return index_price


    @staticmethod
    def get_return_per_security(security):
        sql_df = pd.read_sql(
            """SELECT date, price FROM Security_price s
                JOIN (SELECT MAX(ss.date) 'maxtimestamp'
                FROM Security_price ss
                GROUP BY date(ss.date)) m 
                ON m.maxtimestamp = s.date and s.id_security = {0};""".format(
                    security.id_security
                ),
            con=db.engine,
            parse_dates=[
                'date'
            ]
        )
        array = sql_df['price'].to_numpy()
        # Apply return per security (ponderated)
        security_return = [security.weight*(item/array[i] - 1) for i, item in enumerate(array[1:])]
        app.logger.info(f'{security.name}: RETURN {security_return}')
        return security_return
    
    def add_data(request_dto):
        items = []
        for item in request_dto.values:
            security_price = SecurityPrice()
            for key, value in item.items():
                setattr(security_price, key, value)
            items.append(security_price)
        app.logger.info(f'Inserted into database: {request_dto.values}')
        db.session.bulk_save_objects(items)
        db.session.commit()