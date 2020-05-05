import os
import tkinter as tk
from tkinter.messagebox import showwarning, showinfo

from sqlalchemy_utils import drop_database

import global_library


def delete_database():
    root = tk.Tk()
    root.withdraw()
    if os.path.exists(global_library.database_file_path):
        drop_database(global_library.database_file_uri)
        showinfo('Succes!', 'Baza de date a fost stearsa')
    else:
        showwarning('Esec', 'Baza de date nu exista!')
    root.destroy()
