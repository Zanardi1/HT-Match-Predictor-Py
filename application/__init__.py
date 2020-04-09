from authlib.integrations.flask_client import OAuth
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object('config.Config')

    db = SQLAlchemy(app)
    oauth = OAuth(app)

    with app.app_context():
        from .admin import admin_routes
        from .connected import connected_routes
        from .index import index_routes
        app.register_blueprint(index_routes.index_bp)
        app.register_blueprint(connected_routes.connected_bp, url_prefix='/connected')
        app.register_blueprint(admin_routes.admin_bp, url_prefix='/admin')

        db.create_all()
        oauth.register(name='Hattrick', client_id='Cx7jQlJTOwIRA2XVtRWF19',
                       client_secret='L1gwHsZZuGneTUwZKUevgBUe3HKIMBDiJv7DHwf1RjI',
                       request_token_url='https://chpp.hattrick.org/oauth/request_token.ashx',
                       request_token_params=None,
                       access_token_url='https://chpp.hattrick.org/oauth/access_token.ashx',
                       access_token_params=None,
                       authorize_url='https://chpp.hattrick.org/oauth/authorize.aspx', authorize_params=None,
                       api_base_url='https://chpp.hattrick.org/chppxml.ashx', client_kwargs=None)
        hattrick = oauth.create_client('Hattrick')
        return app
