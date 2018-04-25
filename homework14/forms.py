# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        include = [
            'post_id',
        ]