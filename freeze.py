#!/usr/bin/env python

import flask_frozen

from app import create_app

app = create_app()
freezer = flask_frozen.Freezer(
    app, with_no_argument_rules=False, log_url_for=False
)


@freezer.register_generator
def main():
    for page in app.extensions['flatpages']['pages']:
        if page.meta.get('freeze', True):
            if page.path == 'research':
                yield 'main.research', {}
            elif page.path == 'code':
                yield 'main.code', {}
            elif page.path == 'weblog':
                yield 'main.weblog', {}
            else:
                yield 'main.page', {'name': page.path}


@freezer.register_generator
def research():
    yield 'research.publications', {}


@freezer.register_generator
def weblog():
    for post in app.extensions['flatpages']['posts']:
        if post.meta.get('freeze', True):
            yield 'weblog.post', {'name': post.path}


if __name__ == '__main__':
    freezer.freeze()
