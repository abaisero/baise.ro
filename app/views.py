import os
import pathlib2
import datetime

from flask import g, render_template, url_for, request, abort
# from app import app, pages, posts, notebooks
from app import app, pages, posts

# import bibtexparser
from collections import defaultdict

# import views_rubus

### Adding useful filter to jinja2
import jinja2
jinja2.filters.FILTERS['basename'] = os.path.basename
###

import nbformat
import nbconvert

#  Allows for slash-less urls to work seemlessly
app.url_map.strict_slashes = False
@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path 
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

@app.template_filter('fmt_date')
def fmt_date_filter(value):
    return datetime.datetime.strptime(value, '%d.%m.%Y').strftime('%d %b %Y')

import re
@app.template_filter('boldify')
def boldify_filter(text, author):
    return re.sub(author, '<span class="pub-mainauthor">{}</span>'.format(author), text)


@app.context_processor
def utility_processor():
    def notebook(post):
        fpath = '{}/notebooks/{}.ipynb'.format(app.config['STATIC_DIR'], post.meta['notebook'])
        try:
            notebook = nbformat.read(fpath, 4)
        except IOError:
            abort(404)

        exportMarkdown = nbconvert.MarkdownExporter()
        body, resources = exportMarkdown.from_notebook_node(notebook)

        import re
        for png in resources['outputs'].keys():
            new_png = re.sub('output', post.meta['notebook'], png)
            new_png = url_for('static', filename='notebooks/{}_files/{}'.format(post.meta['notebook'], new_png))
            body = re.sub(png, new_png, body)

        from flask_flatpages.utils import pygmented_markdown
        return pygmented_markdown(body, posts)
        return body
    return dict(notebook=notebook)


@app.route('/<path:ppath>')
@app.route('/', defaults={'ppath': 'home'})
def page(ppath):
    print 'serving PAGE {}'.format(ppath)
    page = pages.get_or_404(ppath)
    active = page.meta['name']
    return render_template('page.html', active=active, page=page)


@app.route('/weblog')
def weblog():
    print 'serving WEBLOG'
    page = pages.get_or_404('weblog')
    active = page.meta['name']
    posts_display = (post for post in posts if not post.meta.get('nopost', False))
    weblogs = sorted(
        posts_display,
        key = lambda post: datetime.datetime.strptime(post.meta['date'], '%d.%m.%Y'),
        reverse = True,
    )
    return render_template('weblog.html', active=active, page=page, weblogs=weblogs)


@app.route('/weblog/<pname>')
def post(pname):
    print 'serving WEBLOG {}'.format(pname)
    post = posts.get_or_404(pname)

    _notebook = post.meta.get('notebook', False)
    if _notebook:
        notebook = '{}.ipynb'.format(_notebook)
        notebook_md = '{}.md'.format(_notebook)

        post.meta['_notebook'] = notebook
        post.meta['_notebook_md'] = notebook_md
        post.meta['_notebook_url'] = url_for('static', filename='notebooks/{}'.format(notebook))
        post.meta['_notebook_md_url'] = url_for('static', filename='notebooks/{}'.format(notebook_md))

    return render_template('post.html', active='weblog', post=post)


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
#     return render_template('publications.html', active='research', page=page, references=refsbyyear)


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from pybtex.database import BibliographyData
from pybtex.database.input import bibtex
from pybtex.database.output.bibtex import Writer


def _get_bibtex_repr(entry):
    """
    Return the bibtex representation of the entry.

    """
    bib_data = BibliographyData(entries={entry.key: entry})
    bibtex_repr = StringIO()
    Writer().write_stream(bib_data, bibtex_repr)
    return bibtex_repr.getvalue()


def _get_authors(entry):
    """
    Return the list of authors as nicely formated string.

    """
    # authors = [" ".join([author.first()[0], author.last()[0]])
    #            for author in entry.persons["author"]]
    # for author in entry.persons["author"]:
    #     print(author.first(), author.middle(), author.last())
    #     print(author)
    authors = [author.last()[0] for author in entry.persons["author"]]
    return ", ".join(authors)


@app.route('/research/publications')
def publications():
    print 'serving publications'

    #Load file
    bibtex_file = '{}/docs/pubs/refs.bib'.format(app.config['STATIC_DIR'])
    parser = bibtex.Parser()
    entries = parser.parse_file(bibtex_file)

    page = pages.get_or_404('research/publications')

    bib = [
        dict(
            type_=entry.type,
            key=key,
            title=entry.fields['title'],
            authors=_get_authors(entry),
            booktitle=entry.fields.get('booktitle', None),
            journal=entry.fields.get('journal', None),
            school=entry.fields.get('school', None),
            year=entry.fields['year'],
            pdf=entry.fields.get('pdf', None),
            bibtex=_get_bibtex_repr(entry),
            talk=entry.fields.get('talk', None),
            note=entry.fields.get('note', None),
        ) for key, entry in entries.entries.iteritems()
    ]

    # NOTE inverting manually enforces that the bibtex file order is also
    # inverted in the case of same year.
    bib = sorted(bib, key=lambda entry: entry['year'])[::-1]

    return render_template('publications.html', active='research', page=page, bib=bib)


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
