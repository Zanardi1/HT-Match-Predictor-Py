import application.dialog_windows as dw
import global_library
from application import config
from application.xml import dl_xml_file as d


def disconnection_engine(show_confirmation_window: bool) -> None:
    """Algoritmul de deconectare de la contul Hattrick. Procedura sterge jetoanele access token si access token secret,
     motiv pentru care utilizatorul va trebui sa reia intreg procesul de conectare la contul de Hattrick, daca vrea
     sa aiba acces la detaliile contului sau

     Parametri:
     ----------
     show_confirmation_window: bool
        arata daca va fi afisata sau nu fereastra de confirmare

     Intoarce:
     ----------
     Nimic"""
    d.download_xml_file(file=config['DEFAULT']['INVALIDATE_TOKEN_PATH'], params={},
                        destination_file=global_library.disconnect_savepath)
    config.remove_option('DEFAULT', 'ACCESS_TOKEN')
    config.remove_option('DEFAULT', 'ACCESS_TOKEN_SECRET')
    with open(file=global_library.configuration_file, mode='w') as configfile:
        config.write(configfile)
    if show_confirmation_window:
        dw.show_info_window_in_thread(title='Disconnection successful!',
                                      message='You are disconnected from your Hattrick account!')
