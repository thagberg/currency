from django.contrib import admin
from sim.models import *

admin.site.register(Exchanger)
admin.site.register(Currency)
admin.site.register(ExchangeRate)
admin.site.register(Transfer)
admin.site.register(UserTradeTrigger)
admin.site.register(UserExchanger)
admin.site.register(UserPreferredTradingPartner)