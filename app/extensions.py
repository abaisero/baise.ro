import flask
import flask_flatpages
import flask_sitemap
import flask_assets
import flask_debugtoolbar

import pandas as pd

from pybtex.database.input import bibtex


# pages

pages = flask_flatpages.FlatPages(name='pages')
posts = flask_flatpages.FlatPages(name='posts')
repos = flask_flatpages.FlatPages(name='repos')
topics = flask_flatpages.FlatPages(name='topics')


# research groups

def title(g):
    if g.ongoing:
        years = f'{g["from"].year}&ndash;'
    elif g['from'] == g['to']:
        years = f'{g["from"].year}'
    else:
        years = f'{g["from"].year}&ndash;{g["to"].year}'

    return f'{g["name"].upper()} @ {g["university"]} ({years})'


groups = pd.read_csv('app/groups.csv',
                     parse_dates=['from', 'to'],
                     date_parser=lambda x: pd.datetime.strptime(x, '%Y'),
                     sep='\s*;\s*', engine='python')
groups['ongoing'] = groups['to'].isnull()
groups['title'] = groups.apply(title, axis=1)


# refs

refs = None


def init_refs(app):
    global refs

    # TODO the problem is that I need the static_folder...
    path = f'{app.static_folder}/docs/pubs/refs.bib'
    refs = bibtex.Parser().parse_file(path)


def get_refs():
    return refs


# sitemap

sitemap = flask_sitemap.Sitemap()


@sitemap.register_generator
def generator():
    for page in pages:
        yield 'main.page', dict(name=page.path)

    for post in posts:
        yield 'weblog.post', dict(name=post.path)


# assets

assets = flask_assets.Environment()


# debugtoolbar

toolbar = flask_debugtoolbar.DebugToolbarExtension()
