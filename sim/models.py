from django.db import models

class Exchanger(models.Model):
    name = models.CharField(max_length=31)

class Currency(models.Model):
    currency_code = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=31)

class ExchangeRate(models.Model):
    exchanger = models.ForeignKey(Exchanger)
    time = models.DateTimeField()
    input_currency = models.ForeignKey(Currency, related_name="+")
    output_currency = models.ForeignKey(Currency, related_name="+")
    exchange_rate = models.DecimalField(max_digits=19,decimal_places=10)
