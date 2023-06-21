import library

from fastapi import FastAPI

from schemes import Trade

import sentry_sdk

sentry_sdk.init(
    dsn="https://57e7cb78c3054eadabd32b54a81fa19b@o4505250926886912.ingest.sentry.io/4505393826037760",
    traces_sample_rate=1.0,
)

app = FastAPI(
    title='Crypto App'
)


@app.post('/trades')
def add_trades(trade: Trade):
    new_trade = {
        'currency': trade.currency,
        'side': trade.side,
    }
    result = library.add_new_trade(new_trade)
    return {'status': 200, 'data': result}


@app.delete('/trades')
def delete_trades(trade: Trade):
    useless_trade = {
        'currency': trade.currency,
        'side': trade.side,
    }
    result = library.delete_new_trade(useless_trade)
    return {'status': 200, 'data': result}


@app.get('/trades')
def get_trades():  # limit - limit po sdelkam na stranice, offset - peremescheniye po spisku(cherez skolko objectov prigayem),   int = 1, int = 0 - znacheniye po umolchaniyu
    return {'data': library.get_all_trades()}  # ?

# fake_users2 = [
#     {'id': 1, 'role': 'admin', 'name': 'George'},
#     {'id': 2, 'role': 'investor', 'name': 'Max'},
#     {'id': 3, 'role': 'trader', 'name': 'Vlad'},
# ]


# @app.post('/users/{user_id}')
# def change_user_name(user_id: int, new_name: str):
#     current_user = List(filter(lambda user: user.get('id') == user_id, fake_users2))[0] #<-iteriruemsya po useru, fake_user2 - iteriruyemiy object
#     current_user['name'] = new_name
#     return {'status': 200, 'data': current_user} #tut vozvrashcaetsya status 200, chto b user ponimal chto vse ok, operaciya vipolnena, a potom vozvraschetsya ego obnovlenniye danniye


# user_id: int):  # vse parametri nahodyaschiesya v seredine path po defoltu = str, chto b privesti vse eto k int nado postavit' (user_id: int)
#         user.get('id') == user_id]  # -> [expression for item in iterable if condition == True]
# return [user for user in fake_users if
