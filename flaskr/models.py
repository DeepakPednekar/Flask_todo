from .extension import db


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True) 
   username = db.Column(db.String(80), nullable=False)

   def __repr__(self):
        return '<User {0}>'.format(self.username)