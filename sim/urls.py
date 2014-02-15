from django.conf.urls import patterns, url

from sim import views

urlpatterns = patterns('',
    url(r'^transfers$', views.get_transfers, name='transfers'),
    url(r'^rates/(?P<exchanger_name>.+)$', views.get_exchange_rates_for_exchanger),
    url(r'^rates/$', views.get_exchange_rates_for_exchanger),
    url(r'^$', views.index)
)
