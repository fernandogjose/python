from flask import Flask
from src.infra.extensions import configuration
from src.infra.extensions.database import db


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app
