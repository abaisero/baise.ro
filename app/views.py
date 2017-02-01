import os
import pathlib
import datetime

from flask import render_template, request, abort
from app import app, pages, posts, notebooks
from site import site

import bibtexparser
from collections import defaultdict

# import views_rubus

### Adding useful filter to jinja2
import jinja2
jinja2.filters.FILTERS['basename'] = os.path.basename
###

import nbformat
import nbconvert
import pygments
from traitlets.config import Config


# # TODO is this used?
# def my_highlight(source, language='ipython'):
#     formatter = pygments.formatters.HtmlFormatter(cssclass='highlight-ipynb')
#     return nbconvert.filters.highlight._pygments_highlight(source, formatter, language)


@app.template_filter()
def fmt_date(value):
    return datetime.datetime.strptime(value, '%d.%m.%Y').strftime('%d %b %Y')


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



@app.route('/weblog/<path:path>/')
def post(path):
    print 'serving WEBLOG {}'.format(path)
    post = posts.get(path)
    if post is None:
        post = notebooks.get_or_404(path)
    return render_template('post.html', site=site, pname='Weblog', post=post)


@app.route('/notebook2html/<fname>')
def notebook2html(fname):
    fpath = '{}/notebooks/{}'.format(app.config['STATIC_DIR'], fname)
    try:
        notebook = nbformat.read(fpath, 4)
    except IOError:
        abort(404)

    # c = Config({'CSSHtmlHeaderTransformer':
    #                 {'enabled':True, 'highlight_class':'highlight-ipynb'}})
    # exportHtml = nbconvert.HTMLExporter(config=c, filters={'highlight': my_highlight})

    config = Config({'HTMLExporter': {'default_template': 'basic'}})
    exportHtml = nbconvert.HTMLExporter(config=config)
    body, resources = exportHtml.from_notebook_node(notebook)
    return body


@app.route('/<path:path>/')
@app.route('/', defaults={'path': 'home'})
def page(path):
    print 'serving PAGE {}'.format(path)

    # default is page
    template = 'page.html'

    # but weblog has different settings
    p = pathlib.Path(path)
    if len(p.parts) == 1 and p.parts[0] == 'weblog':
        template = 'weblog.html'

    page = pages.get_or_404(path)
    return render_template(template, site=site, pname=page.meta['name'], page=page)

@app.route('/research/publications/')
def publications():
    print 'serving PUBLICATIONS'

    #Load file
    bibfname = '{}/docs/refs.bib'.format(app.config['STATIC_DIR'])
    with open(bibfname, 'r') as bibfile:
        bp = bibtexparser.load(bibfile)
    references = sorted(bp.get_entry_list(), key=lambda x: x['year'], reverse=True)        
    refs = defaultdict(list)

    #Preprocess the references
    for r in references:
        if 'labels' in r:
            r['keywordlist'] = r['labels'].split(',')        
        if 'booktitle' in r:
            r['booktitle'] = r['booktitle'].replace('\&', '&amp;')
        r['title'] = r['title'].replace('\&', '&amp;')
        refs[r['year']].append(r)

    page = pages.get_or_404('research/publications')

    #Sort years
    refsbyyear = sorted(refs.items(), key=lambda x: x[0], reverse=True)       
    return render_template('publications.html', site=site, pname='research', page=page, references = refsbyyear)
