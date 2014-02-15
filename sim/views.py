from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User

import json

from .models import *

def merge( a, b ):
    x = {}
    x.update(a)
    x.update(b)
    return x


json_serializer = serializers.get_serializer('json')()

def record_to_json(rec):
    values = rec.fields() #json.loads(json_serializer.serialize(rec))
    values['id'] = rec.pk
    return values

def json_response(query_set):
    return HttpResponse(json_serializer.serialize(query_set), content_type='application/json')

def index(request):
    return HttpResponse("hello")

def get_exchange_rates_for_exchanger(request, exchanger_name='Coinbase'):
    exchanger = Exchanger.objects.get(name=exchanger_name)
    rates = ExchangeRate.objects.filter(exchanger=exchanger)
    return json_response(rates)

def users(request, user_id):
    return json_response(User.objects.filter(id=user_id))

def post_user_trade_trigger(request):
    params = request.POST
    user = User.objects.get(id=params['user'])
    max_price = params['max_price']
    sell_currency = Currency.objects.get(params['sell_currency'])
    buy_currency = Currency.objects.get(params['buy_currency'])
    created = UserTradeTrigger(user=user, max_price=max_price, sell_currency=sell_currency, buy_currency=buy_currency)
    created.save()
    return json_response(UserTradeTrigger.objects.get(id=created.id))

def get_user_trade_triggers(request):
    return json_response(UserTradeTrigger.objects.all())
    
def user_trade_triggers(request):
    if request.method == 'POST':
        return post_user_trade_trigger(request)
    else:
        return get_user_trade_triggers(request)

def transfers(request):
    return json_response(Transfer.objects.all())

def trade(request):
    params = request.POST
    seller = Exchanger.objects.get(id=params['seller'])
    buyer = Exchanger.objects.get(id=params['buyer'])
    sell_currency = Currency.objects.get(params['sell_currency'])
    buy_currency = Currency.objects.get(params['buy_currency'])
    params['sell_amount']
    params['buy_amount']
    params['time']
    
def post_trade(request):
    return HttpResponse(json.dumps({'hi': 'wat ap'}), content_type="application/json")
