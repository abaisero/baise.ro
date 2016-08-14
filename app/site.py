from . import pages, posts, ipynbs
import itertools as itt
import datetime


class Site(object):

    def __init__(self):
        menu = [
            'home',
            'research',
            'teaching',
            # 'code',
            'weblog',
            'about',
        ]

        self.menu = [pages.get(page) for page in menu]

    @property
    def posts(self):
        return sorted(
            itt.chain(list(posts), list(ipynbs)),
            key=lambda post: datetime.datetime.strptime(post.meta['date'], '%d.%m.%Y'),
            reverse=True
        )


site = Site()
