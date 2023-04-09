from flask import Flask
from src.infra.extensions import configuration
from src.infra.extensions.database import db


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    # create_database(app)
    return app


def create_database(app):
    print('criado')
    with app.app_context():
        db.drop_all()
        db.create_all()
