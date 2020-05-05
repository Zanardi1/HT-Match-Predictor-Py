# Subrutinele necesare descarcarii unui fisier XML din Hattrick

import configparser as c

from rauth import OAuth1Session

import global_library


def download_xml_file(file, params, destination_file):
    config = c.ConfigParser()
    config.read(global_library.configuration_file)
    session = OAuth1Session(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                            consumer_secret=config['DEFAULT']['CONSUMER_SECRET'],
                            access_token=config['DEFAULT']['ACCESS_TOKEN'],
                            access_token_secret=config['DEFAULT']['ACCESS_TOKEN_SECRET'])
    query = session.get(file, params=params)
    session.close()

    f = open(destination_file, 'w', encoding='utf-8')
    f.write(query.text)
    f.close()
