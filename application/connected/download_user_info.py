# Subrutinele necesare descarcarii informatiilor de baza despre utilizatorul conectat

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library
from application import config


def download_user_info() -> dict:
    dl.download_xml_file(file=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                         params=cs.create_manager_compendium_string(), destination_file=global_library.user_savepath)
    return xp.parse_user_file()
