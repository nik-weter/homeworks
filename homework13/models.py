# -*- coding: utf-8 -*-

from datetime import date
from app import db
class GuestBookItem(db.Model):
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #title = db.Column(db.String(140), unique=True, nullable=False)
    author = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(3000), nullable=False)
    #date_created = db.Column(db.Date, default=date.today)
    date_created = db.Column(db.Date, default=date.today())
    #is_visible = db.Column(db.Boolean, default=True, nullable=False)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post %r, from %s>'.format(self.id, self.author)