from django.conf.urls import patterns,include,url

from django.contrib import admin
#from django.contrib.sites.models import Site
#from django.contrib.auth.models import Group,User
admin.autodiscover()
#admin.site.unregister(Site)
#admin.site.unregister(Group)
#admin.site.unregister(User)

from pages.views import pageView

urlpatterns = patterns('',
    url(r'^admin/',include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),

    url(r'^',include('pages.urls')),
    url(r'^articles/',include('articles.urls')),
)
