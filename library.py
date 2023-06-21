from copy import copy

import requests
from datetime import datetime

from bson import ObjectId

from database import collection_trades

URL = 'https://api.coinstats.app/public/v1/markets?coinId={}'


def get_current_price(currency_name: str, url: str = URL):
    data = requests.get(url.format(currency_name))
    return data.json()[0]['price']


def add_new_trade(trade: dict):
    trade = copy(trade)
    trade['date'] = datetime.now()
    trade['price'] = get_current_price(trade['currency'])
    collection_trades.insert_one(trade)
    trade['_id'] = str(trade['_id'])
    return trade


def delete_trades(trade: dict):
    trade = copy(trade)
    trade['date'] = datetime.now()
    trade['price'] = get_current_price(trade['currency'])
    collection_trades.find_one_and_delete(trade)
    trade['_id'] = str(trade['_id'])
    return {'_id': ObjectId(trade['_id'])}


def get_all_trades():
    return list(collection_trades.find({}, {'_id': 0}))

