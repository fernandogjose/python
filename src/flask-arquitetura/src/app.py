from flask import Flask
from src.infra.extensions import configuration
from src.application.controllers import home_controller


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app
