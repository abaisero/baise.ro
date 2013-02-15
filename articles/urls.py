from django.conf.urls import patterns,url
from articles.views import articleView

urlpatterns=patterns('',
    url(r'^(?P<article_id>\d+)/',articleView,name='article'),
)
