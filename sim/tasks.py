from __future__ import absolute_import
from datetime import datetime
import random

from celery import Celery
from .models import *

from .trade import get_trade_value


def update():
    currencies = Currency.objects.all()
    pairs = list()
    trades = list()
    
    # get the interested currencies and their trade values
    for currency in currencies:
        pair = '{crypto}_{real}'.format(crypto=currency.currency_code.lower(),
                                        real='usd')
        new_trade = get_trade_value(currency.currency_code.lower(),
                                    'usd')
        trades.append(new_trade)

    # update the database with the new trade values
    for trade in [x for x in trades if x['id']]:
        exchanger = Exchanger.objects.get(name='Coinbase')
        time = datetime.now()
        trade_id = trade['id']
        input_curr = trade_id.split('/')[0]
        output_curr = trade_id.split('/')[1]
        input_curr = Currency.objects.get(currency_code=input_curr.upper())
        output_curr = Currency.objects.get(currency_code=output_curr.upper())
        exchange = ExchangeRate(exchanger=exchanger,
                                input_currency=input_curr,
                                output_currency=output_curr,
                                time=time,
                                exchange_rate=trade['price'])
        exchange.save()

def fuckit():
    for i in range(20):
        exchanger = Exchanger(name='Source{i}'.format(i=i))
        exchanger.save()

    exchangers = Exchanger.objects.all()
    for exchanger in exchangers:
        currencies = Currency.objects.all()
        usd = Currency.objects.get(currency_code='USD')
        for currency in currencies:
            time = datetime.now()
            rate = random.uniform(0.000001, 700.00000)
            exchange = ExchangeRate(exchanger=exchanger,
                                    input_currency=currency,
                                    output_currency=usd,
                                    time=time,
                                    exchange_rate=rate)
            exchange.save()
