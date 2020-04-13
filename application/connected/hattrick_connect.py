import webbrowser

import easygui
from authlib.integrations.requests_client import OAuth1Session
import application.connected.session_config as c


# verifier = PIN-ul de la Hattrick


def ConnectionEngine():
    if c.OAUTH_TOKEN is None and c.OAUTH_TOKEN_SECRET is None:
        oauth = OAuth1Session(client_id=c.CONSUMER_KEY,
                              client_secret=c.CONSUMER_SECRET,
                              redirect_uri=c.REQUEST_TOKEN_PATH, token=c.OAUTH_TOKEN, token_secret=c.OAUTH_TOKEN_SECRET)
        request_token = oauth.fetch_request_token(c.REQUEST_TOKEN_PATH)
        path = oauth.create_authorization_url(c.AUTHORIZE_PATH,
                                              request_token=request_token['oauth_token'])
        webbrowser.open(path, new=2)
        # TODO: sa iau PIN-ul automat si sa il pun in aplicatie
        verifier = easygui.enterbox(msg='Enter the PIN provided by the Hattrick site', title='Enter PIN', strip=True)
        access_token = oauth.fetch_access_token(c.ACCESS_TOKEN_PATH, verifier=verifier)
    else:
        easygui.msgbox('Conectat')
