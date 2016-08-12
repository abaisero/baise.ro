#!/usr/bin/env python

from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
posts = FlatPages(app, 'weblog')
ipynbs = FlatPages(app, 'ipynb')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> cca7916baee0a51c790990f7a1ea9aec5d1cbe31
