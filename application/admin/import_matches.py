import configparser as c
import os

import easygui

from application.xml import create_string as cs
from application.xml import dl_xml_file as dl

savepath = os.path.abspath('application\\xml\\Orders.xml')


def import_engine(low_end, high_end):
    config = c.ConfigParser()
    config.read(os.path.abspath('application\connected\session_config.ini'))
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    for match_id in range(low_end, high_end + 1, 1):
        params = cs.create_match_orders_string(match_id, None)
        dl.download_xml_file(file, params, savepath)
    return easygui.msgbox('Import meciuri')
