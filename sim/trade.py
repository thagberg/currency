import requests

TRADE_URL = 'http://www.cryptocoincharts.info/v2/api/tradingPair/'

def get_trade_value(crypt_curr, world_curr):
    """Get the current trade value of a cryptographic currency for
    a world currency"""
    trade_pair = '{crypt}_{world}'.format(crypt=crypt_curr,
                                          world=world_curr)
    url = '{url}{pair}'.format(url=TRADE_URL, pair=trade_pair)
    trade = requests.get(url)
    return trade.json()

