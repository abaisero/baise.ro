from flask import render_template, request, abort
from app import app, pages, posts, ipynbs
from site import site
import pathlib
import datetime

import nbformat
import nbconvert
import pygments
from traitlets.config import Config


def my_highlight(source, language='ipython'):
    formatter = pygments.formatters.HtmlFormatter(cssclass='highlight-ipynb')
    return nbconvert.filters.highlight._pygments_highlight(source, formatter, language)


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


@app.route('/ipynb2html/<fname>')
def ipynb2html(fname):
    fpath = '{}/ipynb/{}'.format(app.config['STATIC_DIR'], fname)
    try:
        notebook = nbformat.read(fpath, 4)
    except IOError:
        abort(404)

    # c = Config({'CSSHtmlHeaderTransformer':
    #                 {'enabled':True, 'highlight_class':'highlight-ipynb'}})
    # exportHtml = nbconvert.HTMLExporter(config=c, filters={'highlight': my_highlight})
    exportHtml = nbconvert.HTMLExporter()
    body, resources = exportHtml.from_notebook_node(notebook)
    return body


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
