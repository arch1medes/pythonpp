import sqlalchemy
from flask import Blueprint, jsonify, request, abort

from db import db
from models import Offer

offers_blueprint = Blueprint('offers_blueprint', __name__)


def offer_to_dict(offers):
    """
    Prepare an object for JSON
    """
    return {
        "id": offers.id,
        "order_id": offers.order_id,
        "executor_id": offers.executor_id,
    }


@offers_blueprint.route('/offers', methods=['GET'])
def get_all_offers():
    result = []
    offers = Offer.query.all()
    for offer in offers:
        result.append(offer_to_dict(offer))
    return jsonify(result)


@offers_blueprint.route('/offers/<int:uid>', methods=['GET'])
def get_one_offer(uid):
    """
            get one offer. Returns an empty dict if uid is not found
    """
    offer = Offer.query.get(uid)
    if offer:
        return jsonify(offer_to_dict(offer))
    return {}


@offers_blueprint.route('/offers', methods=['POST'])
def create_offer():
    data = request.json
    # print(data)
    offer = Offer(
        id=data.get('id'),
        order_id=data.get('order_id'),
        executor_id=data.get('executor_id'),
    )

    db.session.add(offer)
    db.session.commit()
    return jsonify(offer_to_dict(offer))


@offers_blueprint.route('/offers/<int:uid>', methods=['PUT'])
def update_offer(uid):
    data = request.json

    offer = Offer.query.get(uid)
    try:
        offer.order_id = data.get('order_id')
        offer.executor_id = data.get('executor_id')
    except AttributeError:
        abort(500, "Attribute error (id not present?)")

    # try:
    db.session.commit()
    # except sqlalchemy.exc.IntegrityError:
    #    abort(500, 'Integrity error (unique key not unique?)')

    return jsonify(offer_to_dict(offer))


@offers_blueprint.route('/offers/<int:uid>', methods=['DELETE'])
def delete_offer(uid):
    offer = Offer.query.get(uid)
    try:
        db.session.delete(offer)
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        abort(500, 'Unmapped Instance Error (id not present?)')

    db.session.commit()
    return jsonify('deleted')