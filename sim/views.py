import json

from django.shortcuts import render
import json

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
    return HttpResponse(json_rates, content_type='json')

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
