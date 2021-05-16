from models import Security
import pandas as pd
import numpy as np
from flask import current_app as app
from models import db


class IndexService(object):
    
    @classmethod
    def get_syntetic_index(cls):
        with app.app_context():
            securities = Security.get_all()
            index_price = [100]
            return_security_array = [
                cls.get_return_per_security(security)
                for security in securities
            ]
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