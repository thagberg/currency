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
    #rates = ExchangeRate.objects.get(exchanger=exchanger)
    rates = ExchangeRate.objects.all()
    json_rates = json_serializer.serialize(rates)
    return HttpResponse(json_rates, content_type='json')
