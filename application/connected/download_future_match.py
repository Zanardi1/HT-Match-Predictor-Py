# Subrutina necesara descarcarii unui singur meci, transmis prin numarul lui de identificare
import configparser as c
import os

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl
import application.xml.xml_parsing as xp

savepath = os.path.abspath('application\\xml\\Orders.xml')


def download_future_match(match_id, team_id):
    config = c.ConfigParser()
    config.read(os.path.abspath('application\connected\session_config.ini'))
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    params = cs.create_match_orders_string(match_id, team_id)
    dl.download_xml_file(file, params, savepath)
    user_orders = xp.parse_future_match_file()
    return user_orders
