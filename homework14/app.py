# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    from models import Post, Comment
    from forms import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')

    posts = Post.query.all()
    for post in posts:
        print(post.author, post.title)

        print(post.content)

    return render_template('home.txt', posts=posts)

@app.route('/<id>', methods=['GET', 'POST'])
def home(id):
    from models import Post, Comment
    from forms import PostForm, CommentForm
    if request.method == 'POST':
        print(request.form)
        form = CommentForm(request.form)

        if form.validate():
            comment = Comment(**form.data)
            db.session.add(comment)
            db.session.commit()

            flash('Comment created!')

    post = Post.query.filter_by(id=id)
    comments = Comment.query.filter_by(post_id=id)
    return render_template('comments.txt', post=post, comments=comments)

if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()