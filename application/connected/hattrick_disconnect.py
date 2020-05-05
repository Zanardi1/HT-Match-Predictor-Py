import configparser as c

import global_library
from application.xml import dl_xml_file as d


def disconnection_engine():
    config = c.ConfigParser()
    config.read(global_library.configuration_file)
    d.download_xml_file(config['DEFAULT']['INVALIDATE_TOKEN_PATH'], {}, global_library.disconnect_savepath)
    config.remove_option('DEFAULT', 'ACCESS_TOKEN')
    config.remove_option('DEFAULT', 'ACCESS_TOKEN_SECRET')
    with open(global_library.configuration_file, 'w') as configfile:
        config.write(configfile)
