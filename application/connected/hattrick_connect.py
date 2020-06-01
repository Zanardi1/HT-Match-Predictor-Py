# Subrutinele necesare conectarii la Hattrick

import webbrowser

from rauth import OAuth1Service
from rauth.oauth import HmacSha1Signature

import application.dialog_windows as dw
import application.xml.dl_xml_file as dx
import application.xml.xml_parsing as xl
import global_library
from application import config
from application.connected import download_user_info_file as d
from application.connected import hattrick_disconnect as hd


def check_if_configuration_file_has_access_tokens(test_config: config) -> bool:
    """Functia verifica daca fisierul de configurari are stocate jetoanele access token si access token secret.

    Algoritm:
    ----------
    Cauta in fisierul de configurari cele doua jetoane.

    Parametri:
    ----------
    test_config: config
        instanta a clasei config, definita in ConfigParser. Aceasta retine, printre altele si URL-ul catre fisierul
        ce urmeaza a fi descarcat.

    Intoarce:
    ----------
    True, daca fisierul de configurare are cele doua jetoane. Altfel intoarce False."""

    return True if test_config.has_option('DEFAULT', 'ACCESS_TOKEN') and test_config.has_option('DEFAULT',
                                                                                                'ACCESS_TOKEN_SECRET') \
        else False


def check_if_connection_is_valid(test_config: config) -> bool:
    """Functia verifica daca este valida conexiunea la contul Hattrick. Mai precis, daca programul are acces la
    acest cont. Verificarea se face prin descarcarea unui fisier XML, care spune acest lucru si citirea lui.

    Algoritm:
    ----------
    Descarca fisierul Check.xml care contine jetonul de acces, in cazul in care conexiunea e valida si cauta acest
    jeton in fisierul descarcat.

    Parametri:
    ----------
    test_config: config
        instanta a clasei config, definita in ConfigParser. Aceasta retine, printre altele si URL-ul catre fisierul
        ce urmeaza a fi descarcat.

    Intoarce:
    ----------
    True, daca este valida conexiunea, adica programul are acces la datele contului de Hattrick.
    Altfel intoarce False."""

    dx.download_xml_file(file=test_config['DEFAULT']['CHECK_TOKEN_PATH'], params={},
                         destination_file=global_library.check_connection_savepath)
    return xl.parse_connection_verification_file()


def add_access_tokens_to_config_file(test_config: config, connection: OAuth1Service, request_token: str,
                                     request_token_secret: str, code: str) -> bool:
    """Functia adauga jetoanele access token si access token secret fisierului de configurari. Acestea vor fi
    folosite pentru conectarea site-ului la contul Hattrick, fara a mai fi necesara parcurgerea din nou a intregului
    proces de autentificare.
    
    Algoritm:
    ----------
    Incearca sa obtina cele doua jetoane. Daca nu reuseste, atunci cel mai probabil este deoarece PIN-ul este fie
    introdus gresit, fie utilizatorul a renuntat in a-l introduce (care e cam acelasi lucru). Daca reuseste, atunci
    le salveaza in fisierul de configurari.

    Parametri:
    ----------
    test_config: config
        instanta a clasei config, definita in ConfigParser. Aceasta retine, printre altele si URL-ul catre fisierul
        ce urmeaza a fi descarcat;
    connection: OAuth1Service
        instanta a clasei Oauth1Service, clasa ce retine detaliile necesare conectarii la Hattrick prin protocolul
        oauth;
    request_token: str
        variabila ce retine un sir de caractere, denumit request token, folosit la conectarea la Hattrick si la
        obtinerea jetoanelor de acces;
    request_token_secret: str
        variabila ce retine un sir de caractere, denumit request token secret, folosit la conectarea la Hattrick si
        la obtinerea jetoanelor de acces;
    code: str
        variabila ce retine un sir de caractere, denumit request token secret, folosit la conectarea la Hattrick si
        la obtinerea jetoanelor de acces. Acest sir se numeste cod si trebuie introdus de catre utilizator la
        autentificarea aplicatiei la contul Hattrick.

    Intoarce:
    ---------
    True, daca procesul a avut loc cu succes. Acest lucru implica introducerea corecta a codului primit de catre
    utilizator, fapt care are loc in functia get_access_token. Altfel, daca utilizatorul a introdus codul gresit
    sau a renuntat in a-l introduce, intoarce False."""

    try:
        access_token, access_token_secret = connection.get_access_token(request_token, request_token_secret,
                                                                        params={'oauth_verifier': code})
    except KeyError:
        dw.show_error_window_in_thread(title='Wrong PIN!', message='Wrong PIN inserted.')
        return False
    else:
        test_config['DEFAULT']['ACCESS_TOKEN'] = access_token
        test_config['DEFAULT']['ACCESS_TOKEN_SECRET'] = access_token_secret
        with open(file=global_library.configuration_file, mode='w') as configfile:
            test_config.write(configfile)
        return True


