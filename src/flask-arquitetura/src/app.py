from flask import Flask
from src.infra.extensions import configuration
from src.application import resources
from src.application.controllers import home_controller

app = Flask(__name__)

configuration.init_app(app=app)
resources.init_app(app=app)
home_controller.init_app(app)
