import os
from pathlib import Path

# REPO_NAME = 'flask-ghpages-example'  # Used for FREEZER_BASE_URL
# DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_PATH = Path(__file__).parents[0]
STATIC_PATH = APP_PATH / 'static'
PAGES_PATH = APP_PATH / 'pages'
POSTS_PATH = APP_PATH / 'posts'
REPOS_PATH = APP_PATH / 'repos'
TOPICS_PATH = APP_PATH / 'topics'

APP_DIR = str(APP_PATH)
STATIC_DIR = str(STATIC_PATH)
PAGES_DIR = str(PAGES_PATH)
POSTS_DIR = str(POSTS_PATH)
REPOS_DIR = str(REPOS_PATH)
TOPICS_DIR = str(TOPICS_PATH)

# TODO is this why some files are sent empty?!
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 10 * 1024 * 1024

# PROJECT_ROOT = str(APP_PATH.parents[0])
# # In order to deploy to Github pages, you must build the static files to
# # the project root
# FREEZER_DESTINATION = PROJECT_ROOT
# # Since this is a repo page (not a Github user page),
# # we need to set the BASE_URL to the correct url as per GH Pages' standards
# FREEZER_BASE_URL = f'http://localhost/{REPO_NAME}'
# FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
# # will be deleted when you run the freezer

_extensions = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx.haiku', 'app.mdx.comment', 'app.mdx.mathjax']

FLATPAGES_PAGES_AUTO_RELOAD = True
FLATPAGES_PAGES_ROOT = PAGES_DIR
FLATPAGES_PAGES_EXTENSION = '.md'
FLATPAGES_PAGES_MARKDOWN_EXTENSIONS = _extensions
# FLATPAGES_PAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx.haiku', 'app.mdx.comment', 'app.mdx.mathjax']

FLATPAGES_POSTS_AUTO_RELOAD = True
FLATPAGES_POSTS_ROOT = POSTS_DIR
FLATPAGES_POSTS_EXTENSION = '.md'
FLATPAGES_POSTS_MARKDOWN_EXTENSIONS = _extensions
# FLATPAGES_POSTS_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx.haiku', 'app.mdx.comment', 'app.mdx.mathjax']

FLATPAGES_REPOS_AUTO_RELOAD = True
FLATPAGES_REPOS_ROOT = REPOS_DIR
FLATPAGES_REPOS_EXTENSION = '.md'
FLATPAGES_REPOS_MARKDOWN_EXTENSIONS = _extensions
# FLATPAGES_REPOS_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx.haiku', 'app.mdx.comment', 'app.mdx.mathjax']

FLATPAGES_TOPICS_AUTO_RELOAD = True
FLATPAGES_TOPICS_ROOT = TOPICS_DIR
FLATPAGES_TOPICS_EXTENSION = '.md'
FLATPAGES_TOPICS_MARKDOWN_EXTENSIONS = _extensions
# FLATPAGES_TOPICS_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'abbr', 'attr_list', 'def_list', 'tables', 'app.mdx.haiku', 'app.mdx.comment', 'app.mdx.mathjax']


SECRET_KEY = 'a1fda54a1bb3340f1e7a5f7d1030ad4b9a9282f7b9cc906b'
