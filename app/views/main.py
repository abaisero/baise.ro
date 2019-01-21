import flask

import more_itertools as mitt

from ..extensions import pages, topics, repos, posts
from ..extensions import groups
from ..extensions import get_refs


blueprint = flask.Blueprint('main', __name__)


def show_filter(page):
    return (page.meta.get('show', True) and not page.meta.get('noshow', False))


@blueprint.route('/', defaults={'name': 'home'})
@blueprint.route('/<name>')
def page(name):
    flask.current_app.logger.info(f'Serving PAGE {name}')
    page = pages.get_or_404(name)
    active = page.meta['id']
    return flask.render_template('page.html', active=active, page=page)


@blueprint.route('/research')
def research():
    flask.current_app.logger.info('Serving RESEARCH')
    page = pages.get_or_404('research')

    articles = mitt.bucket(sorted(topics, key=lambda t: t.path),
                           key=lambda a: a.meta['group'])
    refs = get_refs()

    return flask.render_template('research.html', active='research',
                                 page=page,
                                 groups=groups,
                                 articles=articles,
                                 refs=refs)


@blueprint.route('/code')
def code():
    flask.current_app.logger.info('Serving CODE')
    page = pages.get_or_404('code')
    active = page.meta['id']

    repos_shown = flask.current_app.extensions['flatpages']['repos']
    repos_shown = sorted(filter(show_filter, repos_shown),
                         key=lambda repo: repo.path)

    return flask.render_template('code.html', active=active, page=page,
                                 repos=repos_shown)


@blueprint.route('/weblog')
def weblog():
    flask.current_app.logger.info('Serving WEBLOG')
    page = pages.get_or_404('weblog')
    active = page.meta['id']

    posts_shown = sorted(filter(show_filter, posts),
                         key=lambda post: post.meta['date'], reverse=True)

    return flask.render_template('weblog.html',
                                 active=active, page=page, posts=posts_shown)


# @blueprint.route('/sitemap')
# @blueprint.route('/sitemap.html')
# def sitemap():
#     # NOTE this is a cool sitemap https://www.cityhotelderry.com/sitemap.html

#     flask.current_app.logger.info('Serving SITEMAP')
#     page = pages.get_or_404('sitemap')
#     return flask.render_template('sitemap.html', page=page, pages=pages)
