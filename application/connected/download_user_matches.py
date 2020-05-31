# Subrutinele necesare descarcarii meciurilor unei echipe pentru utilizatorul conectat

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library
from application import config


def download_user_matches(team_id: int) -> list:
    dl.download_xml_file(file=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                         params=cs.create_matches_string(team_id=team_id),
                         destination_file=global_library.matches_savepath)
    return xp.parse_matches_file()
