import flask

from .views import main, weblog, research
from .extensions import pages, posts, repos, topics, init_refs, sitemap, assets, toolbar

import markdown
import datetime
import re

import os
from io import StringIO
from pybtex.database import BibliographyData
from pybtex.database.output.bibtex import Writer


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.register_blueprint(main.blueprint, url_prefix='/')
    app.register_blueprint(research.blueprint, url_prefix='/research')
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

    # prerender jinja in markdown files
    # def prerender_jinja(text):
    #     prerendered_body = flask.render_template_string(text)
    #     return markdown.markdown(
    #         prerendered_body,
    #         app.config['FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS'])

    # app.config['FLATPAGES_WEBLOG_HTML_RENDERER'] = prerender_jinja

    # Allows for slash-less urls to work seamlessly
    app.url_map.strict_slashes = False

    # NOTE creates loop with blueprints
    @app.before_request
    def clear_trailing():
        rp = flask.request.path
        if rp != '/' and rp.endswith('/'):
            return flask.redirect(rp[:-1], code=301)

    # TODO make better 404 template
    @app.errorhandler(404)
    def page_not_found(e):
        app.logger.info('DEBUGGING')
        return flask.render_template('404.html'), 404

    @app.template_filter()
    def tagify(string, tag, pattern):
        repl = f'<{tag}>{pattern}</{tag}>'
        return re.sub(pattern, repl, string)

    @app.context_processor
    def inject_anchor():
        return dict(anchor='<span class="fas fa-anchor"></span>')
        return dict(anchor='§')
        return dict(anchor='¶')

    @app.context_processor
    def inject_pages():
        return dict(pages=pages)

    @app.context_processor
    def inject_now():
        return dict(now=datetime.datetime.utcnow())

    @app.context_processor
    def injext_pub():
        return dict(pub_authors=bibentry_authors,
                    pub_has_mp4=bibentry_has_mp4,
                    pub_bibtex=bibentry_bibtex)

    return app


def bibentry_bibtex(entry):
    """ Return the bibtex representation of the entry.  """
    bib_data = BibliographyData(entries={entry.key: entry})
    bibtex_repr = StringIO()
    Writer().write_stream(bib_data, bibtex_repr)
    return bibtex_repr.getvalue()


def bibentry_authors(entry):
    """ Return the list of authors as nicely formated string.  """

    def format(author):
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