def get_access_tokens(test_config: config) -> bool:
    """Functia obtine jetoanele de access la contul Hattrick

    Algoritm:
    ----------
    Functia creaza o instanta a clasei OAuth1Service, responsabila cu conectarea la joc. Dupa ce a fost realizata
    conectarea, se obtin jetoanele request token si request token secret. Dupa executia acestui pas, se deschide un
    tab al browserului implicit, care prezinta pagina din care utilizatorul ia un sir de caractere, numid cod sau PIN
    si-l scrie in fereastra care apare. In cazul in care PIN-ul introdus coincide cu cel din tab, functia primeste
    jetoanele access token si access token secret si le scrie in fisier. Daca nu, atunci utilizatorul a apasat
    butonul Cancel (cazul in care a introdus un cod gresit e tratat in add_access_tokens_to_config_file.

    Parametri:
    ----------
    test_config: config
        instanta a clasei config, definita in ConfigParser. Aceasta retine, printre altele si URL-ul catre fisierul
        ce urmeaza a fi descarcat.

    Intoarce:
    ----------
    True, daca adaugarea jetoanelor de access s-a incheiat cu succes. Acest proces implica introducerea corecta de catre utilizator a unui cod primit de la Hattrick.
    Daca acest cod a fost introdus gresit sau daca utilizatorul a renuntat in a-l introduce, functia intoarce False.
    """

    connection = OAuth1Service(consumer_key=test_config['DEFAULT']['CONSUMER_KEY'],
                               consumer_secret=test_config['DEFAULT']['CONSUMER_SECRET'], name='Hattrick',
                               request_token_url=test_config['DEFAULT']['REQUEST_TOKEN_PATH'],
                               access_token_url=test_config['DEFAULT']['ACCESS_TOKEN_PATH'],
                               authorize_url=test_config['DEFAULT']['AUTHORIZE_PATH'],
                               base_url=test_config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                               signature_obj=HmacSha1Signature)
    request_token, request_token_secret = connection.get_request_token(
        params={'oauth_callback': test_config['DEFAULT']['CALLBACK_URL']})
    webbrowser.open(url=connection.get_authorize_url(request_token), new=2)
    code = dw.show_string_input_window_in_thread(title='PIN Required',
                                                 message='Please insert the PIN specified by Hattrick')
    if code is None: # Utilizatorul a apasat butonul Cancel
        return False
    else:
        return True if add_access_tokens_to_config_file(test_config=test_config, connection=connection,
                                                        request_token=request_token,
                                                        request_token_secret=request_token_secret,
                                                        code=code) else False


def connection_engine() -> tuple:
    """Functia realizeaza conectarea propriu-zisa la Hattrick. Functia obtine informatiile de baza despre
    utilizatorul care s-a conectat. Deoarece procesul este aproape in totalitate automat, singurul punct in care
    omul poate interveni este la introducerea PIN-ului. Fie il poate introduce gresit, fie se poate razgandi si
    nu-l mai introduce. Din aceste motive, functia intoarce True daca procesul de conectare s-a incheiat
    (adica s-au obtinut jetoanele de acces) si False in caz contrar (cel mai probabil atunci cand PIN-ul fie nu
    este introdus corect, fie utilizatorul renunta la procedura in acest punct.

    Algoritm:
    ---------
    1. Testeaza daca se poate conecta la Hattrick. Asta inseamna ca urmatoarele 2 conditii sa fie adevarate:
        1.1. Sa existe jetoanele de acces;
        1.2. Conexiunea sa fie permisa de catre Hattrick.
    2. Daca se poate conecta la Hattrick:
        2.1. Descarca informatiile de baza;
        2.2. Intoarce True.
    3. Daca nu se poate conecta la Hattrick:
        3.1. Obtine jetoanele de access (efectueaza intreaga procedura de conectare). Daca nu poate, intoarce False;
        3.2. Descarca informatiile de baza;
        3.3. Intoarce True.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Un tuplu format dintr-o valoare booleana si un dictionar ce retine datele de utilizator. Daca valoarea booleana
    este True, atunci dictionarul retine datele cerute. Altfel, dictionarul este gol."""

    if check_if_configuration_file_has_access_tokens(test_config=config):
        if check_if_connection_is_valid(test_config=config):
            user_data = d.download_user_info_file()
            return True, user_data
        else:
            hd.disconnection_engine(show_confirmation_window=False)
            if get_access_tokens(test_config=config):
                dw.show_info_window_in_thread(title='Connection complete!',
                                              message='Successfully connected to Hattrick account')
                user_data = d.download_user_info_file()
                return True, user_data
    else:
        if get_access_tokens(test_config=config):
            dw.show_info_window_in_thread(title='Connection complete!',
                                          message='Successfully connected to Hattrick account')
            user_data = d.download_user_info_file()
            return True, user_data
        else:
            return False, {}
