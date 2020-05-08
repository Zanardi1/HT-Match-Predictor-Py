# Subrutina necesara descarcarii unui singur meci, transmis prin numarul lui de identificare
import configparser as c

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp
import global_library


def download_future_match(match_id, team_id):
    config = c.ConfigParser()
    config.read(global_library.configuration_file)
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    params = cs.create_match_orders_string(match_id, team_id)
    dl.download_xml_file(file, params, global_library.orders_savepath)
    user_orders = xp.parse_future_match_file()
    return user_orders