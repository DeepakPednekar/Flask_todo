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

@user_bp.route('', methods=['GET'])
@jwt_required()
def user_root():
    userid = request.args.get('id')
    if userid:
        data = models.User.query.filter_by(id=userid).first()
        data = data.get_json() if isinstance(data, models.User) else {}
        status = 1 if data else 0
        return extension.sendResponse(data=data, status=status)

    data = models.User.query.all()
    data = [each.get_json() for each in data]
    return extension.sendResponse(data=data, status=1)

@user_bp.route('test')
def test():
    log.debug('this is test request ')
    print('controller | ', id(log))
    d = {'msg': 'Operation Successfull', 'type':'+OK'}
    return  jsonify(d), 200

@user_bp.route('register', methods=['POST'])
def register():
    ## check fields
    _json = request.get_json()
    if not _json:
        return extension.sendResponse(msg='Json not found', status=0)

    keys = _json.keys() 
    for each in ['email', 'name', 'password', 'username']:
        if each not in keys:
            return extension.sendResponse(msg='Keys not found', status=0)

    _json['password'] = _sha1.sha1(_json.get('password').encode('utf-8')).hexdigest()[:12] 
    user = models.User(**_json)
    db.session.add(user)
    db.session.commit()
    data = models.User.query.all()
    return extension.sendResponse(status=1)
