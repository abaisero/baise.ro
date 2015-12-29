from app import pages, posts
import datetime


class Site(object):

    def __init__(self):
        menu = [
            'home',
            'research',
            'code',
            'weblog',
            'about',
        ]

        self.menu = [pages.get(page) for page in menu]

    @property
    def posts(self):
        return sorted(
            posts,
            key=lambda post: datetime.datetime.strptime(post.meta['date'], '%d.%m.%Y'),
            reverse=True
        )


site = Site()
