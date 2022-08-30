import requests

# fixtures

USER_GET_UID = 25

USER_POST_DATA = {
    "age": 88,
    "email": "kulit1post@mymail.com",
    "first_name": "Posted",

    "last_name": "User",
    "phone": "61974785684",
    "role": "customer",
}

# UID not used in test below, kept for possible use in the future
USER_PUT_UID = 28

USER_PUT_DATA = {
    "age": 101,
    "email": "kulput@mymail.com",
    "first_name": "Put",

    "last_name": "User",
    "phone": "61974785684",
    "role": "customer"
}

# UID not used in test below, kept for possible use in the future
USER_DELETE_UID = 31

ORDER_GET_UID = 25

ORDER_POST_DATA = {
  "address": "93328 Davis Island, Rodriguezside, VT 16860",
  "customer_id": 16,
  "description": "Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.",
  "end_date": "05/23/2009",
  "executor_id": 19,
  "id": 2,
  "name": "Тестовая задача для добавления",
  "price": 2320,
  "start_date": "04/19/2008"
}

# UID not used in test below, kept for possible use in the future
ORDER_PUT_UID = 28

ORDER_PUT_DATA = {
  "address": "93328 Davis Island, Rodriguezside, VT 16860",
  "customer_id": 16,
  "description": "Площадь 85 м²: нету спальни, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.",
  "end_date": "05/23/2019",
  "executor_id": 19,
  "id": 2,
  "name": "Тестовая задача для исправления",
  "price": 2000,
  "start_date": "04/19/2008"
}

# UID not used in test below, kept for possible use in the future
ORDER_DELETE_UID = 31


# UID not used in test below, kept for possible use in the future
ORDER_DELETE_UID = 31

OFFER_GET_UID = 25

OFFER_POST_DATA = {
  "executor_id": 19,
  "order_id": 2,
  }

# UID not used in test below, kept for possible use in the future
OFFER_PUT_UID = 28

OFFER_PUT_DATA = {
  "executor_id": 9,
  "order_id": 32,
  }

# UID not used in test below, kept for possible use in the future
OFFER_DELETE_UID = 31


# Classes

class Users:
    URL = 'http://127.0.0.1:5000/users'

    @staticmethod
    def post():
        response = requests.post(Users.URL, json=USER_POST_DATA)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def put(uid: int):
        response = requests.put(f'{Users.URL}/{str(uid)}', json=USER_PUT_DATA)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def delete(uid: int):
        response = requests.delete(f'{Users.URL}/{str(uid)}')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_one(uid: int):
        response = requests.get(f'{Users.URL}/{str(uid)}')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_all():
        response = requests.get(Users.URL)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text


class Orders:
    URL = 'http://127.0.0.1:5000/orders'

    @staticmethod
    def post():
        response = requests.post(Orders.URL, json=ORDER_POST_DATA)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def put(uid: int):
        response = requests.put(f'{Orders.URL}/{str(uid)}', json=ORDER_PUT_DATA)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def delete(uid: int):
        response = requests.delete(f'{Orders.URL}/{str(uid)}')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_one(uid: int):
        response = requests.get(f'{Orders.URL}/{str(uid)}')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_all():
        response = requests.get(Orders.URL)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text


class Offers:
    URL = 'http://127.0.0.1:5000/offers'

    @staticmethod
    def post():
        response = requests.post(Offers.URL, json=OFFER_POST_DATA)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def put(uid: int):
        response = requests.put(f'{Offers.URL}/{str(uid)}', json=OFFER_PUT_DATA)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def delete(uid: int):
        response = requests.delete(f'{Offers.URL}/{str(uid)}')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_one(uid: int):
        response = requests.get(f'{Offers.URL}/{str(uid)}')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_all():
        response = requests.get(Offers.URL)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text


# testing modules

