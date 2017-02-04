from flask import Flask, render_template_string, Markup
from flask_flatpages import FlatPages

import markdown

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# prerender jinja in markdown files
def prerender_jinja(text):
    prerendered_body = render_template_string(text)
    return markdown.markdown(prerendered_body, app.config['FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS'])
app.config['FLATPAGES_WEBLOG_HTML_RENDERER'] = prerender_jinja

pages = FlatPages(app)
posts = FlatPages(app, 'weblog')
