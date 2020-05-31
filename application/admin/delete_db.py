import os

from sqlalchemy_utils import drop_database

import application.dialog_windows as dw
import global_library


def delete_database() -> None:
    """Procedura sterge baza de date in care sunt retinute datele din meciurile importate din Hattrick.

    Algoritm:
    ----------
    Daca exista fisierul ce contine baza de date in folerul 'db', atunci il sterge si afiseaza un mesaj de confirmare.
    Daca nu, atunci nu face nimic si afiseaza un mesaj de eroare.

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
