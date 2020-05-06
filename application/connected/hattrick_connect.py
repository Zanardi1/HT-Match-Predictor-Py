# Subrutinele necesare conectarii la Hattrick

import configparser as c
import tkinter as tk
import tkinter.simpledialog as sd
import webbrowser

from rauth import OAuth1Service
from rauth.oauth import HmacSha1Signature

import application.xml.dl_xml_file as dx
import global_library
from application.connected import download_user_info as d
from multiprocessing import Process, Queue


def read_configuration_file():
    config = c.ConfigParser()
    config.read(global_library.configuration_file)
    return config


def check_if_configuration_file_has_access_tokens(config):
    if config.has_option('DEFAULT', 'ACCESS_TOKEN') and config.has_option('DEFAULT', 'ACCESS_TOKEN_SECRET'):
        return True
    else:
        return False


def check_if_connection_is_valid(config):
    dx.download_xml_file(config['DEFAULT']['CHECK_TOKEN_PATH'], {}, global_library.check_connection_savepath)
    return True


def add_access_tokens_to_config_file(config, connection, request_token, request_token_secret, code):
    access_token, access_token_secret = connection.get_access_token(request_token, request_token_secret,
                                                                    params={'oauth_verifier': code})
    config['DEFAULT']['ACCESS_TOKEN'] = access_token
    config['DEFAULT']['ACCESS_TOKEN_SECRET'] = access_token_secret
    with open(global_library.configuration_file, 'w') as configfile:
        config.write(configfile)


def show_pin_window(q):
    root = tk.Tk()
    root.withdraw()
    code = sd.askstring(title='PIN Required', prompt='Please insert the PIN specified by Hattrick')
    root.destroy()
    q.put(code)


def get_access_tokens(config):
    connection = OAuth1Service(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                               consumer_secret=config['DEFAULT']['CONSUMER_SECRET'], name='Hattrick',
                               request_token_url=config['DEFAULT']['REQUEST_TOKEN_PATH'],
                               access_token_url=config['DEFAULT']['ACCESS_TOKEN_PATH'],
                               authorize_url=config['DEFAULT']['AUTHORIZE_PATH'],
                               base_url=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                               signature_obj=HmacSha1Signature)
    request_token, request_token_secret = connection.get_request_token(
        params={'oauth_callback': config['DEFAULT']['CALLBACK_URL']})
    authorization_url = connection.get_authorize_url(request_token)
    webbrowser.open(authorization_url, new=2)
    queue = Queue()
    p = Process(target=show_pin_window, args=(queue,))
    p.start()
    p.join()
    code = queue.get()
    if code is None:
        return False
    else:
        add_access_tokens_to_config_file(config, connection, request_token, request_token_secret, code)
        return True


def connection_engine():
    """Functia obtine informatiile de baza despre utilizatorul care s-a conectat.
    Deoarece procesul este aproape in totalitate automat, singurul punct in care omul poate interveni este la
    introducerea PIN-ului. Fie il poate introduce gresit, fie se poate razgandi si nu-l mai introduce.
    Din aceste motive, functia intoarce True daca procesul de conectare s-a incheiat (adica s-au obtinut jetoanele
    de acces) si False in caz contrar (cel mai probabil atunci cand PIN-ul fie nu este introdus corect, fie
    utilizatorul renunta la procedura in acest punct.
    Algoritmul de functionare:
    1. Testeaza daca se poate conecta la Hattrick. Asta inseamna ca urmatoarele 2 conditii sa fie adevarate:
      1.1. Sa existe jetoanele de acces;
      1.2. Conexiunea sa fie permisa de catre Hattrick
    2. Daca se poate conecta la Hattrick:
      2.1. Descarca informatiile de baza;
      2.2. Intoarce True
    3. Daca nu se poate conecta la Hattrick:
      3.1. Obtine jetoanele de access (efectueaza intreaga procedura de conectare). Daca nu poate, intoarce False
      3.2. Descarca informatiile de baza
      3.3. Intoarce True."""

    config = read_configuration_file()
    if check_if_configuration_file_has_access_tokens(config) and check_if_connection_is_valid(config):
        user_data = d.download_user_info()
        return True, user_data
    else:
        if get_access_tokens(config):
            user_data = d.download_user_info()
            return True, user_data
        else:
            return False, {}
