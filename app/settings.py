# -*- coding: utf-8 -*-
import os

REPO_NAME = "flask-ghpages-example"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))


def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))



PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
# will be deleted when you run the freezer

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'abbr', 'attr_list', 'def_list', 'app.mdx_haiku', 'app.mdx_comment']

FLATPAGES_WEBLOG_AUTO_RELOAD = True
FLATPAGES_WEBLOG_ROOT = os.path.join(APP_DIR, 'posts')
FLATPAGES_WEBLOG_EXTENSION = '.md'
# FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'app.mdx_haiku', 'app.mdx_comment', 'app.mdx_ipynb']
FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'app.mdx_haiku', 'app.mdx_comment']

FLATPAGES_IPYNB_AUTO_RELOAD = True
FLATPAGES_IPYNB_ROOT = os.path.join(APP_DIR, 'posts')
FLATPAGES_IPYNB_EXTENSION = '.ipy'
FLATPAGES_IPYNB_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code']
# FLATPAGES_IPYNB_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'app.mdx_ipynb']
# FLATPAGES_IPYNB_MARKDOWN_EXTENSIONS = ['codehilite', 'app.mdx_comment']
# FLATPAGES_IPYNB_HTML_RENDERER = 'post:ipynb_renderer'
