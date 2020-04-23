from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object('config.Config')

    database = SQLAlchemy(app)

    with app.app_context():
        from .admin import admin_routes
        from .connected import connected_routes
        from .index import index_routes
        app.register_blueprint(index_routes.index_bp)
        app.register_blueprint(connected_routes.connected_bp, url_prefix='/connected')
        app.register_blueprint(admin_routes.admin_bp, url_prefix='/admin')

        database.create_all()

        return app
