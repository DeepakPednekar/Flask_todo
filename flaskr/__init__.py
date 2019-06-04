import os

from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/main')
    def main():
        d = {'type':'+OK', 'msg':'Operation Successfull'}
        return jsonify(d)
    return app