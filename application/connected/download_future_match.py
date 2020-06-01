# Subrutina necesara descarcarii unui singur meci, transmis prin numarul lui de identificare
import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library
from application import config


def download_future_match(match_id: int, team_id: int) -> list:
    """Functia descarca din Hattrick un fisier XML ce contine evaluarile echipei care are un numar de identificare
    transmis ca parametru intr-un meci viitor, cu numarul de identificare transmis si el ca parametru.

    Algoritm:
    ----------
    Se descarca fisierul XML corespunzator, care este citit de catre functia parse_future_match_file. Aceasta functie
    intoarce rezultatul potrivit.

    Parametri:
    ----------
    match_id: int
        numarul de identificare al meciului al caror evaluari vor fi trecute in fisierul XML;
    team_id: int
        numarul de identificare al echipei pentru care se vrea descarcarea fisierului.

    Intoarce:
    ---------
    O lista ce contine cele 7 evaluari ale echipei dorite (evaluarile pentru mijloc, aparare pe dreapta, centru si
    stanga si atac pe dreapta, centru si stanga."""

    dl.download_xml_file(file=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                         params=cs.create_match_orders_string(match_id=match_id, team_id=team_id),
                         destination_file=global_library.orders_savepath)
    return xp.parse_future_match_file()
