import flask
# from flask_flatpages.utils import pygmented_markdown
# from flask_flatpages.utils import pygmented_markdown
import flask_flatpages

import nbformat
import nbconvert
import re

from ..extensions import pages, posts


blueprint = flask.Blueprint('weblog', __name__)


@blueprint.route('/<name>')
def post(name):
    flask.current_app.logger.info(f'Serving WEBLOG {name}')
    page = pages.get_or_404('research')
    post = posts.get_or_404(name)

    # TODO I don't like this anymore..
    try:
        nb = post.meta['notebook']
    except KeyError:
        pass
    else:
        notebook = f'{nb}.ipynb'
        notebook_md = f'{nb}.md'

        post.meta['_notebook'] = notebook
        post.meta['_notebook_md'] = notebook_md
        post.meta['_notebook_url'] = flask.url_for(
            'static', filename=f'notebooks/{notebook}'
        )
        post.meta['_notebook_md_url'] = flask.url_for(
            'static', filename=f'notebooks/{notebook_md}'
        )

    return flask.render_template('post.html', active='weblog', page=page, post=post)


@blueprint.context_processor
def inject():
    return dict(render_notebook=render_notebook)


exportMarkdown = nbconvert.MarkdownExporter()


def render_notebook(post):

    meta_notebook = post.meta['notebook']
    path = f'{flask.current_app.static_folder}/notebooks/{meta_notebook}.ipynb'

    try:
        notebook = nbformat.read(path, 4)
    except IOError:
        flask.abort(404)

    body, resources = exportMarkdown.from_notebook_node(notebook)

    # removes title from body
    body = re.sub('#\s.*', '', body, count=1)

    # embeds images
    for png in resources['outputs'].keys():
        new_png = re.sub('output', post.meta['notebook'], png)
        new_png = flask.url_for(
            'static', filename=f'notebooks/{meta_notebook}_files/{new_png}'
        )
        body = re.sub(png, new_png, body)

    return flask_flatpages.pygmented_markdown(body, posts)
