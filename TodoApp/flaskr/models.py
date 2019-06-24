from .extension import db
from .todo.models import *


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(20), nullable=True, default='')
   username = db.Column(db.String(80), nullable=False)
   email = db.Column(db.String(80), nullable=False)
   password = db.Column(db.String(20))
   todo = db.relationship('Todo', backref='user', lazy=True)

   def __repr__(self):
        return '<User {0}>'.format(self.username)

   def get_json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'name':self.name}