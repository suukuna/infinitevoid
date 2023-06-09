from fastapi import FastAPI

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
    {'id': 5, 'user_id': 5, 'currency': 'ARB', 'side': 'buy', 'price': 32.8, 'date': '12.01.2023'},
    {'id': 6, 'user_id': 6, 'currency': 'ARB', 'side': 'sell', 'price': 32.4, 'date': '12.01.2023'},
    {'id': 7, 'user_id': 7, 'currency': 'ARB', 'side': 'buy', 'price': 22.16, 'date': '12.01.2023'},
    {'id': 8, 'user_id': 8, 'currency': 'ARB', 'side': 'sell', 'price': 22.8, 'date': '12.01.2023'},
    {'id': 9, 'user_id': 9, 'currency': 'ARB', 'side': 'buy', 'price': 130.43, 'date': '12.01.2023'},
    {'id': 10, 'user_id': 10, 'currency': 'ARB', 'side': 'sell', 'price': 130.21, 'date': '12.01.2023'},
    {'id': 11, 'user_id': 11, 'currency': 'ARB', 'side': 'buy', 'price': 4.2, 'date': '12.01.2023'},
    {'id': 12, 'user_id': 12, 'currency': 'ARB', 'side': 'sell', 'price': 4.1, 'date': '12.01.2023'},
]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 0):   #limit - limit po sdelkam na stranice, offset - peremescheniye po spisku(cherez skolko objectov prigayem),   int = 1, int = 0 - znacheniye po umolchaniyu
    return fake_trades[offset:][:limit]                                     #?


fake_users2 = [
    {'id': 1, 'role': 'admin', 'name': 'George'},
    {'id': 2, 'role': 'investor', 'name': 'Max'},
    {'id': 3, 'role': 'trader', 'name': 'Vlad'},
]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users2))[0] #<-iteriruemsya po useru, fake_user2 - iteriruyemiy object
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user} #tut vozvrashcaetsya status 200, chto b user ponimal chto vse ok, operaciya vipolnena, a potom vozvraschetsya ego obnovlenniye danniye
