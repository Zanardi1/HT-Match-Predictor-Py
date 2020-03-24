from flask import Flask
from . import routes


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object('config.Config')
    app.register_blueprint(routes.index_bp)
    return app
