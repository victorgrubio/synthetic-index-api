'''
Created on 12 may. 2021
@author: victorgrubio
'''
import traceback
from flask import Blueprint, jsonify, request
from flask import current_app as app
from components.indexes.service import IndexService
from dto.requests import SyntheticIndexData
from dto.responses import SyntheticIndexReponse


indexes_blueprint = Blueprint("indexes", __name__, url_prefix="/indexes/")


@indexes_blueprint.get('/synthetic')
def get_syntetic_index():
    status = 200
    try:
        values = IndexService.get_syntetic_index()
        response = SyntheticIndexReponse(values=values)
    except Exception as e:
        app.logger.error(traceback.print_exc())
        app.logger.error(e)
        status=500
        response='Internal server error'
    return jsonify(response), status

@indexes_blueprint.post('/synthetic/data')
def add_data_to_db():
    status = 200
    try:
        body_data = request.get_json()
        request_dto = SyntheticIndexData(**body_data)
        IndexService.add_data(request_dto)
        response = 'OK'
    except Exception as e:
        app.logger.error(traceback.print_exc())
        app.logger.error(e)
        status=500
        response='Internal server error'
    return jsonify(response), status