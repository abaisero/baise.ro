import flask
import more_itertools as mitt

from ..extensions import get_refs, groups, pages, topics

blueprint = flask.Blueprint('research', __name__)


@blueprint.route('/')
def publications():
    flask.current_app.logger.info('Serving PUBLICATIONS')
    page = pages.get_or_404('research/publications')

    return flask.render_template(
        'publications.html', active='research', page=page, refs=get_refs()
    )


# # TODO don't even create these... use the static url directly
# @blueprint.route('/publications/<key>')
# def pub(key):
#     flask.abort(404)


# @blueprint.route('/publications/<key>.pdf')
# def pub_pdf(key):
#     url = 'docs/pubs/{}/{}.pdf'.format(key, key)
#     return flask.current_app.send_static_file(url)


# @blueprint.route('/publications/<key>.mp4')
# def pub_mp4(key):
#     url = 'docs/pubs/{}/{}.mp4'.format(key, key)
#     return flask.current_app.send_static_file(url)
