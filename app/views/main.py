import flask
import more_itertools as mitt

from ..extensions import get_refs, groups, pages, posts, repos, topics

blueprint = flask.Blueprint('main', __name__)


@blueprint.route('/', defaults={'name': 'home'})
@blueprint.route('/<name>/')
def page(name):
    flask.current_app.logger.info(f'Serving PAGE {name}')
    page = pages.get_or_404(name)

    return flask.render_template('page.html', page=page)


@blueprint.route('/research/')
def research():
    flask.current_app.logger.info('Serving RESEARCH')
    page = pages.get_or_404('research')

    topic_ids = [
        'llpr.gsr',
        'llpr.istate',
        'llpr.agr',
        'mlr.rfdm',
        'mlr.iden',
        'mlr.tseg',
        'cvap.pathkernel',
    ]
    topics_ = [topics.get(topic_id) for topic_id in topic_ids]
    topic_groups = mitt.bucket(topics_, key=lambda topic: topic.meta['group'])

    return flask.render_template(
        'research.html',
        page=page,
        groups=groups,
        topic_groups=topic_groups,
        refs=get_refs(),
    )


@blueprint.route('/code/')
def code():
    flask.current_app.logger.info('Serving CODE')
    page = pages.get_or_404('code')

    repo_ids = [
        'beamerthemeNU',
        'rlpo18',
        # 'rl',
        'gym_pomdps',
        'rl_parsers',
        'indextools',
        'pytk',
        'baise.ro',
        # 'pyfgraph',
    ]
    repos_ = [repos.get(repo_id) for repo_id in repo_ids]

    return flask.render_template('code.html', page=page, repos=repos_)


@blueprint.route('/weblog/')
def weblog():
    flask.current_app.logger.info('Serving WEBLOG')
    page = pages.get_or_404('weblog')

    posts_ = filter(lambda post: not post.meta.get('hide', False), posts)
    posts_ = sorted(posts_, key=lambda post: post.meta['date'], reverse=True)

    return flask.render_template('weblog.html', page=page, posts=posts_)


# @blueprint.route('/sitemap')
# @blueprint.route('/sitemap.html')
# def sitemap():
#     # NOTE this is a cool sitemap https://www.cityhotelderry.com/sitemap.html

#     flask.current_app.logger.info('Serving SITEMAP')
#     page = pages.get_or_404('sitemap')
#     return flask.render_template('sitemap.html', page=page, pages=pages)
