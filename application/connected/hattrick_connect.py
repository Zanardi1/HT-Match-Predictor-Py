import tkinter as tk
import tkinter.simpledialog as sd
import webbrowser

from rauth import OAuth1Service
from rauth.oauth import HmacSha1Signature

from . import session_config as sc


def connection_engine():
    connection = OAuth1Service(consumer_key=sc.CONSUMER_KEY, consumer_secret=sc.CONSUMER_SECRET, name='Hattrick',
                               request_token_url=sc.REQUEST_TOKEN_PATH, access_token_url=sc.ACCESS_TOKEN_PATH,
                               authorize_url=sc.AUTHORIZE_PATH, base_url=sc.PROTECTED_RESOURCE_PATH,
                               signature_obj=HmacSha1Signature)
    request_token, request_token_secret = connection.get_request_token(params={'oauth_callback': sc.CALLBACK_URL})
    authorization_url = connection.get_authorize_url(request_token)
    webbrowser.open(authorization_url, new=2)
    root = tk.Tk()
    root.withdraw()
    code = sd.askstring(title='PIN Required', prompt='Please insert the PIN specified by Hattrick')
    access_token, access_token_secret = connection.get_access_token(request_token, request_token_secret,
                                                                    params={'oauth_verifier': code})
    return 0
