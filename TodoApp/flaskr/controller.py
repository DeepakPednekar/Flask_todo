from flask_jwt import jwt_required
from flask import Blueprint, jsonify, request, current_app
from . import extension

from . import models
from .extension import db

import logging
import _sha1

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

user_bp = Blueprint('user', __name__, url_prefix='/user') 

@user_bp.route('', methods=['GET','POST'])
@jwt_required()
def user_root():
    if request.method.lower() == 'get':
        data = models.User.query.all()
        data = [each.get_json() for each in data]
        d = {'msg': 'Operation Successful GET', 'type':'+OK', 'return': data}
        return  jsonify(d), 200
    _json = request.get_json() 

    if not _json:
        d = {'type':'-ERR', 'msg':'json not found'}
        return jsonify(d), 404

    if 'username' not in _json.keys() or 'email' not in _json.keys():
        d = {'type':'-ERR', 'msg':'username or email not found'}
        return jsonify(d), 404

    _json['password'] = _sha1.sha1(_json.get('password').encode('utf-8')).hexdigest()[:12] 
    print(_json)
    user = models.User(**_json)
    db.session.add(user)
    db.session.commit()
    data = models.User.query.all()
    d = {'msg': 'Operation Successfull', 'type':'+OK'}
    return  jsonify(d), 200

def sendResponse(success=False, msg=''):
    d = {}
    d['msg'] = msg
    code = 401
    if success:
        code=200
    return jsonify(d) 

@user_bp.route('test')
def test():
    log.debug('this is test request ')
    print('controller | ', id(log))
    d = {'msg': 'Operation Successfull', 'type':'+OK'}
    return  jsonify(d), 200

#user_bp.add_url_rule('', '', user_root, methods=('GET', 'POST'))
