import os
import tkinter as tk
from multiprocessing import Process
from tkinter.messagebox import showwarning, showinfo

from sqlalchemy_utils import drop_database

import global_library


def show_info_window():
    root = tk.Tk()
    root.withdraw()
    showinfo('Succes!', 'Baza de date a fost stearsa')
    root.destroy()


def show_warning_window():
    root = tk.Tk()
    root.withdraw()
    showwarning('Esec', 'Baza de date nu exista!')
    root.destroy()


def delete_database():
    if os.path.exists(global_library.database_file_path):
        drop_database(global_library.database_file_uri)
        p = Process(target=show_info_window)
        p.start()
        p.join()
    else:
        p = Process(target=show_warning_window)
        p.start()
        p.join()
