import json
from datetime import datetime

from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User


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
    return HttpResponse(json_serializer.serialize(query_set), mimetype='application/json')

def index(request):
    return HttpResponse("hello")

def get_exchange_rates_for_exchanger(request, exchanger_name='Coinbase'):
    exchanger = Exchanger.objects.get(name=exchanger_name)
    rates = ExchangeRate.objects.filter(exchanger=exchanger)
    return json_response(rates)

def users(request, user_id):
    return json_response(User.objects.filter(id=user_id))

def post_user_trade_trigger(request):
    params = request.GET
    user = User.objects.get(id=params['user'])
    max_price = params['max_price']
    sell_currency = Currency.objects.get(currency_code=params['sell_currency'])
    buy_currency = Currency.objects.get(currency_code=params['buy_currency'])
    created = UserTradeTrigger(user=user, max_price=max_price, sell_currency=sell_currency, buy_currency=buy_currency)
    created.save()
    return json_response(UserTradeTrigger.objects.filter(id=created.id))

def get_user_trade_triggers(request):
    return json_response(UserTradeTrigger.objects.all())

def user_trade_triggers(request):
    if request.GET.get('method','GET') == 'POST':
        return post_user_trade_trigger(request)
    else:
        return get_user_trade_triggers(request)

def transfers(request):
    return json_response(Transfer.objects.all())

def trade(request):
    params = request.GET
    seller = Exchanger.objects.get(id=params['seller'])
    buyer = Exchanger.objects.get(id=params['buyer'])
    sell_currency = Currency.objects.filter(currency_code=params['sell_currency'].upper())[0]
    buy_currency = Currency.objects.filter(currency_code=params['buy_currency'].upper())[0]
    sold_amount = params['sell_amount']
    buy_amount = params['buy_amount']
    time = datetime.now()
    #time = datetime.strptime(params['time'], '%b %d %Y %I:%M%p')
    sell_transfer = Transfer(time=time,
                             source_exchanger=seller,
                             destination_exchanger=buyer,
                             currency=sell_currency,
                             amount=buy_amount)
    sell_transfer.save()
    buy_transfer = Transfer(time=time,
                            source_exchanger=buyer,
                            destination_exchanger=seller,
                            currency=buy_currency,
                            amount=sold_amount)
    buy_transfer.save()
    return HttpResponse('Success!')
