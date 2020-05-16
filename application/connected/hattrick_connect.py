# Subrutinele necesare conectarii la Hattrick

import tkinter as tk
import tkinter.simpledialog as sd
import webbrowser
from multiprocessing import Process, Queue
from tkinter.messagebox import showinfo, showerror

from rauth import OAuth1Service
from rauth.oauth import HmacSha1Signature

import application.xml.dl_xml_file as dx
import application.xml.xml_parsing as xl
import global_library
from application import config
from application.connected import download_user_info as d


def check_if_configuration_file_has_access_tokens(test_config):
    if test_config.has_option('DEFAULT', 'ACCESS_TOKEN') and test_config.has_option('DEFAULT', 'ACCESS_TOKEN_SECRET'):
        return True
    else:
        return False


def check_if_connection_is_valid(test_config):
    dx.download_xml_file(test_config['DEFAULT']['CHECK_TOKEN_PATH'], {}, global_library.check_connection_savepath)
    return xl.parse_connection_verification_file()


def add_access_tokens_to_config_file(test_config, connection, request_token, request_token_secret, code):
    try:
        access_token, access_token_secret = connection.get_access_token(request_token, request_token_secret,
                                                                        params={'oauth_verifier': code})
    except KeyError:
        p = Process(target=show_wrong_pin_error_window)
        p.start()
        p.join()
        return False
    else:
        test_config['DEFAULT']['ACCESS_TOKEN'] = access_token
        test_config['DEFAULT']['ACCESS_TOKEN_SECRET'] = access_token_secret
        with open(global_library.configuration_file, 'w') as configfile:
            test_config.write(configfile)
        return True


def show_pin_window(q):
    root = tk.Tk()
    root.withdraw()
    code = sd.askstring(title='PIN Required', prompt='Please insert the PIN specified by Hattrick')
    root.destroy()
    q.put(code)


def show_wrong_pin_error_window():
    root = tk.Tk()
    root.withdraw()
    showerror('Wrong PIN', 'Wrong PIN inserted!')
    root.destroy()


def get_access_tokens(test_config):
    connection = OAuth1Service(consumer_key=test_config['DEFAULT']['CONSUMER_KEY'],
                               consumer_secret=test_config['DEFAULT']['CONSUMER_SECRET'], name='Hattrick',
                               request_token_url=test_config['DEFAULT']['REQUEST_TOKEN_PATH'],
                               access_token_url=test_config['DEFAULT']['ACCESS_TOKEN_PATH'],
                               authorize_url=test_config['DEFAULT']['AUTHORIZE_PATH'],
                               base_url=test_config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                               signature_obj=HmacSha1Signature)
    request_token, request_token_secret = connection.get_request_token(
        params={'oauth_callback': test_config['DEFAULT']['CALLBACK_URL']})
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
        if add_access_tokens_to_config_file(test_config, connection, request_token, request_token_secret, code):
            return True
        else:
            return False


def show_connection_successful_window():
    root = tk.Tk()
    root.withdraw()
    showinfo("Connection complete!", "Successfully conected to Hattrick account!")
    root.destroy()


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

    if check_if_configuration_file_has_access_tokens(config):
        if check_if_connection_is_valid(config):
            user_data = d.download_user_info()
            return True, user_data
        else:
            dx.download_xml_file(config['DEFAULT']['INVALIDATE_TOKEN_PATH'], {}, global_library.disconnect_savepath)
            config.remove_option('DEFAULT', 'ACCESS_TOKEN')
            config.remove_option('DEFAULT', 'ACCESS_TOKEN_SECRET')
            with open(global_library.configuration_file, 'w') as configfile:
                config.write(configfile)
            if get_access_tokens(config):
                p = Process(target=show_connection_successful_window)
                p.start()
                p.join()
                user_data = d.download_user_info()
                return True, user_data
    else:
        if get_access_tokens(config):
            p = Process(target=show_connection_successful_window)
            p.start()
            p.join()
            user_data = d.download_user_info()
            return True, user_data
        else:
            return False, []
