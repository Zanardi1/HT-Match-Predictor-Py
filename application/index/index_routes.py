# Defineste rutele pentru pagina de index

import datetime
import os.path
import xml.etree.ElementTree as ET
import zipfile as z

import sqlalchemy.exc
import werkzeug.exceptions as we
from flask import Blueprint
from flask import render_template
from flask import request

import application.dialog_windows as dw
import global_library
from application.admin import create_db
from application.admin import delete_db
from application.admin import import_matches
from application.connected import download_future_match
from application.connected import download_user_matches
from application.connected import hattrick_connect
from application.connected import hattrick_disconnect
from application.estimation import estimation_engine

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')


# Functia intoarce numele echipei selectate pentru a-i afla viitoarele meciuri
def get_user_team_name():
    if global_library.team_id == global_library.user_data['team 1 id']:
        return global_library.user_data['team 1 name']
    elif global_library.team_id == global_library.user_data['team 2 id']:
        return global_library.user_data['team 2 name']
    else:
        return global_library.user_data['team 3 name']


# Functia arata daca echipa test_team joaca acasa sau in deplasare
def team_plays_home_or_away(match_id, team_to_test):
    real_home_team = ''
    match_list = ET.parse(global_library.matches_savepath).getroot()[5][5]
    for match in match_list.findall('Match'):
        if match_id == match[0].text:
            real_home_team = match[1][1].text
            break
    return 'Home' if team_to_test == real_home_team else 'Away'


# index
@index_bp.route('/')
def home():
    return render_template('index.html', title="The Best Match Predictor", ratings=global_library.ratings,
                           positions=global_library.positions,
                           statuses=global_library.statuses, from_index=True,
                           match_orders=global_library.default_match_orders,
                           answer=global_library.ans)


# conectarea la Hattrick
@index_bp.route('/LoginToHattrick')
def LoginToHattrick():
    connection_successful, global_library.user_data = hattrick_connect.connection_engine()
    if connection_successful:
        global_library.connected_to_hattrick = True
        return render_template('connected.html', title="Connected to Hattrick", from_index=False,
                               ratings=global_library.ratings,
                               positions=global_library.positions, statuses=global_library.statuses,
                               user_data=global_library.user_data,
                               match_orders=global_library.default_match_orders,
                               answer=global_library.ans, checked=global_library.default_checked_team)
    else:
        return render_template('index.html', title="The Best Match Predictor", ratings=global_library.ratings,
                               positions=global_library.positions,
                               statuses=global_library.statuses, from_index=True, answer=global_library.ans,
                               match_orders=global_library.default_match_orders)


# algoritmul de estimare
@index_bp.route('/EstimationEngine', methods=['POST'])
def estimation():
    if global_library.connected_to_hattrick:
        return render_template('connected.html', title="Connected to Hattrick", from_index=False,
                               ratings=global_library.ratings,
                               positions=global_library.positions, statuses=global_library.statuses,
                               user_data=global_library.user_data,
                               match_orders=tuple([i for i in request.form.values()]),
                               answer=estimation_engine.estimate_results(
                                   given_ratings=tuple([i for i in request.form.values()])),
                               checked=global_library.default_checked_team, from_estimation=True)
    else:
        return render_template('index.html',
                               title="The Best Match Predictor", ratings=global_library.ratings,
                               positions=global_library.positions,
                               statuses=global_library.statuses, from_index=True,
                               match_orders=tuple([i for i in request.form.values()]),
                               answer=estimation_engine.estimate_results(
                                   given_ratings=tuple([i for i in request.form.values()])), from_estimation=True)


# deconectarea de la Hattrick
@index_bp.route('/DisconnectFromHattrick')
def disconnect_from_hattrick():
    hattrick_disconnect.disconnection_engine(show_confirmation_window=True)
    global_library.connected_to_hattrick = False
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=global_library.ratings, positions=global_library.positions,
                           statuses=global_library.statuses, from_index=True,
                           match_orders=global_library.default_match_orders,
                           answer=global_library.ans)


