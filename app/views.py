from flask import render_template
from app import app, pages

from collections import OrderedDict


class Site(object):

    def __init__(self):
        menu = [
            'home',
            'research',
            'code',
            'about',
        ]

        self.menu = [pages.get(page) for page in menu]

site = Site()


@app.route('/<path:path>/')
@app.route('/', defaults={'path': 'home'})
def page(path):
    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    print 'serving: {}'.format(path)
    page = pages.get_or_404(path)
    return render_template('page.html', site=site, page=page)
