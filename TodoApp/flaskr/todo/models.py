from flaskr.extension import db
from flaskr.models import *


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todoItems = db.relationship('TodoItem', backref='todo', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Todo %s>'.format(self.id)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'), nullable=False)

    def __repr__(self):
        return '<TodoItem %s>'.format(self.title)

    def get_json(self):
        return {'id': self.id, 'title': self.title, 'description': self.description}