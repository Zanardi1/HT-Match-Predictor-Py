# Subrutinele necesare descarcarii unui fisier XML din Hattrick

import configparser as c
import os
import easygui

from rauth import OAuth1Session


def download_xml_file(params, destination_file):
    config = c.ConfigParser()
    config.read(os.path.abspath('application\connected\session_config.ini'))
    session = OAuth1Session(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                            consumer_secret=config['DEFAULT']['CONSUMER_SECRET'],
                            access_token=config['DEFAULT']['ACCESS_TOKEN'],
                            access_token_secret=config['DEFAULT']['ACCESS_TOKEN_SECRET'])
    query = session.get(config['DEFAULT']['PROTECTED_RESOURCE_PATH'], params=params)
    session.close()

    #TODO de introdus o rutina care verifica daca fisierul exista deja sau nu
    f = open(destination_file, 'w', encoding='utf-8')
    f.write(query.text)
    f.close()
