# -*- coding: utf-8 -*-

from datetime import date

from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(140))
    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True)

    def __str__(self):
        return '<Post %r>' % self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id'),
        nullable=False,
        index=True
    )

    post = db.relationship(Post, foreign_keys=[post_id, ])

    user = db.Column(db.String(140))
    #date_created = db.Column(db.Date, default=date.today)
    content = db.Column(db.String(300), nullable=False)

    def __str__(self):
        return '<Comment %r>' % self.content