from django.conf.urls import patterns, url

from sim import views

urlpatterns = patterns('',
    url(r'^transfers$', views.transfers, name='transfers')
)
