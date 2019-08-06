from flaskr.extension import db
from flaskr.models import *


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, index=True)
    description = db.Column(db.String(20), nullable=False, default='')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return '<Todo %s>'.format(self.id)

    def get_json(self):
        return {'id': self.id, 'title':self.title, 'description':self.description, 'user_id':self.user_id}
