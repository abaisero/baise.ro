# -*- coding: utf-8 -*-
import os
from pathlib2 import Path

REPO_NAME = "flask-ghpages-example"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_PATH = Path(__file__).parents[0]
PAGES_PATH = APP_PATH / 'pages'
POSTS_PATH = APP_PATH / 'posts'
STATIC_PATH = APP_PATH / 'static'
RUBUS_PATH = APP_PATH / 'rubus'
USERS_PATH = RUBUS_PATH / 'users'
DB_PATH = APP_PATH / 'rubus.db'

APP_DIR = str(APP_PATH)
PAGES_DIR = str(PAGES_PATH)
POSTS_DIR = str(POSTS_PATH)
STATIC_DIR = str(STATIC_PATH)
RUBUS_DIR = str(RUBUS_PATH)
USERS_DIR = str(USERS_PATH)

# TODO is this why some files are sent empty?!
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 10 * 1024 * 1024


PROJECT_ROOT = str(APP_PATH.parents[0])
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
# will be deleted when you run the freezer

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_ROOT = PAGES_DIR
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx_haiku', 'app.mdx_comment', 'app.mdx_mathjax']

FLATPAGES_WEBLOG_AUTO_RELOAD = True
FLATPAGES_WEBLOG_ROOT = POSTS_DIR
FLATPAGES_WEBLOG_EXTENSION = '.md'
# FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'app.mdx_haiku', 'app.mdx_comment', 'app.mdx_ipynb']
FLATPAGES_WEBLOG_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx_haiku', 'app.mdx_comment', 'app.mdx_mathjax']

# TODO what was this for??
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
