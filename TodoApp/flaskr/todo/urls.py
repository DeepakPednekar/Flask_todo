from flask import Blueprint
from .controller import *

bp_todo = Blueprint('todo', __name__, url_prefix='/todo')

bp_todo.add_url_rule('/', 'root', root, methods=['GET'])
bp_todo.add_url_rule('test', 'test', test, methods=['GET'])