from flask_sqlalchemy import SQLAlchemy
from flask import make_response
import json

db = SQLAlchemy()

log = None

def get_logger(name):
    return log.getLogger(name)


def sendResponse(msg="", data={}, **kwargs):
    _data = {}
    status = kwargs.get('status')

    if msg:
        _data['msg'] = msg

    if status:
        _data['msg'] ="Operation Successfull" if not _data.get('msg') else _data.get('msg')
        _data['code'] = 200
        _data['type'] = "+OK"
    else:
        _data['msg'] = "Error in operation" if not _data.get('msg') else _data.get('msg')
        _data['code'] = 501
        _data['type'] = "-ERR"

    if data:
        _data['return'] = data

    response = make_response(json.dumps(_data))
    response.headers['Content-Type'] = 'application/json'

    return response
