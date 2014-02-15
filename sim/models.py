from django.db import models
from django.contrib.auth.models import User

# Represents some agent in the system
# Coinbase is an exchanger
# The user is also an exchanger
class Exchanger(models.Model):
    name = models.CharField(max_length=31)
    
    def __unicode__(self):
        return "%s (%d)" % (self.name, self.id)

# Identifies a currency type, e.g. USD, BTC
class Currency(models.Model):
    currency_code = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=31)
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.currency_code)

# Represents the rate that someone is willing to exchange
# currency at at some point in time
class ExchangeRate(models.Model):
    exchanger = models.ForeignKey(Exchanger)
    time = models.DateTimeField()
    input_currency = models.ForeignKey(Currency, db_column="input_currency_code", related_name="+")
    output_currency = models.ForeignKey(Currency, db_column="output_currency_code", related_name="+")
    exchange_rate = models.DecimalField(max_digits=19,decimal_places=10) # Inputs per outputs
    
    def __unicode__(self):
        return "%f %s/%s via %s on %s" % (self.exchange_rate, self.input_currency.currency_code, self.output_currency.currency_code, self.exchanger.name, self.time)

class Transfer(models.Model):
    time = models.DateTimeField()
    source_exchanger = models.ForeignKey(Exchanger, related_name="+")
    destination_exchanger = models.ForeignKey(Exchanger, related_name="+")
    currency = models.ForeignKey(Currency, db_column="currency_code", related_name="+")
    amount = models.DecimalField(max_digits=19,decimal_places=10)
    
    def __unicode__(self):
        return "%f %s from %s to %s on %s" % (self.amount, self.currency.currency_code, self.source_exchanger, self.destination_exchanger, self.time)

class UserTradeTrigger(models.Model):
    user = models.ForeignKey(User)
    sell_currency = models.ForeignKey(Currency, db_column="sell_currency_code", related_name="+")
    buy_currency = models.ForeignKey(Currency, db_column="buy_currency_code", related_name="+")
    max_price = models.DecimalField(max_digits=19,decimal_places=10) # max price of currency bought in currency sold
    
    def __unicode__(self):
        return "User %d would like to buy %s for %f %s" % (self.user.id, self.buy_currency.currency_code, self.max_price, self.sell_currency.currency_code)

class UserExchanger(models.Model):
    user = models.ForeignKey(User)
    exchanger = models.ForeignKey(Exchanger)
    
    def __unicode__(self):
        return "User %d controls %s" % (self.user.id, self.exchanger.name)


class UserPreferredTradingPartner(models.Model):
    user = models.ForeignKey(User)
    partner = models.ForeignKey(Exchanger)

    def __unicode__(self):
        return "User %d can trade with %s" % (self.user.id, self.partner.name)
