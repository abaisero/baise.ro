from django.conf.urls import patterns,url
from pages.views import pageView

urlpatterns=patterns('',
    url(r'^$',pageView,name='home',kwargs={'page_name':'home'}),
    url(r'^(?P<page_name>\w+)/$',pageView,name='page'),
)
