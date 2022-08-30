import json

import sqlalchemy

from models import User, Offer, Order
from blueprints.orders_view import date_to_str, str_to_date
from db import db


def get_users_from_json() -> list:

    try:
        with open('raw_data/users.json', encoding='utf-8') as fin:
            users = json.load(fin)
    except FileNotFoundError:
        print('Users file not found!')
        # file_logger.critical(f'JSON file {fname} not found')
        users = []
    except json.JSONDecodeError:
        print('Users Json decoding error')
        # file_logger.critical(f'JSON file {fname} decode error')
        users = []

    return users


def get_orders_from_json() -> list:
    try:
        with open('raw_data/orders.json', encoding='utf-8') as fin:
            orders = json.load(fin)
    except FileNotFoundError:
        print('Orders file not found!')
        # file_logger.critical(f'JSON file {fname} not found')
        orders = []
    except json.JSONDecodeError:
        print('Orders Json decoding error')
        # file_logger.critical(f'JSON file {fname} decode error')
        orders = []

    return orders


def get_offers_from_json() -> list:
    try:
        with open('raw_data/offers.json', encoding='utf-8') as fin:
            offers = json.load(fin)
    except FileNotFoundError:
        print('Offers file not found!')
        # file_logger.critical(f'JSON file {fname} not found')
        offers = []
    except json.JSONDecodeError:
        print('Offers Json decoding error')
        # file_logger.critical(f'JSON file {fname} decode error')
        offers = []

    return offers


def create_db():
    users = get_users_from_json()
    orders = get_orders_from_json()
    offers = get_offers_from_json()

    for user in users:
        db.session.add(User(**user))

    # for user in users:
    #     val = User(
    #             id=user['id'],
    #             first_name=user['first_name'],
    #             last_name=user['last_name'],
    #             age=user['age'],
    #             email=user['email'],
    #             role=user['role'],
    #             phone=user['phone'],
    #             )
    #     db.session.add(val)
    # db.session.commit()

    for order in orders:
        # db.session.add(Order(**order))

        val = Order(
                id=order['id'],
                name=order['name'],
                description=order['description'],
                start_date=str_to_date(order['start_date']),
                end_date=str_to_date(order['end_date']),
                address=order['address'],
                price=order['price'],
                customer_id=order['customer_id'],
                executor_id=order['executor_id'],
        )
        db.session.add(val)
    # db.session.commit()

    for offer in offers:
        db.session.add(Offer(**offer))

        # val = Offer(
        #         id=offer['id'],
        #         order_id=offer['order_id'],
        #         executor_id=offer['executor_id'],
        # )
        # db.session.add(val)

    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        print(f'INFO: Data already exists')


if __name__ == '__main__':
    a = get_users_from_json()
    # print(a)
    db.create_all()
    create_db()

    print(User.query.get(1).first_name)
    print(Order.query.get(1).name)
    print(Offer.query.get(1).order_id)