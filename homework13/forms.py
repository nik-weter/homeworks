# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import GuestBookItem

class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBookItem