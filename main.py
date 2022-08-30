from app import app
from blueprints.users_view import users_blueprint
from blueprints.orders_view import orders_blueprint
from blueprints.offers_view import offers_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(offers_blueprint)


if __name__ == '__main__':
    app.run()