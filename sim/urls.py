from django.conf.urls import patterns, url
from django.contrib.auth.models import User
from sim import views

urlpatterns = patterns('',
    url(r'^transfers$', views.transfers, name='transfers'),
    url(r'^users/(?P<user_id>.+)$', views.users),
    url(r'^usertradetriggers$', views.user_trade_triggers),
    url(r'^rates/(?P<exchanger_name>.+)$', views.get_exchange_rates_for_exchanger),
    url(r'^rates$', views.get_exchange_rates_for_exchanger),
    url(r'^trades$', views.trade)
)
