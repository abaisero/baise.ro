from flask import render_template
from app import app, pages, posts, ipynbs
from site import site
import pathlib
import datetime


@app.template_filter()
def fmt_date(value):
    return datetime.datetime.strptime(value, '%d.%m.%Y').strftime('%d %b %Y')


@app.route('/weblog/<path:path>/')
def post(path):
    print 'serving WEBLOG {}'.format(path)
    post = posts.get(path)
    if post is None:
        post = ipynbs.get_or_404(path)
    return render_template('post.html', site=site, pname='Weblog', post=post)


@app.route('/ipynb/<path:path>/')
def ipynb(path):
    print 'serving IPYNB {}'.format(path)
    post = ipynbs.get_or_404(path)
    return render_template('ipynb.html', site=site, pname='IPynb', post=post)


@app.route('/<path:path>/')
@app.route('/', defaults={'path': 'home'})
def page(path):
    print 'serving PAGE {}'.format(path)

    # default is page
    template = 'page.html'
    book = pages

    # but weblog has different settings
    p = pathlib.Path(path)
    if len(p.parts) == 1 and p.parts[0] == 'weblog':
        template = 'weblog.html'

    page = book.get_or_404(path)
    return render_template(template, site=site, pname=page.meta['name'], page=page)
