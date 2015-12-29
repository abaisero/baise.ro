from flask import render_template
from app import app, pages, posts
from site import site
import pathlib
import datetime


@app.template_filter()
def fmt_date(value):
    return datetime.datetime.strptime(value, '%d.%m.%Y').strftime('%d %b %Y')


@app.route('/weblog/<path:path>/')
def post(path):
    print 'serving WEBLOG {}'.format(path)
    post = posts.get_or_404(path)
    return render_template('post.html', site=site, pname='weblog', post=post)


@app.route('/<path:path>/')
@app.route('/', defaults={'path': 'home'})
def page(path):
    print 'serving PAGE {}'.format(path)

    # default is page
    html = 'page.html'
    book = pages

    # but weblog has different settings
    p = pathlib.Path(path)
    if len(p.parts) == 1 and p.parts[0] == 'weblog':
        html = 'weblog.html'

    page = book.get_or_404(path)
    return render_template(html, site=site, pname=page.meta['name'], page=page)
