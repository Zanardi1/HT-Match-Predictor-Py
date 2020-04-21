# Defineste rutele pentru pagina de index

from flask import Blueprint
from flask import render_template
from flask import request

import global_library
from application.admin import create_db
from application.admin import delete_db
from application.admin import import_matches
from application.connected import download_future_match
from application.connected import download_user_matches
from application.connected import hattrick_connect
from application.connected import hattrick_disconnect
from application.estimation import Estimation_engine

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')
ratings = global_library.ratings
positions = global_library.positions
statuses = global_library.statuses

user_data_global = {}
team_id_global = 0
user_team_name_global = ''
user_matches_global = []


# index
@index_bp.route('/')
def home():
    match_orders = (-1, -1, -1, -1, -1, -1, -1)
    return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True, match_orders=match_orders)


# conectarea la Hattrick
@index_bp.route('/LoginToHattrick')
def LoginToHattrick():
    global user_data_global
    connection_successful, user_data = hattrick_connect.connection_engine()
    user_data_global = user_data
    match_orders = (-1, -1, -1, -1, -1, -1, -1)
    if connection_successful:
        return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                               positions=positions, statuses=statuses, user_data=user_data, match_orders=match_orders)
    else:
        return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                               statuses=statuses, from_index=True)


# algoritmul de estimare
@index_bp.route('/EstimationEngine')
def EstimationEngine():
    Estimation_engine.Estimate()
    return 0


# deconectarea de la Hattrick
@index_bp.route('/DisconnectFromHattrick')
def DisconnectFromHattrick():
    hattrick_disconnect.DisconnectionEngine()
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True)


# importarea de meciuri in baza de date
@index_bp.route('/import')
def import_matches():
    import_matches.import_engine()
    return 0


# iesirea din panoul de control catre prima pagina
@index_bp.route('/LogoutToIndex')
def logout():
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True)


# crearea bazei de date
@index_bp.route('/create')
def create():
    create_db.create_database()
    return render_template('admin.html')


# stergerea bazei de date
@index_bp.route('/delete')
def delete():
    delete_db.delete_database()
    return render_template('admin.html')


# Intoarce numele echipei selectate
@index_bp.route('/Team', methods=['POST'])
def get_team_id():
    global user_matches_global
    global team_id_global
    global user_team_name_global
    team_id = request.form['HattrickTeams']
    team_id_global = team_id
    user_matches = download_user_matches.download_user_matches(team_id)
    user_matches_global = user_matches
    match_orders = (-1, -1, -1, -1, -1, -1, -1)
    return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                           positions=positions, statuses=statuses, user_data=user_data_global,
                           user_matches=user_matches, match_orders=match_orders)


# Intoarce numarul de identificare al unui meci selectat
# TODO De aflat daca echipa mea joaca acasa sau in deplasare si de completat combobox-urile potrivite
@index_bp.route('/GetMatch', methods=['POST'])
def get_match_id():
    match_id = request.form['FutureMatches']
    match_orders = download_future_match.download_future_match(match_id, team_id_global)
    return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                           positions=positions, statuses=statuses, user_data=user_data_global,
                           user_matches=user_matches_global, match_orders=match_orders)
