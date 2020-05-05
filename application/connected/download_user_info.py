# Subrutinele necesare descarcarii informatiilor de baza despre utilizatorul conectat

import configparser as c
import os

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library


def download_user_info():
    config = c.ConfigParser()
    config.read(os.path.abspath('application\connected\session_config.ini'))
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    params = cs.create_manager_compendium_string()
    dl.download_xml_file(file, params, global_library.user_savepath)
    user_data = xp.parse_user_file()
    return user_data
