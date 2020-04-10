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
    oauth = OAuth1Session(client_id=CONSUMER_KEY, client_secret=CONSUMER_SECRET, redirect_uri=REQUEST_TOKEN_PATH)
    request_token = oauth.fetch_request_token(REQUEST_TOKEN_PATH)
    resource_owner_key = request_token['oauth_token']
    resource_owner_secret = request_token['oauth_token_secret']
    # easygui.msgbox(request_token)
    authorize = oauth.create_authorization_url(AUTHORIZE_PATH)
    easygui.msgbox(authorize)
    params = oauth.parse_authorization_response(authorize)
    # easygui.msgbox(params)
    oauth = OAuth1Session(client_id=CONSUMER_KEY, client_secret=CONSUMER_SECRET, redirect_uri=REQUEST_TOKEN_PATH,
                          token=resource_owner_key, token_secret=resource_owner_secret)
    token = oauth.fetch_access_token(ACCESS_TOKEN_PATH, verifier=params['oauth_token'])
    easygui.msgbox(token)
