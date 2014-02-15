import json

from django.shortcuts import render
import json

from django.http import HttpResponse
from django.core import serializers

from .models import *

def json_response(stuff):
    json_serializer = serializers.get_serializer('json')
    json_serializer = json_serializer()
    f = json.loads(json_serializer.serialize(stuff))
    data = map(lambda q: q['fields'], f)
    return HttpResponse(data, content_type='application/json')

def index(request):
    return HttpResponse("hello")

def get_exchange_rates_for_exchanger(request, exchanger_name='Coinbase'):
    json_serializer = serializers.get_serializer('json')
    json_serializer = json_serializer()
    exchanger = Exchanger.objects.get(name=exchanger_name)
    #rates = ExchangeRate.objects.get(exchanger=exchanger)
    rates = ExchangeRate.objects.all()
    json_rates = json_serializer.serialize(rates)
    return HttpResponse(json_rates, content_type='json')

def transfers(request):
    return json_response(Transfer.objects.all())

def trade(request):
    params = request.POST
    seller = Exchanger.objects.get(id=params['seller_id'])
    buyer = Exchanger.objects.get(id=params['partner_id'])
    sell_currency = Currency.objects.get(params['sell_currency_code'])
    buy_currency = Currency.objects.get(params['buy_currency_code'])
    params['sell_amount']
    params['buy_amount']
    
    

def post_trade(request):
    return HttpResponse(json.dumps({'hi': 'wat ap'}), content_type="application/json")
