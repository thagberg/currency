import json
from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

from .models import *

def merge( a, b ):
    x = {}
    x.update(a)
    x.update(b)
    return x


json_serializer = serializers.get_serializer('json')()

def record_to_json(rec):
    values = json.loads(json_serializer.serialize(rec))
    values['id'] = rec.pk
    return values

def json_response(stuff):
    data = map(lambda r: record_to_json(r), stuff)
    return HttpResponse(json.dumps(data), content_type='application/json')

def index(request):
    return HttpResponse("hello")

def get_exchange_rates_for_exchanger(request, exchanger_name='Coinbase'):
    json_serializer = serializers.get_serializer('json')
    json_serializer = json_serializer()
    exchanger = Exchanger.objects.get(name=exchanger_name)
    rates = ExchangeRate.objects.filter(exchanger=exchanger)
    json_rates = json_serializer.serialize(rates)
    json_rates = serializers.serialize('json', rates)
    return HttpResponse(json_rates, content_type='json')

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
    

def post_trade(request):
    return HttpResponse(json.dumps({'hi': 'wat ap'}), content_type="application/json")
