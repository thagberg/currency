from sim.models import Transfer
from django.db.models import Q

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
