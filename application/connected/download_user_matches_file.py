# Subrutinele necesare descarcarii meciurilor unei echipe pentru utilizatorul conectat

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library
from application import config


def download_user_matches_file(team_id: int) -> list:
    """Algoritmul descarca din Hattrick un fisier XML ce contine meciurile pe care le-a avut si le va avea o echipa
    a utilizatorului.

    Parametri:
    ----------
    team_id: int
        retine numarul de identificare al echipei pentru care se obtin meciurile

    Intoarce:
    ----------
        o lista de tupluri. Fiecare tuplu retine numarul de identificare al meciului viitor, echipa gazda si echipa
        oaspete a meciului cu numarul de identificare respectiv"""
    dl.download_xml_file(file=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                         params=cs.create_matches_string(team_id=team_id),
                         destination_file=global_library.matches_savepath)
    return xp.parse_matches_file()
