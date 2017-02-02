from flask import Flask, render_template_string, Markup
from flask_flatpages import FlatPages

import markdown

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# from flaskext.markdown import Markdown
# Markdown(app)

# prerender jinja in markdown files
def prerender_jinja(text):
    prerendered_body = render_template_string(text)
    return markdown.markdown(prerendered_body, app.config['FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS'])
app.config['FLATPAGES_WEBLOG_HTML_RENDERER'] = prerender_jinja

from flask import url_for
@app.context_processor
def utility_processor():
    def notebook2html(fname):
        url = url_for('notebook2html', fname=fname)
        html = '<div class=\'notebook\'><object class=\'notebook\' type=\'text/html\' data=\'{}\' onload="resizeIframe(this)"></object></div>'.format(url)
        return Markup(html)
    return dict(notebook2html=notebook2html)

import nbformat
import nbconvert

@app.context_processor
def utility_processor():
    # def notebook2md(fname):
    #     url = url_for('notebook2md', fname=fname)
    #     html = '<div class=\'notebook\'><object class=\'notebook\' type=\'text/markdown\' data=\'{}\'"></object></div>'.format(url)
    #     return Markup(html)
    # return dict(notebook2md=notebook2md)
    def notebook2md(fname):
        fpath = '{}/notebooks/{}'.format(app.config['STATIC_DIR'], fname)
        try:
            notebook = nbformat.read(fpath, 4)
        except IOError:
            abort(404)

        # config = Config({'MarkdownExporter': {'default_template': 'basic'}})
        # exportMarkdown = nbconvert.MarkdownExporter(config=config)
        exportMarkdown = nbconvert.MarkdownExporter()
        body, resources = exportMarkdown.from_notebook_node(notebook)
        return body
    return dict(notebook2md=notebook2md)


# @app.context_processor
# def utility_processor():
#     def notebook(post):
#         fpath = '{}/notebooks/{}'.format(app.config['STATIC_DIR'], post.meta['notebook'])
#         try:
#             notebook = nbformat.read(fpath, 4)
#         except IOError:
#             abort(404)

#         # config = Config({'MarkdownExporter': {'default_template': 'basic'}})
#         # exportMarkdown = nbconvert.MarkdownExporter(config=config)
#         exportMarkdown = nbconvert.MarkdownExporter()
#         body, resources = exportMarkdown.from_notebook_node(notebook)
#         # return markdown.markdown(body, app.config['FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS'])
#         # TODO

#         from flask_flatpages.utils import pygmented_markdown
#         return pygmented_markdown(body, posts)
#     return dict(notebook=notebook)

pages = FlatPages(app)
posts = FlatPages(app, 'weblog')
# notebooks = FlatPages(app, 'notebook')
