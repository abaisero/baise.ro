import datetime
import os
import re
from io import StringIO

import flask
import markdown
from pybtex.database import BibliographyData
from pybtex.database.output.bibtex import Writer

from .extensions import (
    assets,
    init_refs,
    pages,
    posts,
    repos,
    sitemap,
    toolbar,
    topics,
)
from .views import main, research, weblog


# prerender jinja in markdown files
def prerender_jinja(text, pages):
    prerendered_body = flask.render_template_string(text)
    extensions = pages.config('MARKDOWN_EXTENSIONS')
    rendered_body = markdown.markdown(prerendered_body, extensions=extensions)
    return rendered_body


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config['FLATPAGES_PAGES_HTML_RENDERER'] = prerender_jinja
    app.config['FLATPAGES_POSTS_HTML_RENDERER'] = prerender_jinja
    app.config['FLATPAGES_REPOS_HTML_RENDERER'] = prerender_jinja
    app.config['FLATPAGES_TOPICS_HTML_RENDERER'] = prerender_jinja

    app.register_blueprint(main.blueprint, url_prefix='/')
    app.register_blueprint(
        research.blueprint, url_prefix='/research/publications'
    )
    app.register_blueprint(weblog.blueprint, url_prefix='/weblog')

    # NOTE pages and sitemap registered in app.extensions
    pages.init_app(app)
    posts.init_app(app)
    repos.init_app(app)
    topics.init_app(app)
    init_refs(app)
    sitemap.init_app(app)
    assets.init_app(app)
    toolbar.init_app(app)

    # Allows for slash-less urls to work seamlessly
    # app.url_map.strict_slashes = False

    # NOTE creates loop with blueprints
    # @app.before_request
    # def clear_trailing():
    #     rp = flask.request.path
    #     if rp != '/' and rp.endswith('/'):
    #         return flask.redirect(rp[:-1], code=301)

    # TODO make better 404 template
    # @app.errorhandler(404)
    # def page_not_found(e):  # pylint: disable=unused-variable,unused-argument
    #     app.logger.info('DEBUGGING')
    #     return flask.render_template('404.html'), 404

    @app.template_filter()
    def tagify(string, tag, pattern):  # pylint: disable=unused-variable
        repl = f'<{tag}>{pattern}</{tag}>'
        return re.sub(pattern, repl, string)

    @app.context_processor
    def inject_anchor():  # pylint: disable=unused-variable
        return dict(anchor='<span class="fas fa-anchor"></span>')
        # return dict(anchor='§')
        # return dict(anchor='¶')

    @app.context_processor
    def inject_pages():  # pylint: disable=unused-variable
        return dict(pages=pages)

    @app.context_processor
    def inject_now():  # pylint: disable=unused-variable
        return dict(now=datetime.datetime.utcnow())

    @app.context_processor
    def injext_pub():  # pylint: disable=unused-variable
        return dict(
            pub_authors=bibentry_authors,
            pub_has_mp4=bibentry_has_mp4,
            pub_has_poster=bibentry_has_poster,
            pub_bibtex=bibentry_bibtex,
        )

    return app


def bibentry_bibtex(entry):
    """ Return the bibtex representation of the entry.  """
    bib_data = BibliographyData(entries={entry.key: entry})
    bibtex_repr = StringIO()
    Writer().write_stream(bib_data, bibtex_repr)
    return bibtex_repr.getvalue()


def bibentry_authors(entry):
    """ Return the list of authors as nicely formated string.  """

    def format(author):  # pylint: disable=redefined-builtin
        names = []
        names.extend(name[0] for name in author.first_names)
        names.extend(name[0] for name in author.middle_names)
        names.extend(name for name in author.last_names)
        return ' '.join(names)

    return ', '.join(map(format, entry.persons['author']))


def bibentry_has_mp4(entry):
    """ Return link to video, if it exists """
    path = f'docs/pubs/{entry.key}/{entry.key}.mp4'
    path = flask.safe_join(flask.current_app.static_folder, path)
    return os.path.exists(path)


def bibentry_has_poster(entry):
    """ Return link to poster, if it exists """
    path = f'docs/pubs/{entry.key}/poster.pdf'
    path = flask.safe_join(flask.current_app.static_folder, path)
    return os.path.exists(path)
