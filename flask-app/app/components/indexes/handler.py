'''
Created on 12 may. 2021
@author: victorgrubio
'''
import traceback
from flask import Blueprint, jsonify
from flask import current_app as app
from components.indexes.service import IndexService
from dto.responses import SynteticIndexReponse


indexes_blueprint = Blueprint("indexes", __name__, url_prefix="/indexes/")


@indexes_blueprint.get('/synthetic')
def get_syntetic_index():
    status = 200
    try:
        values = IndexService.get_syntetic_index()
        response = SynteticIndexReponse(values=values)
    except Exception as e:
        app.logger.error(traceback.print_exc())
        app.logger.error(e)
        status=500
        response='Internal server error'
    return jsonify(response), status
