import os

from flask import Flask, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from .extension import db, log

from . import controller

def create_app(test_config=None):
    app = Flask(__name__)
    db_url = os.path.join(app.instance_path, 'flaskr.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.debug=True
    # app.config.from_mapping()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    db.init_app(app)
    log = app.logger

    with app.app_context():
        app.register_blueprint(controller.user_bp)
        db.create_all()


    # log.info('blueprints | %s', app.blueprints.get('user').url_prefix)
    # with app.test_request_context():
        # log.debug('url | %s ', url_for('user.user_root'))


    ## register template


    @app.route('/main')
    def main():
        d = {'type':'+OK', 'msg':'Operation Successfull'}
        return jsonify(d)

    return app
