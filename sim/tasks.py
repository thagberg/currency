from __future__ import absolute_import
from datetime import datetime

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
        exchanges = ExchangeRate.objects.filter(input_currency=input_curr,
                                                output_currency=output_curr)
        if len(exchanges) == 0:
            exchange = ExchangeRate(exchanger=exchanger,
                                    input_currency=input_curr,
                                    output_currency=output_curr,
                                    exchange_rate=trade['price'],
                                    time=time)
            exchange.save()
        else:
            exchange = exchanges[0]
            exchange.exchange_rate = trade['price']
            exchange.time = time
            exchange.save()
