from authlib.integrations.flask_client import OAuth

import wsgi


def ConnectionEngine():
    oauth = OAuth(wsgi.app)
    oauth.register(name='Hattrick', client_id='Cx7jQlJTOwIRA2XVtRWF19',
                   client_secret='L1gwHsZZuGneTUwZKUevgBUe3HKIMBDiJv7DHwf1RjI',
                   request_token_url='https://chpp.hattrick.org/oauth/request_token.ashx', request_token_params=None,
                   access_token_url='https://chpp.hattrick.org/oauth/access_token.ashx', access_token_params=None,
                   authorize_url='https://chpp.hattrick.org/oauth/authorize.aspx', authorize_params=None,
                   api_base_url='https://chpp.hattrick.org/chppxml.ashx', client_kwargs=None)
    hattrick = oauth.create_client('Hattrick')
    return hattrick.authorize_redirect('https://chpp.hattrick.org/oauth/authorize.aspx')
