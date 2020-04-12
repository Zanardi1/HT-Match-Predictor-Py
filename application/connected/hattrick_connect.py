import webbrowser

import easygui
from authlib.integrations.requests_client import OAuth1Session

CONSUMER_KEY = 'Cx7jQlJTOwIRA2XVtRWF19'
CONSUMER_SECRET = 'L1gwHsZZuGneTUwZKUevgBUe3HKIMBDiJv7DHwf1RjI'
REQUEST_TOKEN_PATH = 'https://chpp.hattrick.org/oauth/request_token.ashx'
AUTHORIZE_PATH = 'https://chpp.hattrick.org/oauth/authorize.aspx'
AUTHENTICATE_PATH = 'https://chpp.hattrick.org/oauth/authenticate.aspx'
ACCESS_TOKEN_PATH = 'https://chpp.hattrick.org/oauth/access_token.ashx'


# verifier = PIN-ul de la Hattrick


def ConnectionEngine():
    oauth = OAuth1Session(client_id=CONSUMER_KEY, client_secret=CONSUMER_SECRET,
                          callback_uri=REQUEST_TOKEN_PATH, redirect_uri=REQUEST_TOKEN_PATH)
    request_token = oauth.fetch_request_token(REQUEST_TOKEN_PATH)
    path = oauth.create_authorization_url(AUTHORIZE_PATH, request_token=request_token['oauth_token'])
    webbrowser.open(path, new=2)
    # verifier = easygui.enterbox(msg='Enter the PIN provided by the Hattrick site', title='Enter PIN', strip=True)
    path2 = oauth.parse_authorization_response(path)
    easygui.msgbox(path2)
    access_token = oauth.fetch_access_token(ACCESS_TOKEN_PATH, verifier=path2['oauth_verifier'])