def test_users():
    print('Testing users...')

    all_users = Users.get_all()
    if all_users[1]['first_name'] == 'George':
        print('Get all users: Ok!')
    else:
        print('Get all users: ERROR!')
        exit()
    max_id = all_users[-1]['id']
    print('Max id:', max_id, '\n')

    a = Users.get_one(USER_GET_UID)
    print(a)
    if a['phone'] == '8143159413':
        print('Get single user: Ok!\n')
    else:
        print('Get single user: ERROR!')
        exit()

    print(Users.post())
    b = Users.get_one(max_id + 1)
    if b['first_name'] == USER_POST_DATA['first_name']:
        print('Post single user: Ok!\n')
    else:
        print('Post single user: ERROR!')
        exit()

    print(Users.put(max_id + 1))
    b = Users.get_one(max_id + 1)
    if b['first_name'] == USER_PUT_DATA['first_name']:
        print('Put single user: Ok!\n')
    else:
        print('Put single user: ERROR!')
        exit()


    #comment out to check unique values
    print(Users.delete(max_id + 1))
    all_users = Users.get_all()
    if all_users[-1]['id'] == max_id:
        print('Delete single user: Ok!\n')
    else:
        print('Delete single user: ERROR!')
        exit()


def test_orders():
    print('Testing orders...')

    all_orders = Orders.get_all()
    if all_orders[1]['price'] == 2800:
        print('Get all orders: Ok!')
    else:
        print('Get all orders: ERROR!')
        exit()
    max_id = all_orders[-1]['id']
    print('Max id:', max_id, '\n')

    a = Orders.get_one(ORDER_GET_UID)
    print(a)
    if a["name"] == "Встретить тетю на вокзале":
        print('Get single order: Ok!\n')
    else:
        print('Get single order: ERROR!')
        exit()

    print(Orders.post())
    b = Orders.get_one(max_id + 1)
    if b['name'] == ORDER_POST_DATA['name']:
        print('Post single order: Ok!\n')
    else:
        print('Post single order: ERROR!')
        exit()

    print(Orders.put(max_id + 1))
    b = Orders.get_one(max_id + 1)
    if b['name'] == ORDER_PUT_DATA['name']:
        print('Put single order: Ok!\n')
    else:
        print('Put single order: ERROR!')
        exit()

    print(Orders.delete(max_id + 1))
    all_orders = Orders.get_all()
    if all_orders[-1]['id'] == max_id:
        print('Delete single order: Ok!\n')
    else:
        print('Delete single order: ERROR!')
        exit()


def test_offers():
    print('Testing offers...')

    all_offers = Offers.get_all()
    if all_offers[1]['executor_id'] == 4:
        print('Get all offers: Ok!')
    else:
        print('Get all offers: ERROR!')
        exit()
    max_id = all_offers[-1]['id']
    print('Max id:', max_id, '\n')

    a = Offers.get_one(OFFER_GET_UID)
    print(a)
    if a["order_id"] == 47:
        print('Get single offer: Ok!\n')
    else:
        print('Get single offer: ERROR!')
        exit()

    print(Offers.post())
    b = Offers.get_one(max_id + 1)
    if b['order_id'] == OFFER_POST_DATA['order_id']:
        print('Post single offer: Ok!\n')
    else:
        print('Post single offer: ERROR!')
        exit()

    print(Offers.put(max_id + 1))
    b = Offers.get_one(max_id + 1)
    if b['order_id'] == OFFER_PUT_DATA['order_id']:
        print('Put single offer: Ok!\n')
    else:
        print('Put single offer: ERROR!')
        exit()

    print(Offers.delete(max_id + 1))
    all_offers = Offers.get_all()
    if all_offers[-1]['id'] == max_id:
        print('Delete single offer: Ok!\n')
    else:
        print('Delete single offer: ERROR!')
        exit()


# just in case

def _test_invalid_id():
    print(Users.get_one(88))


def main():
    test_users()
    test_orders()
    test_offers()
    print('All seems Ok!')


if __name__ == '__main__':
    main()