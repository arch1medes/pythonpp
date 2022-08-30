import sqlalchemy
from flask import Blueprint, jsonify, request, abort
import datetime

from models import Order
from db import db


orders_blueprint = Blueprint('orders_blueprint', __name__)


# Two functions to deal with datetime format
def str_to_date(s: str):
    s_format = '%m/%d/%Y'
    datetime_str = datetime.datetime.strptime(s, s_format)
    return datetime_str.date()


def date_to_str(d):
    s_format = '%m/%d/%Y'
    s = datetime.datetime.strftime(d, s_format)
    return s


def order_to_dict(order):
    """
    Prepare an object for JSON
    """
    return {
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": date_to_str(order.start_date),
        "end_date": date_to_str(order.end_date),
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id,
    }


@orders_blueprint.route('/orders', methods=['GET'])
def get_all_orders():
    result = []
    orders = Order.query.all()
    for order in orders:
        result.append(order_to_dict(order))
    return jsonify(result)


@orders_blueprint.route('/orders/<int:uid>', methods=['GET'])
def get_one_order(uid):
    """
        get one order. Returns an empty dict if uid is not found
    """
    order = Order.query.get(uid)
    if order:
        return jsonify(order_to_dict(order))
    return {}


@orders_blueprint.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    # print(data)
    order = Order(
        name=data.get('name'),
        description=data.get('description'),
        start_date=str_to_date(data.get('start_date')),
        end_date=str_to_date(data.get('end_date')),
        address=data.get('address'),
        price=data.get('price'),
        customer_id=data.get('customer_id'),
        executor_id=data.get('executor_id'),
    )
    db.session.add(order)
    db.session.commit()
    return jsonify(order_to_dict(order))


@orders_blueprint.route('/orders/<int:uid>', methods=['PUT'])
def update_order(uid):
    data = request.json

    order = Order.query.get(uid)
    try:
        order.name = data.get('name')
        order.description = data.get('description')
        order.start_date = str_to_date(data.get('start_date'))
        order.end_date = str_to_date(data.get('end_date'))
        order.address = data.get('address')
        order.price = data.get('price')
        order.customer_id = data.get('customer_id')
        order.executor_id = data.get('executor_id')
    except AttributeError:
        abort(500, "Attribute error (id not present?)")

    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        abort(500, 'Integrity error (unique key not unique?)')

    return jsonify(order_to_dict(order))


@orders_blueprint.route('/orders/<int:uid>', methods=['DELETE'])
def delete_order(uid):
    order = Order.query.get(uid)
    try:
        db.session.delete(order)
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        abort(500, 'Unmapped Instance Error (id not present?)')

    db.session.commit()
    return jsonify('deleted')