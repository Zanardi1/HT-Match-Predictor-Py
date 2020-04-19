import configparser as c
import os

from application.xml import dl_xml_file as d

savepath = os.path.abspath('application\\xml\\Disconnect.xml')
configuration_file = os.path.abspath('application\connected\session_config.ini')


def DisconnectionEngine():
    config = c.ConfigParser()
    config.read(configuration_file)
    d.download_xml_file(config['DEFAULT']['INVALIDATE_TOKEN_PATH'], {}, savepath)
    # TODO un mesaj care sa confirme faptul ca deconectarea a fost realizata
    config.remove_option('DEFAULT', 'ACCESS_TOKEN')
    config.remove_option('DEFAULT', 'ACCESS_TOKEN_SECRET')
    with open(configuration_file, 'w') as configfile:
        config.write(configfile)
