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
from application import config
from application.admin import create_db
from application.admin import delete_db
from application.admin import import_matches
from application.connected import download_future_match
from application.connected import download_user_matches_file
from application.connected import hattrick_connect
from application.connected import hattrick_disconnect
from application.connected.hattrick_connect import check_if_connection_is_valid
from application.estimation import estimation_engine

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')


# Functia intoarce numele echipei selectate pentru a-i afla viitoarele meciuri
def get_user_team_name() -> str:
    """Functia intoarce numele echipei selectate de catre utilizator.

    Algoritm:
    ----------
    Se compara numarul de identificare al echipei, din biblioteca globala, cu fiecare dintre numerele de
    identificare ale echipelor utilizatorului.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Numele echipei selectate."""

    if global_library.team_id == global_library.user_data['team 1 id']:
        return global_library.user_data['team 1 name']
    elif global_library.team_id == global_library.user_data['team 2 id']:
        return global_library.user_data['team 2 name']
    else:
        return global_library.user_data['team 3 name']


def team_plays_home_or_away(match_id: int, team_to_test: str) -> str:
    """Functia arata daca o echipa joaca acasa sau in deplasare intr-un meci.

    Algoritm:
    ----------
    Se citeste fisierul Matches.xml. Din acest fisier se cicleaza prin toate nodurile cu numele Match, pana cand
    numarul de identificare al acestuia coincide cu cel transmis ca parametru. In acel moment, se citeste echipa
    de acasa care joaca respectivul meci si se compara cu echipa transmisa ca parametru. Daca cele doua variabile
    au aceeasi valoare, atunci echipa testata joaca acasa. Altfel, ea joaca in deplasare.

    Parametri:
    ----------
    match_id: int
        numarul de identificare al meciului pentru care se verifica unde joaca echipa;
    team_to_test: str
        numele echipei care se verifica daca joaca acasa sau in deplasare.

    Intoarce:
    ----------
    'Home', daca echipa testata joaca acasa. Altfel, 'Away'."""

    real_home_team = ''
    match_list = ET.parse(global_library.matches_savepath).getroot()[5][5]
    for match in match_list.findall('Match'):
        if match_id == match[0].text:
            real_home_team = match[1][1].text
            break
    return 'Home' if team_to_test == real_home_team else 'Away'


# index
@index_bp.route('/')
def home() -> None:
    """Procedura ce afiseaza pagina index, cea care apare la pornirea programului.

    Algoritm:
    ----------
    Afiseaza pagina de inceput.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    return render_template('index.html', title="The Best Match Predictor", ratings=global_library.ratings,
                           positions=global_library.positions,
                           statuses=global_library.statuses, from_index=True,
                           match_orders=global_library.default_match_orders,
                           answer=global_library.ans)


# conectarea la Hattrick
@index_bp.route('/LoginToHattrick')
def login_to_hattrick() -> None:
    """Procedura ce conecteaza utilizatorul programului la contul sau de Hattrick si afiseaza pagina cu datele
    utilizatorului, dupa conectarea acestuia la cont.

    Algoritm:
    ----------
    Incearca sa se conecteze la contul de Hattrick. Daca reuseste, atunci obtine datele contului utilizatorului, pe
    care le afiseaza in pagina. Daca nu reuseste incercarea, revine la prima pagina.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

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
def estimation() -> None:
    """Procedura ce ruleaza algoritmul de estimare a sanselor de castig, in functie de evaluarile introduse. Rularea
    are loc la apasarea butonului de estimare.

    Algoritm:
    ----------
    Incearca sa se conecteze la contul de Hattrick. Daca reuseste, atunci preia datele contului utilizatorului. Daca
    nu, atunci revine la prima pagina. In ambele cazuri, exista butonul de estimare.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

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
def disconnect_from_hattrick() -> None:
    """Procedura ce deconecteaza utilizatorul de la contul Hattrick si afiseaza prima pagina, cea de start.
    Utilizatorul va trebui sa se reconecteze la cont pentru a avea acces la informatiile din contul sau.

    Algoritm:
    ----------
    Se deconecteaza de la contul utilizatorului de Hattrick si afiseaza prima pagina.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    hattrick_disconnect.disconnection_engine(show_confirmation_window=True)
    global_library.connected_to_hattrick = False
    return render_template('index.html', title="The Best Match Predictor",
                           ratings=global_library.ratings, positions=global_library.positions,
                           statuses=global_library.statuses, from_index=True,
                           match_orders=global_library.default_match_orders,
                           answer=global_library.ans)


