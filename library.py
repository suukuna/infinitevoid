from copy import copy

import requests
from datetime import datetime

from database import collection_trades

URL = 'https://api.coinstats.app/public/v1/markets?coinId={}'


def get_current_price(currency_name: str, url: str=URL):
    data = requests.get(url.format(currency_name))
    return data.json()[0]['price']


def add_new_trade(trade: dict):
    trade = copy(trade)
    trade['date'] = datetime.now()
    trade['price'] = get_current_price(trade['currency'])
    collection_trades.insert_one(trade)
    trade['_id'] = str(trade['_id'])
    return trade
