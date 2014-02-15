from django.db import models

# Represents some agent in the system
# Coinbase is an exchanger
# The user is also an exchanger
class Exchanger(models.Model):
    name = models.CharField(max_length=31)

# Identifies a currency type, e.g. USD, BTC
class Currency(models.Model):
    currency_code = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=31)

# Represents the rate that someone is willing to exchange
# currency at at some point in time
class ExchangeRate(models.Model):
    exchanger = models.ForeignKey(Exchanger)
    time = models.DateTimeField()
    input_currency = models.ForeignKey(Currency, related_name="+")
    output_currency = models.ForeignKey(Currency, related_name="+")
    exchange_rate = models.DecimalField(max_digits=19,decimal_places=10)

class Transaction(models.Model):
    time = models.DateTimeField()
    source_exchanger = models.ForeignKey(Exchanger, related_name="+")
    destination_exchanger = models.ForeignKey(Exchanger, related_name="+")
    currency = models.ForeignKey(Currency, related_name="+")
    amount = models.DecimalField(max_digits=19,decimal_places=10)
