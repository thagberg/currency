import json
from django.http import HttpResponse
from django.core import serializers
import sim

def get_transfers(request):
    return HttpResponse(serializers.serialize('json', sim.models.Transfer.objects.all()), content_type="application/json")

def post_trade(request):
    return HttpResponse(json.dumps({'hi': 'wat ap'}), content_type="application/json")
