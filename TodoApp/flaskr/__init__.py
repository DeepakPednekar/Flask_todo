import os
from _sha1 import sha1

from flask import Flask, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT

from .extension import db, log
from . import models
from . import controller


def create_app(test_config=None):
    app = Flask(__name__)
    db_url = os.path.join(app.instance_path, 'flaskr.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_url)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['DEBUG']=True
    app.config['SECRET_KEY']=sha1(b'for test').hexdigest()
    app.config['JWT_LEEWAY']=216000

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/main')
    def main():
        d = {'type':'+OK', 'msg':'Operation Successfull'}
        return jsonify(d)

    def authenticate(username, password):
        user = models.User.query.filter_by(username=username).first()
        if user.password == sha1(password.encode('utf-8')).hexdigest()[:12]:
            return user
        else:
            return None

    def identity(payload):
        _id = payload['identity']
        return models.User.query.filter_by(id=_id)

    with app.app_context():
        app.register_blueprint(controller.user_bp)
        db.init_app(app)
        db.create_all()
        JWT(app, authenticate, identity)
        Migrate(app, db)

    return app
