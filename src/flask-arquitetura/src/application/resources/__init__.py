from flask import Blueprint
from flask_restful import Api
from .home_resource import HomeResource

blueprint = Blueprint("restapi", __name__, url_prefix="/api/v1")

api = Api(blueprint)
api.add_resource(HomeResource, "/home/")


def init_app(app):
    app.register_blueprint(blueprint)
