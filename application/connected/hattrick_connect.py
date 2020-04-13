from . import session_config as sc
import oauthlib.oauth1
import easygui
import webbrowser


# verifier = PIN-ul de la Hattrick

# {'Authorization': 'OAuth oauth_nonce="44261210707564116121586782517",
# oauth_timestamp="1586782517",
# oauth_version="1.0",
# oauth_signature_method="HMAC-SHA1",
# oauth_consumer_key="Cx7jQlJTOwIRA2XVtRWF19",
# oauth_signature="Umw4RAMIzSan%2Bg5lBbj6tRDkwhs%3D"'}


def ConnectionEngine():
    client = oauthlib.oauth1.Client(sc.CONSUMER_KEY, client_secret=sc.CONSUMER_SECRET)
    uri, headers, body = client.sign(sc.REQUEST_TOKEN_PATH)
    easygui.msgbox(headers)
    # webbrowser.open(sc.ACCESS_TOKEN_PATH + 'oauth=' + headers['oauth_signature'])