@index_bp.route('/import', methods=['POST'])
def import_matches_into_database() -> None:
    """Procedura ce ruleaza algoritmul de importare a evaluarilor necesare in baza de date, plecand de la
    fisierele XML necesare, obtinute din Hattrick. Se apeleaza engine-ul de import, transmitandu-i limita
    inferioara si cea superioara a numerelor de identificare ale meciurilor ce trebuie introduse.

    Algoritm:
    -----------
    Incearca sa importe in baza de date meciurile cu numerele de identificare ce se afla intre cele doua limite. In
    functie de exceptiile care apar, afiseaza mesajele de eroare corespunzatoare. Indiferent de reusita operatiei
    de import, se revine la pagina panoului de control.

    Parametri:
    -----------
    Niciunul.

    Intoarce:
    -----------
    Nimic.

    Exceptii:
    ------------
    ValueError:
        In casutele in care se introduc limitele specificate mai sus, nu sunt introduse valori numerice, intregi;
    IndexError:
        Una sau amandoua dintre limitele specificate mai sus au numere negative, sau 0;
    sqlalchemy.exc.IntegrityError:
        In intervalul specificat de cele doua limite exista minim un meci al carui numar de identificare exista
        in baza de date."""

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
def logout() -> None:
    """Procedura ce deconecteaza utilizatorul de la pagina de administrare a bazei de date cu meciurile ale caror
     evaluari vor fi folosite pentru simulare.

    Algoritm:
    ----------
    Se afiseaza prima pagina.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    return render_template('index.html', title="The Best Match Predictor",
                           ratings=global_library.ratings, positions=global_library.positions,
                           statuses=global_library.statuses, from_index=True,
                           match_orders=global_library.default_match_orders,
                           answer=global_library.ans)


# crearea bazei de date
@index_bp.route('/create')
def create() -> None:
    """Procedura ce creaza baza de date ce contine meciurile ale caror evaluari vor fi folosite pentru simulare.

    Algoritm:
    ----------
    Se ruleaza procedura de creare a bazei de date. Indiferent de rezultatul ei, se afiseaza pagina panoului de
    control.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    create_db.create_database()
    return render_template('admin.html')


