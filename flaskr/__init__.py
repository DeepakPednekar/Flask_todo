import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from .extension import db, log

def create_app(test_config=None):
    app = Flask(__name__)
    db_url = os.path.join(app.instance_path, 'flaskr.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllit://'.join([db_url])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.debug=True
    # app.config.from_mapping()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    db.init_app(app)
    log = app.logger

    log.info('sql path | %s', 'sqllit://'.join([db_url]))

    @app.route('/main')
    def main():
        d = {'type':'+OK', 'msg':'Operation Successfull'}
        return jsonify(d)
    return app
