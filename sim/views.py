import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import *

def index(request):
    return HttpResponse("hello")

def get_exchange_rates_for_exchanger(request, exchanger_name='Coinbase'):
    json_serializer = serializers.get_serializer('json')
    json_serializer = json_serializer()
    exchanger = Exchanger.objects.get(name=exchanger_name)
    rates = ExchangeRate.objects.filter(exchanger=exchanger)
    json_rates = json_serializer.serialize(rates)
    return HttpResponse(json_rates, content_type='json')

def get_transfers(request):
    return HttpResponse(serializers.serialize('json', sim.models.Transfer.objects.all()), content_type="application/json")

def post_trade(request):
    return HttpResponse(json.dumps({'hi': 'wat ap'}), content_type="application/json")
