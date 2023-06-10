from fastapi import FastAPI

from pydantic import BaseModel, Field

app = FastAPI(
    title='Crypto App'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'George'},
    {'id': 2, 'role': 'investor', 'name': 'Max'},
    {'id': 3, 'role': 'trader', 'name': 'Vlad'},
]


@app.get('/users/{user_id}')  # <- path
def get_user_id(user_id: int):  #vse parametri nahodyaschiesya v seredine path po defoltu = str, chto b privesti vse eto k int nado postavit' (user_id: int)
    return [user for user in fake_users if user.get('id') == user_id]  #-> [expression for item in iterable if condition == True]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'ARB', 'side': 'buy', 'price': 8.12, 'date': '12.01.2023'},
    {'id': 2, 'user_id': 2, 'currency': 'ARB', 'side': 'sell', 'price': 8.1, 'date': '12.01.2023'},
    {'id': 3, 'user_id': 3, 'currency': 'ARB', 'side': 'buy', 'price': 16.4, 'date': '12.01.2023'},
    {'id': 4, 'user_id': 4, 'currency': 'ARB', 'side': 'sell', 'price': 16.2, 'date': '12.01.2023'},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    date: float


@app.post('/trades')
def add_trades(trades: list[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}



# @app.get('/trades')
# def get_trades(limit: int = 1, offset: int = 0):   #limit - limit po sdelkam na stranice, offset - peremescheniye po spisku(cherez skolko objectov prigayem),   int = 1, int = 0 - znacheniye po umolchaniyu
#     return fake_trades[offset:][:limit]                                     #?


# fake_users2 = [
#     {'id': 1, 'role': 'admin', 'name': 'George'},
#     {'id': 2, 'role': 'investor', 'name': 'Max'},
#     {'id': 3, 'role': 'trader', 'name': 'Vlad'},
# ]


# @app.post('/users/{user_id}')
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get('id') == user_id, fake_users2))[0] #<-iteriruemsya po useru, fake_user2 - iteriruyemiy object
#     current_user['name'] = new_name
#     return {'status': 200, 'data': current_user} #tut vozvrashcaetsya status 200, chto b user ponimal chto vse ok, operaciya vipolnena, a potom vozvraschetsya ego obnovlenniye danniye