# importarea de meciuri in baza de date
@index_bp.route('/import', methods=['POST'])
def import_matches_into_database():
    try:
        import_matches.import_engine(low_end=int(request.form['InferiorLimit']),
                                     high_end=int(request.form['SuperiorLimit']))
    except ValueError:
        dw.show_error_window_in_thread(title='Date introduse gresit!',
                                       message='Trebuie sa introduci valori numerice intregi in ambele casute!')
    except IndexError:
        dw.show_error_window_in_thread(title='Numar inexistent!',
                                       message='Numarul de identificare al unei limite (sau a ambelor) nu exista. Cel '
                                               'mai probabil ai introdus numere negative sau 0.')
    except sqlalchemy.exc.IntegrityError:
        dw.show_error_window_in_thread(title='Meciuri existente',
                                       message='In intervalul introdus este macar un meci care este in baza de date')
    else:
        dw.show_info_window_in_thread(title='Import terminat', message='Am importat toate meciurile alese')
    return render_template('admin.html', title='Admin Control Panel')


# iesirea din panoul de control catre prima pagina
@index_bp.route('/LogoutToIndex')
def logout():
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=global_library.ratings, positions=global_library.positions,
                           statuses=global_library.statuses, from_index=True,
                           match_orders=global_library.default_match_orders,
                           answer=global_library.ans)


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


def mark_chosen_option():
    if global_library.team_id == global_library.user_data['team 1 id']:
        checked = ('checked', '', '')
    elif global_library.team_id == global_library.user_data['team 2 id']:
        checked = ('', 'checked', '')
    else:
        checked = ('', '', 'checked')
    return checked


# Intoarce numarul de identificare al unui meci selectat
@index_bp.route('/GetMatch', methods=['POST'])
def get_match_id():
    global_library.team_id = request.form['HattrickTeams']
    global_library.user_team_name = get_user_team_name()
    global_library.user_matches = download_user_matches.download_user_matches(global_library.team_id)
    checked = mark_chosen_option()
    if len(global_library.user_matches) == 0:
        dw.show_error_window_in_thread(title='No match found',
                                       message='This team does not have any future matches of the selected types '
                                               'scheduled')
        match_orders = global_library.default_match_orders
        place_to_play = 'Home'
    else:
        try:
            if global_library.old_checked == checked:
                match_id = request.form['FutureMatches']
            else:
                match_id = global_library.user_matches[0][0]
        except we.BadRequestKeyError:
            match_id = global_library.user_matches[0][0]
        match_orders = download_future_match.download_future_match(match_id=match_id,
                                                                   team_id=global_library.team_id)
        place_to_play = team_plays_home_or_away(match_id=match_id, team_to_test=global_library.user_team_name)
    global_library.old_checked = checked
    return render_template('connected.html', title="Connected to Hattrick", from_index=False,
                           ratings=global_library.ratings,
                           positions=global_library.positions, statuses=global_library.statuses,
                           user_data=global_library.user_data,
                           user_matches=global_library.user_matches,
                           match_orders=match_orders,
                           place=place_to_play,
                           answer=global_library.ans, checked=checked)


@index_bp.route('/backup')
def backup_database():
    with z.ZipFile(file=global_library.database_backup_path + '\\backup ' + datetime.datetime.now().strftime(
            '%Y-%m-%d %H-%M-%S') + '.zip', mode='w') as backup:
        backup.write(global_library.database_file_path,
                     arcname='matches.db')
    dw.show_info_window_in_thread(title='Backup terminat', message='Am terminat backupul bazei de date.')
    return render_template('admin.html')


@index_bp.route('/restore')
def restore_database():
    with z.ZipFile(file=dw.restore_backup_window_in_thread(), mode='r') as restore:
        restore.extractall(os.path.dirname(global_library.database_file_path))
    dw.show_info_window_in_thread(title='Restaurare incheiata', message='S-a incheiat restaurarea backupului ales')
    return render_template('admin.html')
