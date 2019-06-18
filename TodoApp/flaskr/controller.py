from flask import Blueprint, jsonify, request, current_app
from . import extension
from . import models
from .extension import db, log

log = None
user_bp = Blueprint('user', __name__, url_prefix='/user') 

def user_root():
    log.info('user_root | request | %s', request)
    if request.method.lower() == 'get':
        data = models.User.query.all()
        d = {'msg': 'Operation Successful GET', 'type':'+OK'}
        return  jsonify(d), 200
    _json = request.get_json() 
    print('json', _json)
    if not _json:
        d = {'type':'-ERR', 'msg':'json not found'}
        return jsonify(d), 404

    if 'username' not in _json.keys() or 'email' not in _json.keys():
        d = {'type':'-ERR', 'msg':'username or email not found'}
        return jsonify(d), 404

    models.User(**_json)
    db.session.commit()
    d = {'msg': 'Operation Successfull', 'type':'+OK'}
    return  jsonify(d), 200

def sendResponse(success=False, msg=''):
    d = {}
    d['msg'] = msg
    code = 401
    if success:
        code=200
    return jsonify(d) 

user_bp.add_url_rule('', '', user_root, methods=('GET', 'POST'))
