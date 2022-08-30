import sqlalchemy
from flask import Blueprint, jsonify, request, abort

from db import db
from models import User

users_blueprint = Blueprint('users_blueprint', __name__)


def user_to_dict(user):
    """
    Prepare an object for JSON
    """
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone,
    }


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    result = []
    users = User.query.all()
    for user in users:
        result.append(user_to_dict(user))
    return jsonify(result)


@users_blueprint.route('/users/<int:uid>', methods=['GET'])
def get_one_user(uid):
    """
    get one user. Returns an empty dict if uid is not found
    """
    user = User.query.get(uid)
    if user:
        return jsonify(user_to_dict(user))
    return {}


@users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    # print(data)
    user = User(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        age=data.get('age'),
        email=data.get('email'),
        role=data.get('role'),
        phone=data.get('phone'),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user_to_dict(user))


@users_blueprint.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    data = request.json

    user = User.query.get(uid)
    try:
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.age = data.get('age')
        user.email = data.get('email')
        user.role = data.get('role')
        user.phone = data.get('phone')
    except AttributeError:
        abort(500, "Attribute error (id not present?)")

    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        abort(500, 'Integrity error (unique key not unique?)')

    return jsonify(user_to_dict(user))


@users_blueprint.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    user = User.query.get(uid)
    try:
        db.session.delete(user)
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        abort(500, 'Unmapped Instance Error (id not present?)')

    db.session.commit()
    return jsonify('deleted')