from django.db import models

class TradingPair(models.Model):
    crypt_currency = models.CharField(max_length=5)
    world_currency = models.CharField(max_length=5)
    current_value = models.DecimalField(max_digits=20, decimal_places=10)
