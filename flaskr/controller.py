from flask import Blueprint, jsonify, request, current_app
from . import extension

log = None
user_bp = Blueprint('user', __name__, url_prefix='/user') 

def user_root():
    if request.method.lower() == 'get':

        d = {'msg': 'Operation Successful GET', 'type':'+OK'}
        return  jsonify(d), 200
    # log.info('user_root | request | %s', request.get_json())
    d = {'msg': 'Operation Successfull', 'type':'+OK'}
    return  jsonify(d), 200

user_bp.add_url_rule('', '', user_root, methods=('GET', 'POST'))
