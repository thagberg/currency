from sim.models import Exchanger
from sim.balance import ExchangerBalance
exchanger = Exchanger.objects.get(id=3)
balancer = ExchangerBalance(exchanger)
from datetime import datetime
balancer.generate_exchange_rates( datetime.strptime('2013-01-01', '%Y-%m-%d'), datetime.strptime('2014-03-01', '%Y-%m-%d'), 500 )