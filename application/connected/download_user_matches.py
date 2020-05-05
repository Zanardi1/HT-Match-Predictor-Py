# Subrutinele necesare descarcarii meciurilor unei echipe pentru utilizatorul conectat

import configparser as c
import os

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library


def download_user_matches(team_id):
    config = c.ConfigParser()
    config.read(os.path.abspath('application\connected\session_config.ini'))
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    params = cs.create_matches_string(team_id)
    dl.download_xml_file(file, params, global_library.matches_savepath)
    user_matches = xp.parse_matches_file()
    return user_matches
