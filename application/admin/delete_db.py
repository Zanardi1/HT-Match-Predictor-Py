import os

from sqlalchemy_utils import drop_database

import application.dialog_windows as dw
import global_library


def delete_database() -> None:
    """Algoritmul de stergere a bazei de date in care sunt retinute datele din meciurile importate
    din Hattrick.

    Parametri:
    ----------
    Niciunul

    Intoarce:
    ----------
    Nimic"""

    if os.path.exists(global_library.database_file_path):
        drop_database(global_library.database_file_uri)
        dw.show_info_window_in_thread(title='Succes!', message='Baza de date a fost stearsa.')
    else:
        dw.show_error_window_in_thread(title='Esec!', message='Baza de date nu exista')
