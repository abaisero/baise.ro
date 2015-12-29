# -*- coding: utf-8 -*-

from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
posts = FlatPages(app, 'weblog')
