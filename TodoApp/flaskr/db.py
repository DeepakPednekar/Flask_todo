import sqlite3

from flask_sqlalchemy import SQLAlchemy
from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = SQLAlchemy(current_app.config['SQLALCHEMY_DATABASE_URI']) 

    print('db | ', g)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    print('db is | {0} | {1}'.format(db, type(db)))
    # if db not None:
        # db.close()

def init_db(app):
    # db = SQLAlchemy(app)
    # db.create_all()
    db = get_db()
    print('app | ', app)
