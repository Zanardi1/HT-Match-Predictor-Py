from flask import Flask
from .index import index_routes
from .connected import connected_routes
from .admin import admin_routes


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object('config.Config')
    app.register_blueprint(index_routes.index_bp)
    app.register_blueprint(connected_routes.connected_bp)
    app.register_blueprint(admin_routes.admin_bp)
    return app
