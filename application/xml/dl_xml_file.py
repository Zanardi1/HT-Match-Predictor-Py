# Subrutinele necesare descarcarii unui fisier XML din Hattrick

from rauth import OAuth1Session

from application import config


def download_xml_file(file, params, destination_file):
    import easygui
    if config.has_option('DEFAULT', 'ACCESS_TOKEN'):
        access_token = config['DEFAULT']['ACCESS_TOKEN']
    else:
        access_token = None
    if config.has_option('DEFAULT', 'ACCESS_TOKEN_SECRET'):
        access_token_secret = config['DEFAULT']['ACCESS_TOKEN_SECRET']
    else:
        access_token_secret = None
    easygui.msgbox(access_token)
    easygui.msgbox(access_token_secret)
    session = OAuth1Session(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                            consumer_secret=config['DEFAULT']['CONSUMER_SECRET'],
                            access_token=access_token,
                            access_token_secret=access_token_secret)
    easygui.msgbox(file)
    easygui.msgbox(destination_file)
    query = session.get(file, params=params)
    session.close()

    f = open(destination_file, 'w', encoding='utf-8')
    f.write(query.text)
    f.close()
