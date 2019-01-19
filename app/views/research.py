import flask

from ..extensions import pages, get_refs

blueprint = flask.Blueprint('research', __name__)


@blueprint.route('/publications')
def publications():
    flask.current_app.logger.info('Serving PUBLICATIONS')
    page = pages.get_or_404('research/publications')
    refs = get_refs()

    return flask.render_template('publications.html',
                                 active='research',
                                 page=page,
                                 refs=refs)


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
