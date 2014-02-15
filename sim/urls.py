from django.conf.urls import patterns, url

from sim import views

urlpatterns = patterns('',
    url(r'^transfers$', views.get_transfers, name='transfers')
)
