'''
Created on 12 may. 2021
@author: victorgrubio
'''
import json
import config as cfg
from flask import Blueprint, abort, request

from dto.responses import SynteticIndexReponse


indexes = Blueprint(cfg.BLUEPRINT_NAME, __name__, url_prefix="/indexes/")


@indexes.route('/syntetic', methods=['GET'])
def get_syntetic_index():
    status = 200
    try:
        response = SynteticIndexReponse()
    except Exception as e:
        print(e)
        status=500
        response=json.dumps({'Internal server error'})
    return response, status