# Subrutina necesara descarcarii unui singur meci, transmis prin numarul lui de identificare
import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library
from application import config


def download_future_match(match_id: int, team_id: int) -> list:
    dl.download_xml_file(file=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                         params=cs.create_match_orders_string(match_id=match_id, team_id=team_id),
                         destination_file=global_library.orders_savepath)
    return xp.parse_future_match_file()