# stergerea bazei de date
@index_bp.route('/delete')
def delete() -> None:
    """Procedura ce sterge baza de date ce contine meciurile ale caror evaluari vor fi folosite pentru simulare.

    Algoritm:
    ----------
    Se ruleaza procedura de stergere a bazei de date. Indiferent de rezultatul ei, se afiseaza pagina panoului de
    control.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    delete_db.delete_database()
    return render_template('admin.html')


def get_chosen_option() -> tuple:
    """Functia stabileste numarul de ordine al echipei ale caror meciuri viitoate vor fi descarcate pentru
    utilizare ulterioara.

    Algoritm:
    ----------
    Se compara numarul de identificare al echipei, aflat in biblioteca globala cu numerele de identificare ale
    echipelor utilizatorului. In functie de pozitia pe care s-a gasit echipa, se intoarce rezultatul corespunzator.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Un tuplu cu trei elemente de tip str. Doua vor fi siruri goale iar al treilea va contine cuvantul 'checked'.
    Pozitia din tuplu care contine acest cuvant arata a cata echipa va fi utilizata mai departe."""

    if global_library.team_id == global_library.user_data['team 1 id']:
        checked = ('checked', '', '')
    elif global_library.team_id == global_library.user_data['team 2 id']:
        checked = ('', 'checked', '')
    else:
        checked = ('', '', 'checked')
    return checked


# Intoarce numarul de identificare al unui meci selectat
@index_bp.route('/GetMatch', methods=['POST'])
def get_match_ratings_for_a_future_match() -> None:
    """Procedura obtine evaluarile echipei utilizatorului pentru un meci ce se va disputa in viitor, stabilit de
    catre utilizator.

    Algoritm:
    ----------
    Se obtine numele de identificare al echipei pentru care se doreste obtinerea evaluarilor. In functie de aceasta,
    se stabileste numele echipei si se descarca fisierul XML cu meciurile viitoare ale acesteia. Daca exista meciuri
    viitoare, se stabileste daca utilizatorul a dorit meciurile unei alte echipe de pe cont sau a echipei sale.
    Aceasta verificare este necesara pentru ca, daca utilizatorul a dorit sa vada meciurile viitoare ale unei alte
    echipe din contul sau, se se selecteze automat primul meci din lista. Daca utilizatorul a dorit sa vada alt meci
    al aceleiasi echipe, se citeste pozitia pe care se afla acel meci. Se descarca fisierul cu ordinele de meci pentru
    meciul selectat, se stabileste daca echipa joaca acasa sau in deplasare si se afiseaza pagina utilizatorului
    conectat la joc, cu evaluarile incarcate in pozitiile corecte.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    if not check_if_connection_is_valid(test_config=config):
        dw.show_error_window_in_thread(title='Connection lost',
                                       message='We cannot access anymore your Hattrick account. This is probably because you revoked the application''s access from the Hattrick account, or there is a problem with the Hattrick server!')
        return render_template('index.html', title="The Best Match Predictor",
                               ratings=global_library.ratings, positions=global_library.positions,
                               statuses=global_library.statuses, from_index=True,
                               match_orders=global_library.default_match_orders,
                               answer=global_library.ans)
    global_library.team_id = request.form['HattrickTeams']
    global_library.user_team_name = get_user_team_name()
    global_library.user_matches = download_user_matches_file.download_user_matches_file(global_library.team_id)
    checked = get_chosen_option()
    selected_position: int = 0
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
                for match in global_library.user_matches:
                    if match_id != match[0]:
                        selected_position += 1
                    else:
                        break
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
                           answer=global_library.ans, checked=checked, position=selected_position)


@index_bp.route('/backup')
def backup_database() -> None:
    """Procedura face backup la baza de date. Mai precis, o arhiveaza.
    Numele arhivei are forma: 'backup yyyy-mm-dd hh-mm-ss.zip'.

    Algoritm:
    ----------
    Se creaza arhiva, la care se adauga baza de date. Se afiseaza un mesaj de incheiere a operatiunii si se afiseaza
    pagina panoului de control.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    with z.ZipFile(file=global_library.database_backup_path + '\\backup ' + datetime.datetime.now().strftime(
            '%Y-%m-%d %H-%M-%S') + '.zip', mode='w') as backup:
        backup.write(global_library.database_file_path,
                     arcname='matches.db')
    dw.show_info_window_in_thread(title='Backup terminat', message='Am terminat backupul bazei de date.')
    return render_template('admin.html')


@index_bp.route('/restore')
def restore_database() -> None:
    """Procedura reface un backup al bazei de date, ales de catre utilizator. Prin 'refacere' se intelege inlocuirea
    bazei de date existente cu una obtinuta din dezarhivarea arhivei selectate de catre utilizator.

    Algoritm:
    ----------
    Se dezarhiveaza arhiva specificata de catre utilizator in folderul 'db', inlocuind arhiva existenta acolo. La
    final, se afiseaza un mesaj de confirmare a incheierii operatiunii.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    with z.ZipFile(file=dw.restore_backup_window_in_thread(), mode='r') as restore:
        restore.extractall(os.path.dirname(global_library.database_file_path))
    dw.show_info_window_in_thread(title='Restaurare incheiata', message='S-a incheiat restaurarea backupului ales')
    return render_template('admin.html')
