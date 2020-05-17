import application.dialog_windows as dw
import global_library
from application import config
from application.xml import dl_xml_file as d


def disconnection_engine():
    d.download_xml_file(config['DEFAULT']['INVALIDATE_TOKEN_PATH'], {}, global_library.disconnect_savepath)
    config.remove_option('DEFAULT', 'ACCESS_TOKEN')
    config.remove_option('DEFAULT', 'ACCESS_TOKEN_SECRET')
    with open(global_library.configuration_file, 'w') as configfile:
        config.write(configfile)
    dw.show_info_window_in_thread(title='Disconnection successful!',
                                  message='You are disconnected from your Hattrick account!')
