from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from cryptwatch import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cryptwatch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sim/', include('sim.urls')),
    url(r'^$', views.index, name='home page'),
    url(r'^app$', views.index, name='ze app'),
    url(r'^(?P<filename>.+)$', views.serve_file, name='ze app'),
)
