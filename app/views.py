from flask import render_template, request, abort
from app import app, pages, posts, ipynbs
from site import site
import pathlib
import datetime

import nbformat
import nbconvert
import pygments
from traitlets.config import Config


def my_highlight(source, language='ipython'):
    formatter = pygments.formatters.HtmlFormatter(cssclass='highlight-ipynb')
    return nbconvert.filters.highlight._pygments_highlight(source, formatter, language)


@app.template_filter()
def fmt_date(value):
    return datetime.datetime.strptime(value, '%d.%m.%Y').strftime('%d %b %Y')


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_index')
def upload_index():
    return render_template('upload_index.html')


from werkzeug import secure_filename
import os
from flask import redirect, url_for, send_from_directory

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_DIR'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file', filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_DIR'], filename)

@app.route('/weblog/<path:path>/')
def post(path):
    print 'serving WEBLOG {}'.format(path)
    post = posts.get(path)
    if post is None:
        post = ipynbs.get_or_404(path)
    return render_template('post.html', site=site, pname='Weblog', post=post)


@app.route('/ipynb2html/<fname>')
def ipynb2html(fname):
    fpath = '{}/ipynb/{}'.format(app.config['STATIC_DIR'], fname)
    try:
        notebook = nbformat.read(fpath, 4)
    except IOError:
        abort(404)

    # c = Config({'CSSHtmlHeaderTransformer':
    #                 {'enabled':True, 'highlight_class':'highlight-ipynb'}})
    # exportHtml = nbconvert.HTMLExporter(config=c, filters={'highlight': my_highlight})
    exportHtml = nbconvert.HTMLExporter()
    body, resources = exportHtml.from_notebook_node(notebook)
    return body


@app.route('/<path:path>/')
@app.route('/', defaults={'path': 'home'})
def page(path):
    print 'serving PAGE {}'.format(path)

    # default is page
    template = 'page.html'
    book = pages

    # but weblog has different settings
    p = pathlib.Path(path)
    if len(p.parts) == 1 and p.parts[0] == 'weblog':
        template = 'weblog.html'

    page = book.get_or_404(path)
    return render_template(template, site=site, pname=page.meta['name'], page=page)

