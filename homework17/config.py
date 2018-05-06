# -*- coding: utf-8 -*-

__author__ = 'savelev'


DEBUG = True
SECRET_KEY = 'SavelevSecretKey'

# Database settings:
SQLALCHEMY_DATABASE_URI = 'sqlite:///myblog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False