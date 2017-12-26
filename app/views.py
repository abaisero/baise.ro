import os
from pathlib2 import Path
import datetime

import flask

# from app import app, pages, posts, notebooks
from app import app, pages, posts

# import bibtexparser
from collections import defaultdict

import nbformat
import nbconvert

#  Allows for slash-less urls to work seamlessly
app.url_map.strict_slashes = False
@app.before_request
def clear_trailing():
    rp = flask.request.path
    if rp != '/' and rp.endswith('/'):
        return flask.redirect(rp[:-1])


import re
@app.template_filter()
def tagify(string, pattern, tag):
    return re.sub(pattern, '<{}>{}</{}>'.format(tag, pattern, tag), string)


@app.context_processor
def utility_processor():
    def notebook(post):
        fpath = '{}/notebooks/{}.ipynb'.format(app.config['STATIC_DIR'], post.meta['notebook'])
        try:
            notebook = nbformat.read(fpath, 4)
        except IOError:
            flask.abort(404)

        exportMarkdown = nbconvert.MarkdownExporter()
        body, resources = exportMarkdown.from_notebook_node(notebook)

        import re
        for png in resources['outputs'].keys():
            new_png = re.sub('output', post.meta['notebook'], png)
            new_png = flask.url_for('static', filename='notebooks/{}_files/{}'.format(post.meta['notebook'], new_png))
            body = re.sub(png, new_png, body)

        from flask_flatpages.utils import pygmented_markdown
        return pygmented_markdown(body, posts)
        return body

    return dict(notebook=notebook)


@app.route('/<path:ppath>')
@app.route('/', defaults={'ppath': 'home'})
def page(ppath):
    app.logger.info('Serving PAGE {}'.format(ppath))
    page = pages.get_or_404(ppath)
    active = page.meta['name']
    return flask.render_template('page.html', active=active, page=page)


@app.route('/weblog')
def weblog():
    app.logger.info('Serving WEBLOG')
    page = pages.get_or_404('weblog')
    active = page.meta['name']
    posts_display = (post for post in posts if not post.meta.get('nopost', False))
    weblogs = sorted(
        posts_display,
        # key = lambda post: datetime.datetime.strptime(post.meta['date'], '%d.%m.%Y'),
        # key = lambda post: datetime.datetime.strptime(post.meta['date'], '%Y-%m-%d'),
        key = lambda post: post.meta['date'],
        reverse = True,
    )
    return flask.render_template('weblog.html', active=active, page=page, weblogs=weblogs)


@app.route('/weblog/<pname>')
def post(pname):
    app.logger.info('Serving WEBLOG {}'.format(pname))
    post = posts.get_or_404(pname)

    _notebook = post.meta.get('notebook', False)
    if _notebook:
        notebook = '{}.ipynb'.format(_notebook)
        notebook_md = '{}.md'.format(_notebook)

        post.meta['_notebook'] = notebook
        post.meta['_notebook_md'] = notebook_md
        post.meta['_notebook_url'] = flask.url_for('static', filename='notebooks/{}'.format(notebook))
        post.meta['_notebook_md_url'] = flask.url_for('static', filename='notebooks/{}'.format(notebook_md))

    return flask.render_template('post.html', active='weblog', post=post)


# @app.route('/research/publications')
# def publications():
#     print 'serving PUBLICATIONS'

#     #Load file
#     bibfname = '{}/docs/pubs/refs.bib'.format(app.config['STATIC_DIR'])
#     with open(bibfname, 'r') as bibfile:
#         bp = bibtexparser.load(bibfile)
#     references = sorted(bp.get_entry_list(), key=lambda x: x['year'], reverse=True)
#     refs = defaultdict(list)

#     #Preprocess the references
#     for r in references:
#         if 'labels' in r:
#             r['keywordlist'] = r['labels'].split(',')
#         if 'booktitle' in r:
#             r['booktitle'] = r['booktitle'].replace('\&', '&amp;')
#         r['title'] = r['title'].replace('\&', '&amp;')
#         refs[r['year']].append(r)

#     page = pages.get_or_404('research/publications')

#     #Sort years
#     refsbyyear = sorted(refs.items(), key=lambda x: x[0], reverse=True)
#     return flask.render_template('publications.html', active='research', page=page, references=refsbyyear)


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from pybtex.database import BibliographyData
from pybtex.database.input import bibtex
from pybtex.database.output.bibtex import Writer


def _bibentry_bibtex(entry):
    """ Return the bibtex representation of the entry.  """
    bib_data = BibliographyData(entries={entry.key: entry})
    bibtex_repr = StringIO()
    Writer().write_stream(bib_data, bibtex_repr)
    return bibtex_repr.getvalue()


def _bibentry_authors(entry):
    print(entry.persons)
    """ Return the list of authors as nicely formated string.  """
    authors = [author.last_names[0] for author in entry.persons['author']]
    return ', '.join(authors)

def _bibentry_has_mp4(entry):
    """ Return link to video, if it exists """
    fpath = 'docs/pubs/{}/{}.mp4'.format(entry.key, entry.key)
    fpath = flask.safe_join(app.config['STATIC_DIR'], fpath)
    return os.path.exists(fpath)

@app.context_processor
def pub_processor():
    return dict(
        pub_authors=_bibentry_authors,
        pub_has_mp4=_bibentry_has_mp4,
        pub_bibtex=_bibentry_bibtex,
    )


# TODO make better 404 template
@app.errorhandler(404)
def page_not_found(e):
    app.logger.info('DEBUGGING')
    return flask.render_template('404.html'), 404

@app.route('/research/publications/<key>')
def pub(key):
    flask.abort(404)

@app.route('/research/publications/<key>.pdf')
def pub_pdf(key):
    return app.send_static_file('docs/pubs/{}/{}.pdf'.format(key, key))

@app.route('/research/publications/<key>.mp4')
def pub_mp4(key):
    return app.send_static_file('docs/pubs/{}/{}.mp4'.format(key, key))

@app.route('/research/publications')
def publications():
    app.logger.info('Serving publications')

    page = pages.get_or_404('research/publications')

    fname = '{}/docs/pubs/refs.bib'.format(app.config['STATIC_DIR'])
    publications = bibtex.Parser().parse_file(fname)

    return flask.render_template('publications.html', active='research', page=page, publications=publications)


# setup global menu variable
@app.before_first_request
def setup_menu():
    global menu
    menu = map(pages.get, [
        'home',
        'research',
        'teaching',
        'code',
        'weblog',
        'about',
    ])

# inject menu list into templates
@app.context_processor
def inject_menu():
    return dict(menu=menu)
