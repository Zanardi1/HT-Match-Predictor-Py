import tkinter as tk
import tkinter.simpledialog as sd
import webbrowser
import configparser as c
import easygui
import os

from rauth import OAuth1Service
from rauth.oauth import HmacSha1Signature


def connection_engine():
    # TODO deoarece, in realitate, mai multi utilizatori se vor conecta la aplicatie cu contul de Hattrick,
    #  consumer key, consumer secret, access token si access token secret trebuie puse intr-o baza de date
    #  si luate de acolo, la nevoie. Sau intr-un cookie. Sau altundeva.
    configuration_file = os.path.abspath('application\connected\session_config.ini')
    config = c.ConfigParser()
    config.read(configuration_file)
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
    root = tk.Tk()
    root.withdraw()
    code = sd.askstring(title='PIN Required', prompt='Please insert the PIN specified by Hattrick')
    root.destroy()
    #  TODO: sa tratez cazul in care PIN-ul introdus este gresit
    if code is None:
        return False
    else:
        access_token, access_token_secret = connection.get_access_token(request_token, request_token_secret,
                                                                        params={'oauth_verifier': code})
        config['DEFAULT']['ACCESS_TOKEN'] = access_token
        config['DEFAULT']['ACCESS_TOKEN_SECRET'] = access_token_secret
        with open(configuration_file, 'w') as configfile:
            config.write(configfile)
        return True
