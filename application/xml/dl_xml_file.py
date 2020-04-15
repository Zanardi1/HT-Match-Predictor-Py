# Subrutinele necesare descarcarii unui fisier XML din Hattrick

import configparser as c
import os
import easygui
from rauth import OAuth1Session
import xml.etree.ElementTree as ET


def download_xml_file(path, destination_file):
    config = c.ConfigParser()
    config.read(os.path.abspath('application\connected\session_config.ini'))
    session = OAuth1Session(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                            consumer_secret=config['DEFAULT']['CONSUMER_SECRET'],
                            access_token=config['DEFAULT']['ACCESS_TOKEN'],
                            access_token_secret=config['DEFAULT']['ACCESS_TOKEN_SECRET'])
    query = session.get(path)
    query.encoding = 'UTF-8'

    f = open(destination_file, 'w')
    f.write(query.text)
    f.close()
