"""Defineste rutele pentru pagina de index"""

from flask import Blueprint
from flask import render_template

import global_library
from application.connected import hattrick_connect
from application.connected import hattrick_disconnect
from application.estimation import Estimation_engine

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')
ratings = global_library.ratings
positions = global_library.positions
statuses = global_library.statuses


@index_bp.route('/')
def home():
    return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True)


@index_bp.route('/LoginToHattrick')
def LoginToHattrick():
    hattrick_connect.ConnectionEngine()
    return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                           positions=positions, statuses=statuses)


@index_bp.route('/EstimationEngine')
def EstimationEngine():
    Estimation_engine.Estimate()
    return 0


@index_bp.route('/DisconnectFromHattrick')
def DisconnectFromHattrick():
    hattrick_disconnect.DisconnectionEngine()
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True)


@index_bp.route('/import')
def import_matches():
    from application.admin import import_matches
    import_matches.import_engine()
    return 0


@index_bp.route('/LogoutToIndex')
def logout():
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True)
