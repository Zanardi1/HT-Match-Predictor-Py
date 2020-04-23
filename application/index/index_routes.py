# Defineste rutele pentru pagina de index

import os
import xml.etree.ElementTree as ET

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
from application.estimation import estimation_engine
import easygui

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')
ratings = global_library.ratings
positions = global_library.positions
statuses = global_library.statuses

user_data_global = {}
team_id_global = 0
user_team_name_global = ''
user_matches_global = []
default_match_orders = (-1, -1, -1, -1, -1, -1, -1)


# Functia intoarce numele echipei selectate pentru a-i afla viitoarele meciuri
def get_user_team_name():
    if team_id_global == user_data_global['team 1 id']:
        return user_data_global['team 1 name']
    elif team_id_global == user_data_global['team 2 id']:
        return user_data_global['team 2 name']
    else:
        return user_data_global['team 3 name']


# Functia arata daca echipa test_team joaca acasa sau in deplasare
def home_or_away(match_id, test_team):
    real_home_team = ''
    tree = ET.parse(os.path.abspath('application\\xml\\Matches.xml'))
    root = tree.getroot()
    match_list = root[5][5]
    for match in match_list.findall('Match'):
        found_match_id = match[0].text
        if match_id == found_match_id:
            real_home_team = match[1][1].text
            break
    if test_team == real_home_team:
        return 'Home'
    else:
        return 'Away'


# index
@index_bp.route('/')
def home():
    match_orders = default_match_orders
    return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True, match_orders=match_orders)


# conectarea la Hattrick
@index_bp.route('/LoginToHattrick')
def LoginToHattrick():
    global user_data_global
    connection_successful, user_data = hattrick_connect.connection_engine()
    user_data_global = user_data
    match_orders = default_match_orders
    if connection_successful:
        return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                               positions=positions, statuses=statuses, user_data=user_data, match_orders=match_orders)
    else:
        return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                               statuses=statuses, from_index=True)


# algoritmul de estimare
@index_bp.route('/EstimationEngine')
def EstimationEngine():
    estimation_engine.estimate()
    return 0


# deconectarea de la Hattrick
@index_bp.route('/DisconnectFromHattrick')
def disconnect_from_hattrick():
    hattrick_disconnect.disconnection_engine()
    match_orders = default_match_orders
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True, match_orders=match_orders)


# importarea de meciuri in baza de date
@index_bp.route('/import', methods=['POST'])
def import_matches_into_database():
    low_end = request.form['InferiorLimit']
    high_end = request.form['SuperiorLimit']
    low_end = int(low_end)
    high_end = int(high_end)
    import_matches.import_engine(low_end, high_end)
    easygui.msgbox('Gata')
    return render_template('admin.html', title='Admin Control Panel')


# iesirea din panoul de control catre prima pagina
@index_bp.route('/LogoutToIndex')
def logout():
    match_orders = default_match_orders
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True, match_orders=match_orders)


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
# TODO atunci cand selectez a doua sau a treia echipa, prima optiune redevine marcata dupa apasarea butonului OK.
#  Sa fac astfel incat sa ramana marcata optiunea selectata dinainte de apasarea butonului OK.
@index_bp.route('/Team', methods=['POST'])
def get_team_id():
    global user_matches_global
    global team_id_global
    global user_team_name_global
    team_id = request.form['HattrickTeams']
    team_id_global = team_id
    user_team_name_global = get_user_team_name()
    user_matches = download_user_matches.download_user_matches(team_id)
    user_matches_global = user_matches
    match_orders = default_match_orders
    return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                           positions=positions, statuses=statuses, user_data=user_data_global,
                           user_matches=user_matches, match_orders=match_orders)


# Intoarce numarul de identificare al unui meci selectat
# TODO De aflat daca echipa mea joaca acasa sau in deplasare si de completat combobox-urile potrivite
@index_bp.route('/GetMatch', methods=['POST'])
def get_match_id():
    match_id = request.form['FutureMatches']
    match_orders = download_future_match.download_future_match(match_id, team_id_global)
    place = home_or_away(match_id, user_team_name_global)
    return render_template('connected.html', title="Connected to Hattrick", from_index=False, ratings=ratings,
                           positions=positions, statuses=statuses, user_data=user_data_global,
                           user_matches=user_matches_global, match_orders=match_orders, place=place)
