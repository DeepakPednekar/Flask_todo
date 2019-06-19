from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

log = None

def get_logger(name):
    return log.getLogger(name)