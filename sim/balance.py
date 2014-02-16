import random
from sim.models import *
from django.db.models import Q
from datetime import datetime, timedelta

class ExchangerBalance:
    def __init__(self, exchanger):
        self.exchanger = exchanger
    
    def get_transfers(self):
        return Transfer.objects.filter(Q(source_exchanger_id=self.exchanger.id) | Q(destination_exchanger_id=self.exchanger.id))
    
    def get_balances(self):
        balances = {}
        for transfer in self.get_transfers():
            delta = 0
            if self.exchanger.id == transfer.source_exchanger.id:
                delta = delta - transfer.amount
            if self.exchanger.id == transfer.destination_exchanger.id:
                delta = delta + transfer.amount
            cc = transfer.currency.currency_code
            balances[cc] = delta + balances.get(cc, 0)
        return balances
    
    def generate_exchange_rates(self, begin_date, end_date, begin_price):
        usd = Currency.objects.get(currency_code='USD')
        btc = Currency.objects.get(currency_code='BTC')
        
        date = begin_date
        price = begin_price
        while date < end_date:
            price = price + random.random() * 5
            ExchangeRate(exchanger=self.exchanger, time=date, input_currency=btc, output_currency=usd, exchange_rate=price).save()
            ExchangeRate(exchanger=self.exchanger, time=date, input_currency=usd, output_currency=btc, exchange_rate=1/price).save()
            date = date + timedelta(days=1)
